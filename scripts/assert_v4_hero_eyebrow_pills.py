#!/usr/bin/env python3
"""Assertions for split v4 hero eyebrow breadcrumb + metadata pills."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROUTES = {
    "program/index.html": {
        "crumbs": ["Home", "Program"],
        "forbidden_crumbs": ["Lane Root", "Canonical"],
        "type": "Lane Root",
        "status": "Canonical",
    },
    "impact/index.html": {
        "crumbs": ["Home", "Impact"],
        "forbidden_crumbs": ["Lane Root", "Conditional"],
        "type": "Lane Root",
        "status": "Conditional",
    },
    "impact/existential-orientation/index.html": {
        "crumbs": ["Home", "Impact"],
        "forbidden_crumbs": ["Existential Orientation", "Impact Stratum", "Conditional"],
        "type": "Impact Stratum",
        "status": "Conditional",
    },
    "results/world-readout/physics/index.html": {
        "crumbs": ["Home", "Results"],
        "forbidden_crumbs": ["Physics World-Readout", "domain hub", "canonical"],
        "type": "domain hub",
        "status": "canonical",
    },
    "verify/release-manifest/index.html": {
        "crumbs": ["Home", "Verify"],
        "forbidden_crumbs": ["Release Manifest", "Verification Surface", "Canonical"],
        "type": "Verification Surface",
        "status": "Canonical",
    },
}


def read(path: Path) -> str:
    if not path.exists():
        raise AssertionError(f"Missing file: {path}")
    return path.read_text(encoding="utf-8")


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise AssertionError(f"{label} missing expected text: {needle}")


def extract_breadcrumb(raw: str, route: str) -> str:
    match = re.search(r'<nav class="[^"]*\bhero-breadcrumb-pill\b[^"]*"[^>]*>(.*?)</nav>', raw, re.S)
    if not match:
        raise AssertionError(f"{route} missing breadcrumb pill")
    return match.group(1)


def require_meta(raw: str, route: str, kind: str, value: str) -> None:
    pattern = rf'<span class="[^"]*\bhero-meta-pill--{kind}\b[^"]*"[^>]*>\s*{re.escape(value)}\s*</span>'
    if not re.search(pattern, raw):
        raise AssertionError(f"{route} missing {kind} metadata pill: {value}")


def main() -> int:
    site = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")
    css = read(site / "assets/css/main.css")

    for selector in [".hero-eyebrow-row", ".hero-breadcrumb-pill", ".hero-breadcrumb-link", ".hero-meta-pill"]:
        require(css, selector, "compiled hero eyebrow CSS")

    for route, expected in ROUTES.items():
        raw = read(site / route)
        require(raw, 'class="hero-eyebrow-row"', f"eyebrow row for {route}")
        require(raw, 'aria-label="Breadcrumb"', f"breadcrumb label for {route}")
        require(raw, '"@type": "BreadcrumbList"', f"breadcrumb JSON-LD for {route}")
        if '<nav class="breadcrumb"' in raw:
            raise AssertionError(f"{route} renders detached visual breadcrumb nav")
        breadcrumb = extract_breadcrumb(raw, route)
        require(breadcrumb, 'class="hero-eyebrow-separator hero-breadcrumb-separator" aria-hidden="true">/</span>', f"slash separator for {route}")
        for crumb in expected["crumbs"]:
            require(breadcrumb, crumb, f"breadcrumb crumb for {route}")
        for forbidden in expected["forbidden_crumbs"]:
            if forbidden in breadcrumb:
                raise AssertionError(f"{route} breadcrumb pill leaks current title or metadata: {forbidden}")
        if "·" in breadcrumb:
            raise AssertionError(f"{route} breadcrumb pill still uses centered-dot separators")
        require_meta(raw, route, "type", expected["type"])
        require_meta(raw, route, "status", expected["status"])

    print("v4 hero eyebrow breadcrumb split assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
