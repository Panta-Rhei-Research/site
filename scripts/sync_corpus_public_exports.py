#!/usr/bin/env python3
"""Sync public Corpus projections into the v2 site worktree."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
from collections import Counter
from pathlib import Path
from typing import Any


SITE_ROOT = Path(__file__).resolve().parents[1]
ORG_ROOT = SITE_ROOT.parent
CORPUS_EXPORTS = Path(os.environ.get("CORPUS_EXPORTS_DIR", ORG_ROOT / "corpus" / "exports" / "public"))
TAULIB_PROJECTION_PIN = "cb5e83015b54dd72eba560953fe2461820078757"
STALE_TAULIB_SOURCE_PINS = (
    "37c12411e76f4bb89f7bc463d1443eecc0bd9afe",
)


def copy_file(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    print(f"synced {target.relative_to(SITE_ROOT)}")


def copy_tree(source: Path, target: Path) -> None:
    target.mkdir(parents=True, exist_ok=True)
    for path in sorted(source.rglob("*")):
        if path.is_file():
            copy_file(path, target / path.relative_to(source))


def copy_tree_filtered(source: Path, target: Path, suffixes: set[str]) -> None:
    if target.exists():
        shutil.rmtree(target)
    target.mkdir(parents=True, exist_ok=True)
    for path in sorted(source.rglob("*")):
        if path.is_file() and path.suffix in suffixes:
            copy_file(path, target / path.relative_to(source))


def normalize_taulib_projection_routes(path: Path) -> None:
    if not path.exists() or not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    normalized = text.replace("/verify/taulib/docs/", "/corpus/taulib/docs/")
    for stale_pin in STALE_TAULIB_SOURCE_PINS:
        normalized = normalized.replace(stale_pin, TAULIB_PROJECTION_PIN)
    if normalized != text:
        path.write_text(normalized, encoding="utf-8")


def normalize_taulib_projection_tree(root: Path) -> None:
    if not root.exists():
        return
    for path in sorted(root.rglob("*")):
        if path.suffix in {".csv", ".json", ".md", ".ndjson"}:
            normalize_taulib_projection_routes(path)


def normalize_monograph_projection_routes(path: Path) -> None:
    if not path.exists() or not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    normalized = (
        text.replace("/corpus/construction-map/", "/corpus/construction-spine/")
        .replace("[Construction Map]", "[Construction Spine]")
        .replace("the [Construction Map]", "the [Construction Spine]")
    )
    if normalized != text:
        path.write_text(normalized, encoding="utf-8")


def clean_generated_tree(
    target: Path,
    suffixes: tuple[str, ...] = (".md", ".json", ".csv", ".ndjson"),
    preserve_names: set[str] | None = None,
) -> None:
    if not target.exists():
        return
    preserve_names = preserve_names or set()
    for path in sorted(target.rglob("*"), reverse=True):
        if path.is_file() and path.suffix in suffixes and path.name not in preserve_names:
            path.unlink()
    for path in sorted(target.rglob("*"), reverse=True):
        if path.is_dir():
            try:
                path.rmdir()
            except OSError:
                pass


def read_json(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return data if isinstance(data, list) else data.get("items", [])


def yaml_scalar(value: Any) -> str:
    if value is None:
        return '""'
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value)
    if text == "":
        return '""'
    return json.dumps(text, ensure_ascii=False)


def yaml_dump(data: dict[str, Any], indent: int = 0) -> str:
    lines: list[str] = []
    pad = " " * indent
    for key, value in data.items():
        if isinstance(value, dict):
            lines.append(f"{pad}{key}:")
            lines.append(yaml_dump(value, indent + 2))
        elif isinstance(value, list):
            if not value:
                lines.append(f"{pad}{key}: []")
            else:
                lines.append(f"{pad}{key}:")
                for item in value:
                    if isinstance(item, dict):
                        lines.append(f"{pad}  -")
                        lines.append(yaml_dump(item, indent + 4))
                    else:
                        lines.append(f"{pad}  - {yaml_scalar(item)}")
        else:
            lines.append(f"{pad}{key}: {yaml_scalar(value)}")
    return "\n".join(lines)


def write_markdown(path: Path, frontmatter: dict[str, Any], body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("---\n" + yaml_dump(frontmatter) + "\n---\n\n" + body.strip() + "\n", encoding="utf-8")
    print(f"generated {path.relative_to(SITE_ROOT)}")


def read_frontmatter_scalars_text(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    scalars: dict[str, str] = {}
    for raw_line in parts[1].splitlines():
        if not raw_line or raw_line.startswith((" ", "-", "{", "}", "[")):
            continue
        if ":" not in raw_line:
            continue
        key, raw_value = raw_line.split(":", 1)
        key = key.strip()
        value = raw_value.strip()
        if not key or value == "":
            continue
        try:
            if value.startswith(("\"", "'")):
                value = json.loads(value)
        except json.JSONDecodeError:
            value = value.strip("\"'")
        scalars[key] = str(value)
    return scalars


def read_frontmatter_scalars(path: Path) -> dict[str, str]:
    return read_frontmatter_scalars_text(path.read_text(encoding="utf-8", errors="replace"))


def monograph_stable_key(frontmatter: dict[str, str]) -> str:
    layout = frontmatter.get("layout", "")
    permalink = frontmatter.get("permalink", "")
    book_slug = frontmatter.get("book_slug", "")
    if layout == "redirect" and frontmatter.get("compatibility_key"):
        return frontmatter["compatibility_key"]
    if layout == "corpus-monograph-chapter":
        chapter_number = frontmatter.get("chapter_number", "")
        if book_slug and chapter_number:
            return f"chapter:{book_slug}:{chapter_number}"
    if layout == "corpus-monograph-part":
        title = re.sub(r"\s+", " ", frontmatter.get("title", "").strip())
        title = re.sub(r"^Part\s+[IVXLCDM]+:\s*", "", title)
        if book_slug and title:
            return f"part:{book_slug}:{title}"
    if layout == "corpus-monograph-book" and book_slug:
        return f"book:{book_slug}"
    if permalink == "/corpus/monographs/":
        return "monograph-root"
    return ""


def collect_monograph_routes(root: Path) -> dict[str, dict[str, str]]:
    routes: dict[str, dict[str, str]] = {}
    if not root.exists():
        return routes
    for path in sorted(root.rglob("index.md")):
        frontmatter = read_frontmatter_scalars(path)
        key = monograph_stable_key(frontmatter)
        permalink = frontmatter.get("permalink", "")
        if key and permalink:
            entry = {
                "permalink": permalink,
                "title": frontmatter.get("title", "Corpus monograph page"),
                "relative_path": str(path.relative_to(SITE_ROOT)),
                "layout": frontmatter.get("layout", ""),
            }
            if key not in routes or entry["layout"] == "redirect" or routes[key].get("layout") != "redirect":
                routes[key] = entry
    return routes


def collect_monograph_routes_from_git(ref: str) -> dict[str, dict[str, str]]:
    try:
        listing = subprocess.run(
            ["git", "ls-tree", "-r", "--name-only", ref, "--", "corpus/monographs"],
            cwd=SITE_ROOT,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.splitlines()
    except subprocess.CalledProcessError:
        return {}
    routes: dict[str, dict[str, str]] = {}
    for relative in sorted(path for path in listing if path.endswith("/index.md")):
        try:
            blob = subprocess.run(
                ["git", "show", f"{ref}:{relative}"],
                cwd=SITE_ROOT,
                check=True,
                capture_output=True,
                text=True,
            ).stdout
        except subprocess.CalledProcessError:
            continue
        frontmatter = read_frontmatter_scalars_text(blob)
        key = monograph_stable_key(frontmatter)
        permalink = frontmatter.get("permalink", "")
        if key and permalink:
            entry = {
                "permalink": permalink,
                "title": frontmatter.get("title", "Corpus monograph page"),
                "relative_path": relative,
                "layout": frontmatter.get("layout", ""),
            }
            if key not in routes or entry["layout"] == "redirect" or routes[key].get("layout") != "redirect":
                routes[key] = entry
    return routes


def domain_label(domain: str) -> str:
    return {
        "mathematics": "Mathematics",
        "physics": "Physics",
        "life": "Life",
        "metaphysics": "Metaphysics",
        "metaphysics-philosophy": "Metaphysics / Philosophy",
        "metaphysics_philosophy": "Metaphysics / Philosophy",
    }.get(domain, domain.replace("-", " ").replace("_", " ").title())


def result_status_label(value: str) -> str:
    labels = {
        "R": "Internally addressed",
        "resolved": "Internally addressed",
        "internally_addressed": "Internally addressed",
        "partially_addressed": "Partially addressed",
        "partial": "Partial",
        "not_yet_classified": "Not yet touched",
        "not_addressed": "Not addressed",
        "not_externally_reviewed": "Not externally reviewed",
        "not_yet_verified": "Not yet verified",
        "pending_bridge_verification": "Pending bridge verification",
        "pending_formal_verification": "Pending formal verification",
        "pending_physics_verification": "Pending physics verification",
        "pending_life_verification": "Pending life verification",
        "pending_metaphysics_verification": "Pending metaphysics verification",
        "route_available": "Route available",
    }
    if not value:
        return "Pending"
    return labels.get(value, value.replace("_", " ").replace("-", " ").title())


def domain_counts(items: list[dict[str, Any]]) -> dict[str, int]:
    counts = {"mathematics": 0, "physics": 0, "life": 0, "metaphysics-philosophy": 0}
    for item in items:
        domain = item.get("domain_slug", "")
        counts[domain] = counts.get(domain, 0) + 1
    return counts


def title_from_url(url: str) -> str:
    stripped = url.strip("/")
    if not stripped:
        return "Linked page"
    if stripped.startswith("verify/domain-verification/"):
        return f"Domain Verification: {domain_label(stripped.split('/')[-1])}"
    if stripped == "verify/construction-spine-verification":
        return "Construction Spine Verification"
    if stripped.startswith("results/world-readout/") and stripped.count("/") == 2:
        return f"World Readout: {domain_label(stripped.split('/')[-1])}"
    parts = stripped.split("/")
    last = parts[-1]
    if last in {"index", "browse"} and len(parts) > 1:
        last = parts[-2]
    return last.replace("-", " ").replace("_", " ").title()


def looks_like_identifier(text: str) -> bool:
    return (
        text.startswith(("CS-", "PREC-", "MREC-", "MREF-", "LREC-", "METH-", "phys-", "math-", "life-", "meta-"))
        or (" " not in text and "." in text)
        or text.isupper()
    )


def bullet_lines(items: list[Any], empty_message: str) -> str:
    if not items:
        return f"- {empty_message}"
    lines: list[str] = []
    for item in items:
        if isinstance(item, dict):
            title = item.get("title") or item.get("url") or item.get("id") or "Linked item"
            url = item.get("url", "")
            if url:
                lines.append(f"- [{title}]({url})")
            else:
                lines.append(f"- {title}")
        elif isinstance(item, str) and item.startswith("/"):
            lines.append(f"- [{title_from_url(item)}]({item})")
        else:
            lines.append(f"- `{item}`" if isinstance(item, str) and looks_like_identifier(item) else f"- {item}")
    return "\n".join(lines)


def sync_problem_answer_pages() -> None:
    raise RuntimeError(
        "The v1 Problem Answers projection is retired. Use the v4 Challenge Responses export path instead."
    )


def generate_problem_answer_pages() -> None:
    raise RuntimeError(
        "The v1 Problem Ledger Answers generator is retired. Use the v4 Challenge Responses export path instead."
    )

def generate_recovery_status_pages() -> None:
    items = read_json(CORPUS_EXPORTS / "recovery-requirements.json")
    root = SITE_ROOT / "results" / "recovery-target-status"
    domains = ["mathematics", "physics", "life", "metaphysics"]

    root_body = """> Current program status against the structures the kernel promised to recover.

