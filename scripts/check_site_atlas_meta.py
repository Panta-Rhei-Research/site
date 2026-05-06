#!/usr/bin/env python3
"""Validate rendered prrp:* metadata against _data/site_atlas."""

from __future__ import annotations

import argparse
import json
from html.parser import HTMLParser
from pathlib import Path


META_FIELDS = {
    "prrp:atlas_id": "atlas_id",
    "prrp:page_key": "page_key",
    "prrp:ia_path": "ia_path",
    "prrp:lane": "lane",
    "prrp:status": "status",
    "prrp:canonical_role": "canonical_role",
}
CHECKED_STATUSES = {"canonical", "auxiliary", "archive", "deprecated", "redirected"}


class MetaParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.meta: dict[str, str] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "meta":
            return
        attr_map = {key.lower(): value or "" for key, value in attrs}
        key = attr_map.get("name") or attr_map.get("property")
        if key:
            self.meta[key] = attr_map.get("content", "")


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def route_to_file(built_root: Path, route: str) -> Path:
    if route == "/":
        return built_root / "index.html"
    primary = built_root / route.strip("/") / "index.html"
    if primary.exists():
        return primary
    if route.endswith(".html"):
        return built_root / route.strip("/")
    if route.strip("/") == "404":
        return built_root / "404.html"
    return primary


def parse_meta(path: Path) -> dict[str, str]:
    parser = MetaParser()
    parser.feed(path.read_text(encoding="utf-8", errors="ignore"))
    parser.close()
    return parser.meta


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("built_root", type=Path)
    parser.add_argument("--site-root", type=Path, default=Path("."))
    args = parser.parse_args()

    route_index = load_json(args.site_root / "_data/site_atlas/route_index.json")
    errors: list[str] = []
    checked = 0
    for route, atlas_page in sorted(route_index.items()):
        if atlas_page.get("status") not in CHECKED_STATUSES:
            continue
        checked += 1
        html_path = route_to_file(args.built_root, route)
        if not html_path.exists():
            errors.append(f"{atlas_page.get('page_key')}: missing built route {route}")
            continue
        meta = parse_meta(html_path)
        for meta_name, field_name in META_FIELDS.items():
            expected = str(atlas_page.get(field_name, ""))
            actual = meta.get(meta_name)
            if actual is None:
                errors.append(f"{atlas_page.get('page_key')}: missing {meta_name}")
            elif actual != expected:
                errors.append(f"{atlas_page.get('page_key')}: {meta_name} expected {expected!r}, got {actual!r}")

    if errors:
        print("Site Atlas metadata check failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Site Atlas metadata check passed: {checked} governed routes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
