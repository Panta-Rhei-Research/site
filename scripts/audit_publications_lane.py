#!/usr/bin/env python3
"""Audit the public Publications lane against the canonical publications catalog.

The catalog in ``../publications/catalog/publications.json`` is the source of
truth. Site data, front matter, local PDF assets, built pages, live URLs, DOI
links, and prrp.site short routes are evidence surfaces that can reveal catalog
or projection drift, but they do not override the catalog.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


SITE_ROOT = Path(__file__).resolve().parents[1]
ORG_ROOT = SITE_ROOT.parent
CATALOG_PATH = ORG_ROOT / "publications" / "catalog" / "publications.json"
ATLAS_AUDIT_DIR = ORG_ROOT / "atlas" / "audits" / "publications-lane-qa"

PUBLICATION_ID_RE = re.compile(
    r"^(?:wp|lwp|rn|rp|pgd|pgb|c|rm|ms|so|gt)\d{3}(?:-rc\d+)?$"
)
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")


@dataclass
class Finding:
    severity: str
    publication_id: str
    artifact_id: str
    issue_class: str
    message: str
    surface: str
    expected: str = ""
    actual: str = ""


def read_yaml(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return yaml.safe_load(path.read_text(encoding="utf-8")) or default


def read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def load_catalog() -> list[dict[str, Any]]:
    payload = read_json(CATALOG_PATH, {})
    rows = payload.get("publications", [])
    if not isinstance(rows, list):
        raise SystemExit(f"Invalid catalog payload: {CATALOG_PATH}")
    return rows


def load_manifest(row: dict[str, Any]) -> dict[str, Any]:
    github_path = str(row.get("github_path") or "")
    if not github_path:
        return {}
    return read_json(ORG_ROOT / "publications" / github_path / "manifest.json", {})


def normalize_abs_url(value: str) -> str:
    value = str(value or "")
    if value.startswith("https://panta-rhei.site/"):
        return value
    if value.startswith("/"):
        return "https://panta-rhei.site" + value
    return value


def site_path_from_url(url: str) -> str:
    url = normalize_abs_url(url)
    return url.removeprefix("https://panta-rhei.site")


def built_path_for_url(url: str) -> Path:
    rel = site_path_from_url(url).lstrip("/")
    if not rel:
        return SITE_ROOT / "_site" / "index.html"
    if rel.endswith("/"):
        return SITE_ROOT / "_site" / rel / "index.html"
    return SITE_ROOT / "_site" / rel


def load_site_publications() -> dict[str, dict[str, Any]]:
    payload = read_yaml(SITE_ROOT / "_data" / "corpus" / "publications.yml", {})
    return {
        str(item.get("publication_id")): item
        for item in payload.get("publications", [])
        if isinstance(item, dict) and item.get("publication_id")
    }


def load_latest_publications() -> dict[str, dict[str, Any]]:
    payload = read_yaml(SITE_ROOT / "_data" / "corpus" / "latest_publications.yml", {})
    return {
        str(item.get("publication_id")): item
        for item in payload.get("publications", [])
        if isinstance(item, dict) and item.get("publication_id")
    }


def load_research_note_frontmatter() -> dict[str, dict[str, Any]]:
    notes: dict[str, dict[str, Any]] = {}
    for path in sorted((SITE_ROOT / "_research_notes").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        parts = text.split("---", 2)
        if len(parts) < 3:
            continue
        data = yaml.safe_load(parts[1]) or {}
        if data.get("publication_id"):
            notes[str(data["publication_id"]).lower().replace("-", "")] = {
                **data,
                "_path": str(path.relative_to(SITE_ROOT)),
            }
    return notes


def load_research_papers_data() -> dict[str, dict[str, Any]]:
    rows = read_yaml(SITE_ROOT / "_data" / "publications" / "research_papers.yml", [])
    return {
        str(item.get("slug")): item
        for item in rows
        if isinstance(item, dict) and item.get("slug")
    }


def catalog_pdf_site_path(row: dict[str, Any], manifest: dict[str, Any]) -> str:
    source = str(((manifest.get("file") or {}).get("source_website_asset_path")) or "")
    if source.startswith("site/"):
        return "/" + source.removeprefix("site/")
    pdf = str(row.get("pdf") or "")
    if not pdf:
        return ""
    if pdf.startswith("research-note-"):
        return f"/assets/pdfs/research-notes/{pdf}"
    if pdf.startswith("research-paper-"):
        return f"/assets/pdfs/research-papers/{pdf}"
    if pdf.startswith("public-good-impact-dossier-") or pdf.startswith("public-good-briefing-"):
        return f"/assets/pdfs/research-briefings/public-good/{pdf}"
    if pdf.startswith("white-paper-"):
        return f"/assets/pdfs/white-papers/{pdf}"
    if pdf.startswith("guided-tour-book-"):
        return f"/assets/media/{pdf}"
    return ""


def add(
    findings: list[Finding],
    severity: str,
    row: dict[str, Any],
    issue_class: str,
    message: str,
    surface: str,
    expected: str = "",
    actual: str = "",
) -> None:
    findings.append(
        Finding(
            severity=severity,
            publication_id=str(row.get("publication_id") or ""),
            artifact_id=str(row.get("id") or ""),
            issue_class=issue_class,
            message=message,
            surface=surface,
            expected=expected,
            actual=actual,
        )
    )


def audit_catalog(rows: list[dict[str, Any]]) -> list[Finding]:
    findings: list[Finding] = []
    seen_ids: dict[str, dict[str, Any]] = {}
    seen_short: dict[str, str] = {}
    seen_canonical: dict[str, str] = {}
    seen_pdf: dict[str, str] = {}
    seen_doi: dict[str, str] = {}
    for row in rows:
        pid = str(row.get("publication_id") or "")
        if not PUBLICATION_ID_RE.match(pid):
            add(findings, "error", row, "id-shape", "Publication ID does not match canonical catalog shape.", "catalog")
        if pid in seen_ids:
            add(findings, "error", row, "duplicate-publication-id", "Duplicate publication_id in catalog.", "catalog", pid, seen_ids[pid].get("id", ""))
        seen_ids[pid] = row

        status = str(row.get("status") or "")
        canonical_url = str(row.get("canonical_url") or "")
        if status == "released" and not canonical_url.startswith("https://panta-rhei.site/"):
            add(findings, "error", row, "canonical-url", "Released artifact has no canonical panta-rhei.site URL.", "catalog")

        doi = str(row.get("doi") or "")
        if doi and doi != "forthcoming" and not DOI_RE.match(doi):
            add(findings, "error", row, "doi-shape", "DOI does not match DOI syntax.", "catalog", actual=doi)

        for value, label, seen, unique_statuses in (
            (str(row.get("short_url") or ""), "short-url", seen_short, {"released"}),
            (canonical_url, "canonical-url", seen_canonical, {"released"}),
            (str(row.get("pdf") or ""), "pdf", seen_pdf, {"released", "superseded"}),
            (doi, "doi", seen_doi, {"released", "superseded"}),
        ):
            if not value or status not in unique_statuses:
                continue
            if label == "canonical-url" and str(row.get("type") or "") == "guided_tour":
                # Guided tours intentionally share the category landing page while
                # preserving distinct PDF artifacts and publication IDs.
                continue
            if value in seen and seen[value] != pid:
                add(findings, "warning", row, f"duplicate-{label}", f"Duplicate {label} value across catalog records.", "catalog", value, f"{seen[value]} and {pid}")
            seen[value] = pid
    return findings


def audit_site_projection(rows: list[dict[str, Any]], findings: list[Finding]) -> None:
    site_records = load_site_publications()
    latest_records = load_latest_publications()
    catalog_ids = {str(row.get("publication_id")) for row in rows}
    site_ids = set(site_records)
    for missing in sorted(catalog_ids - site_ids):
        row = next(row for row in rows if str(row.get("publication_id")) == missing)
        add(findings, "error", row, "site-projection-missing", "Catalog artifact is missing from site _data/corpus/publications.yml.", "site-data")
    for extra in sorted(site_ids - catalog_ids):
        findings.append(Finding("error", extra, "", "site-projection-extra", "Site projection contains artifact absent from catalog.", "site-data"))

    for row in rows:
        pid = str(row.get("publication_id") or "")
        site = site_records.get(pid)
        if not site:
            continue
        pairs = (
            ("title", str(row.get("title") or ""), str(site.get("title") or "")),
            ("status", str(row.get("status") or ""), str(site.get("status") or "")),
            ("date", str(row.get("date") or ""), str(site.get("release_date") or "")),
            ("canonical_url", str(row.get("canonical_url") or ""), str(site.get("canonical_url") or "")),
            ("short_url", str(row.get("short_url") or ""), str(site.get("short_url") or "")),
            ("doi", str(row.get("doi") or ""), str((site.get("identifiers") or {}).get("doi") or "")),
        )
        for field, expected, actual in pairs:
            if expected != actual:
                add(findings, "error", row, f"site-projection-{field}", f"Site publication projection has mismatched {field}.", "site-data", expected, actual)
        expected_pdf = catalog_pdf_site_path(row, load_manifest(row)).lstrip("/")
        actual_pdf = str(((site.get("files") or {}).get("pdf_path_site")) or "").lstrip("/")
        if expected_pdf and actual_pdf and expected_pdf != actual_pdf:
            add(findings, "error", row, "site-projection-pdf", "Site publication projection has mismatched PDF path.", "site-data", expected_pdf, actual_pdf)

        if str(row.get("status") or "") in {"released", "superseded"} and pid not in latest_records:
            add(findings, "warning", row, "latest-projection-missing", "Released/superseded artifact is absent from latest_publications projection.", "site-data")


def audit_family_surfaces(rows: list[dict[str, Any]], findings: list[Finding]) -> None:
    notes = load_research_note_frontmatter()
    papers = load_research_papers_data()
    for row in rows:
        pid = str(row.get("publication_id") or "")
        row_type = str(row.get("type") or "")
        if row_type == "research_note" and str(row.get("status")) == "released":
            note = notes.get(pid.lower())
            if not note:
                add(findings, "error", row, "research-note-frontmatter-missing-id", "Released research note page has no matching publication_id front matter.", "_research_notes")
                continue
            doi = str(row.get("doi") or "")
            page_doi = str(note.get("doi") or note.get("doi_url") or "")
            if doi and doi not in page_doi:
                add(findings, "error", row, "research-note-doi-mismatch", "Research note front matter DOI does not match catalog.", note["_path"], doi, page_doi)
            pdf_path = catalog_pdf_site_path(row, load_manifest(row))
            page_pdf = str(note.get("pdf_url") or note.get("pdf_path") or "")
            if pdf_path and page_pdf and pdf_path not in page_pdf:
                add(findings, "error", row, "research-note-pdf-mismatch", "Research note front matter PDF path does not match catalog.", note["_path"], pdf_path, page_pdf)
        if row_type == "research_paper" and str(row.get("status")) == "released":
            slug = site_path_from_url(str(row.get("canonical_url") or "")).rstrip("/").split("/")[-1]
            paper = papers.get(slug)
            if not paper:
                add(findings, "error", row, "research-paper-data-missing", "Released research paper is missing from _data/publications/research_papers.yml.", "_data/publications/research_papers.yml")
                continue
            if str(paper.get("publication_id") or "") != pid:
                add(findings, "error", row, "research-paper-id-missing", "Research paper data does not expose catalog publication_id.", "_data/publications/research_papers.yml", pid, str(paper.get("publication_id") or ""))
            expected_short = str(row.get("short_url") or "")
            if expected_short and str(paper.get("short_url") or "") != expected_short:
                add(findings, "error", row, "research-paper-short-url-missing", "Research paper data does not expose catalog short_url.", "_data/publications/research_papers.yml", expected_short, str(paper.get("short_url") or ""))


def audit_files_and_build(rows: list[dict[str, Any]], findings: list[Finding]) -> None:
    build_exists = (SITE_ROOT / "_site").exists()
    for row in rows:
        manifest = load_manifest(row)
        pdf_path = catalog_pdf_site_path(row, manifest)
        if str(row.get("artifact_availability")) == "local_pdf":
            if not pdf_path:
                add(findings, "error", row, "pdf-path-missing", "Local-PDF artifact has no site PDF path.", "catalog/manifest")
            else:
                local_pdf = SITE_ROOT / pdf_path.lstrip("/")
                if not local_pdf.exists():
                    add(findings, "error", row, "pdf-asset-missing", "Local PDF asset is missing from site worktree.", "site-assets", pdf_path)
                elif row.get("doi"):
                    try:
                        text = subprocess.run(
                            ["pdftotext", str(local_pdf), "-"],
                            text=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.DEVNULL,
                            timeout=20,
                            check=False,
                        ).stdout
                    except (FileNotFoundError, subprocess.TimeoutExpired):
                        text = ""
                    if text and str(row.get("doi")) not in text:
                        add(findings, "warning", row, "pdf-doi-missing", "Catalog DOI is not visible in the local PDF text extraction.", "site-assets", str(row.get("doi") or ""), pdf_path)
                    elif not text:
                        add(findings, "warning", row, "pdf-text-unavailable", "Could not extract PDF text to verify visible DOI.", "site-assets", pdf_path)
        canonical_url = str(row.get("canonical_url") or "")
        if build_exists and canonical_url.startswith("https://panta-rhei.site/"):
            built = built_path_for_url(canonical_url)
            if not built.exists():
                add(findings, "error", row, "built-page-missing", "Built canonical page is missing from _site.", "_site", str(built.relative_to(SITE_ROOT)))


def http_headish(url: str, timeout: float = 12.0) -> tuple[int, str]:
    request = urllib.request.Request(url, method="GET", headers={"User-Agent": "PantaRhei-PublicationsAudit/1.0"})
    opener = urllib.request.build_opener(urllib.request.HTTPRedirectHandler())
    try:
        with opener.open(request, timeout=timeout) as response:
            return int(response.status), response.geturl()
    except urllib.error.HTTPError as exc:
        return int(exc.code), exc.geturl()
    except Exception as exc:  # pragma: no cover - used as operational diagnostic.
        return 0, f"{type(exc).__name__}: {exc}"


def audit_live(rows: list[dict[str, Any]], findings: list[Finding]) -> None:
    for row in rows:
        status = str(row.get("status") or "")
        if status != "released":
            continue
        for url, issue_class in (
            (str(row.get("canonical_url") or ""), "live-canonical"),
            (normalize_abs_url(catalog_pdf_site_path(row, load_manifest(row))), "live-pdf"),
            (str(row.get("doi_url") or ""), "live-doi"),
            (str(row.get("short_url") or ""), "live-short-url"),
        ):
            if not url:
                continue
            status_code, final_url = http_headish(url)
            if status_code < 200 or status_code >= 400:
                add(findings, "error", row, issue_class, "Live URL did not return a 2xx/3xx-successful response.", "live", url, f"{status_code} {final_url}")
            if issue_class == "live-short-url":
                expected = str(row.get("canonical_url") or "")
                if expected and expected.rstrip("/") not in final_url.rstrip("/"):
                    add(findings, "warning", row, issue_class, "Short URL final target does not match catalog canonical URL.", "live", expected, final_url)


def write_atlas(rows: list[dict[str, Any]], findings: list[Finding], *, live: bool = False) -> None:
    ATLAS_AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    findings_data = [asdict(item) for item in findings]
    suffix = "-live" if live else ""
    mode_label = "Live" if live else "Local"
    findings_name = f"findings{suffix}.json"
    ledger_name = f"ledger{suffix}.csv"
    readme_name = f"README{suffix}.md"
    (ATLAS_AUDIT_DIR / findings_name).write_text(json.dumps(findings_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    with (ATLAS_AUDIT_DIR / ledger_name).open("w", encoding="utf-8", newline="") as handle:
        fieldnames = [
            "publication_id",
            "title",
            "type",
            "status",
            "canonical_url",
            "pdf",
            "doi",
            "short_url",
            "catalog_state",
            "site_state",
            "issue_count",
            "error_count",
            "warning_count",
        ]
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        by_pid: dict[str, list[Finding]] = {}
        for finding in findings:
            by_pid.setdefault(finding.publication_id, []).append(finding)
        for row in rows:
            issues = by_pid.get(str(row.get("publication_id")), [])
            writer.writerow(
                {
                    "publication_id": row.get("publication_id", ""),
                    "title": row.get("title", ""),
                    "type": row.get("type", ""),
                    "status": row.get("status", ""),
                    "canonical_url": row.get("canonical_url", ""),
                    "pdf": row.get("pdf", ""),
                    "doi": row.get("doi", ""),
                    "short_url": row.get("short_url", ""),
                    "catalog_state": "present",
                    "site_state": "see findings" if issues else "aligned",
                    "issue_count": len(issues),
                    "error_count": sum(1 for item in issues if item.severity == "error"),
                    "warning_count": sum(1 for item in issues if item.severity == "warning"),
                }
            )

    error_count = sum(1 for item in findings if item.severity == "error")
    warning_count = sum(1 for item in findings if item.severity == "warning")
    lines = [
        f"# Publications Lane QA ({mode_label})",
        "",
        f"Generated: `{generated_at}`",
        f"Mode: `{mode_label.lower()}`",
        "",
        "## Scope",
        "",
        "This audit covers the citable Publications artifact layer: catalog records, artifact manifests, site data projections, family index data, PDF assets, built pages, and optional live DOI/short-route checks. Generated monograph chapter pages are intentionally out of scope.",
        "",
        "## Source Basis",
        "",
        "- Authority: `publications/catalog/publications.json` and per-artifact `manifest.json` files.",
        "- Site evidence: `site/_data/corpus/publications.yml`, `site/_data/corpus/latest_publications.yml`, family front matter/data, local PDF assets, and `_site/publications/**` when built.",
        "- Live evidence, when enabled: canonical URLs, PDF URLs, DOI URLs, and non-empty `prrp.site` short routes.",
        "",
        "## Summary",
        "",
        f"- Catalog records: `{len(rows)}`",
        f"- Findings: `{len(findings)}`",
        f"- Errors: `{error_count}`",
        f"- Warnings: `{warning_count}`",
        "",
        "## Findings",
        "",
    ]
    if not findings:
        lines.append("No findings.")
    else:
        for finding in findings:
            lines.append(
                f"- **{finding.severity.upper()}** `{finding.publication_id}` `{finding.issue_class}`: {finding.message} "
                f"({finding.surface}; expected `{finding.expected}`, actual `{finding.actual}`)"
            )
    lines.extend(
        [
            "",
            "## Artifacts",
            "",
            f"- `{ledger_name}` — per-artifact audit ledger.",
            f"- `{findings_name}` — machine-readable findings.",
        ]
    )
    (ATLAS_AUDIT_DIR / readme_name).write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-atlas", action="store_true", help="Write Atlas audit pack.")
    parser.add_argument("--live", action="store_true", help="Check live canonical/PDF/DOI/short URLs.")
    parser.add_argument("--report-only", action="store_true", help="Return success even if errors are found.")
    args = parser.parse_args()

    rows = load_catalog()
    findings = audit_catalog(rows)
    audit_site_projection(rows, findings)
    audit_family_surfaces(rows, findings)
    audit_files_and_build(rows, findings)
    if args.live:
        audit_live(rows, findings)
    if args.write_atlas:
        write_atlas(rows, findings, live=args.live)

    errors = [finding for finding in findings if finding.severity == "error"]
    warnings = [finding for finding in findings if finding.severity == "warning"]
    print(f"Audited {len(rows)} publication records: {len(errors)} error(s), {len(warnings)} warning(s).")
    for finding in findings:
        print(f"{finding.severity.upper()}: {finding.publication_id} {finding.issue_class}: {finding.message}")
    return 0 if args.report_only or not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
