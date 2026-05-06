#!/usr/bin/env python3
"""Validate Site Atlas governed routes and manifest duplicate routes."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


CHECKED_STATUSES = {"canonical", "auxiliary", "archive", "deprecated", "redirected"}


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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("built_root", type=Path)
    parser.add_argument("--site-root", type=Path, default=Path("."))
    args = parser.parse_args()

    route_index = load_json(args.site_root / "_data/site_atlas/route_index.json")
    collections = load_json(args.site_root / "_data/site_atlas/collections.json").get("collections", [])
    errors: list[str] = []
    route_to_keys: dict[str, list[str]] = defaultdict(list)
    for route, atlas_page in sorted(route_index.items()):
        route_to_keys[route].append(atlas_page.get("page_key", "<missing>"))
        if atlas_page.get("status") in CHECKED_STATUSES and not route_to_file(args.built_root, route).exists():
            errors.append(f"{atlas_page.get('page_key')}: missing route {route}")
    for route, keys in route_to_keys.items():
        if len(keys) > 1:
            errors.append(f"duplicate Site Atlas route {route}: {', '.join(keys)}")
    for collection in collections:
        route = collection.get("index_route")
        if route and not route_to_file(args.built_root, route).exists():
            errors.append(f"{collection.get('collection_key')}: missing collection index route {route}")
    if errors:
        print("Site Atlas route check failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Site Atlas route check passed: {len(route_index)} governed routes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
