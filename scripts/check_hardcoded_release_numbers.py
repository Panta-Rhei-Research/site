#!/usr/bin/env python3
"""Fail on current release metrics that bypass the Corpus release manifest.

This is intentionally conservative and source-oriented. It scans public prose
and templates for release-changing count phrases that should be rendered via
`release-metric.html` or a generated README block.
"""

from __future__ import annotations

import os
import json
import re
import sys
from pathlib import Path
from typing import Any


README_START = "<!-- release-metrics:start -->"
README_END = "<!-- release-metrics:end -->"


SKIP_PARTS = {
    ".git",
    "_site",
    "node_modules",
    "vendor",
    "assets",
    "_data",
    "_data/release",
    "_data/registry/release_manifest_sections.yml",
    "corpus/taulib/docs",
    "_taulib_docs",
    "_bibliography",
}


CHECK_SUFFIXES = {".md", ".html", ".liquid", ".yml", ".yaml"}


FORBIDDEN = [
    (re.compile(r"\b522\s+modules\b", re.I), "stale TauLib module count"),
    (re.compile(r"\b445\s+Lean\s+4?\s*modules\b", re.I), "stale TauLib module count"),
    (re.compile(r"\b4,139\s+public\s+(?:registry\s+)?objects\b", re.I), "stale registry object count"),
    (re.compile(r"\b4,547\s+(?:typed\s+mathematical\s+)?objects\b", re.I), "hardcoded registry total"),
    (re.compile(r"\b4,863\s+theorem", re.I), "hardcoded theorem/lemma count"),
    (re.compile(r"\b142,406\s+lines\b", re.I), "hardcoded TauLib line count"),
    (re.compile(r"\b1,125\s+references\b", re.I), "stale bibliography count"),
    (re.compile(r"\b67\s+zero-parameter\b", re.I), "hardcoded prediction count"),
    (re.compile(r"\b67\s+(?:numerical\s+)?predictions\b", re.I), "hardcoded prediction count"),
    (re.compile(r"\b30[- ]item\b", re.I), "hardcoded falsification count"),
    (re.compile(r"\b30[- ]prediction\b", re.I), "hardcoded falsification count"),
    (re.compile(r"\b30\s+(?:named|sharp)\b", re.I), "hardcoded falsification count"),
]

SOURCE_BYPASS = [
    (re.compile(r"site\.data\.publications\.(?:books|chapters)\s*\|\s*size"), "media page collection-derived publication count"),
    (re.compile(r"site\.data\.results\.results\s*\|\s*size"), "media page collection-derived result count"),
    (re.compile(r"site\.data\.results\.results\s*\|\s*where:"), "media page collection-derived domain result count"),
    (re.compile(r"site\.data\.registry\.objects\s*\|\s*size"), "media page collection-derived registry count"),
]


def strip_generated_blocks(text: str) -> str:
    if README_START not in text:
        return text
    pattern = re.compile(re.escape(README_START) + r".*?" + re.escape(README_END), re.S)
    return pattern.sub("", text)


def load_manifest_metrics(root: Path) -> list[dict[str, Any]]:
    path = root / "_data/release/current.json"
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    return list(data.get("metrics", []))


def dynamic_manifest_patterns(root: Path) -> list[tuple[re.Pattern[str], str]]:
    patterns: list[tuple[re.Pattern[str], str]] = []
    for metric in load_manifest_metrics(root):
        display = str(metric.get("display_value", "")).strip()
        unit = str(metric.get("unit", "")).strip()
        if not display or not unit:
            continue
        if unit in {"records", "items", "steps", "entries", "plates", "mentions"} and display in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"}:
            continue
        number_forms = {display}
        if "," in display:
            number_forms.add(display.replace(",", ""))
        unit_pattern = re.escape(unit).replace(r"\ ", r"\s+")
        for number in sorted(number_forms):
            patterns.append((
                re.compile(rf"\b{re.escape(number)}\s+{unit_pattern}\b", re.I),
                f"hardcoded manifest metric {metric.get('id', '<unknown>')}",
            ))
    return patterns


def should_skip(path: Path, root: Path) -> bool:
    rel = path.relative_to(root).as_posix()
    return any(part in rel for part in SKIP_PARTS)


def iter_check_files(root: Path):
    for directory, dirnames, filenames in os.walk(root):
        dir_path = Path(directory)
        dirnames[:] = [
            name for name in dirnames
            if not should_skip(dir_path / name, root)
        ]
        for filename in filenames:
            path = dir_path / filename
            if path.suffix in CHECK_SUFFIXES and not should_skip(path, root):
                yield path


def is_generated_or_historical(path: Path, root: Path, text: str) -> bool:
    rel = path.relative_to(root).as_posix()
    if rel.startswith(("_changelog/", "publications/archived/")):
        return True
    if rel.startswith(("registry/object/", "corpus/monographs/")):
        return True
    frontmatter = text.split("---", 2)
    if len(frontmatter) >= 3 and "do_not_edit: true" in frontmatter[1]:
        return True
    return False


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    failures: list[str] = []
    manifest_patterns = dynamic_manifest_patterns(root)
    for path in sorted(iter_check_files(root)):
        text = strip_generated_blocks(path.read_text(encoding="utf-8", errors="ignore"))
        if is_generated_or_historical(path, root, text):
            continue
        for pattern, label in FORBIDDEN + manifest_patterns:
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                rel = path.relative_to(root)
                failures.append(f"{rel}:{line}: {label}: {match.group(0)!r}")
        if path.relative_to(root).as_posix().startswith("media/"):
            for pattern, label in SOURCE_BYPASS:
                for match in pattern.finditer(text):
                    line = text.count("\n", 0, match.start()) + 1
                    rel = path.relative_to(root)
                    failures.append(f"{rel}:{line}: {label}: {match.group(0)!r}")
    if failures:
        print("Hardcoded release-changing metric phrases found:", file=sys.stderr)
        for item in failures:
            print(f"- {item}", file=sys.stderr)
        return 1
    print("✓ No hardcoded release-changing metric phrases found outside manifest-approved blocks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
