#!/usr/bin/env python3
"""Generate Jekyll collection documents for Corpus v3 items.

Reads corpus-v3/items/{type}/cid######-*.yaml and emits one Markdown
collection document per item under site/_corpus_v3_items/cid######.md.
Each carries:

  ---
  layout: corpus-v3-item
  permalink: /id/{cid}/
  cid: cid######
  primary_alias: THM0042
  ... (full item data inlined as frontmatter)
  ---

  (optional rendered body; the layout reads from frontmatter)

Atomic write per page. Idempotent (re-running produces no changes for
unchanged items).

Wave 7 deliverable. Web addendum §10 Option A (generated collection
documents).
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Any

import yaml

SITE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS_V3_ROOT = SITE_ROOT.parent / "corpus-v3"
OUTPUT_DIR = SITE_ROOT / "_corpus_v3_items"


def atomic_write(target: Path, content: str) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_suffix(target.suffix + ".tmp")
    tmp.write_text(content, encoding="utf-8")
    os.replace(tmp, target)


def iter_corpus_items(corpus_v3_root: Path):
    """Yield (cid, source_path, parsed_data) for every item under corpus-v3/items/."""
    items_dir = corpus_v3_root / "items"
    if not items_dir.is_dir():
        return
    for path in sorted(items_dir.rglob("cid*.yaml")):
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"  WARN: parse failed for {path}: {e}", file=sys.stderr)
            continue
        if not isinstance(data, dict) or "id" not in data:
            continue
        yield data["id"], path, data


def build_page_frontmatter(item: dict[str, Any]) -> dict[str, Any]:
    """Build the Jekyll page frontmatter for one Corpus Item."""
    cid = item["id"]
    primary_alias = item.get("primary_alias", "")
    type_ = item.get("type", "")
    title = item.get("title", cid)
    status = item.get("status", "")
    visibility = item.get("visibility", "")
    current_version = item.get("current_version", "v1")

    fm = {
        "layout": "corpus-v3-item",
        "permalink": f"/id/{cid}/",
        "title": title,
        "cid": cid,
        "primary_alias": primary_alias,
        "type": type_,
        "lane": "corpus",
        "status": status,
        "visibility": visibility,
        "current_version": current_version,
        "release_lines": item.get("release_lines", []),
        "summary": item.get("summary", ""),
        "aliases": item.get("aliases", []),
        "layers": item.get("layers", []),
        "domains": item.get("domains", []),
        "relations": item.get("relations", []),
        "depends_on": item.get("depends_on", []),
        "appears_in": item.get("appears_in", []),
        "formalized_by": item.get("formalized_by", []),
        "sources": item.get("sources", []),
        "contains": item.get("contains", []),
        "part_of": item.get("part_of", []),
        "history": item.get("history", []),
        "external_identifiers": item.get("external_identifiers", {}),
        "payload": item.get("payload", {}),
        "formalization": item.get("formalization", {}),
        "proof": item.get("proof", {}),
        "result": item.get("result", {}),
        "commentary": item.get("commentary", {}),
        "tombstone": item.get("tombstone", False),
        "superseded_by": item.get("superseded_by", ""),
        "retired_at": item.get("retired_at", ""),
        "retirement_reason": item.get("retirement_reason", ""),
        "refuted_at": item.get("refuted_at", ""),
        "refutation_reason": item.get("refutation_reason", ""),
        # SEO hints
        "description": item.get("summary", "")[:240] if item.get("summary") else f"Corpus Item {cid}",
        "noindex": False if visibility in ("public", "deprecated_public") else True,
    }
    return fm


def render_page(fm: dict[str, Any]) -> str:
    """Render the full page with frontmatter + minimal body."""
    fm_yaml = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, default_flow_style=False, width=120)
    body = ""  # the layout reads everything from frontmatter
    return f"---\n{fm_yaml}---\n{body}\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--corpus-v3-root", type=Path, default=DEFAULT_CORPUS_V3_ROOT)
    parser.add_argument("--output-dir", type=Path, default=OUTPUT_DIR)
    parser.add_argument("--visibility", default="public,deprecated_public",
                        help="Comma-separated visibility filter (default: public + deprecated_public)")
    parser.add_argument("--limit", type=int, default=None,
                        help="For testing — emit only first N pages")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not args.corpus_v3_root.is_dir():
        print(f"FAIL: corpus-v3 root not found: {args.corpus_v3_root}", file=sys.stderr)
        return 1

    visibility_filter = {v.strip() for v in args.visibility.split(",")}

    args.output_dir.mkdir(parents=True, exist_ok=True)

    print(f"=== Generate corpus_v3 Jekyll pages ===")
    print(f"  source:     {args.corpus_v3_root}")
    print(f"  target:     {args.output_dir.relative_to(SITE_ROOT)}")
    print(f"  visibility filter: {sorted(visibility_filter)}")
    print()

    written = 0
    skipped_visibility = 0
    seen = 0

    for cid, src_path, item in iter_corpus_items(args.corpus_v3_root):
        seen += 1
        if args.limit and written >= args.limit:
            break

        visibility = item.get("visibility", "")
        if visibility not in visibility_filter:
            skipped_visibility += 1
            continue

        fm = build_page_frontmatter(item)
        content = render_page(fm)
        outpath = args.output_dir / f"{cid}.md"

        if args.dry_run:
            print(f"  [dry-run] would write {outpath.relative_to(SITE_ROOT)} ({len(content)} bytes)")
            written += 1
            continue

        atomic_write(outpath, content)
        written += 1

    print()
    print(f"  items scanned:           {seen}")
    print(f"  pages written:           {written}")
    print(f"  skipped (visibility):    {skipped_visibility}")
    print()
    print("✓ Generation complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
