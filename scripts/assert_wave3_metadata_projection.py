#!/usr/bin/env python3
"""Focused assertions for the Corpus Metadata Wave 3 site projection."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "_data/corpus/wave3_index.yml",
    "_data/corpus/registry_count_model.yml",
    "_data/corpus/registry_object_types.yml",
    "_data/corpus/construction_steps.yml",
    "_data/corpus/construction_review_packets.yml",
    "_data/corpus/construction_motifs.yml",
    "_data/corpus/monograph_books.yml",
    "_data/corpus/monograph_parts.yml",
    "_data/corpus/monograph_chapters.yml",
    "_data/corpus/taulib_projection.yml",
    "_data/corpus/glossary_entries.yml",
    "_data/corpus/graph_index.yml",
    "_data/corpus/graph/objects.json",
    "_data/corpus/graph/adjacency.json",
    "assets/data/corpus-wave3/index.json",
    "assets/data/corpus-wave3/registry-count-model.json",
    "assets/data/corpus-wave3/construction-review-packets.json",
    "assets/data/corpus-wave3/construction-motifs.json",
    "assets/data/corpus-wave3/graph/objects.json",
]

TEXT_ASSERTIONS = [
    (
        "corpus/registry/index.md",
        ["manifest-pinned", "typed public spine"],
        [],
    ),
    (
        "corpus/bi-square/index.md",
        ["The Bi-Square Motif", "not a second construction spine"],
        ["The Bi-Square Spine"],
    ),
    (
        "corpus/foundational-hinges/index.md",
        ["Construction Steps 1-3 Review Packet", "not as a standalone Corpus collection"],
        ["Foundational Hinges as a separate collection"],
    ),
    (
        "corpus/construction-spine/index.md",
        ["Construction review packet", "Bi-Square Motif"],
        ["Bi-Square Spine", "Open the Foundational Hinges"],
    ),
    (
        "_data/nav.yml",
        ["Bi-Square Motif", "Construction Review Packet"],
        ["Bi-Square Spine"],
    ),
]


def fail(message: str) -> None:
    raise SystemExit(f"Wave 3 projection assertion failed: {message}")


def require_file(path: str) -> None:
    if not (ROOT / path).is_file():
        fail(f"missing required projection file: {path}")


def require_text(path: str, required: list[str], forbidden: list[str]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in required:
        if needle not in text:
            fail(f"{path} does not contain required text: {needle}")
    for needle in forbidden:
        if needle in text:
            fail(f"{path} still contains stale text: {needle}")


def require_counts() -> None:
    index = json.loads((ROOT / "assets/data/corpus-wave3/index.json").read_text(encoding="utf-8"))
    counts = index.get("counts", {})
    expected = {
        "registry_public_objects": 4139,
        "construction_steps": 10,
        "review_packets": 1,
        "construction_motifs": 1,
        "monograph_books": 7,
        "monograph_parts": 79,
        "taulib_modules": 512,
        "glossary_entries": 282,
    }
    for key, value in expected.items():
        if counts.get(key) != value:
            fail(f"count mismatch for {key}: expected {value}, got {counts.get(key)}")

    count_model = json.loads(
        (ROOT / "assets/data/corpus-wave3/registry-count-model.json").read_text(encoding="utf-8")
    )
    model = count_model.get("count_model", {})
    if model.get("registry_root_total", {}).get("value") != 4547:
        fail("registry_root_total is not 4547")
    if model.get("typed_public_spine_total", {}).get("value") != 4139:
        fail("typed_public_spine_total is not 4139")


def main() -> None:
    for path in REQUIRED_FILES:
        require_file(path)
    for path, required, forbidden in TEXT_ASSERTIONS:
        require_text(path, required, forbidden)
    require_counts()
    print("Wave 3 site projection assertions passed.")


if __name__ == "__main__":
    main()
