#!/usr/bin/env python3
"""Assert the v4 dossier export pipeline is wired into the built site."""

from __future__ import annotations

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from typing import Any


EXPECTED_ROUTES = {
    "/corpus/construction-spine/",
    "/corpus/construction-spine/build-the-kernel/",
    "/corpus/construction-spine/recover-core-mathematics/",
    "/corpus/construction-spine/internalize-self-enrichment/",
    "/corpus/construction-spine/identify-physical-carrier/",
    "/corpus/construction-spine/recover-internal-physical-grammar/",
    "/corpus/construction-spine/measurement-empirical-bridges/",
    "/corpus/construction-spine/recover-life/",
    "/corpus/construction-spine/recover-reflective-structure/",
    "/corpus/construction-spine/self-host-formal-systems/",
    "/corpus/construction-spine/test-ontic-closure/",
}


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.alternates: list[dict[str, str]] = []
        self.anchors: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = {key: value or "" for key, value in attrs}
        if tag == "link" and data.get("rel") == "alternate":
            self.alternates.append(data)
        if tag == "a" and data.get("href"):
            self.anchors.append(data["href"])


def load_manifest(built_root: Path) -> dict[str, Any]:
    path = built_root / "assets" / "dossier-manifest.json"
    if not path.exists():
        raise AssertionError(f"Missing public dossier manifest: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("entries"), list):
        raise AssertionError("Invalid dossier manifest shape")
    return data


def html_path_for_route(built_root: Path, route: str) -> Path:
    if route == "/":
        return built_root / "index.html"
    return built_root / route.strip("/") / "index.html"


def assert_route(entry: dict[str, Any], built_root: Path) -> None:
    html_path = html_path_for_route(built_root, entry["route"])
    if not html_path.exists():
        raise AssertionError(f"Missing enabled page HTML: {entry['route']}")
    html = html_path.read_text(encoding="utf-8")
    parser = LinkParser()
    parser.feed(html)
    alternate_types = {item.get("type"): item.get("href") for item in parser.alternates}
    if alternate_types.get("application/pdf") != entry["pdf_path"]:
        raise AssertionError(f"Missing PDF alternate for {entry['route']}")
    if alternate_types.get("text/markdown") != entry["markdown_path"]:
        raise AssertionError(f"Missing Markdown alternate for {entry['route']}")
    if entry["pdf_path"] not in parser.anchors:
        raise AssertionError(f"Page tools missing Dossier PDF link for {entry['route']}")
    if entry["markdown_path"] not in parser.anchors:
        raise AssertionError(f"Page tools missing Markdown link for {entry['route']}")


def assert_artifacts(entry: dict[str, Any], built_root: Path) -> None:
    for key in ("markdown_path", "typst_path", "pdf_path"):
        path = built_root / entry[key].strip("/")
        if not path.exists():
            raise AssertionError(f"Missing {key} artifact for {entry['route']}: {path}")
        if path.stat().st_size < (10_000 if key == "pdf_path" else 500):
            raise AssertionError(f"{key} artifact is unexpectedly small for {entry['route']}")
        if key != "pdf_path":
            text = path.read_text(encoding="utf-8")
            if "{%" in text or "{{" in text:
                raise AssertionError(f"Unresolved Liquid in {key} for {entry['route']}")


def validate(built_root: Path) -> None:
    manifest = load_manifest(built_root)
    routes = {entry["route"] for entry in manifest["entries"]}
    if routes != EXPECTED_ROUTES:
        raise AssertionError(f"Unexpected dossier routes: {sorted(routes)}")
    if "/corpus/construction-spine/define-the-kernel/" in routes or "/corpus/construction-spine/internalize-logic/" in routes:
        raise AssertionError("Redirect alias routes must not be dossier-enabled")
    for entry in manifest["entries"]:
        assert_artifacts(entry, built_root)
        assert_route(entry, built_root)

    corpus_html = (built_root / "corpus" / "index.html").read_text(encoding="utf-8")
    if re.search(r"/exports/(markdown|pdf)/corpus(?:\.md|-dossier\.pdf)", corpus_html):
        raise AssertionError("Non-enabled Corpus root exposes dossier export links")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("built_root", nargs="?", default="_site")
    args = parser.parse_args()
    validate(Path(args.built_root).resolve())
    print("v4 dossier export assertion passed")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except AssertionError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
