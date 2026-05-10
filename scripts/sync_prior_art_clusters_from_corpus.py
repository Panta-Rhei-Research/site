#!/usr/bin/env python3
"""Sync prior-art clusters from the corpus repo into site/_data/bibliography/.

Source-of-truth discipline: corpus/data/bibliography/prior-art-clusters.yml is
canonical. The site repo mirrors that file at
site/_data/bibliography/prior-art-clusters.yml so Liquid can read it via
site.data.bibliography['prior-art-clusters'] (Jekyll auto-loads YAML in
_data/).

Usage:

    python3 scripts/sync_prior_art_clusters_from_corpus.py
    python3 scripts/sync_prior_art_clusters_from_corpus.py --corpus-root /path

Resolves corpus root in this order:
  1. --corpus-root flag
  2. PRRP_CORPUS_ROOT env var
  3. ../corpus relative to site repo

Exit code 0 on success, 1 on missing source / parse failure.
"""
from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

import yaml

SITE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS_ROOT = SITE_ROOT.parent / "corpus"
SITE_TARGET = SITE_ROOT / "_data" / "bibliography" / "prior-art-clusters.yml"
SOURCE_REL = "data/bibliography/prior-art-clusters.yml"


def resolve_corpus_root(arg: str | None) -> Path:
    if arg:
        return Path(arg).resolve()
    env = os.environ.get("PRRP_CORPUS_ROOT")
    if env:
        return Path(env).resolve()
    return DEFAULT_CORPUS_ROOT.resolve()


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync prior-art clusters corpus → site")
    parser.add_argument("--corpus-root", default=None, help="Path to corpus repo (default: ../corpus)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    corpus_root = resolve_corpus_root(args.corpus_root)
    src = corpus_root / SOURCE_REL

    if not src.is_file():
        print(f"FAIL: source file not found at {src}", file=sys.stderr)
        return 1

    # Validate parses + has clusters[] before copying
    try:
        data = yaml.safe_load(src.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        print(f"FAIL: source did not parse as YAML: {e}", file=sys.stderr)
        return 1
    if not isinstance(data, dict) or "clusters" not in data:
        print(f"FAIL: {src} does not look like a prior-art cluster file (missing 'clusters')", file=sys.stderr)
        return 1

    n_clusters = len(data["clusters"])
    n_refs = sum(len(c.get("references") or []) for c in data["clusters"])
    n_chs = sum(len(c.get("related_challenges") or []) for c in data["clusters"])

    SITE_TARGET.parent.mkdir(parents=True, exist_ok=True)

    if args.dry_run:
        print(f"  [dry-run] would copy {src} → {SITE_TARGET}")
        print(f"  [dry-run] {n_clusters} clusters · {n_refs} refs · {n_chs} challenges")
        return 0

    shutil.copy2(src, SITE_TARGET)
    sz = SITE_TARGET.stat().st_size

    print(f"✓ Prior-art clusters sync complete")
    print(f"  Source: {src}")
    print(f"  Target: _data/bibliography/prior-art-clusters.yml")
    print(f"  Clusters: {n_clusters}")
    print(f"  Refs:     {n_refs}")
    print(f"  Challenges: {n_chs}")
    print(f"  Size:     {sz} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
