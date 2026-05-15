#!/usr/bin/env python3
"""Clean Jekyll-expanded dossier Markdown, render Typst, and compile PDFs."""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urljoin


SITE_URL = "https://panta-rhei.site"


def load_manifest(built_root: Path) -> dict[str, Any]:
    path = built_root / "assets" / "dossier-manifest.json"
    if not path.exists():
        raise SystemExit(f"Missing dossier manifest: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not data.get("entries"):
        raise SystemExit(f"Dossier manifest has no entries: {path}")
    return data


def artifact_path(built_root: Path, public_path: str) -> Path:
    return built_root / public_path.strip("/")


def absolutize_url(url: str) -> str:
    if url.startswith(("http://", "https://", "mailto:", "#")):
        return url
    return urljoin(SITE_URL + "/", url.lstrip("/"))


def strip_jekyll_noise(markdown: str) -> str:
    markdown = re.sub(r"<!--.*?-->", "", markdown, flags=re.S)
    markdown = markdown.replace("\r\n", "\n")
    markdown = re.sub(r"\n{4,}", "\n\n\n", markdown)
    return markdown.strip() + "\n"


def replace_formula_blocks(markdown: str) -> str:
    def repl(match: re.Match[str]) -> str:
        block = match.group(0)
        fallback = re.search(r'<p[^>]*class="[^"]*formula-fallback[^"]*"[^>]*>(.*?)</p>', block, re.S)
        if fallback:
            text = html_to_text(fallback.group(1))
        else:
            text = html_to_text(block)
        return f"\n\n{text.strip()}\n\n"

    return re.sub(r'<div[^>]*class="[^"]*formula-block[^"]*"[^>]*>.*?</div>', repl, markdown, flags=re.S)


def replace_known_html(markdown: str) -> str:
    def link_repl(match: re.Match[str]) -> str:
        href = absolutize_url(html.unescape(match.group(1)))
        text = html_to_text(match.group(2)).strip() or href
        return f"[{text}]({href})"

    markdown = replace_formula_blocks(markdown)
    markdown = re.sub(r'<a\b[^>]*href="([^"]+)"[^>]*>(.*?)</a>', link_repl, markdown, flags=re.S)
    markdown = re.sub(r'<br\s*/?>', "\n", markdown, flags=re.I)
    markdown = re.sub(r'</(p|li|h[1-6]|div|section|article|figure|figcaption|ul|ol|table|tr)>', "\n", markdown, flags=re.I)
    markdown = re.sub(r'<li\b[^>]*>', "\n- ", markdown, flags=re.I)
    markdown = re.sub(r'<[^>]+>', "", markdown)
    return html.unescape(markdown)


def html_to_text(value: str) -> str:
    value = re.sub(r"<br\s*/?>", "\n", value, flags=re.I)
    value = re.sub(r"<[^>]+>", " ", value)
    value = html.unescape(value)
    return re.sub(r"[ \t]+", " ", value).strip()


def absolutize_markdown_links(markdown: str) -> str:
    def repl(match: re.Match[str]) -> str:
        label = match.group(1)
        url = match.group(2)
        return f"[{label}]({absolutize_url(url)})"

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl, markdown)


def clean_markdown(markdown: str) -> str:
    markdown = replace_known_html(markdown)
    markdown = absolutize_markdown_links(markdown)
    markdown = re.sub(r"[ \t]+\n", "\n", markdown)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    markdown = strip_jekyll_noise(markdown)
    if "{%" in markdown or "{{" in markdown:
        raise SystemExit("Unresolved Liquid detected in dossier Markdown")
    return markdown


def typst_escape(value: str) -> str:
    replacements = {
        "\\": "\\\\",
        "#": "\\#",
        "$": "\\$",
        "[": "\\[",
        "]": "\\]",
        "_": "\\_",
        "^": "\\^",
        "&": "\\&",
        "%": "\\%",
    }
    for old, new in replacements.items():
        value = value.replace(old, new)
    return value


def typst_string(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")


def inline_to_typst(text: str) -> str:
    chunks: list[str] = []
    cursor = 0
    for match in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", text):
        chunks.append(typst_escape(strip_inline_marks(text[cursor : match.start()])))
        label = typst_escape(strip_inline_marks(match.group(1)))
        url = typst_string(match.group(2))
        chunks.append(f'#link("{url}")[{label}]')
        cursor = match.end()
    chunks.append(typst_escape(strip_inline_marks(text[cursor:])))
    return "".join(chunks)


def strip_inline_marks(text: str) -> str:
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"__([^_]+)__", r"\1", text)
    return text


def table_to_typst(rows: list[str]) -> str:
    parsed: list[list[str]] = []
    for row in rows:
        cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
        if cells:
            parsed.append(cells)
    if len(parsed) < 2:
        return "\n".join(inline_to_typst(row) for row in rows)
    if re.match(r"^:?-{3,}:?$", parsed[1][0]):
        parsed.pop(1)
    columns = max(len(row) for row in parsed)
    cells: list[str] = []
    for row_index, row in enumerate(parsed):
        padded = row + [""] * (columns - len(row))
        for cell in padded:
            text = inline_to_typst(cell)
            if row_index == 0:
                text = f"*{text}*"
            cells.append(f"[{text}]")
    return (
        "#table(\n"
        f"  columns: {columns},\n"
        '  stroke: rgb("#d8ded2"),\n'
        "  inset: 4pt,\n"
        "  " + ",\n  ".join(cells) + ",\n"
        ")\n"
    )


