#!/usr/bin/env python3
"""Validate generated dossier export artifacts."""

from __future__ import annotations

import argparse
import json
import sys
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


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise AssertionError(f"Missing JSON file: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise AssertionError(f"Expected object in {path}")
    return data


def assert_file(path: Path, minimum_bytes: int, label: str) -> None:
    if not path.exists():
        raise AssertionError(f"Missing {label}: {path}")
    size = path.stat().st_size
    if size < minimum_bytes:
        raise AssertionError(f"{label} too small: {path} ({size} bytes)")


def validate(built_root: Path, minimum_pdf_bytes: int) -> None:
    manifest = load_json(built_root / "assets" / "dossier-manifest.json")
    report = load_json(built_root / "assets" / "dossier-build-report.json")
    entries = manifest.get("entries", [])
    if not isinstance(entries, list):
        raise AssertionError("dossier manifest entries must be a list")
    routes = {entry.get("route") for entry in entries}
    if routes != EXPECTED_ROUTES:
        missing = sorted(EXPECTED_ROUTES - routes)
        extra = sorted(routes - EXPECTED_ROUTES)
        raise AssertionError(f"Unexpected dossier route set. Missing={missing} Extra={extra}")
    if report.get("entry_count") != len(entries):
        raise AssertionError("build report entry count does not match manifest")

    for entry in entries:
        assert_file(built_root / entry["markdown_path"].strip("/"), 500, "Markdown export")
        assert_file(built_root / entry["typst_path"].strip("/"), 500, "Typst export")
        assert_file(built_root / entry["pdf_path"].strip("/"), minimum_pdf_bytes, "PDF export")
        markdown = (built_root / entry["markdown_path"].strip("/")).read_text(encoding="utf-8")
        typst = (built_root / entry["typst_path"].strip("/")).read_text(encoding="utf-8")
        if "{%" in markdown or "{{" in markdown or "{%" in typst or "{{" in typst:
            raise AssertionError(f"Unresolved Liquid in dossier artifact for {entry['route']}")
        if entry["url"] not in markdown:
            raise AssertionError(f"Canonical URL missing from Markdown export for {entry['route']}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--built-root", default="_site")
    parser.add_argument("--minimum-pdf-bytes", type=int, default=10_000)
    args = parser.parse_args()
    validate(Path(args.built_root).resolve(), args.minimum_pdf_bytes)
    print("Dossier artifact check passed")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except AssertionError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
