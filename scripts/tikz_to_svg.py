#!/usr/bin/env python3
"""
TikZ → SVG Conversion Pipeline for Framework Module Diagrams

Extracts a specific figure (by label) from a book LaTeX chapter file,
wraps it in a standalone document with shared styles, compiles it with
lualatex, and converts the resulting PDF to SVG via pdf2svg.

Single-diagram usage:
    python3 scripts/tikz_to_svg.py \\
        --tex-file /path/to/ch01-five-generators.tex \\
        --label fig:bookI-ch01-generators-order \\
        --output assets/diagrams/framework/book-i/my-diagram.svg

Batch mode (reads mapping JSON):
    python3 scripts/tikz_to_svg.py --mapping scripts/framework-diagrams-mapping.json
    python3 scripts/tikz_to_svg.py --mapping ... --book I    # only book I
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.resolve()
STANDALONE_STYLES = SCRIPT_DIR / "tikz-standalone-styles.tex"
SITE_ROOT = SCRIPT_DIR.parent.resolve()
BOOKS_ROOT = Path("/Users/thorfuchs/Books/PantaRhei-2ndEd")

STANDALONE_TEMPLATE = r"""\documentclass[tikz,border=4pt]{standalone}
\usepackage{amsmath,amssymb}
\usepackage{xcolor}
\usepackage{tikz}
\usepackage{tikz-cd}
\usetikzlibrary{positioning,calc,shapes.geometric,arrows.meta,matrix,decorations.pathreplacing,decorations.markings}
\input{%(styles)s}
\begin{document}
%(body)s
\end{document}
"""


class ConversionError(Exception):
    """Raised when any step in the pipeline fails."""


def extract_figure_block(tex_path: Path, label: str) -> str:
    """Find the \\begin{figure}...\\end{figure} block containing the given label.

    Returns the full figure block as a string. Raises if not found.
    """
    text = tex_path.read_text(encoding="utf-8")

    # Find all figure environments
    figure_pattern = re.compile(
        r"\\begin\{figure\*?\}.*?\\end\{figure\*?\}",
        re.DOTALL,
    )
    for match in figure_pattern.finditer(text):
        block = match.group(0)
        if f"\\label{{{label}}}" in block:
            return block

    raise ConversionError(
        f"Figure label '{label}' not found in {tex_path}"
    )


def extract_tikzpicture(figure_block: str) -> str:
    """Extract the \\begin{tikzpicture}...\\end{tikzpicture} portion from a figure block.

    If the figure contains a tikz-cd block, use that instead.
    """
    # Prefer tikzpicture if present
    tikz_pattern = re.compile(
        r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}",
        re.DOTALL,
    )
    tikz_match = tikz_pattern.search(figure_block)
    if tikz_match:
        return tikz_match.group(0)

    # Fall back to tikzcd
    tikzcd_pattern = re.compile(
        r"\\begin\{tikzcd\}.*?\\end\{tikzcd\}",
        re.DOTALL,
    )
    tikzcd_match = tikzcd_pattern.search(figure_block)
    if tikzcd_match:
        return tikzcd_match.group(0)

    raise ConversionError("No tikzpicture or tikzcd environment found in figure block")


def compile_standalone(tikz_body: str, work_dir: Path) -> Path:
    """Compile a standalone .tex file containing tikz_body. Returns path to PDF."""
    tex_file = work_dir / "diagram.tex"
    content = STANDALONE_TEMPLATE % {
        "styles": str(STANDALONE_STYLES).replace("\\", "/"),
        "body": tikz_body,
    }
    tex_file.write_text(content, encoding="utf-8")

    result = subprocess.run(
        ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "diagram.tex"],
        cwd=work_dir,
        capture_output=True,
        text=True,
    )

    pdf_file = work_dir / "diagram.pdf"
    if not pdf_file.exists():
        # Show last 30 lines of output for diagnostics
        tail = "\n".join(result.stdout.splitlines()[-30:])
        raise ConversionError(
            f"lualatex failed to produce PDF:\n{tail}"
        )

    return pdf_file


def pdf_to_svg(pdf_file: Path, output_svg: Path) -> None:
    """Convert PDF to SVG using pdf2svg."""
    output_svg.parent.mkdir(parents=True, exist_ok=True)

    result = subprocess.run(
        ["pdf2svg", str(pdf_file), str(output_svg)],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0 or not output_svg.exists():
        raise ConversionError(
            f"pdf2svg failed: {result.stderr}\n{result.stdout}"
        )


def optimize_svg(svg_file: Path) -> None:
    """Light optimization: strip extraneous whitespace and comments."""
    content = svg_file.read_text(encoding="utf-8")
    # Remove XML comments
    content = re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL)
    # Collapse blank lines
    content = re.sub(r"\n\s*\n", "\n", content)
    svg_file.write_text(content.strip() + "\n", encoding="utf-8")


def convert_one(tex_file: Path, label: str, output_svg: Path, verbose: bool = True) -> None:
    """Run the full pipeline for a single diagram."""
    if not tex_file.exists():
        raise ConversionError(f"Source .tex not found: {tex_file}")
    if not STANDALONE_STYLES.exists():
        raise ConversionError(f"Standalone styles not found: {STANDALONE_STYLES}")

    if verbose:
        print(f"  Extracting {label} from {tex_file.name}")

    figure_block = extract_figure_block(tex_file, label)
    tikz_body = extract_tikzpicture(figure_block)

    with tempfile.TemporaryDirectory() as tmp:
        work_dir = Path(tmp)
        if verbose:
            print(f"  Compiling with lualatex...")
        pdf_file = compile_standalone(tikz_body, work_dir)

        if verbose:
            print(f"  Converting PDF → SVG...")
        pdf_to_svg(pdf_file, output_svg)

    optimize_svg(output_svg)

    size = output_svg.stat().st_size
    if verbose:
        try:
            rel = output_svg.resolve().relative_to(SITE_ROOT)
            display = str(rel)
        except ValueError:
            display = str(output_svg)
        print(f"  ✓ {display} ({size:,} bytes)")


def resolve_tex_path(tex_ref: str) -> Path:
    """Resolve a tex file reference to an absolute path.

    Accepts: absolute paths, or relative paths starting with 'books/'.
    """
    if tex_ref.startswith("/"):
        return Path(tex_ref)
    if tex_ref.startswith("books/"):
        return BOOKS_ROOT / tex_ref
    # Try both interpretations
    abs_path = Path(tex_ref)
    if abs_path.exists():
        return abs_path
    books_path = BOOKS_ROOT / tex_ref
    if books_path.exists():
        return books_path
    raise ConversionError(f"Cannot resolve tex file path: {tex_ref}")


def convert_mapping(mapping_file: Path, book_filter: str = None) -> dict:
    """Process a batch mapping file. Returns stats dict."""
    mapping = json.loads(mapping_file.read_text(encoding="utf-8"))

    stats = {"total": 0, "succeeded": 0, "failed": 0, "errors": []}

    for module_slug, module_data in mapping.items():
        if book_filter and module_data.get("source_book") != book_filter:
            continue

        diagrams = module_data.get("diagrams", [])
        if not diagrams:
            continue

        book = module_data["source_book"]
        book_dir_name = f"book-{book.lower()}"
        output_dir = SITE_ROOT / "assets" / "diagrams" / "framework" / book_dir_name

        for idx, diag in enumerate(diagrams):
            stats["total"] += 1

            # Generate output filename
            label = diag["label"]
            # Extract short id from label: fig:bookI-ch01-generators-order → generators-order
            short_id = re.sub(r"^fig:book[IVX]+-ch\d+-", "", label)
            if idx > 0:
                output_file = output_dir / f"{module_slug}-{short_id}.svg"
            else:
                output_file = output_dir / f"{module_slug}-{short_id}.svg"

            try:
                tex_path = resolve_tex_path(diag["tex_file"])
                print(f"\n[{module_slug}] diagram {idx+1}/{len(diagrams)}")
                convert_one(tex_path, label, output_file, verbose=True)
                stats["succeeded"] += 1
            except ConversionError as e:
                print(f"  ✗ FAILED: {e}", file=sys.stderr)
                stats["failed"] += 1
                stats["errors"].append({
                    "module": module_slug,
                    "label": label,
                    "error": str(e),
                })

    return stats


def main():
    parser = argparse.ArgumentParser(
        description="Convert TikZ figures from book manuscripts to SVG.",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--mapping", help="Path to batch mapping JSON")
    group.add_argument("--tex-file", help="Single-mode: source .tex path")

    parser.add_argument("--label", help="Single-mode: figure label to extract")
    parser.add_argument("--output", help="Single-mode: output SVG path")
    parser.add_argument("--book", help="Batch mode: filter to one book (I, II, …)")

    args = parser.parse_args()

    # Verify tools
    if not shutil.which("lualatex"):
        print("ERROR: lualatex not found on PATH", file=sys.stderr)
        sys.exit(1)
    if not shutil.which("pdf2svg"):
        print("ERROR: pdf2svg not found on PATH (brew install pdf2svg)", file=sys.stderr)
        sys.exit(1)

    if args.mapping:
        mapping_file = Path(args.mapping)
        if not mapping_file.exists():
            print(f"ERROR: mapping file not found: {mapping_file}", file=sys.stderr)
            sys.exit(1)
        stats = convert_mapping(mapping_file, book_filter=args.book)
        print(f"\n{'='*60}")
        print(f"  Total:     {stats['total']}")
        print(f"  Succeeded: {stats['succeeded']}")
        print(f"  Failed:    {stats['failed']}")
        if stats["errors"]:
            print(f"\n  Errors:")
            for err in stats["errors"]:
                print(f"    - {err['module']} / {err['label']}")
                print(f"      {err['error']}")
        sys.exit(1 if stats["failed"] > 0 else 0)

    # Single mode
    if not args.label or not args.output:
        parser.error("--tex-file requires --label and --output")

    try:
        convert_one(Path(args.tex_file), args.label, Path(args.output))
    except ConversionError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
