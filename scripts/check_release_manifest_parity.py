#!/usr/bin/env python3
"""Validate the generated site release-metric payload."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any

import yaml


COMPARE_FIELDS = [
    "value",
    "display_value",
    "unit",
    "public_label",
    "scope",
    "source_repo",
    "source_commit",
    "source_path",
    "filter_rule",
    "public_safe",
]


def read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def read_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def metric_index(manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["id"]: item for item in manifest.get("metrics", [])}


def compare(label: str, expected: dict[str, Any], actual: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    expected_index = metric_index(expected)
    actual_index = metric_index(actual)
    if set(expected_index) != set(actual_index):
        missing = sorted(set(expected_index) - set(actual_index))
        extra = sorted(set(actual_index) - set(expected_index))
        if missing:
            failures.append(f"{label}: missing metric ids: {', '.join(missing)}")
        if extra:
            failures.append(f"{label}: extra metric ids: {', '.join(extra)}")
    for metric_id in sorted(set(expected_index) & set(actual_index)):
        for field in COMPARE_FIELDS:
            if expected_index[metric_id].get(field) != actual_index[metric_id].get(field):
                failures.append(f"{label}: {metric_id}.{field} drift")
    for field in ["schema_version", "release_id", "title", "status", "generated_at", "policy", "sources", "toolchain"]:
        if expected.get(field) != actual.get(field):
            failures.append(f"{label}: top-level {field} drift")
    return failures


def default_canonical(root: Path) -> Path | None:
    env = os.environ.get("PANTA_RHEI_RELEASE_MANIFEST")
    candidates = []
    if env:
        candidates.append(Path(env))
    candidates.extend([
        root.parent / "corpus" / "release-manifests/public/release-manifest.json",
        root.parent / "corpus-release-manifest-canonical" / "release-manifests/public/release-manifest.json",
    ])
    for path in candidates:
        if path.exists():
            return path
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-root", default=".")
    parser.add_argument("--canonical", default="")
    parser.add_argument("--require-canonical", action="store_true")
    args = parser.parse_args()

    root = Path(args.site_root).resolve()
    yml = read_yaml(root / "_data/release/current.yml")
    js = read_json(root / "_data/release/current.json")
    failures = compare("_data/release/current.json", yml, js)

    canonical_path = Path(args.canonical).resolve() if args.canonical else default_canonical(root)
    if canonical_path:
        canonical = read_json(canonical_path)
        failures.extend(compare(str(canonical_path), canonical, yml))
    elif args.require_canonical:
        failures.append("canonical Corpus release manifest not found")

    if failures:
        print("Release manifest parity check failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    if canonical_path:
        print(f"✓ Site release manifest matches Corpus canonical payload: {canonical_path}")
    else:
        print("✓ Site release manifest YAML/JSON parity passed; Corpus canonical payload not present locally.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
