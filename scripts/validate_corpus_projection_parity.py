#!/usr/bin/env python3
"""Validate that site projection files were synced from Corpus exports."""

from __future__ import annotations

import filecmp
import json
import os
from pathlib import Path


SITE_ROOT = Path(__file__).resolve().parents[1]
ORG_ROOT = SITE_ROOT.parent
CORPUS_EXPORTS = Path(os.environ.get("CORPUS_EXPORTS_DIR", ORG_ROOT / "corpus" / "exports" / "public"))


def assert_same_file(source: Path, target: Path) -> None:
    if not source.exists():
        raise AssertionError(f"missing source export: {source}")
    if not target.exists():
        raise AssertionError(f"missing synced target: {target}")
    if not filecmp.cmp(source, target, shallow=False):
        raise AssertionError(f"synced file differs: {target} != {source}")


def assert_tree_same(source: Path, target: Path, suffix: str = ".md") -> int:
    source_files = sorted(path for path in source.rglob(f"*{suffix}") if path.is_file())
    target_files = sorted(path for path in target.rglob(f"*{suffix}") if path.is_file())
    source_rel = {path.relative_to(source) for path in source_files}
    target_rel = {path.relative_to(target) for path in target_files}
    if source_rel != target_rel:
        missing = sorted(source_rel - target_rel)[:10]
        extra = sorted(target_rel - source_rel)[:10]
        raise AssertionError(f"tree mismatch {target}: missing={missing}, extra={extra}")
    for rel in source_rel:
        assert_same_file(source / rel, target / rel)
    return len(source_files)


def count_json(path: Path) -> int:
    data = json.loads(path.read_text(encoding="utf-8"))
    return len(data) if isinstance(data, list) else len(data.get("items", []))


def main() -> int:
    for filename in ("problem-ledger.json", "problem-ledger.ndjson", "problem-ledger.csv"):
        assert_same_file(CORPUS_EXPORTS / filename, SITE_ROOT / "_data" / "problem_ledger" / filename)
    for filename in ("results.json", "results.ndjson", "results.csv"):
        assert_same_file(CORPUS_EXPORTS / filename, SITE_ROOT / "_data" / "results" / filename)
    for filename in ("bibliography.json", "bibliography.ndjson", "bibliography.csv"):
        assert_same_file(CORPUS_EXPORTS / filename, SITE_ROOT / "_data" / "bibliography" / filename)
        assert_same_file(CORPUS_EXPORTS / filename, SITE_ROOT / "assets" / "data" / "bibliography" / filename)
    for filename in ("index.json", "groups.json", "cited_entries.json", "citation_index.json", "orphan_report.json", "batch_plan.json"):
        assert_same_file(CORPUS_EXPORTS / "bibliography-data" / filename, SITE_ROOT / "_data" / "bibliography" / filename)
    assert_same_file(CORPUS_EXPORTS / "references.bib", SITE_ROOT / "assets" / "bibliography" / "references.bib")
    for filename in ("predictions.json", "predictions.ndjson", "predictions.csv"):
        assert_same_file(CORPUS_EXPORTS / filename, SITE_ROOT / "_data" / "predictions" / filename)
        assert_same_file(CORPUS_EXPORTS / filename, SITE_ROOT / "assets" / "data" / "predictions" / filename)
    for filename in ("falsifications.json", "falsifications.ndjson", "falsifications.csv"):
        assert_same_file(CORPUS_EXPORTS / filename, SITE_ROOT / "_data" / "falsifications" / filename)
        assert_same_file(CORPUS_EXPORTS / filename, SITE_ROOT / "assets" / "data" / "falsifications" / filename)
    for filename in ("parts.json", "chapters.json"):
        assert_same_file(
            CORPUS_EXPORTS / "monograph-projections" / "data" / filename,
            SITE_ROOT / "_data" / "publications" / filename,
        )

    problem_count = assert_tree_same(CORPUS_EXPORTS / "problem-items", SITE_ROOT / "_problem_ledger")
    result_count = assert_tree_same(CORPUS_EXPORTS / "result-pages", SITE_ROOT / "results" / "problem")
    bibliography_count = assert_tree_same(CORPUS_EXPORTS / "bibliography-pages", SITE_ROOT / "_bibliography")
    prediction_count = assert_tree_same(CORPUS_EXPORTS / "prediction-pages", SITE_ROOT / "_predictions")
    falsification_count = assert_tree_same(CORPUS_EXPORTS / "falsification-pages", SITE_ROOT / "_falsifications")
    monograph_count = assert_tree_same(CORPUS_EXPORTS / "monograph-projections" / "pages", SITE_ROOT / "corpus" / "monographs")

    expected = {
        "problem-ledger.json": 239,
        "results.json": 255,
        "recovery-requirements.json": 45,
        "construction-spine.json": 10,
        "agenda-progress.json": 284,
        "bibliography.json": 1148,
        "predictions.json": 67,
        "falsifications.json": 30,
    }
    for filename, count in expected.items():
        actual = count_json(CORPUS_EXPORTS / filename)
        if actual != count:
            raise AssertionError(f"{filename}: expected {count}, found {actual}")

    if problem_count != 239:
        raise AssertionError(f"expected 239 problem item pages, found {problem_count}")
    if result_count != 255:
        raise AssertionError(f"expected 255 result pages, found {result_count}")
    if bibliography_count != 1148:
        raise AssertionError(f"expected 1148 bibliography pages, found {bibliography_count}")
    if prediction_count != 67:
        raise AssertionError(f"expected 67 prediction pages, found {prediction_count}")
    if falsification_count != 30:
        raise AssertionError(f"expected 30 falsification pages, found {falsification_count}")
    if monograph_count != 622:
        raise AssertionError(f"expected 622 monograph pages, found {monograph_count}")

    print("Corpus projection parity passed.")
    print(f"Problem Ledger pages: {problem_count}")
    print(f"Result pages: {result_count}")
    print(f"Bibliography pages: {bibliography_count}")
    print(f"Prediction pages: {prediction_count}")
    print(f"Falsification pages: {falsification_count}")
    print(f"Monograph pages: {monograph_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
