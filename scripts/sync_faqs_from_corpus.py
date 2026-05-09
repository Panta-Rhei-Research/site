#!/usr/bin/env python3
"""Sync FAQ entity collection from the Corpus repo into the site _data/faqs/ tree.

Source-of-truth discipline: corpus/faqs/ is canonical. The site repo mirrors
that tree as Jekyll data files under _data/faqs/, plus a generated index.yml
with counts and ID rosters for fast Liquid lookup.

Usage:

    python3 scripts/sync_faqs_from_corpus.py
    python3 scripts/sync_faqs_from_corpus.py --corpus-root /path/to/corpus

Resolves the corpus root in this order:
  1. --corpus-root flag
  2. PRRP_CORPUS_ROOT env var
  3. ../corpus relative to site repo

Exit code 0 on success, 1 on missing files / mismatched layer files / I/O error.
"""
from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

import yaml

LAYER_FILES = [
    "first_contact.yml",
    "first_orientation.yml",
    "journalist_due_diligence.yml",
    "technical_credibility.yml",
    "expert_handoff.yml",
]

SITE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS_ROOT = SITE_ROOT.parent / "corpus"
SITE_DATA_DIR = SITE_ROOT / "_data" / "faqs"


def resolve_corpus_root(arg: str | None) -> Path:
    if arg:
        return Path(arg).resolve()
    env = os.environ.get("PRRP_CORPUS_ROOT")
    if env:
        return Path(env).resolve()
    return DEFAULT_CORPUS_ROOT.resolve()


def write_index(target_dir: Path, layer_records: list[tuple[str, dict]]) -> None:
    """Write an aggregate index.yml with per-layer counts and ID rosters."""
    layers = []
    total = 0
    all_ids: list[str] = []
    for fname, data in layer_records:
        faqs = data.get("faqs") or []
        ids = [f.get("id") for f in faqs if isinstance(f, dict) and f.get("id")]
        layers.append(
            {
                "file": fname,
                "collection": data.get("collection"),
                "layer": data.get("layer", {}),
                "version": data.get("version"),
                "last_reviewed": data.get("last_reviewed"),
                "count": len(faqs),
                "ids": ids,
            }
        )
        total += len(faqs)
        all_ids.extend(ids)

    index = {
        "generated_by": "scripts/sync_faqs_from_corpus.py",
        "source_repo": "corpus",
        "source_path": "corpus/faqs/",
        "total_entries": total,
        "total_layers": len(layers),
        "all_ids": all_ids,
        "layers": layers,
    }
    (target_dir / "index.yml").write_text(
        yaml.safe_dump(index, sort_keys=False, allow_unicode=True, default_flow_style=False, width=120),
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync FAQ entity collection from corpus → site")
    parser.add_argument("--corpus-root", default=None, help="Path to corpus repo root (default: ../corpus)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would happen without writing")
    args = parser.parse_args()

    corpus_root = resolve_corpus_root(args.corpus_root)
    corpus_faqs = corpus_root / "faqs"

    if not corpus_faqs.is_dir():
        print(f"FAIL: corpus FAQ dir not found at {corpus_faqs}", file=sys.stderr)
        print("  Pass --corpus-root <path> or set PRRP_CORPUS_ROOT.", file=sys.stderr)
        return 1

    SITE_DATA_DIR.mkdir(parents=True, exist_ok=True)

    layer_records: list[tuple[str, dict]] = []
    missing: list[str] = []
    bytes_written = 0

    for fname in LAYER_FILES:
        src = corpus_faqs / fname
        if not src.is_file():
            missing.append(fname)
            continue
        # Validate parses as YAML before copying
        try:
            data = yaml.safe_load(src.read_text(encoding="utf-8"))
        except yaml.YAMLError as e:
            print(f"FAIL: {src} did not parse as YAML: {e}", file=sys.stderr)
            return 1
        if not isinstance(data, dict) or "faqs" not in data:
            print(f"FAIL: {src} does not look like a FAQ collection (missing 'faqs')", file=sys.stderr)
            return 1
        layer_records.append((fname, data))

        dst = SITE_DATA_DIR / fname
        if args.dry_run:
            print(f"  [dry-run] would copy {src} → {dst} ({len(data.get('faqs') or [])} entries)")
        else:
            shutil.copy2(src, dst)
            sz = dst.stat().st_size
            bytes_written += sz
            print(f"  copied {src.name} → _data/faqs/{fname} ({len(data.get('faqs') or [])} entries, {sz} bytes)")

    if missing:
        print(f"FAIL: missing layer files in corpus/faqs/: {', '.join(missing)}", file=sys.stderr)
        return 1

    if args.dry_run:
        print("\n[dry-run] would also write _data/faqs/index.yml with counts + ID rosters")
        return 0

    write_index(SITE_DATA_DIR, layer_records)
    total_entries = sum(len(d.get("faqs") or []) for _, d in layer_records)
    total_ids = sum(len([f.get("id") for f in (d.get("faqs") or []) if f.get("id")]) for _, d in layer_records)

    print()
    print(f"✓ FAQ sync complete")
    print(f"  Files mirrored: {len(layer_records)}")
    print(f"  Total entries:  {total_entries}")
    print(f"  Unique IDs:     {total_ids}")
    print(f"  Bytes written:  {bytes_written}")
    print(f"  Source: {corpus_faqs.relative_to(corpus_root.parent) if corpus_faqs.is_relative_to(corpus_root.parent) else corpus_faqs}")
    print(f"  Target: _data/faqs/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
