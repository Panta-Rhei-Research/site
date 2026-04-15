#!/usr/bin/env python3
"""
Build citation index from Panta Rhei book LaTeX sources.

Walks every active book's .tex files, extracts every \\cite{KEY} citation with
surrounding sentence context, and produces two JSON outputs:

  - _data/bibliography/citation_index.json : key → list of citation locations
  - _data/bibliography/orphan_report.json  : .bib keys NOT cited anywhere

Active scope: books/{I..VII}-*/latex/sections/**/*.tex, excluding /archive/.
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BOOKS_ROOT = Path("/Users/thorfuchs/Books/PantaRhei-2ndEd/books")
BIBFILE = Path(
    "/Users/thorfuchs/Books/PantaRhei-2ndEd/website/specs/bibliography-briefing-pack/references.bib"
)
OUT_DIR = Path(__file__).parent.parent / "_data" / "bibliography"

ACTIVE_BOOKS = [
    ("I", "I-CategoricalFoundations", "Categorical Foundations"),
    ("II", "II-CategoricalHolomorphy", "Categorical Holomorphy"),
    ("III", "III-CategoricalSpectrum", "Categorical Spectrum"),
    ("IV", "IV-CategoricalMicrocosm", "Categorical Microcosm"),
    ("V", "V-CategoricalMacrocosm", "Categorical Macrocosm"),
    ("VI", "VI-CategoricalLife", "Categorical Life"),
    ("VII", "VII-CategoricalMetaphysics", "Categorical Metaphysics"),
]

# Matches \cite / \citep / \citet / \citeauthor etc., capturing the key list.
CITE_RE = re.compile(r"\\cite[a-zA-Z]*\s*(?:\[[^\]]*\])?\s*\{([^}]*)\}")

# \chapter{Title} or \chapter*{Title} — captures the title.
CHAPTER_RE = re.compile(r"\\chapter\*?\s*(?:\[[^\]]*\])?\s*\{((?:[^{}]|\{[^{}]*\})*)\}")

# partNN from path components.
PART_RE = re.compile(r"part(\d+)")


# ---------------------------------------------------------------------------
# LaTeX text cleaners
# ---------------------------------------------------------------------------

LATEX_ACCENTS = [
    # Umlaut
    (re.compile(r'\\"\s*\{?([a-zA-Z])\}?'), lambda m: _combine_diacritic(m.group(1), "\u0308")),
    # Acute
    (re.compile(r"\\'\s*\{?([a-zA-Z])\}?"), lambda m: _combine_diacritic(m.group(1), "\u0301")),
    # Grave
    (re.compile(r"\\`\s*\{?([a-zA-Z])\}?"), lambda m: _combine_diacritic(m.group(1), "\u0300")),
    # Circumflex
    (re.compile(r"\\\^\s*\{?([a-zA-Z])\}?"), lambda m: _combine_diacritic(m.group(1), "\u0302")),
    # Tilde
    (re.compile(r"\\~\s*\{?([a-zA-Z])\}?"), lambda m: _combine_diacritic(m.group(1), "\u0303")),
    # Cedilla
    (re.compile(r"\\c\s*\{?([a-zA-Z])\}?"), lambda m: _combine_diacritic(m.group(1), "\u0327")),
    # Ring above
    (re.compile(r"\\r\s*\{?([a-zA-Z])\}?"), lambda m: _combine_diacritic(m.group(1), "\u030A")),
    # Caron
    (re.compile(r"\\v\s*\{?([a-zA-Z])\}?"), lambda m: _combine_diacritic(m.group(1), "\u030C")),
]


def _combine_diacritic(base: str, combining: str) -> str:
    """Combine a base letter with a combining diacritic, then NFC-normalize."""
    import unicodedata

    return unicodedata.normalize("NFC", base + combining)


# Simple Greek letter replacements (for context cleaning; titles use mathml module)
GREEK = {
    r"\\alpha": "α",
    r"\\beta": "β",
    r"\\gamma": "γ",
    r"\\delta": "δ",
    r"\\epsilon": "ε",
    r"\\zeta": "ζ",
    r"\\eta": "η",
    r"\\theta": "θ",
    r"\\iota": "ι",
    r"\\kappa": "κ",
    r"\\lambda": "λ",
    r"\\mu": "μ",
    r"\\nu": "ν",
    r"\\xi": "ξ",
    r"\\pi": "π",
    r"\\rho": "ρ",
    r"\\sigma": "σ",
    r"\\tau": "τ",
    r"\\phi": "φ",
    r"\\chi": "χ",
    r"\\psi": "ψ",
    r"\\omega": "ω",
    r"\\Gamma": "Γ",
    r"\\Delta": "Δ",
    r"\\Theta": "Θ",
    r"\\Lambda": "Λ",
    r"\\Xi": "Ξ",
    r"\\Pi": "Π",
    r"\\Sigma": "Σ",
    r"\\Phi": "Φ",
    r"\\Psi": "Ψ",
    r"\\Omega": "Ω",
    r"\\partial": "∂",
    r"\\infty": "∞",
    r"\\to": "→",
    r"\\Rightarrow": "⇒",
    r"\\Leftarrow": "⇐",
    r"\\neq": "≠",
    r"\\leq": "≤",
    r"\\geq": "≥",
    r"\\in": "∈",
    r"\\subset": "⊂",
    r"\\subseteq": "⊆",
    r"\\cup": "∪",
    r"\\cap": "∩",
    r"\\otimes": "⊗",
    r"\\oplus": "⊕",
    r"\\times": "×",
    r"\\approx": "≈",
    r"\\equiv": "≡",
    r"\\cong": "≅",
    r"\\sim": "∼",
    r"\\forall": "∀",
    r"\\exists": "∃",
    r"\\emptyset": "∅",
    r"\\mathbb\{R\}": "ℝ",
    r"\\mathbb\{C\}": "ℂ",
    r"\\mathbb\{N\}": "ℕ",
    r"\\mathbb\{Z\}": "ℤ",
    r"\\mathbb\{Q\}": "ℚ",
    r"\\mathbb\{H\}": "ℍ",
    r"\\mathbb\{F\}": "𝔽",
}


def strip_tex_comments(src: str) -> str:
    """Drop % comment lines, preserving \\%."""
    out_lines = []
    for line in src.split("\n"):
        # Find first unescaped %
        idx = -1
        i = 0
        while i < len(line):
            if line[i] == "%" and (i == 0 or line[i - 1] != "\\"):
                idx = i
                break
            i += 1
        if idx >= 0:
            out_lines.append(line[:idx])
        else:
            out_lines.append(line)
    return "\n".join(out_lines)


def resolve_latex_accents(text: str) -> str:
    """Apply accent resolution non-destructively."""
    for pattern, fn in LATEX_ACCENTS:
        text = pattern.sub(fn, text)
    return text


def resolve_greek(text: str) -> str:
    """Apply Greek/math symbol substitution."""
    for pattern, replacement in GREEK.items():
        text = re.sub(pattern, replacement, text)
    return text


def clean_context_text(text: str) -> str:
    """Produce a clean, readable context snippet from raw .tex source."""
    # Strip \cite{...} and related
    text = CITE_RE.sub("", text)
    # Strip \footnote{...} entirely (content usually not needed)
    text = re.sub(r"\\footnote\s*\{(?:[^{}]|\{[^{}]*\})*\}", "", text)
    # Unwrap \textit{x}, \textbf{x}, \emph{x}, \mbox{x}
    for cmd in ["textit", "textbf", "emph", "mbox", "text", "textsc", "underline"]:
        text = re.sub(r"\\" + cmd + r"\{([^{}]*)\}", r"\1", text)
    # Resolve \% to %
    text = text.replace(r"\%", "%")
    # Tilde-binding → space
    text = text.replace("~", " ")
    # Accents
    text = resolve_latex_accents(text)
    # Greek/math symbols
    text = resolve_greek(text)
    # Strip remaining \command{...} → content
    text = re.sub(r"\\[a-zA-Z]+\*?\s*\{([^{}]*)\}", r"\1", text)
    # Strip remaining bare \command
    text = re.sub(r"\\[a-zA-Z]+\*?", "", text)
    # Strip leftover braces
    text = text.replace("{", "").replace("}", "")
    # Collapse whitespace
    text = re.sub(r"\s+", " ", text).strip()
    # Strip leading/trailing punctuation debris
    text = text.strip(" ,.;:")
    return text


# ---------------------------------------------------------------------------
# Chapter title and part resolution
# ---------------------------------------------------------------------------


def find_chapter_title(src: str) -> str | None:
    """Extract the first \\chapter{...} title, cleaned for display."""
    match = CHAPTER_RE.search(src)
    if not match:
        return None
    title = match.group(1)
    return clean_context_text(title) or None


def parse_part_from_path(path: Path) -> str:
    """From .../part18/ch71-...tex → 'Part 18'. Returns '' if no part segment."""
    for part in path.parts:
        m = PART_RE.match(part)
        if m:
            return f"Part {int(m.group(1))}"
    return ""


# ---------------------------------------------------------------------------
# Citation extraction
# ---------------------------------------------------------------------------

SENTENCE_END = re.compile(r"[.!?]\s")


def extract_sentence_context(src: str, offset: int, max_window: int = 600) -> str:
    """Walk backward/forward from offset to nearest sentence boundaries.

    Returns the sentence containing the citation, with a fallback to a
    ±300 char window if the sentence exceeds max_window.
    """
    # Walk backward for sentence start
    start = offset
    while start > 0:
        # Sentence boundary: "." "!" "?" followed by whitespace
        if (
            src[start - 1] in ".!?"
            and (start == 1 or src[start - 2] != ".")  # not an ellipsis
            and start < len(src)
            and (start == len(src) or src[start] in " \n\t")
        ):
            break
        start -= 1
        if offset - start > max_window:
            break

    # Walk forward for sentence end
    end = offset
    while end < len(src):
        if (
            src[end] in ".!?"
            and (end + 1 >= len(src) or src[end + 1] in " \n\t")
        ):
            end += 1
            break
        end += 1
        if end - offset > max_window:
            break

    # Pull the raw slice and clean it
    raw = src[max(0, start):min(len(src), end)]
    return clean_context_text(raw)


def iter_citations(src: str):
    """Yield (offset, [keys]) for every citation in src."""
    for match in CITE_RE.finditer(src):
        keys_raw = match.group(1)
        keys = [k.strip() for k in keys_raw.split(",") if k.strip()]
        if keys:
            yield match.start(), keys


# ---------------------------------------------------------------------------
# Book walk
# ---------------------------------------------------------------------------


def walk_book(book_num: str, book_dir: str, book_title: str, index: dict) -> int:
    """Walk all .tex files in a book, appending to index. Returns file count."""
    sections = BOOKS_ROOT / book_dir / "latex" / "sections"
    if not sections.exists():
        print(f"  WARN: {sections} does not exist")
        return 0

    file_count = 0
    for tex_path in sorted(sections.rglob("*.tex")):
        # Exclude anything under an archive/ directory
        if any(part == "archive" for part in tex_path.parts):
            continue
        file_count += 1

        try:
            raw = tex_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            raw = tex_path.read_text(encoding="latin-1")

        src = strip_tex_comments(raw)
        chapter_title = find_chapter_title(src) or tex_path.stem
        part_label = parse_part_from_path(tex_path.relative_to(sections))

        for offset, keys in iter_citations(src):
            context = extract_sentence_context(src, offset)
            raw_excerpt = src[max(0, offset - 150):min(len(src), offset + 150)]
            raw_excerpt = raw_excerpt.replace("\n", " ").strip()
            for key in keys:
                index[key].append(
                    {
                        "book": book_num,
                        "book_title": book_title,
                        "part": part_label,
                        "chapter_file": tex_path.stem,
                        "chapter_title": chapter_title,
                        "context": context,
                        "raw_excerpt": raw_excerpt,
                    }
                )

    return file_count


# ---------------------------------------------------------------------------
# Orphan report
# ---------------------------------------------------------------------------

BIB_KEY_RE = re.compile(r"@\w+\s*\{\s*([^,\s]+)\s*,")


def read_bib_keys(bibfile: Path) -> list[str]:
    """Extract all @type{KEY,...} keys from the .bib file, in order."""
    text = bibfile.read_text(encoding="utf-8")
    return BIB_KEY_RE.findall(text)


def build_orphan_report(all_bib_keys: list[str], cited_keys: set[str]) -> dict:
    """Produce a list of keys in the .bib but never cited."""
    orphans = [k for k in all_bib_keys if k not in cited_keys]
    return {
        "total_bib_keys": len(all_bib_keys),
        "cited_count": len(cited_keys),
        "orphan_count": len(orphans),
        "orphan_keys": orphans,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    print(f"Reading .bib: {BIBFILE}")
    all_bib_keys = read_bib_keys(BIBFILE)
    print(f"  Found {len(all_bib_keys)} bibliography entries")

    index: dict[str, list] = defaultdict(list)

    total_files = 0
    for book_num, book_dir, book_title in ACTIVE_BOOKS:
        print(f"Walking Book {book_num} ({book_dir})...")
        count = walk_book(book_num, book_dir, book_title, index)
        total_files += count
        print(f"  {count} .tex files scanned")

    print(f"\nTotal .tex files scanned: {total_files}")
    print(f"Unique cited keys: {len(index)}")
    print(f"Total citation locations: {sum(len(v) for v in index.values())}")

    # Sort citations within each key for determinism
    for key in index:
        index[key].sort(
            key=lambda c: (c["book"], c["chapter_file"], c["context"][:60])
        )

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    citation_path = OUT_DIR / "citation_index.json"
    citation_path.write_text(
        json.dumps(dict(sorted(index.items())), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"\nWrote {citation_path}")

    orphan_report = build_orphan_report(all_bib_keys, set(index.keys()))
    orphan_path = OUT_DIR / "orphan_report.json"
    orphan_path.write_text(
        json.dumps(orphan_report, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"Wrote {orphan_path}")

    # Top-cited summary
    top = sorted(index.items(), key=lambda kv: -len(kv[1]))[:10]
    print("\nTop-10 most-cited keys:")
    for key, citations in top:
        print(f"  {len(citations):4}  {key}")

    # Warn on dangling citations (in .tex but not in .bib)
    dangling = sorted(set(index.keys()) - set(all_bib_keys))
    if dangling:
        print(f"\nWARNING: {len(dangling)} cited keys not found in references.bib:")
        for k in dangling[:20]:
            print(f"  {k}")
        if len(dangling) > 20:
            print(f"  ... and {len(dangling) - 20} more")


if __name__ == "__main__":
    main()
