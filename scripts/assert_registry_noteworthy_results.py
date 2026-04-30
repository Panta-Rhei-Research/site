#!/usr/bin/env python3
"""Targeted assertions for Registry-backed noteworthy Results pages."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path


SITE_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = SITE_ROOT / "_data" / "registry_noteworthy_results" / "registry-noteworthy-results.json"
RESULTS_PATH = SITE_ROOT / "_data" / "results" / "results.json"
SOURCE_ROOT = SITE_ROOT / "results" / "additional-noteworthy-results"
BUILD_ROOT = SITE_ROOT / "_site"
EXPECTED_COUNTS = {
    "related_existing_surface": 235,
    "standalone_additional_result": 104,
}
EXPECTED_DOMAIN_COUNTS = {
    "physics": 307,
    "life": 24,
    "metaphysics": 8,
}


def load_json(path: Path) -> list[dict]:
    return json.loads(path.read_text(encoding="utf-8"))


def built_html_path(url: str) -> Path:
    return BUILD_ROOT / url.strip("/") / "index.html"


def visible_text(html: str) -> str:
    html = re.sub(r"<script\b.*?</script>", "", html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r"<style\b.*?</style>", "", html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r"<[^>]+>", " ", html)
    return re.sub(r"\s+", " ", html)


def main() -> int:
    errors: list[str] = []
    records = load_json(DATA_PATH)
    results = load_json(RESULTS_PATH)
    if len(records) != 339:
        errors.append(f"expected 339 Registry noteworthy records, found {len(records)}")
    if dict(sorted(Counter(record.get("cluster") for record in records).items())) != EXPECTED_COUNTS:
        errors.append("Registry noteworthy cluster counts changed")
    if dict(sorted(Counter(record.get("domain") for record in records).items())) != EXPECTED_DOMAIN_COUNTS:
        errors.append("Registry noteworthy domain counts changed")
    if len(results) != 255:
        errors.append(f"generic Results count changed from 255 to {len(results)}")

    source_pages = sorted(path for path in SOURCE_ROOT.glob("*/*/index.md") if path.parts[-3] in EXPECTED_DOMAIN_COUNTS)
    if len(source_pages) != 339:
        errors.append(f"expected 339 generated detail pages, found {len(source_pages)}")

    slugs = [record.get("slug") for record in records]
    if len(slugs) != len(set(slugs)):
        errors.append("Registry noteworthy slugs are not unique")

    if BUILD_ROOT.exists():
        root_html = BUILD_ROOT / "results" / "additional-noteworthy-results" / "index.html"
        if not root_html.exists():
            errors.append("built Additional Noteworthy Results root is missing")
        for record in records:
            url = record["url"]
            path = built_html_path(url)
            if not path.exists():
                errors.append(f"built page missing: {url}")
                continue
            html = path.read_text(encoding="utf-8", errors="replace")
            if len(re.findall(r"<h1\b", html, flags=re.IGNORECASE)) != 1:
                errors.append(f"{url}: expected exactly one H1")
            if len(re.findall(r"<title\b", html, flags=re.IGNORECASE)) != 1:
                errors.append(f"{url}: expected exactly one title tag")
            if 'rel="canonical"' not in html:
                errors.append(f"{url}: missing canonical link")
            if 'name="description"' not in html:
                errors.append(f"{url}: missing description metadata")
            text = visible_text(html).lower()
            for phrase in ("registry item", "claim boundary", "external validation"):
                if phrase not in text:
                    errors.append(f"{url}: missing {phrase!r}")

    if errors:
        print("Registry noteworthy Results assertions failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Registry noteworthy Results assertions passed (339 pages; generic Results count 255).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
