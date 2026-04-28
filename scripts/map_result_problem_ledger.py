#!/usr/bin/env python3
"""Map Results pages to public Problem Ledger item IDs.

The mapper is intentionally conservative. It writes only direct, high-confidence
relations into Result page frontmatter and mirrors the same field into
_data/results/results.json. Ambiguous candidates are reported, not applied.
"""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from collections import defaultdict
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT_PAGES = ROOT / "results" / "problem"
RESULTS_JSON = ROOT / "_data" / "results" / "results.json"
PROBLEM_LEDGER_JSON = ROOT / "_data" / "problem_ledger" / "problem-ledger.json"
REPORT_PATH = ROOT / "specs" / "results" / "problem-ledger-mapping-audit.md"


DOMAIN_MAP = {
    "biology": "life",
    "life": "life",
    "mathematics": "mathematics",
    "metaphysics": "metaphysics_philosophy",
    "philosophy": "metaphysics_philosophy",
    "physics": "physics",
}


# Explicit editorial mappings for high-confidence relations that are not same-
# domain exact slug matches. These are deliberately narrow.
MANUAL_MAPPINGS = {
    "free-will-as-branching": [
        "life-biology-free-will",
        "life-neuroscience-free-will-particularly-the-neuroscience-of-free-will",
    ],
    "free-will-and-moral-responsibility": [
        "life-biology-free-will",
        "life-neuroscience-free-will-particularly-the-neuroscience-of-free-will",
    ],
    "quantum-computing": ["phys-temperature"],
    "galaxy-rotation-curves-without-dark-matter": [
        "phys-dark-matter",
        "phys-galaxy-rotation-problem",
    ],
    "flat-rotation-curves": [
        "phys-dark-matter",
        "phys-galaxy-rotation-problem",
    ],
    "lithium-7-problem-resolved": ["phys-the-lithium-problem"],
    "dark-sector-closure": ["phys-dark-matter", "phys-dark-energy"],
}


EXPECTED_EXAMPLES = {
    "hubble-tension": "phys-hubble-tension",
    "riemann-hypothesis": "math-riemann-hypothesis",
    "no-dark-matter-particle": "phys-dark-matter",
    "abiogenesis-inevitability": "life-origin-of-life",
    "consciousness-global-section": "life-consciousness",
    "free-will-as-branching": "life-biology-free-will",
    "why-something-rather-than-nothing": "meta-why-something-rather-than-nothing",
    "quantum-computing": "phys-temperature",
}