This is the Results-side mirror of the Program-side Recovery Requirements ledger. Recovery requirements remain obligations; this surface reports their current public status.

<div class="notice note"><strong>Status note.</strong> Partial or internally addressed recovery is not the same as formal verification or external acceptance.</div>

## Browse by domain

{% assign recovery_items = site.data.recovery_requirements["recovery-requirements"] %}
{% assign recovery_domains = "mathematics,physics,life,metaphysics" | split: "," %}
<ul class="v2-grid v2-card-list">
{% for domain in recovery_domains %}
  {% assign domain_items = recovery_items | where: "domain_slug", domain %}
  {% assign partial_count = domain_items | where: "recovery_status", "partial" | size %}
  {% assign not_applicable_count = domain_items | where: "recovery_status", "not_applicable" | size %}
  {% assign pending_count = domain_items | where: "recovery_status", "pending_recovery" | size %}
  {% if partial_count >= not_applicable_count and partial_count >= pending_count %}
    {% assign dominant_status = "Partial" %}
  {% elsif not_applicable_count >= partial_count and not_applicable_count >= pending_count %}
    {% assign dominant_status = "Not applicable / refused" %}
  {% else %}
    {% assign dominant_status = "Pending recovery" %}
  {% endif %}
  <li>
    <article class="v2-tile">
      <h3>{{ domain | replace: '-', ' ' | capitalize }}</h3>
      <p>{{ domain_items | size }} public recovery/refusal item{% unless domain_items.size == 1 %}s{% endunless %}.</p>
      <p><strong>Dominant status:</strong> {{ dominant_status }}</p>
      <p><a href="{{ '/results/recovery-target-status/' | append: domain | append: '/' | relative_url }}">Results mirror</a> · <a href="{{ '/program/research-agenda/recovery-requirements/' | append: domain | append: '/' | relative_url }}">Recovery Requirements</a></p>
    </article>
  </li>
{% endfor %}
</ul>
"""
    write_markdown(
        root / "index.md",
        {
            "layout": "program-doc",
            "title": "Recovery Target Status",
            "permalink": "/results/recovery-target-status/",
            "lane": "results",
            "v2_lane": "results",
            "type": "Result Mirror",
            "status": "Canonical",
            "summary_short": "Current Results-side status against public Recovery Requirements.",
        },
        root_body,
    )

    for domain in domains:
        domain_items = [item for item in items if item["domain_slug"] == domain]
        lines = "\n".join(f"- [{item['title']}]({recovery_result_path(item)}) - {result_status_label(item.get('recovery_status', ''))}" for item in domain_items)
        write_markdown(
            root / domain / "index.md",
            {
                "layout": "program-doc",
                "title": f"Recovery Target Status: {domain_label(domain)}",
                "permalink": f"/results/recovery-target-status/{domain}/",
                "lane": "results",
                "v2_lane": "results",
                "type": "Result Mirror Domain",
                "status": "Canonical",
                "summary_short": f"Current recovery status for {domain_label(domain)} targets.",
            },
            f"""<div class="notice note"><strong>Status note.</strong> Recovery status is internal unless formal or external verification is explicitly linked.</div>

