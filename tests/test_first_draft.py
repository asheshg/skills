"""Regression checks for local file and renderer trust boundaries."""
import argparse
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1] / "skills/first-draft"


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


class SafetyTests(unittest.TestCase):
    def test_asset_inspector_identifies_active_parts_and_external_targets(self):
        spec = importlib.util.spec_from_file_location("asset_inspector", ROOT.parents[1] / "scripts/inspect_first_draft_assets.py")
        inspector = importlib.util.module_from_spec(spec); spec.loader.exec_module(inspector)
        with tempfile.TemporaryDirectory(dir=ROOT.parents[1] / "tests") as tmp:
            source = Path(tmp) / "fixture.pptx"
            with zipfile.ZipFile(source, "w") as archive:
                archive.writestr("ppt/vbaProject.bin", b"fixture")
                archive.writestr("../escape", b"fixture")
                archive.writestr("ppt/_rels/presentation.xml.rels", '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship TargetMode="External" Target="file:///private" Type="https://example.com/hyperlink"/></Relationships>')
            result = inspector.inspect(source)
            self.assertEqual(len(result["risks"]), 3)

    def test_sanitizer_cannot_truncate_its_input(self):
        sanitizer = module("sanitize_pptx")
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "source.pptx"; source.write_bytes(b"keep original")
            with self.assertRaises(ValueError): sanitizer.sanitize_pptx(source, source)
            self.assertEqual(source.read_bytes(), b"keep original")

    def test_template_canvas_bounds_notes_and_placeholder_contrast(self):
        renderer = module("render_pptx")
        from pptx import Presentation
        from pptx.dml.color import RGBColor
        with tempfile.TemporaryDirectory() as tmp:
            for template in (renderer.DEFAULT_LIGHT, renderer.DEFAULT_DARK):
                original = Presentation(str(template))
                output = Path(tmp) / "test.pptx"
                renderer.render({"slides": [{"title": "QA", "body": ["Observation"],
                    "notes": "Keep this in notes", "visual": {"type": "chart", "description": "Sample"}}]}, output, template)
                deck = Presentation(str(output)); slide = deck.slides[0]
                self.assertEqual(len(deck.slide_layouts), len(original.slide_layouts))
                self.assertEqual(slide.notes_slide.notes_text_frame.text, "Keep this in notes")
                self.assertNotIn("Keep this in notes", " ".join(s.text for s in slide.shapes if s.has_text_frame))
                for shape in slide.shapes:
                    if shape.has_text_frame and shape.text:
                        self.assertLessEqual(shape.left + shape.width, deck.slide_width)
                        self.assertLessEqual(shape.top + shape.height, deck.slide_height)
                visual = next(s for s in slide.shapes if s.has_text_frame and s.text.startswith("chart:"))
                self.assertEqual(visual.text_frame.paragraphs[0].font.color.rgb, RGBColor(30, 30, 30))
    def test_html_rejects_injection_without_writing_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            spec, output = Path(tmp) / "spec.json", Path(tmp) / "deck.html"
            for field, payload in (("colors", "</style><script>alert(1)</script>"),
                                   ("colors", "red; background:url(https://example.com)"),
                                   ("fonts", "Arial; color:red"), ("fonts", r"Arial\3c style")):
                key = "primary" if field == "colors" else "body"
                spec.write_text(json.dumps({"brand": {field: {key: payload}}, "slides": [{}]}))
                run = subprocess.run([sys.executable, str(ROOT / "scripts/render_html_deck.py"),
                                      str(spec), "--out", str(output)], capture_output=True)
                self.assertNotEqual(run.returncode, 0)
                self.assertFalse(output.exists())

    def test_html_accepts_fonts_and_escapes_text(self):
        renderer = module("render_html_deck")
        self.assertEqual(renderer.css_value("'Helvetica Neue', Arial", r"[\w ,.'\"-]+"),
                         "'Helvetica Neue', Arial")
        self.assertEqual(renderer.esc("<script>"), "&lt;script&gt;")

    def test_failed_manifest_replace_preserves_old_manifest(self):
        store = module("brand_store")
        with tempfile.TemporaryDirectory() as tmp:
            brands = Path(tmp); manifest = brands / "manifest.json"
            manifest.write_text('{"brands": []}')
            with patch.multiple(store, BRANDS_DIR=brands, MANIFEST=manifest):
                with patch.object(Path, "replace", side_effect=OSError("simulated disk failure")):
                    with self.assertRaises(OSError): store.save_manifest({"brands": [{"slug": "new"}]})
            self.assertEqual(json.loads(manifest.read_text()), {"brands": []})
            self.assertEqual(list(brands.iterdir()), [manifest])

    def test_missing_and_pointer_templates_do_not_fall_back(self):
        renderer = module("render_pptx")
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "missing.pptx"
            with self.assertRaises(ValueError):
                renderer.resolve_template({}, str(path))
            path.write_text("version https://git-lfs.github.com/spec/v1\n")
            with self.assertRaises(ValueError):
                renderer.resolve_template({}, str(path))

    def test_dense_slides_fail_before_creating_output(self):
        renderer = module("render_pptx")
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "deck.pptx"
            for field, values in (("body", ["item"] * 7), ("evidence", [{}] * 4)):
                with self.assertRaises(ValueError):
                    renderer.render({"slides": [{field: values}]}, output, None)
                self.assertFalse(output.exists())

    def test_brand_existing_overlap_merge_and_confirmation(self):
        store = module("brand_store")
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp); brands = base / "brands"; brands.mkdir()
            source = base / "upload"; source.mkdir(); (source / "new.txt").write_text("new")
            target = brands / "test"; target.mkdir(); (target / "original.txt").write_text("keep")
            args = argparse.Namespace(source=str(source), name="Test", slug="test", notes="", merge=False)
            with patch.multiple(store, BRANDS_DIR=brands, MANIFEST=brands / "manifest.json"):
                store.save_manifest({"brands": [{"slug": "test", "name": "Test", "templates": {"light": "custom.pptx"}}]})
                with self.assertRaises(SystemExit): store.add_brand(args)
                self.assertEqual((target / "original.txt").read_text(), "keep")
                args.source = str(target)
                with self.assertRaises(SystemExit): store.add_brand(args)
                args.source = str(source); args.merge = True
                store.add_brand(args)
                self.assertTrue((target / "new.txt").exists())
                self.assertEqual(store.load_manifest()["brands"][0]["templates"], {"light": "custom.pptx"})
                with self.assertRaises(SystemExit): store.add_brand(args)
                with self.assertRaises(SystemExit): store.delete_brand(argparse.Namespace(slug="test", yes=False))
                self.assertTrue(target.exists())
                with self.assertRaises(SystemExit): store.delete_brand(argparse.Namespace(slug="../test", yes=True))
                store.delete_brand(argparse.Namespace(slug="test", yes=True))
                self.assertFalse(target.exists())


if __name__ == "__main__":
    unittest.main()