def normalize(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text or "")
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = text.lower()
    text = text.replace("&", " and ")
    text = re.sub(r"\b(the|a|an|is|there|of|and)\b", " ", text)
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def split_frontmatter(text: str) -> tuple[str, str, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing opening frontmatter delimiter")
    marker = "\n---"
    end = text.find(marker, 4)
    if end == -1:
        raise ValueError("missing closing frontmatter delimiter")
    return text[:4], text[4:end], text[end:]


def parse_scalar(frontmatter: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.+)$", frontmatter, re.MULTILINE)
    if not match:
        return ""
    value = match.group(1).strip()
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def parse_result_page(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    _, frontmatter, _ = split_frontmatter(text)
    slug = path.stem
    layer = parse_scalar(frontmatter, "layer")
    topic = parse_scalar(frontmatter, "topic")
    return {
        "path": path,
        "slug": slug,
        "result_id": parse_scalar(frontmatter, "result_id"),
        "title": parse_scalar(frontmatter, "title"),
        "topic": topic,
        "layer": layer,
        "domain": DOMAIN_MAP.get(layer) or DOMAIN_MAP.get(topic) or layer or topic,
        "frontmatter": frontmatter,
        "text": text,
    }


def yaml_array(values: list[str]) -> str:
    if not values:
        return "[]"
    return "[" + ", ".join(json.dumps(value, ensure_ascii=False) for value in values) + "]"


def upsert_problem_ledger_ids(path: Path, ids: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    open_delim, frontmatter, rest = split_frontmatter(text)
    replacement = f"problem_ledger_ids: {yaml_array(ids)}"

    if re.search(r"^problem_ledger_ids:", frontmatter, re.MULTILINE):
        frontmatter = re.sub(
            r"^problem_ledger_ids:\s*(?:\[.*?\]|(?:\n\s+-\s+.*?)+)",
            replacement,
            frontmatter,
            flags=re.MULTILINE,
        )
    elif re.search(r"^result_id:", frontmatter, re.MULTILINE):
        frontmatter = re.sub(
            r"^(result_id:\s*.+)$",
            r"\1\n" + replacement,
            frontmatter,
            count=1,
            flags=re.MULTILINE,
        )
    else:
        frontmatter = frontmatter.rstrip() + "\n" + replacement + "\n"

    path.write_text(open_delim + frontmatter + rest, encoding="utf-8")


def build_problem_indexes(problems: list[dict]) -> tuple[dict, dict, dict]:
    by_id = {problem["id"]: problem for problem in problems}
    by_slug = {problem["slug"]: problem for problem in problems}
    by_normalized_title: dict[str, list[dict]] = defaultdict(list)
    for problem in problems:
        for key in ("title", "short_title"):
            title_key = normalize(problem.get(key, ""))
            if title_key:
                by_normalized_title[title_key].append(problem)
    return by_id, by_slug, by_normalized_title


def explicit_problem_relations(problems: list[dict]) -> dict[str, set[str]]:
    mapped: dict[str, set[str]] = defaultdict(set)
    for problem in problems:
        problem_id = problem["id"]
        mirror_id = (problem.get("results_mirror") or {}).get("result_id") or ""
        if mirror_id:
            mapped[mirror_id].add(problem_id)
        for result_id in (problem.get("related") or {}).get("results") or []:
            if result_id:
                mapped[result_id].add(problem_id)
    return mapped


def source_terms(problem: dict) -> set[str]:
    terms = {problem.get("slug", ""), problem.get("title", ""), problem.get("short_title", "")}
    source = problem.get("source") or {}
    terms.add(source.get("source_item_anchor", ""))
    for record in source.get("source_entry_records") or []:
        terms.add(record.get("source_title", ""))
    return {normalize(term) for term in terms if normalize(term)}


def compute_mappings(pages: list[dict], problems: list[dict]) -> tuple[dict[str, list[str]], list[dict]]:
    by_id, by_slug, by_title = build_problem_indexes(problems)
    explicit = explicit_problem_relations(problems)
    uncertain: list[dict] = []
    mappings: dict[str, list[str]] = {}

    problem_terms = {problem["id"]: source_terms(problem) for problem in problems}

    for page in pages:
        ids: set[str] = set()
        reasons: dict[str, str] = {}
        slug = page["slug"]
        title_key = normalize(page["title"])

        for problem_id in explicit.get(page["result_id"], set()):
            ids.add(problem_id)
            reasons[problem_id] = "existing Problem Ledger result relation"

        if slug in by_slug:
            ids.add(by_slug[slug]["id"])
            reasons[by_slug[slug]["id"]] = "exact slug match"

        title_matches = by_title.get(title_key, [])
        if len(title_matches) == 1:
            ids.add(title_matches[0]["id"])
            reasons[title_matches[0]["id"]] = "exact normalized title match"

        for problem_id in MANUAL_MAPPINGS.get(slug, []):
            if problem_id not in by_id:
                raise ValueError(f"manual mapping references unknown Problem Ledger ID: {problem_id}")
            ids.add(problem_id)
            reasons[problem_id] = "manual high-confidence editorial mapping"

        for problem in problems:
            problem_id = problem["id"]
            if problem_id in ids:
                continue
            if problem.get("domain") != page["domain"]:
                continue
            problem_slug = problem.get("slug", "")
            if len(problem_slug) >= 8 and len(slug) >= 8 and (
                problem_slug in slug or slug in problem_slug
            ):
                ids.add(problem_id)
                reasons[problem_id] = "same-domain slug containment"
                continue
            if title_key and title_key in problem_terms[problem_id]:
                ids.add(problem_id)
                reasons[problem_id] = "same-domain source-title containment"

        # Record plausible but not applied cross-domain title overlaps for audit review.
        for problem in problems:
            problem_id = problem["id"]
            if problem_id in ids:
                continue
            shared = problem_terms[problem_id]
            if title_key and title_key in shared:
                uncertain.append(
                    {
                        "result_slug": slug,
                        "result_title": page["title"],
                        "candidate_problem_id": problem_id,
                        "candidate_problem_title": problem["title"],
                        "reason": "cross-domain exact title/source-title overlap",
                    }
                )

        mappings[slug] = sorted(ids)
        page["_mapping_reasons"] = {problem_id: reasons.get(problem_id, "") for problem_id in mappings[slug]}

    for result_slug, expected_problem_id in EXPECTED_EXAMPLES.items():
        if expected_problem_id not in mappings.get(result_slug, []):
            raise AssertionError(
                f"expected mapping missing: {result_slug} -> {expected_problem_id}"
            )

    return mappings, uncertain


def page_record_from_frontmatter(page: dict) -> dict:
    canonical_books = []
    books_match = re.search(r"^canonical_books:\s*\[(.*?)\]\s*$", page["frontmatter"], re.MULTILINE)
    if books_match:
        canonical_books = [
            item.strip().strip('"').strip("'")
            for item in books_match.group(1).split(",")
            if item.strip()
        ]
    return {
        "id": page["result_id"],
        "slug": page["slug"],
        "title": page["title"],
        "topic": page["topic"],
        "layer": page["layer"],
        "result_type": parse_scalar(page["frontmatter"], "result_type"),
        "bridge_status": parse_scalar(page["frontmatter"], "bridge_status"),
        "summary_short": parse_scalar(page["frontmatter"], "summary_short"),
        "url": f"/results/problem/{page['slug']}/",
        "canonical_books": canonical_books,
        "result_kind": parse_scalar(page["frontmatter"], "result_kind"),
        "importance_class": parse_scalar(page["frontmatter"], "importance_class"),
        "status_code": parse_scalar(page["frontmatter"], "status_code"),
        "domain_group": parse_scalar(page["frontmatter"], "domain_group"),
        "primary_domain": page["domain"],
        "secondary_domains": [],
        "stance_type": "",
    }


def update_results_json(pages: list[dict], mappings: dict[str, list[str]], write: bool) -> list[dict]:
    records = json.loads(RESULTS_JSON.read_text(encoding="utf-8"))
    by_id = {record["id"]: record for record in records}
    added: list[dict] = []

    for page in pages:
        record = by_id.get(page["result_id"])
        if record is None:
            record = page_record_from_frontmatter(page)
            records.append(record)
            by_id[record["id"]] = record
            added.append(record)
        record["problem_ledger_ids"] = mappings[page["slug"]]

    def sort_key(record: dict) -> tuple[int, str]:
        match = re.search(r"(\d+)$", record.get("id", ""))
        return (int(match.group(1)) if match else 999999, record.get("id", ""))

    records.sort(key=sort_key)
    if write:
        RESULTS_JSON.write_text(
            json.dumps(records, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    return added


def write_report(
    pages: list[dict],
    problems: list[dict],
    mappings: dict[str, list[str]],
    uncertain: list[dict],
    added_records: list[dict],
    write: bool,
) -> None:
    mapped_pages = [page for page in pages if mappings[page["slug"]]]
    problem_links = sum(len(ids) for ids in mappings.values())
    lines = [
        "# Result Items ↔ Problem Ledger Mapping Audit",
        "",
        f"Date: {date.today().isoformat()}",
        "",
        "## Summary",
        "",
        f"- Result pages reviewed: {len(pages)}",
        f"- Problem Ledger items available: {len(problems)}",
        f"- Result pages with at least one mapped Problem Ledger item: {len(mapped_pages)}",
        f"- Result pages left unmapped: {len(pages) - len(mapped_pages)}",
        f"- Total Result → Problem Ledger links written: {problem_links}",
        f"- Result records added to `_data/results/results.json` for page parity: {len(added_records)}",
        f"- Uncertain candidates intentionally left unmapped: {len(uncertain)}",
        "",
        "## Mapping Policy",
        "",
        "Mappings are conservative. A Problem Ledger ID is written only when the Result page directly addresses, partially addresses, reframes, or records the current program stance for that public Problem Ledger item. Broad foundation results are not mapped to downstream problems unless the relation is explicit or title/slug-level direct.",
        "",
        "## High-Confidence Mappings",
        "",
    ]

    for page in sorted(mapped_pages, key=lambda item: item["slug"]):
        ids = mappings[page["slug"]]
        lines.append(f"### `{page['slug']}` — {page['title']}")
        lines.append("")
        lines.append(f"- Result ID: `{page['result_id']}`")
        lines.append(f"- Result page: `/results/problem/{page['slug']}/`")
        for problem_id in ids:
            reason = page.get("_mapping_reasons", {}).get(problem_id, "")
            lines.append(f"- Problem Ledger: `{problem_id}` ({reason})")
        lines.append("")

    if added_records:
        lines += ["## JSON Parity Additions", ""]
        for record in added_records:
            lines.append(f"- `{record['id']}` — `{record['slug']}`")
        lines.append("")

    lines += ["## Uncertain Candidates Left Unmapped", ""]
    if uncertain:
        for item in sorted(uncertain, key=lambda x: (x["result_slug"], x["candidate_problem_id"])):
            lines.append(
                f"- `{item['result_slug']}` ({item['result_title']}) → "
                f"`{item['candidate_problem_id']}` ({item['candidate_problem_title']}): "
                f"{item['reason']}"
            )
    else:
        lines.append("- None.")
    lines.append("")

    if write:
        REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
        REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="write frontmatter, JSON, and audit report")
    args = parser.parse_args()

    pages = [parse_result_page(path) for path in sorted(RESULT_PAGES.glob("*.md"))]
    problems = json.loads(PROBLEM_LEDGER_JSON.read_text(encoding="utf-8"))
    mappings, uncertain = compute_mappings(pages, problems)

    added_records = update_results_json(pages, mappings, args.write)

    if args.write:
        for page in pages:
            upsert_problem_ledger_ids(page["path"], mappings[page["slug"]])

    write_report(pages, problems, mappings, uncertain, added_records, args.write)

    mapped = sum(1 for ids in mappings.values() if ids)
    print(f"result pages reviewed: {len(pages)}")
    print(f"mapped pages: {mapped}")
    print(f"unmapped pages: {len(pages) - mapped}")
    print(f"total links: {sum(len(ids) for ids in mappings.values())}")
    print(f"json parity additions: {len(added_records)}")
    print(f"uncertain candidates: {len(uncertain)}")
    if not args.write:
        print("dry run only; pass --write to update files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