## Items

{lines}
""",
        )

    for item in items:
        related = item.get("related", {})
        verification = item.get("verification", {})
        result_lines = related.get("results") or []
        if result_lines:
            results_body = "\n".join(f"- `{result}`" for result in result_lines)
        else:
            results_body = "- Granular Result mapping pending."
        verify_body = bullet_lines(verification.get("related_verify_pages", related.get("verify", [])), "Dedicated Verify surface pending.")
        corpus_steps_body = bullet_lines(verification.get("related_corpus_steps", related.get("construction_steps", [])), "Construction Spine mapping pending.")
        verification_results_body = bullet_lines(verification.get("related_results", result_lines), "Granular Result mapping pending.")
        body = f"""<div class="notice note"><strong>Status note.</strong> This page reports current recovery status. It does not imply external acceptance unless explicitly stated.</div>

## Status Separation

- Internal status: **{result_status_label(item.get('recovery_status', 'pending'))}**
- Verification state: **{result_status_label(verification.get('status', item.get('verification_status', 'not_yet_verified')))}**
- External status: **Not externally reviewed**

## Requirement

{item.get('public_summary') or item.get('short_title', item['title'])}

## Current Recovery Status

- Recovery status: **{result_status_label(item.get('recovery_status', 'pending'))}**
- Verification status: **{result_status_label(verification.get('status', item.get('verification_status', 'not_yet_verified')))}**
- Program ledger item: [{item['id']}]({item['url']})
- Verification mode: `{verification.get('mode', item.get('program_role', 'pending'))}`

