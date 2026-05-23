#!/usr/bin/env python3
"""Sync corpus-v3 items + manifests into site/_data/corpus_v3/.

Source-of-truth discipline: corpus-v3/ is the canonical repository for
Corpus v3 items. The site mirrors selected files at site/_data/corpus_v3/
so Jekyll's Liquid can read them and generate the /id/cid######/ surface
via the corpus-v3-item layout.

Sync targets:
  corpus-v3/manifests/alias-index.yaml          → _data/corpus_v3/alias-index.yaml
  corpus-v3/manifests/cid-index.yaml            → _data/corpus_v3/cid-index.yaml
  corpus-v3/manifests/cid-transition-manifest.yaml → _data/corpus_v3/transition.yaml

  corpus-v3/manifests/item-types.yaml           → _data/corpus_v3/item-types.yaml
  corpus-v3/manifests/relation-vocabulary.yaml  → _data/corpus_v3/relation-vocabulary.yaml
  corpus-v3/manifests/visibility-values.yaml    → _data/corpus_v3/visibility-values.yaml
  corpus-v3/manifests/lifecycle-statuses.yaml   → _data/corpus_v3/lifecycle-statuses.yaml

Items themselves are NOT copied into _data/ (their content lives at the
per-item layer used by generate_corpus_v3_pages.py).

Resolves corpus-v3 root in this order:
  1. --corpus-v3-root flag
  2. PRRP_CORPUS_V3_ROOT env var
  3. ../corpus-v3 relative to site repo

Atomic write per file. Validates each file parses + has expected top-level
keys before copying.

Wave 7 deliverable. Charter §6 (web projection doctrine).
"""
from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path
from typing import Any

import yaml

SITE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS_V3_ROOT = SITE_ROOT.parent / "corpus-v3"
SITE_DATA_TARGET = SITE_ROOT / "_data" / "corpus_v3"

# (source rel path under corpus-v3, target filename under _data/corpus_v3, expected top-level key)
SYNC_TARGETS: list[tuple[str, str, str]] = [
    ("manifests/alias-index.yaml",           "alias-index.yaml",      "aliases"),
    ("manifests/cid-index.yaml",             "cid-index.yaml",        "cids"),
    ("manifests/cid-transition-manifest.yaml", "transition.yaml",     "transitions"),
    ("manifests/item-types.yaml",            "item-types.yaml",       "types"),
    ("manifests/relation-vocabulary.yaml",   "relation-vocabulary.yaml", "predicates"),
    ("manifests/visibility-values.yaml",     "visibility-values.yaml",   "values"),
    ("manifests/lifecycle-statuses.yaml",    "lifecycle-statuses.yaml",  "statuses"),
]


def resolve_corpus_v3_root(arg: str | None) -> Path:
    if arg:
        return Path(arg).resolve()
    env = os.environ.get("PRRP_CORPUS_V3_ROOT")
    if env:
        return Path(env).resolve()
    return DEFAULT_CORPUS_V3_ROOT.resolve()


def atomic_write(target: Path, payload: bytes) -> None:
    """Write to a sibling .tmp then os.replace — survives SIGINT mid-copy."""
    tmp = target.with_suffix(target.suffix + ".tmp")
    tmp.write_bytes(payload)
    os.replace(tmp, target)


def sync_file(src: Path, target: Path, expected_top_key: str) -> tuple[bool, str]:
    """Sync one file. Returns (ok, message)."""
    if not src.is_file():
        return False, f"source not found: {src}"
    try:
        raw = src.read_bytes()
        parsed = yaml.safe_load(raw.decode("utf-8"))
    except Exception as e:
        return False, f"parse failed: {e}"
    if not isinstance(parsed, dict) or expected_top_key not in parsed:
        return False, f"missing top-level key {expected_top_key!r}"
    target.parent.mkdir(parents=True, exist_ok=True)
    atomic_write(target, raw)
    return True, f"{src.stat().st_size} bytes → {target.relative_to(SITE_ROOT)}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--corpus-v3-root", default=None,
                        help="Path to corpus-v3 repo (default: ../corpus-v3)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    corpus_v3_root = resolve_corpus_v3_root(args.corpus_v3_root)
    if not corpus_v3_root.is_dir():
        print(f"FAIL: corpus-v3 root not found: {corpus_v3_root}", file=sys.stderr)
        return 1

    print(f"=== Sync corpus-v3 → site/_data/corpus_v3/ ===")
    print(f"  source:  {corpus_v3_root}")
    print(f"  target:  {SITE_DATA_TARGET.relative_to(SITE_ROOT)}")
    print()

    errors: list[str] = []
    synced: list[str] = []

    for src_rel, target_name, expected_key in SYNC_TARGETS:
        src = corpus_v3_root / src_rel
        target = SITE_DATA_TARGET / target_name

        if args.dry_run:
            ok = src.is_file()
            status = "would-sync" if ok else "missing"
            print(f"  [dry-run] {status:12s} {src_rel:48s} → {target.name}")
            if not ok:
                errors.append(f"{src_rel}: source missing")
            continue

        ok, msg = sync_file(src, target, expected_key)
        marker = "✓" if ok else "✗"
        print(f"  {marker} {src_rel:48s} {msg}")
        if ok:
            synced.append(src_rel)
        else:
            errors.append(f"{src_rel}: {msg}")

    print()
    print(f"  synced: {len(synced)} files")
    print(f"  errors: {len(errors)}")

    if errors:
        print()
        for e in errors:
            print(f"  ✗ {e}")
        return 1

    print()
    print("✓ Sync complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
