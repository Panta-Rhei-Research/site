#!/usr/bin/env python3
"""Sync prior-art clusters from the corpus repo into site/_data/bibliography/.

Source-of-truth discipline: corpus/data/bibliography/prior-art-clusters.yml is
canonical. The site repo mirrors that file at
site/_data/bibliography/prior-art-clusters.yml so Liquid can read it via
site.data.bibliography['prior-art-clusters'] (Jekyll auto-loads YAML in
_data/).

Cluster schema (per-cluster fields)
-----------------------------------
The Liquid layouts and the auto-detect include consume only a subset of the
fields each cluster carries. The rest are mirrored faithfully from corpus
for traceability, even though the site doesn't render them. This split is
intentional and worth knowing when reading the synced YAML.

  Consumed by site (rendered into pages):
    cluster_id          stable id of form `pa<NNNNNN>` for citation continuity
    cluster_key         snake_case key matching the cluster page filename
    title               human-readable cluster name
    description         long-form prose rendered on the per-cluster page
    references          list of bib_keys → resolved via corpus slugify rule
                        (lowercase + `_`→`-`) to /bibliography/<slug>/
    related_construction_steps   list of CS-NN ids → resolved via
                        _data/construction_spine to /corpus/construction-spine/<slug>/
    related_challenges  list of {SCL-id} → resolved via
                        _data/corpus/structural_challenges to canonical SCL URL
    reference_count     total count of bibliography entries in domain
                        (separate from len(references), which is the
                        curated subset shown on the page)
    metadata_pending    boolean — when true, page surfaces a
                        "Provisional metadata" pill near the title

  Carried for traceability but not rendered:
    summary             short tagline (rendered titles use `title` directly)
    domains             corpus-side domain-tag list (used in corpus exports)
    related_publications  list of book identifiers (book-i…book-vii) — corpus
                        contract, not currently surfaced on site

Future site work that exposes the carried fields should update both this
docstring and the layout — keep the schema documentation centralised here.

Usage:

    python3 scripts/sync_prior_art_clusters_from_corpus.py
    python3 scripts/sync_prior_art_clusters_from_corpus.py --corpus-root /path

Resolves corpus root in this order:
  1. --corpus-root flag
  2. PRRP_CORPUS_ROOT env var
  3. ../corpus relative to site repo

Exit code 0 on success, 1 on missing source / parse failure / unresolved refs
(unless --allow-missing-refs is passed for emergency syncs).
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import yaml

SITE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS_ROOT = SITE_ROOT.parent / "corpus"
SITE_TARGET = SITE_ROOT / "_data" / "bibliography" / "prior-art-clusters.yml"
SOURCE_REL = "data/bibliography/prior-art-clusters.yml"
BIB_DIR = SITE_ROOT / "_bibliography"


def resolve_corpus_root(arg: str | None) -> Path:
    if arg:
        return Path(arg).resolve()
    env = os.environ.get("PRRP_CORPUS_ROOT")
    if env:
        return Path(env).resolve()
    return DEFAULT_CORPUS_ROOT.resolve()


def slugify(key: str) -> str:
    """Mirror corpus/scripts/bibliography_common.py::slugify_key.

    Lowercase, then collapse runs of non-alphanumeric (including underscores)
    into single hyphens; strip leading/trailing hyphens. This matches the
    bibliography filename convention Jekyll derives URLs from, so the YAML
    key `FuchsFuchs26_Primon` resolves to `fuchsfuchs26-primon` — the same
    transform the layout's `| downcase | replace: "_", "-"` Liquid filter
    chain applies at render time.
    """
    import re

    slug = re.sub(r"[^a-z0-9]+", "-", key.lower()).strip("-")
    return slug or "reference"


def index_bibliography_slugs() -> dict[str, str]:
    """Return {filename_stem: actual_stem} for all _bibliography/*.md.

    Bibliography URLs are derived from the filename (lowercase, hyphen-
    separated). YAML bib_keys may carry mixed-case + underscores, so we
    resolve via the corpus slugify rule rather than naive lowercase.
    """
    if not BIB_DIR.is_dir():
        return {}
    return {p.stem: p.stem for p in BIB_DIR.glob("*.md")}


def validate_references(data: dict, bib_index: dict[str, str]) -> tuple[list[str], list[str]]:
    """Return (case_mismatch, truly_missing) lists of bib_keys.

    case_mismatch: YAML key resolves to a real bibliography file under a
    different casing or with underscores that map to hyphens (the layout's
    `| downcase | replace: "_", "-"` filter chain handles the URL emit;
    these are warnings, not failures).

    truly_missing: no bibliography file exists even after slugify
    normalization. These will 404 regardless of layout filtering and
    constitute a hard failure.
    """
    refs: set[str] = set()
    for c in data.get("clusters", []):
        for r in c.get("references") or []:
            if isinstance(r, str):
                refs.add(r)

    case_mismatch: list[str] = []
    truly_missing: list[str] = []
    for r in sorted(refs):
        slug = slugify(r)
        if slug in bib_index:
            if bib_index[slug] != r:
                case_mismatch.append(r)
        else:
            truly_missing.append(r)
    return case_mismatch, truly_missing


def atomic_write(target: Path, payload: bytes) -> None:
    """Write to a sibling .tmp then os.replace — survives SIGINT mid-copy."""
    tmp = target.with_suffix(target.suffix + ".tmp")
    tmp.write_bytes(payload)
    os.replace(tmp, target)


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync prior-art clusters corpus → site")
    parser.add_argument("--corpus-root", default=None, help="Path to corpus repo (default: ../corpus)")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--allow-missing-refs",
        action="store_true",
        help="Don't fail when a reference has no bibliography file (default: fail).",
    )
    args = parser.parse_args()

    corpus_root = resolve_corpus_root(args.corpus_root)
    src = corpus_root / SOURCE_REL

    if not src.is_file():
        print(f"FAIL: source file not found at {src}", file=sys.stderr)
        return 1

    # Validate parses + has clusters[] before copying
    try:
        payload = src.read_bytes()
        data = yaml.safe_load(payload.decode("utf-8"))
    except yaml.YAMLError as e:
        print(f"FAIL: source did not parse as YAML: {e}", file=sys.stderr)
        return 1
    if not isinstance(data, dict) or "clusters" not in data:
        print(f"FAIL: {src} does not look like a prior-art cluster file (missing 'clusters')", file=sys.stderr)
        return 1

    n_clusters = len(data["clusters"])
    n_refs = sum(len(c.get("references") or []) for c in data["clusters"])
    n_chs = sum(len(c.get("related_challenges") or []) for c in data["clusters"])

    # Validate bib_key resolution before writing — surfaces the casing/missing
    # gap that PR #170 QA caught after the fact (#1, #3 in the QA findings).
    bib_index = index_bibliography_slugs()
    if not bib_index:
        print(f"WARN: no _bibliography/*.md files found at {BIB_DIR} — skipping reference validation", file=sys.stderr)
        case_mismatch, truly_missing = [], []
    else:
        case_mismatch, truly_missing = validate_references(data, bib_index)

    if case_mismatch:
        print(f"INFO: {len(case_mismatch)} bib_key{'s' if len(case_mismatch) != 1 else ''} need slug normalization (case/underscores) — layout '| downcase | replace: \"_\", \"-\"' handles this:", file=sys.stderr)
        for r in case_mismatch[:5]:
            print(f"  · {r}", file=sys.stderr)
        if len(case_mismatch) > 5:
            print(f"  · ... and {len(case_mismatch) - 5} more", file=sys.stderr)

    if truly_missing:
        print(f"FAIL: {len(truly_missing)} bib_key{'s' if len(truly_missing) != 1 else ''} have no _bibliography/*.md file (will 404 if linked):", file=sys.stderr)
        for r in truly_missing:
            print(f"  ✗ {r}", file=sys.stderr)
        if not args.allow_missing_refs:
            print(f"\nFix in corpus/data/bibliography/prior-art-clusters.yml — add stubs or remove from references.", file=sys.stderr)
            print(f"To bypass for an emergency sync, pass --allow-missing-refs.", file=sys.stderr)
            return 1

    SITE_TARGET.parent.mkdir(parents=True, exist_ok=True)

    if args.dry_run:
        print(f"  [dry-run] would copy {src} → {SITE_TARGET}")
        print(f"  [dry-run] {n_clusters} clusters · {n_refs} refs · {n_chs} challenges")
        return 0

    atomic_write(SITE_TARGET, payload)
    sz = SITE_TARGET.stat().st_size

    print(f"✓ Prior-art clusters sync complete")
    print(f"  Source: {src}")
    print(f"  Target: _data/bibliography/prior-art-clusters.yml")
    print(f"  Clusters:   {n_clusters}")
    print(f"  Refs:       {n_refs} ({len(case_mismatch)} case-normalized at render, {len(truly_missing)} unresolved)")
    print(f"  Challenges: {n_chs}")
    print(f"  Size:       {sz} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
