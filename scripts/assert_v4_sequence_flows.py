#!/usr/bin/env python3
"""Assertions for the compact v4 sequence-flow component."""

from __future__ import annotations

import re
import sys
from pathlib import Path


TARGET_ROUTES = [
    "impact/index.html",
    "impact/impact-framework/index.html",
    "impact/foundational-science/index.html",
    "impact/applied-science-and-research/index.html",
    "impact/global-education/index.html",
    "impact/existential-orientation/index.html",
    "impact/societal-coherence/index.html",
    "impact/global-public-good/index.html",
    "publications/research-briefings/public-good/index.html",
    "impact/global-public-good/ocean/index.html",
    "results/world-readout/physics/from-ratio-to-measurement-iota-tau-and-the-calibration-of-physics/index.html",
    "results/predictions/index.html",
    "results/predictions/browse/index.html",
]

RAW_IMPACT_CHAINS = [
    "Result → Verification & Review → Translation Layer → Domain Uptake → Consequence",
    "Result → Verification & Review → Translation layer → Domain uptake → Consequence",
]


def read(path: Path) -> str:
    if not path.exists():
        raise AssertionError(f"Missing file: {path}")
    return path.read_text(encoding="utf-8")


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise AssertionError(f"{label} missing expected text: {needle}")


def local_href_to_file(site: Path, href: str) -> Path:
    if href == "/":
        return site / "index.html"
    return site / href.strip("/") / "index.html"


def main() -> int:
    site = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")
    root = site.parent

    for path in [
        root / "_data" / "sequence_flows.yml",
        root / "_includes" / "sequence-flow.html",
        root / "_sass" / "_sequence-flow.scss",
    ]:
        if not path.exists():
            raise AssertionError(f"Missing sequence-flow source file: {path}")

    data = read(root / "_data" / "sequence_flows.yml")
    for flow_id in ["impact_chain:", "portfolio_dependency:", "calibration_cascade:"]:
        require(data, flow_id, "sequence flow data")

    include = read(root / "_includes" / "sequence-flow.html")
    require(include, "<ol class=\"sequence-flow", "semantic ordered-list include")
    require(include, "aria-hidden=\"true\"", "visual-only arrow include")
    require(include, "site.data.sequence_flows", "data-driven include")

    sass = read(root / "_sass" / "_sequence-flow.scss").lower()
    compiled_css = read(site / "assets/css/main.css").lower()
    for css in [sass, compiled_css]:
        require(css.replace(" ", ""), "flex-wrap:wrap", "sequence flow wrap behavior")
        require(css.replace(" ", ""), "max-width:100%", "sequence flow overflow guard")
        require(css, ".sequence-flow__arrow", "sequence flow arrow styling")
    if "white-space: nowrap" in sass:
        raise AssertionError("Sequence-flow Sass must not force nowrap")
    require(sass, "@media (max-width: 620px)", "mobile sequence-flow wrapping rules")

    for route in TARGET_ROUTES:
        raw = read(site / route)
        require(raw, '<ol class="sequence-flow', f"sequence flow rendered on {route}")
        require(raw, 'class="sequence-flow__arrow" aria-hidden="true"', f"visual-only arrows on {route}")
        for chain in RAW_IMPACT_CHAINS:
            if chain in raw:
                raise AssertionError(f"{route} still contains raw prose Impact chain: {chain}")
        hrefs = re.findall(r'<a class="sequence-flow__node" href="([^"]+)"', raw)
        for href in hrefs:
            if href.startswith("/"):
                target = local_href_to_file(site, href)
                if not target.exists():
                    raise AssertionError(f"{route} sequence-flow link does not resolve: {href}")

    impact = read(site / "impact/index.html")
    require(impact, "What the program currently claims follows.", "Impact sequence-flow descriptions")
    require(impact, "/impact/impact-framework/", "Impact sequence-flow translation link")

    predictions = read(site / "predictions/mh-gev/index.html")
    if '<ol class="sequence-flow' in predictions:
        raise AssertionError("Generated prediction formula page should not be converted into a sequence-flow")
    require(predictions, "→ m_H = 125.21 GeV", "generated formula arrow preserved")

    physics = read(
        site
        / "results/world-readout/physics/from-ratio-to-measurement-iota-tau-and-the-calibration-of-physics/index.html"
    )
    for label in ["L0 Algebraic", "L1 Dimensionless", "L2 SI Anchor", "L3 SI-Derived", "L4 Verification"]:
        require(physics, label, "calibration cascade sequence labels")

    print("v4 sequence-flow assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
