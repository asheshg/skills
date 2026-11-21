#!/usr/bin/env python
"""Manage retained brand guideline folders for the first-draft skill."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import tempfile
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BRANDS_DIR = ROOT / "sources" / "brands"
MANIFEST = BRANDS_DIR / "manifest.json"


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "brand"


def load_manifest() -> dict:
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text(encoding="utf-8"))
    return {"brands": []}


def save_manifest(data: dict) -> None:
    BRANDS_DIR.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(data, indent=2, sort_keys=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=BRANDS_DIR, delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(payload)
        temporary.replace(MANIFEST)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def list_brands(_: argparse.Namespace) -> None:
    data = load_manifest()
    if not data["brands"]:
        print("No retained brands.")
        return
    for brand in data["brands"]:
        print(f"{brand['slug']}\t{brand['name']}\t{brand.get('updated_at', '')}")


def add_brand(args: argparse.Namespace) -> None:
    source = Path(args.source).resolve()
    if not source.exists():
        raise SystemExit(f"Source not found: {source}")
    slug = slugify(args.slug or args.name or source.stem)
    target = BRANDS_DIR / slug
    if target.is_symlink() or target.resolve().parent != BRANDS_DIR.resolve():
        raise SystemExit("Brand destination must be a real folder inside the brand store.")
    if source == target.resolve() or source.is_relative_to(target.resolve()) or target.resolve().is_relative_to(source):
        raise SystemExit("Brand source and destination must not overlap.")
    incoming = list(source.rglob("*")) if source.is_dir() else [source]
    if any(item.is_symlink() or not item.resolve().is_relative_to(source) for item in incoming):
        raise SystemExit("Brand source must not contain symbolic links.")
    if target.exists() and not args.merge:
        raise SystemExit("Brand already exists; choose a new slug or use --merge to add new files.")
    for item in incoming:
        relative = item.relative_to(source) if source.is_dir() else Path(source.name)
        destination = target / relative
        if (destination.is_symlink() or not destination.resolve().is_relative_to(target.resolve())
                or (destination.exists() and not (item.is_dir() and destination.is_dir()))):
            raise SystemExit(f"Merge would overwrite an existing path: {destination}")
    data = load_manifest()
    previous = next((brand for brand in data["brands"] if brand["slug"] == slug), {})
    # shortcut: failed merges can leave new files; use staged directory swaps if rollback is required.
    target.mkdir(parents=True, exist_ok=True)
    if source.is_dir():
        for child in source.iterdir():
            destination = target / child.name
            if child.is_dir():
                shutil.copytree(child, destination, dirs_exist_ok=True)
            else:
                shutil.copy2(child, destination)
    else:
        shutil.copy2(source, target / source.name)
    now = datetime.now(timezone.utc).isoformat()
    data["brands"] = [b for b in data["brands"] if b["slug"] != slug]
    data["brands"].append({
        **previous,
        "slug": slug,
        "name": args.name or previous.get("name") or source.stem,
        "path": f"sources/brands/{slug}",
        "updated_at": now,
        "notes": args.notes or previous.get("notes", ""),
    })
    data["brands"].sort(key=lambda item: item["slug"])
    save_manifest(data)
    print(f"Added brand: {slug}")


def delete_brand(args: argparse.Namespace) -> None:
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", args.slug):
        raise SystemExit("Use the exact retained brand slug for deletion.")
    slug = slugify(args.slug)
    target = BRANDS_DIR / slug
    if not args.yes:
        raise SystemExit("Deletion requires --yes after confirming the brand and backing it up.")
    if target.is_symlink() or target.resolve().parent != BRANDS_DIR.resolve():
        raise SystemExit("Brand destination must be a real folder inside the brand store.")
    if target.exists():
        shutil.rmtree(target)
    data = load_manifest()
    data["brands"] = [b for b in data["brands"] if b["slug"] != slug]
    save_manifest(data)
    print(f"Deleted brand: {slug}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(required=True)

    list_parser = sub.add_parser("list")
    list_parser.set_defaults(func=list_brands)

    add_parser = sub.add_parser("add")
    add_parser.add_argument("source")
    add_parser.add_argument("--name")
    add_parser.add_argument("--slug")
    add_parser.add_argument("--notes")
    add_parser.add_argument("--merge", action="store_true", help="Add new files to an existing brand; refuse overwrites.")
    add_parser.set_defaults(func=add_brand)

    delete_parser = sub.add_parser("delete")
    delete_parser.add_argument("slug")
    delete_parser.add_argument("--yes", action="store_true", help="Confirm permanent deletion of this retained brand.")
    delete_parser.set_defaults(func=delete_brand)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
