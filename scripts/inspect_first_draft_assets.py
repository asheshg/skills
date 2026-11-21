"""Inventory all bundled PPTX members without executing Office content."""
import hashlib
import json
from pathlib import Path, PurePosixPath
import sys
import zipfile
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def inspect(path):
    result = {"path": path.relative_to(ROOT).as_posix(),
              "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
              "xml_parts": 0, "media_parts": 0, "external_relationships": [], "risks": []}
    with zipfile.ZipFile(path) as archive:
        result["members"] = len(archive.infolist())
        bad = archive.testzip()
        if bad: result["risks"].append("CRC failure: " + bad)
        for part in archive.infolist():
            name = part.filename
            member = PurePosixPath(name.replace("\\", "/"))
            if member.is_absolute() or ".." in member.parts or ":" in member.parts[0]:
                result["risks"].append("Unsafe member path: " + name)
            if any(word in name.lower() for word in ("vbaproject", "/activex/", "/embeddings/")):
                result["risks"].append("Active or embedded payload: " + name)
            if name.startswith("ppt/media/"): result["media_parts"] += 1
            if name.endswith((".xml", ".rels")):
                data = archive.read(name)
                if b"<!DOCTYPE" in data or b"<!ENTITY" in data:
                    result["risks"].append("DTD/entity declaration: " + name)
                    continue
                xml = ET.fromstring(data)
                result["xml_parts"] += 1
                for node in xml.iter():
                    if node.tag.endswith("}Relationship") and node.get("TargetMode") == "External":
                        target = node.get("Target", "")
                        result["external_relationships"].append({"part": name, "type": node.get("Type"), "target": target})
                        if not node.get("Type", "").endswith("/hyperlink"):
                            result["risks"].append("External content dependency: " + target)
                        if not target.lower().startswith(("https://", "http://", "mailto:")):
                            result["risks"].append("Unexpected external target: " + target)
    return result


if __name__ == "__main__":
    reports = [inspect(path) for path in sorted((ROOT / "skills/first-draft/sources").rglob("*.pptx"))]
    output = Path(sys.argv[1]); output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(reports, indent=2), encoding="utf-8")
    for report in reports:
        print(report["path"], "members", report["members"], "risks", len(report["risks"]),
              "external", len(report["external_relationships"]))
    if len(reports) != 6 or any(report["risks"] for report in reports):
        raise SystemExit(1)