## Result Summary

{item.get('expanded_rationale') or 'Detailed result summary pending.'}

## Related Result Items

{verification_results_body}

## Related Corpus Construction Steps

{corpus_steps_body}

## Related Verify Surfaces

{verify_body}

## What This Status Does Not Yet Establish

{chr(10).join(f'- {entry}' for entry in item.get('what_this_does_not_claim', [])) or '- External acceptance is not implied by this status.'}

## Projection Metadata

- Generated from: `{item.get('generated_from', 'corpus/recovery-requirements')}`
- Projection version: `{item.get('projection_version', 'v0.1')}`
- Do not edit generated projection: `{item.get('do_not_edit', True)}`
"""
        write_markdown(
            SITE_ROOT / recovery_result_path(item).strip("/") / "index.md",
            {
                "layout": "program-doc",
                "title": item["title"],
                "permalink": recovery_result_path(item),
                "lane": "results",
                "v2_lane": "results",
                "type": "Recovery Target Status",
                "status": "Canonical",
                "summary_short": f"Current Results-side recovery status for {item['title']}.",
                "canonical_recovery_id": item["id"],
            },
            body,
        )


def sync_problem_recovery_agenda() -> None:
    # v4 public Agenda/Results obligations are Structural Challenges and
    # Challenge Responses. The retired v1 Problem Ledger/Problem Answers
    # projections must not be recreated in the public site repo.
    for filename in ("recovery-requirements.json", "recovery-requirements.ndjson", "recovery-requirements.csv"):
        source = CORPUS_EXPORTS / filename
        if source.exists():
            copy_file(source, SITE_ROOT / "_data" / "recovery_requirements" / filename)
            copy_file(source, SITE_ROOT / "assets" / "data" / "recovery-requirements" / filename)

    source = CORPUS_EXPORTS / "agenda-progress.json"
    copy_file(source, SITE_ROOT / "_data" / "agenda_progress" / "agenda-progress.json")
    copy_file(source, SITE_ROOT / "assets" / "data" / "agenda-progress" / "agenda-progress.json")

    recovery_source = CORPUS_EXPORTS / "recovery-requirements"
    if recovery_source.exists():
        copy_tree(recovery_source, SITE_ROOT / "_recovery_requirements")
    generate_recovery_status_pages()


def sync_results() -> None:
    for filename in ("results.json", "results.ndjson", "results.csv"):
        source = CORPUS_EXPORTS / filename
        copy_file(source, SITE_ROOT / "assets" / "data" / "results" / filename)
    copy_file(CORPUS_EXPORTS / "results.json", SITE_ROOT / "_data" / "results" / "results.json")
    clean_generated_tree(SITE_ROOT / "results" / "problem")
    copy_tree(CORPUS_EXPORTS / "result-pages", SITE_ROOT / "results" / "problem")

    for filename in ("predictions.json", "predictions.ndjson", "predictions.csv"):
        source = CORPUS_EXPORTS / filename
        copy_file(source, SITE_ROOT / "_data" / "predictions" / filename)
        copy_file(source, SITE_ROOT / "assets" / "data" / "predictions" / filename)
    clean_generated_tree(SITE_ROOT / "predictions", preserve_names={"index.md"})
    copy_tree(CORPUS_EXPORTS / "prediction-pages", SITE_ROOT / "predictions")

    for filename in ("falsifications.json", "falsifications.ndjson", "falsifications.csv"):
        source = CORPUS_EXPORTS / filename
        copy_file(source, SITE_ROOT / "_data" / "falsifications" / filename)
        copy_file(source, SITE_ROOT / "assets" / "data" / "falsifications" / filename)
    clean_generated_tree(SITE_ROOT / "falsifications", preserve_names={"index.md"})
    copy_tree(CORPUS_EXPORTS / "falsification-pages", SITE_ROOT / "falsifications")

    sync_registry_noteworthy_results()


def sync_wave2_metadata() -> None:
    source_root = CORPUS_EXPORTS / "metadata-wave2"
    if not source_root.exists():
        raise SystemExit(f"Missing Wave 2 metadata public export: {source_root}")

    corpus_data_targets = {
        "index.yml": "wave2_index.yml",
        "structural-challenges.yml": "structural_challenges.yml",
        "challenge-responses.yml": "challenge_responses.yml",
        "results.yml": "results.yml",
        "predictions.yml": "predictions.yml",
        "falsifications.yml": "falsifications.yml",
        "domain-metadata.yml": "domain_metadata.yml",
        "progress.yml": "wave2_progress.yml",
        "result-statuses.yml": "result_statuses.yml",
        "response-statuses.yml": "response_statuses.yml",
        "status-grammars.yml": "status_grammars.yml",
        "prediction-falsification-taxonomy.yml": "prediction_falsification_taxonomy.yml",
    }
    for source_name, target_name in corpus_data_targets.items():
        source = source_root / source_name
        if source.exists():
            copy_file(source, SITE_ROOT / "_data" / "corpus" / target_name)

    copy_tree(source_root, SITE_ROOT / "assets" / "data" / "corpus-wave2")

    structural_root = CORPUS_EXPORTS / "structural-challenges"
    if structural_root.exists():
        index_source = structural_root / "index.json"
        if index_source.exists():
            copy_file(index_source, SITE_ROOT / "assets" / "data" / "structural-challenges" / "index.json")
        manifest_root = structural_root / "manifest"
        if manifest_root.exists():
            for source in sorted(manifest_root.glob("*.json")):
                copy_file(source, SITE_ROOT / "_data" / "structural_challenges" / source.name)
                copy_file(source, SITE_ROOT / "assets" / "data" / "structural-challenges" / "manifest" / source.name)
        items_root = structural_root / "items"
        if items_root.exists():
            copy_tree(items_root, SITE_ROOT / "agenda" / "structural-challenge-ledger")
        generate_problem_ledger_answer_compatibility_pages()

    monograph_index = CORPUS_EXPORTS / "monograph-projections" / "pages" / "index.md"
    if monograph_index.exists():
        target = SITE_ROOT / "corpus" / "monographs" / "index.md"
        copy_file(monograph_index, target)
        normalize_monograph_projection_routes(target)


def sync_wave3_metadata() -> None:
    source_root = CORPUS_EXPORTS / "metadata-wave3"
    if not source_root.exists():
        raise SystemExit(f"Missing Wave 3 metadata public export: {source_root}")

    corpus_data_targets = {
        "index.yml": "wave3_index.yml",
        "registry-count-model.yml": "registry_count_model.yml",
        "registry-object-types.yml": "registry_object_types.yml",
        "registry-scope-labels.yml": "registry_scope_labels.yml",
        "registry-book-index.yml": "registry_book_index.yml",
        "construction-steps.yml": "construction_steps.yml",
        "construction-projections.yml": "construction_projections.yml",
        "construction-review-packets.yml": "construction_review_packets.yml",
        "construction-motifs.yml": "construction_motifs.yml",
        "monograph-books.yml": "monograph_books.yml",
        "monograph-parts.yml": "monograph_parts.yml",
        "monograph-chapters.yml": "monograph_chapters.yml",
        "taulib-projection.yml": "taulib_projection.yml",
        "taulib-modules.yml": "taulib_modules.yml",
        "taulib-module-families.yml": "taulib_module_families.yml",
        "taulib-registry-links.yml": "taulib_registry_links.yml",
        "glossary-entries.yml": "glossary_entries.yml",
        "glossary-domains.yml": "glossary_domains.yml",
        "glossary-coverage.yml": "glossary_coverage.yml",
        "graph-edge-types.yml": "graph_edge_types.yml",
        "graph-index.yml": "graph_index.yml",
    }
    for source_name, target_name in corpus_data_targets.items():
        source = source_root / source_name
        if source.exists():
            copy_file(source, SITE_ROOT / "_data" / "corpus" / target_name)

    graph_root = source_root / "graph"
    if graph_root.exists():
        for source in sorted(graph_root.glob("*.json")):
            copy_file(source, SITE_ROOT / "_data" / "corpus" / "graph" / source.name)

    copy_tree_filtered(source_root, SITE_ROOT / "assets" / "data" / "corpus-wave3", {".json", ".yml"})


def generate_problem_ledger_answer_compatibility_pages() -> None:
    manifest_root = SITE_ROOT / "_data" / "structural_challenges"
    if not manifest_root.exists():
        return
    root = SITE_ROOT / "results" / "problem-ledger-answers"
    generated_paths: set[Path] = set()
    for manifest in sorted(manifest_root.glob("*.json")):
        data = json.loads(manifest.read_text(encoding="utf-8"))
        domain = data.get("domain") or manifest.stem
        for item in data.get("items", []):
            slug = item.get("slug")
            source_url = item.get("url", "")
            if not slug or not source_url:
                continue
            target = source_url.replace(
                "/agenda/structural-challenge-ledger/",
                "/results/challenge-responses/",
            )
            write_markdown(
                root / domain / slug / "index.md",
                {
                    "layout": "redirect",
                    "title": f"{item.get('title', slug)} moved",
                    "permalink": f"/results/problem-ledger-answers/{domain}/{slug}/",
                    "redirect_to": target,
                    "lane": "results",
                    "v2_lane": "results",
                    "type": "Compatibility Redirect",
                    "status": "Compatibility",
                    "summary_short": "Redirects the retired Problem Ledger Answer route to the canonical Challenge Response route.",
                    "generated_from": "corpus/exports/public/structural-challenges/manifest",
                    "projection_version": "v0.1",
                    "canonical_source": "corpus/structural-challenge-ledger",
                    "do_not_edit": True,
                },
                f"Redirecting to the canonical Challenge Response route: [{target}]({target}).",
            )
            generated_paths.add(root / domain / slug / "index.md")

    legacy_pattern = re.compile(r"/results/problem-ledger-answers/[A-Za-z0-9/_-]+/?")
    for source in sorted((SITE_ROOT / "results").rglob("*.md")):
        if root in source.parents:
            continue
        legacy_urls = sorted(set(legacy_pattern.findall(source.read_text(encoding="utf-8", errors="replace"))))
        for legacy_url in legacy_urls:
            normalized_url = "/" + legacy_url.strip("/") + "/"
            if normalized_url == "/results/problem-ledger-answers/":
                continue
            target_path = SITE_ROOT / normalized_url.strip("/") / "index.md"
            if target_path.exists() or target_path in generated_paths:
                continue
            parts = normalized_url.strip("/").split("/")
            domain = parts[2] if len(parts) > 2 else ""
            title_slug = parts[-1] if parts else "legacy-problem-ledger-answer"
            redirect_target = "/results/challenge-responses/"
            write_markdown(
                target_path,
                {
                    "layout": "redirect",
                    "title": f"{title_from_url(title_slug)} moved",
                    "permalink": normalized_url,
                    "redirect_to": redirect_target,
                    "lane": "results",
                    "v2_lane": "results",
                    "type": "Compatibility Redirect",
                    "status": "Compatibility",
                    "summary_short": "Redirects a retired Problem Ledger Answer route to the canonical Challenge Responses surface.",
                    "generated_from": str(source.relative_to(SITE_ROOT)),
                    "projection_version": "v0.1",
                    "canonical_source": "corpus/structural-challenge-ledger",
                    "do_not_edit": True,
                    "legacy_domain": domain,
                },
                f"Redirecting retired Problem Ledger Answer route to [Challenge Responses]({redirect_target}).",
            )
            generated_paths.add(target_path)


def sync_registry_noteworthy_results() -> None:
    source_root = CORPUS_EXPORTS / "registry-noteworthy-results"
    if not source_root.exists():
        return
    for filename in (
        "registry-noteworthy-results.json",
        "registry-noteworthy-results.ndjson",
        "registry-noteworthy-results.csv",
    ):
        source = source_root / filename
        copy_file(source, SITE_ROOT / "_data" / "registry_noteworthy_results" / filename)
        copy_file(source, SITE_ROOT / "assets" / "data" / "registry-noteworthy-results" / filename)
    clean_generated_tree(SITE_ROOT / "results" / "additional-noteworthy-results")
    copy_tree(source_root / "pages", SITE_ROOT / "results" / "additional-noteworthy-results")


def sync_foundations() -> None:
    for filename in ("construction-spine.json", "construction-spine.ndjson", "construction-spine.csv"):
        source = CORPUS_EXPORTS / filename
        copy_file(source, SITE_ROOT / "_data" / "construction_spine" / filename)
        copy_file(source, SITE_ROOT / "assets" / "data" / "construction-spine" / filename)
    copy_file(
        CORPUS_EXPORTS / "construction-spine.json",
        SITE_ROOT / "_data" / "construction_spine" / "construction-spine-data.json",
    )

    for filename in ("foundational-hinges.json", "foundational-hinges.ndjson", "foundational-hinges.csv"):
        source = CORPUS_EXPORTS / filename
        copy_file(source, SITE_ROOT / "_data" / "foundational_hinges" / filename)
        copy_file(source, SITE_ROOT / "assets" / "data" / "foundational-hinges" / filename)
    copy_file(
        CORPUS_EXPORTS / "foundational-hinges.json",
        SITE_ROOT / "_data" / "foundational_hinges" / "foundational-hinges-data.json",
    )

    copy_tree(CORPUS_EXPORTS / "construction-spine" / "steps", SITE_ROOT / "corpus" / "construction-spine")
    copy_tree(CORPUS_EXPORTS / "foundational-hinges", SITE_ROOT / "corpus" / "foundational-hinges")


def sync_construction_map() -> None:
    source_root = CORPUS_EXPORTS / "construction-map"
    if not source_root.exists():
        return
    for filename in ("construction-map.json", "construction-map.ndjson", "construction-map.csv"):
        source = source_root / filename
        copy_file(source, SITE_ROOT / "_data" / "construction_map" / filename)
        copy_file(source, SITE_ROOT / "assets" / "data" / "construction-map" / filename)
    clean_generated_tree(SITE_ROOT / "corpus" / "construction-map")
    copy_tree(source_root / "pages", SITE_ROOT / "corpus" / "construction-map")


def sync_monograph_projections() -> None:
    source_root = CORPUS_EXPORTS / "monograph-projections"
    if not source_root.exists():
        return
    old_routes = collect_monograph_routes(SITE_ROOT / "corpus" / "monographs")
    old_routes.update(collect_monograph_routes_from_git("origin/main"))
    clean_generated_tree(SITE_ROOT / "corpus" / "monographs")
    copy_tree(source_root / "pages", SITE_ROOT / "corpus" / "monographs")
    copy_tree(source_root / "data", SITE_ROOT / "_data" / "monograph_projections")
    copy_tree(source_root / "data", SITE_ROOT / "assets" / "data" / "monograph-projections")
    new_routes = collect_monograph_routes(SITE_ROOT / "corpus" / "monographs")
    missing = sorted(key for key in old_routes if key not in new_routes)
    if missing:
        sample = ", ".join(missing[:10])
        raise SystemExit(f"Refusing monograph sync: {len(missing)} old monograph route(s) have no certified target: {sample}")
    for key, old in sorted(old_routes.items()):
        new = new_routes[key]
        old_permalink = old["permalink"]
        new_permalink = new["permalink"]
        if old_permalink == new_permalink:
            continue
        redirect_path = SITE_ROOT / old_permalink.strip("/") / "index.md"
        if redirect_path.exists():
            raise SystemExit(
                "Refusing to overwrite an existing certified monograph page while writing redirect: "
                f"{redirect_path.relative_to(SITE_ROOT)}"
            )
        write_markdown(
            redirect_path,
            {
                "layout": "redirect",
                "title": f"{old['title']} moved",
                "permalink": old_permalink,
                "redirect_to": new_permalink,
                "compatibility_key": key,
                "lane": "corpus",
                "v2_lane": "corpus",
                "type": "Compatibility Redirect",
                "status": "Compatibility",
                "summary_short": "Redirects to the certified Corpus monograph projection route.",
                "generated_from": "corpus/monograph-projections",
                "projection_version": "v0.1",
                "canonical_source": "corpus/monograph-projections",
                "do_not_edit": True,
            },
            f"Redirecting to the certified Corpus monograph route: [{new_permalink}]({new_permalink}).",
        )


def write_redirect(path: Path, target: str, title: str, summary: str) -> None:
    write_markdown(
        path,
        {
            "layout": "redirect",
            "title": title,
            "permalink": "/" + str(path.relative_to(SITE_ROOT).with_suffix("")).replace("index", "").strip("/") + "/",
            "redirect_to": target,
            "lane": "verify",
            "v2_lane": "verify",
            "type": "Compatibility Redirect",
            "status": "Compatibility",
            "summary_short": summary,
        },
        f"Redirecting to [{target}]({target}).",
    )


def sync_taulib_projection() -> None:
    source_root = CORPUS_EXPORTS / "taulib"
    if source_root.exists():
        for filename in (
            "summary.json",
            "module-inventory.json",
            "module-inventory.ndjson",
            "module-inventory.csv",
            "registry-links.json",
            "registry-links.ndjson",
            "registry-links.csv",
            "import-graph.json",
        ):
            source = source_root / filename
            if source.exists():
                copy_file(source, SITE_ROOT / "_data" / "taulib" / filename)
                copy_file(source, SITE_ROOT / "assets" / "data" / "taulib" / filename)

    tailored_root = CORPUS_EXPORTS / "taulib-projections"
    if not tailored_root.exists():
        return

    data_source = tailored_root / "data"
    pages_source = tailored_root / "pages"
    if data_source.exists():
        clean_generated_tree(SITE_ROOT / "_data" / "taulib_projections")
        clean_generated_tree(SITE_ROOT / "assets" / "data" / "taulib-projections")
        copy_tree(data_source, SITE_ROOT / "_data" / "taulib_projections")
        copy_tree(data_source, SITE_ROOT / "assets" / "data" / "taulib-projections")
        normalize_taulib_projection_tree(SITE_ROOT / "_data" / "taulib_projections")
        normalize_taulib_projection_tree(SITE_ROOT / "assets" / "data" / "taulib-projections")

    if pages_source.exists():
        clean_generated_tree(SITE_ROOT / "_taulib_docs")
        clean_generated_tree(SITE_ROOT / "verify" / "taulib" / "docs")
        copy_tree(pages_source, SITE_ROOT / "_taulib_docs")
        normalize_taulib_projection_tree(SITE_ROOT / "_taulib_docs")


def sync_change_control() -> None:
    source_root = CORPUS_EXPORTS / "corpus-changelog"
    if not source_root.exists():
        raise SystemExit(f"Missing Corpus Changelog public export: {source_root}")
    for filename in ("corpus-changelog.json", "corpus-changelog.ndjson", "corpus-changelog.csv"):
        source = source_root / filename
        copy_file(source, SITE_ROOT / "_data" / "corpus_changelog" / filename)
        copy_file(source, SITE_ROOT / "assets" / "data" / "corpus-changelog" / filename)
    report = source_root / "projection-report.md"
    if report.exists():
        copy_file(report, SITE_ROOT / "assets" / "data" / "corpus-changelog" / "projection-report.md")
    clean_generated_tree(SITE_ROOT / "_corpus_changelog")
    pages_source = source_root / "pages"
    if pages_source.exists():
        copy_tree(pages_source, SITE_ROOT / "_corpus_changelog")


def sync_publication_metadata() -> None:
    corpus_data_targets = {
        "publications.yml": "publications.yml",
        "latest-publications.yml": "latest_publications.yml",
        "publication-types.yml": "publication_types.yml",
        "people.yml": "people.yml",
        "external-surfaces.yml": "external_surfaces.yml",
        "bibliography-summary.yml": "bibliography_summary.yml",
    }
    for source_name, target_name in corpus_data_targets.items():
        copy_file(CORPUS_EXPORTS / source_name, SITE_ROOT / "_data" / "corpus" / target_name)

    asset_names = (
        "publications.json",
        "publications.ndjson",
        "publications.csv",
        "latest-publications.json",
        "latest-publications.ndjson",
        "latest-publications.csv",
        "publication-types.json",
        "people.json",
        "external-surfaces.json",
        "bibliography-summary.json",
    )
    for filename in asset_names:
        source = CORPUS_EXPORTS / filename
        if source.exists():
            copy_file(source, SITE_ROOT / "assets" / "data" / "publications" / filename)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--scope",
        choices=(
            "all",
            "foundations",
            "corpus-v3",
            "taulib",
            "ledgers",
            "results",
            "monographs",
            "change-control",
            "publications",
            "wave2-metadata",
            "wave3-metadata",
        ),
        default="all",
        help=(
            "Sync all Corpus public exports, only Construction Spine / review packet routes, "
            "the Corpus v3 Construction Map / Monograph / TauLib projections, "
            "only the tailored TauLib projection, the Results/ledger projections, "
            "the Corpus Changelog change-control projection, the Corpus publication metadata projection, "
            "the Wave 2 Agenda/Results metadata projection, "
            "or the Wave 3 construction-facing Corpus metadata projection."
        ),
    )
    args = parser.parse_args()

    if not CORPUS_EXPORTS.exists():
        raise SystemExit(f"Missing Corpus public exports: {CORPUS_EXPORTS}")

    if args.scope in {"all", "ledgers"}:
        sync_problem_recovery_agenda()
    if args.scope in {"all", "results"}:
        sync_results()
    if args.scope in {"all", "wave2-metadata"}:
        sync_wave2_metadata()
    if args.scope in {"all", "wave3-metadata"}:
        sync_wave3_metadata()
    if args.scope in {"all", "foundations"}:
        sync_foundations()
    if args.scope in {"all", "corpus-v3", "monographs"}:
        sync_monograph_projections()
    if args.scope in {"all", "corpus-v3"}:
        sync_construction_map()
    if args.scope in {"all", "corpus-v3", "taulib"}:
        sync_taulib_projection()
    if args.scope in {"all", "change-control"}:
        sync_change_control()
    if args.scope in {"all", "publications"}:
        sync_publication_metadata()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
