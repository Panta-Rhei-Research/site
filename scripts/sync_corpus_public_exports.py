#!/usr/bin/env python3
"""Sync public Corpus projections into the v2 site worktree."""

from __future__ import annotations

import shutil
from pathlib import Path


SITE_ROOT = Path(__file__).resolve().parents[1]
ORG_ROOT = SITE_ROOT.parent
CORPUS_EXPORTS = ORG_ROOT / "corpus" / "exports" / "public"


def copy_file(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    print(f"synced {target.relative_to(SITE_ROOT)}")


def copy_tree(source: Path, target: Path) -> None:
    target.mkdir(parents=True, exist_ok=True)
    for path in sorted(source.rglob("*")):
        if path.is_file():
            copy_file(path, target / path.relative_to(source))


def main() -> int:
    if not CORPUS_EXPORTS.exists():
        raise SystemExit(f"Missing Corpus public exports: {CORPUS_EXPORTS}")

    for filename in ("problem-ledger.json", "problem-ledger.ndjson", "problem-ledger.csv"):
        source = CORPUS_EXPORTS / filename
        copy_file(source, SITE_ROOT / "_data" / "problem_ledger" / filename)
        copy_file(source, SITE_ROOT / "assets" / "data" / "problem-ledger" / filename)

    for filename in ("recovery-requirements.json", "recovery-requirements.ndjson", "recovery-requirements.csv"):
        source = CORPUS_EXPORTS / filename
        copy_file(source, SITE_ROOT / "_data" / "recovery_requirements" / filename)
        copy_file(source, SITE_ROOT / "assets" / "data" / "recovery-requirements" / filename)

    copy_tree(CORPUS_EXPORTS / "problem-items", SITE_ROOT / "_problem_ledger")
    copy_tree(CORPUS_EXPORTS / "recovery-requirements", SITE_ROOT / "_recovery_requirements")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
