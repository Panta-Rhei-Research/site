#!/usr/bin/env python3
"""
Helper: Join citation_index with references.bib metadata for editorial review.

Produces _data/bibliography/cited_entries.json with one entry per cited key
containing:
  - bib metadata (title, authors, year, type, journal, publisher)
  - citation locations from citation_index
  - statistics (citation count, primary book)

Used by the human (or assistant) to write hand-crafted editorial overrides
in _data/bibliography/overrides.yml.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from latex_to_mathml import convert_title, clean_bibfield, latex_accents_to_unicode

BIBFILE = Path(
    "/Users/thorfuchs/Books/PantaRhei-2ndEd/website/specs/bibliography-briefing-pack/references.bib"
)
SITE_DATA = Path(__file__).parent.parent / "_data" / "bibliography"
CITATION_INDEX = SITE_DATA / "citation_index.json"
OUT = SITE_DATA / "cited_entries.json"

# ---------------------------------------------------------------------------
# Minimal BibTeX parser (same style as build_bibliography.py — regex-based)
# ---------------------------------------------------------------------------

ENTRY_RE = re.compile(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", re.DOTALL)
FIELD_RE = re.compile(r"(\w+)\s*=\s*[{\"]", re.DOTALL)


def parse_bib(text: str) -> dict:
    """Return {key: {entry_type, fields}}."""
    entries = {}

    # Skip past @comment
    text = re.sub(r"@comment\s*\{[^}]*\}", "", text)

    i = 0
    while i < len(text):
        m = ENTRY_RE.search(text, i)
        if not m:
            break
        entry_type = m.group(1).lower()
        key = m.group(2)

        if entry_type == "comment":
            i = m.end()
            continue

        # Find entry end by brace matching
        start = m.end() - 1  # Back up to the comma; find the opening {
        # Find the opening { of the entry
        brace_start = m.start()
        while brace_start < len(text) and text[brace_start] != "{":
            brace_start += 1
        depth = 0
        j = brace_start
        while j < len(text):
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1

        entry_body = text[m.end():j]  # after "@type{key,"

        fields = {}
        # Parse fields inside entry_body
        fi = 0
        while fi < len(entry_body):
            fm = FIELD_RE.search(entry_body, fi)
            if not fm:
                break
            field_name = fm.group(1).lower()
            # Find the opening delimiter
            delim = entry_body[fm.end() - 1]
            close = "}" if delim == "{" else '"'
            # Brace matching for the value
            if delim == "{":
                fdepth = 1
                fj = fm.end()
                while fj < len(entry_body) and fdepth > 0:
                    if entry_body[fj] == "{":
                        fdepth += 1
                    elif entry_body[fj] == "}":
                        fdepth -= 1
                    fj += 1
                value = entry_body[fm.end():fj - 1]
            else:
                # Quoted value
                fj = fm.end()
                while fj < len(entry_body) and entry_body[fj] != '"':
                    fj += 1
                value = entry_body[fm.end():fj]
                fj += 1
            # Collapse whitespace in value
            value = re.sub(r"\s+", " ", value).strip()
            fields[field_name] = value
            fi = fj + 1

        entries[key] = {"entry_type": entry_type, "fields": fields}
        i = j + 1

    return entries


# ---------------------------------------------------------------------------
# Main join
# ---------------------------------------------------------------------------


def main():
    print(f"Parsing {BIBFILE}")
    bib_text = BIBFILE.read_text(encoding="utf-8")
    bib = parse_bib(bib_text)
    print(f"  {len(bib)} bibliography entries parsed")

    citations = json.loads(CITATION_INDEX.read_text(encoding="utf-8"))
    print(f"  {len(citations)} cited keys")

    joined = {}
    missing = []
    for key, cites in citations.items():
        entry = bib.get(key)
        if not entry:
            missing.append(key)
            continue

        fields = entry["fields"]
        raw_title = fields.get("title", "")
        _, title_plain = convert_title(raw_title)

        authors = clean_bibfield(fields.get("author", ""))
        year = fields.get("year", "")
        journal = clean_bibfield(fields.get("journal") or fields.get("journaltitle") or "")
        booktitle = clean_bibfield(fields.get("booktitle", ""))
        publisher = clean_bibfield(fields.get("publisher", ""))

        books = Counter(c["book"] for c in cites)
        primary_book = books.most_common(1)[0][0]

        joined[key] = {
            "key": key,
            "title_plain": title_plain,
            "title_raw": raw_title,
            "authors": authors,
            "year": year,
            "entry_type": entry["entry_type"],
            "journal": journal,
            "booktitle": booktitle,
            "publisher": publisher,
            "citation_count": len(cites),
            "primary_book": primary_book,
            "books": dict(books),
            "citations": cites,
        }

    print(f"\nJoined {len(joined)} entries.")
    if missing:
        print(f"MISSING (cited but not in .bib): {len(missing)}")
        for k in missing[:10]:
            print(f"  {k}")

    SITE_DATA.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(joined, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nWrote {OUT}")

    # Print per-book tallies
    from collections import defaultdict
    by_book = defaultdict(list)
    for key, data in joined.items():
        by_book[data["primary_book"]].append(key)

    print("\nPer primary-book tally:")
    for b in ["I", "II", "III", "IV", "V", "VI", "VII"]:
        print(f"  Book {b}: {len(by_book[b])} entries")


if __name__ == "__main__":
    main()
