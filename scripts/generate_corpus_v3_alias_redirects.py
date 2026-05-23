#!/usr/bin/env python3
"""Generate alias short-route redirect pages.

For every typed alias (e.g., THM0001, DEF0142, PAP0001) on a public Corpus
Item, emit a Jekyll redirect page at /{alias-lowercased}/ that 301-redirects
to /id/{cid}/.

Skips aliases that collide with existing top-level site paths (e.g., /faq,
/publications, /verify) so the redirects don't clobber program surfaces.

Wave 7b deliverable. Doctrine §14.3.

Usage:
    python3 scripts/generate_corpus_v3_alias_redirects.py
    python3 scripts/generate_corpus_v3_alias_redirects.py --dry-run
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

import yaml

SITE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS_V3_ROOT = SITE_ROOT.parent / "corpus-v3"
OUTPUT_DIR = SITE_ROOT / "_corpus_v3_alias_redirects"

# Paths reserved by the site itself — never override with an alias redirect
RESERVED_TOP_LEVEL = {
    "about", "agenda", "assets", "atlas", "bibliography", "brand", "cite",
    "colophon", "corpus", "discover", "engage", "faqs", "id", "impact",
    "index", "manifest", "ontology", "preview", "program", "publications",
    "redirects", "research-graph", "research-log", "research-notes",
    "research-program", "results", "search", "site-atlas", "support",
    "tau-library", "taulib", "verify", "workflows",
}

# Typed alias pattern (e.g., THM0001, DEF0142, BOK0001, MOD0265)
TYPED_ALIAS_RE = re.compile(r"^[A-Z]{3}[0-9]{4,}$")


def atomic_write(target: Path, content: str) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_suffix(target.suffix + ".tmp")
    tmp.write_text(content, encoding="utf-8")
    os.replace(tmp, target)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--corpus-v3-root", type=Path, default=DEFAULT_CORPUS_V3_ROOT)
    parser.add_argument("--output-dir", type=Path, default=OUTPUT_DIR)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not args.corpus_v3_root.is_dir():
        print(f"FAIL: corpus-v3 root not found: {args.corpus_v3_root}", file=sys.stderr)
        return 1

    items_dir = args.corpus_v3_root / "items"
    args.output_dir.mkdir(parents=True, exist_ok=True)

    print(f"=== Generate alias short-route redirects ===")
    print(f"  source:  {args.corpus_v3_root}")
    print(f"  target:  {args.output_dir.relative_to(SITE_ROOT)}")
    print()

    redirects: dict[str, str] = {}  # alias_lower → cid
    collisions: list[str] = []
    skipped_reserved: list[str] = []
    skipped_already_seen: list[tuple[str, str]] = []
    skipped_non_typed = 0

    for path in sorted(items_dir.rglob("cid*.yaml")):
        try:
            item = yaml.safe_load(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(item, dict) or "id" not in item:
            continue
        if item.get("visibility") not in ("public", "deprecated_public"):
            continue

        cid = item["id"]
        for alias in item.get("aliases", []) or []:
            if not isinstance(alias, str):
                continue
            if not TYPED_ALIAS_RE.match(alias):
                skipped_non_typed += 1
                continue
            alias_lower = alias.lower()
            if alias_lower in RESERVED_TOP_LEVEL:
                skipped_reserved.append(alias_lower)
                continue
            if alias_lower in redirects and redirects[alias_lower] != cid:
                collisions.append(f"{alias_lower}: maps to both {redirects[alias_lower]} and {cid}")
                continue
            if alias_lower in redirects:
                skipped_already_seen.append((alias_lower, cid))
                continue
            redirects[alias_lower] = cid

    print(f"  typed aliases collected:    {len(redirects)}")
    print(f"  skipped (reserved path):    {len(skipped_reserved)}")
    print(f"  skipped (non-typed alias):  {skipped_non_typed}")
    print(f"  collisions:                 {len(collisions)}")

    if collisions:
        print()
        print("Collisions:")
        for c in collisions[:10]:
            print(f"  ✗ {c}")

    written = 0
    for alias_lower, cid in sorted(redirects.items()):
        outpath = args.output_dir / f"{alias_lower}.md"
        content = f"""---
layout: redirect
permalink: /{alias_lower}/
redirect_to: /id/{cid}/
sitemap: false
---
"""
        if args.dry_run:
            continue
        atomic_write(outpath, content)
        written += 1

    print()
    print(f"  redirects written: {written}")
    print()
    print("✓ Alias redirect generation complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