def markdown_to_typst(markdown: str) -> str:
    lines = markdown.splitlines()
    out: list[str] = []
    paragraph: list[str] = []
    i = 0
    in_code = False

    def flush_paragraph() -> None:
        if paragraph:
            out.append(inline_to_typst(" ".join(part.strip() for part in paragraph if part.strip())))
            out.append("")
            paragraph.clear()

    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("```"):
            flush_paragraph()
            out.append("```")
            in_code = not in_code
            i += 1
            continue
        if in_code:
            out.append(line)
            i += 1
            continue
        if not line.strip():
            flush_paragraph()
            i += 1
            continue
        table_candidate = line.strip().startswith("|") and "|" in line.strip()[1:]
        if table_candidate and i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$", lines[i + 1]):
            flush_paragraph()
            table_rows = [line, lines[i + 1]]
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_rows.append(lines[i])
                i += 1
            out.append(table_to_typst(table_rows))
            out.append("")
            continue
        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading:
            flush_paragraph()
            level = len(heading.group(1))
            out.append("=" * level + " " + inline_to_typst(heading.group(2).strip()))
            out.append("")
            i += 1
            continue
        bullet = re.match(r"^(\s*)[-*]\s+(.+)$", line)
        if bullet:
            flush_paragraph()
            indent = "  " * (len(bullet.group(1)) // 2)
            out.append(f"{indent}- {inline_to_typst(bullet.group(2).strip())}")
            i += 1
            continue
        numbered = re.match(r"^(\s*)\d+\.\s+(.+)$", line)
        if numbered:
            flush_paragraph()
            indent = "  " * (len(numbered.group(1)) // 2)
            out.append(f"{indent}+ {inline_to_typst(numbered.group(2).strip())}")
            i += 1
            continue
        quote = re.match(r"^>\s*(.+)$", line)
        if quote:
            flush_paragraph()
            out.append(
                '#block(fill: rgb("#f6f7f3"), stroke: (left: 1pt + rgb("#163e64")), inset: 8pt, radius: 3pt)['
            )
            out.append(inline_to_typst(quote.group(1).strip()))
            out.append("]")
            out.append("")
            i += 1
            continue
        paragraph.append(line)
        i += 1

    flush_paragraph()
    return "\n".join(out).strip() + "\n"


def write_typst(entry: dict[str, Any], markdown: str, built_root: Path, generated_at: str) -> Path:
    typ_path = artifact_path(built_root, entry["typst_path"])
    typ_path.parent.mkdir(parents=True, exist_ok=True)
    template_target = built_root / "templates" / "typst" / "panta-rhei-dossier.typ"
    template_target.parent.mkdir(parents=True, exist_ok=True)
    template_source = Path("templates/typst/panta-rhei-dossier.typ")
    if template_source.exists():
        shutil.copyfile(template_source, template_target)
    body = markdown_to_typst(markdown)
    typ_path.write_text(
        '#import "../../templates/typst/panta-rhei-dossier.typ": dossier\n\n'
        "#show: dossier.with(\n"
        f'  title: "{typst_string(entry["title"])}",\n'
        f'  description: "{typst_string(entry.get("description", ""))}",\n'
        f'  canonical_url: "{typst_string(entry["url"])}",\n'
        f'  kind: "{typst_string(entry.get("kind", ""))}",\n'
        f'  status: "{typst_string(entry.get("status", ""))}",\n'
        f'  review_angle: "{typst_string(entry.get("review_angle", ""))}",\n'
        f'  generated: "{typst_string(generated_at)}",\n'
        ")\n\n"
        + body,
        encoding="utf-8",
    )
    return typ_path


def compile_pdf(typ_path: Path, pdf_path: Path, built_root: Path) -> None:
    typst = shutil.which("typst")
    if not typst:
        raise SystemExit("Typst is required for dossier PDF generation. Install typst 0.14.2.")
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [typst, "compile", "--root", str(built_root), str(typ_path), str(pdf_path)],
        check=True,
    )


def build_dossiers(built_root: Path) -> dict[str, Any]:
    manifest = load_manifest(built_root)
    generated_at = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    results: list[dict[str, Any]] = []
    for entry in manifest["entries"]:
        markdown_path = artifact_path(built_root, entry["markdown_path"])
        if not markdown_path.exists():
            raise SystemExit(f"Missing expanded Markdown export: {markdown_path}")
        clean = clean_markdown(markdown_path.read_text(encoding="utf-8"))
        markdown_path.write_text(clean, encoding="utf-8")
        typ_path = write_typst(entry, clean, built_root, generated_at)
        pdf_path = artifact_path(built_root, entry["pdf_path"])
        compile_pdf(typ_path, pdf_path, built_root)
        results.append(
            {
                "slug": entry["slug"],
                "route": entry["route"],
                "markdown_path": entry["markdown_path"],
                "markdown_bytes": markdown_path.stat().st_size,
                "typst_path": entry["typst_path"],
                "typst_bytes": typ_path.stat().st_size,
                "pdf_path": entry["pdf_path"],
                "pdf_bytes": pdf_path.stat().st_size,
            }
        )
    report = {
        "schema_version": "1.0",
        "generated_at": generated_at,
        "entry_count": len(results),
        "entries": results,
    }
    report_path = built_root / "assets" / "dossier-build-report.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--built-root", default="_site", help="Built Jekyll output root")
    args = parser.parse_args()
    report = build_dossiers(Path(args.built_root).resolve())
    print(f"Built {report['entry_count']} dossiers")
    return 0


if __name__ == "__main__":
    sys.exit(main())
