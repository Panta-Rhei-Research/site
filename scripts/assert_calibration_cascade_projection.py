#!/usr/bin/env python3
"""Focused assertions for the Calibration Cascade site projection."""

from __future__ import annotations

import re
from pathlib import Path


SITE_ROOT = Path(__file__).resolve().parents[1]
BUILD_ROOT = SITE_ROOT / "_site"


def read(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"Missing expected file: {path.relative_to(SITE_ROOT)}")
    return path.read_text(encoding="utf-8", errors="replace")


def assert_contains(text: str, needle: str, context: str) -> None:
    if needle not in text:
        raise SystemExit(f"{context} missing expected text: {needle}")


def assert_not_contains(text: str, needle: str, context: str) -> None:
    if needle in text:
        raise SystemExit(f"{context} contains banned text: {needle}")


def main() -> int:
    data_root = SITE_ROOT / "_data" / "corpus" / "calibration"
    asset_root = SITE_ROOT / "assets" / "data" / "calibration"
    required_data = [
        "index.yml",
        "calibration_cascade.yml",
        "cascade_layers.yml",
        "constant_nodes.yml",
        "cascade_edges.yml",
        "ui_groups.yml",
        "constant_pages.yml",
        "coupling_ledger.yml",
        "mass_ratio_chain.yml",
        "constants_ledger.yml",
        "g_alpha_bridge.yml",
        "verification_comparisons.yml",
    ]
    for filename in required_data:
        read(data_root / filename)
    for filename in ("index.json", "constants-ledger.json", "constant-pages.json", "coupling-ledger.json", "ui-groups.json"):
        read(asset_root / filename)
    read(asset_root / "diagrams" / "alpha.mmd")

    route = read(SITE_ROOT / "results" / "calibration-cascade" / "index.md")
    assert_contains(route, "Calibration Cascade", "source route")
    assert_contains(route, "directed acyclic dependency structure", "source route")
    assert_contains(route, "Cascade overview", "source route")
    assert_contains(route, "calibration-compact-schematic", "source route")
    assert_contains(route, "ι_τ = 2/(π+e)", "source route")
    assert_contains(route, "Numerical Prediction Supplement", "source route")
    assert_contains(route, "calibration-key-node-grid", "source route")
    assert_contains(route, "Dependency edge table", "source route")
    assert_contains(route, "Follow the cascade", "source route")
    assert_contains(route, "Key constant cascades", "source route")
    assert_contains(route, "/results/calibration-cascade/constants/", "source route")
    assert_contains(route, "Tau-effective means τ-effective", "source route")
    assert_contains(route, "The page does not recompute CODATA 2022 values or change the existing numerical prediction artifact.", "source route")
    assert_contains(route, "<details", "source route")
    assert_contains(route, "<summary", "source route")
    assert_contains(route, "Mass-Ratio Chain", "source route")
    assert_contains(route, "scope group", "source route")
    assert_contains(route, "Source chapter details", "source route")
    assert_contains(route, "The constants ledger is a table of cascade outputs", "source route")
    assert_contains(route, "SI readout / unit realization", "source route")
    assert_contains(route, "CODATA 2018", "source route")
    assert_contains(route, "Bohr radius", "source route")
    assert_contains(route, "Text equivalent", "source route")
    assert_not_contains(route, "force-directed", "source route")
    assert_not_contains(route, "draggable", "source route")
    assert_not_contains(route, "Every SI value derives", "source route")
    assert_not_contains(route, "Numerical Physics Ledger PDF artifact", "source route")
    assert_not_contains(route, "Numerical Physics Ledger Artifact", "source route")
    assert_not_contains(route, "old Physics Ledger ontology", "source route")
    assert_not_contains(route, "calibration-layer-grid", "source route")
    if re.search(r"(?<![A-Za-z0-9])a_0(?!\^\{Bohr\})", route):
        raise SystemExit("source route contains bare a_0")

    expected_constants = [
        "alpha",
        "r1",
        "electron-mass",
        "alpha-g",
        "g",
        "planck-mass",
        "rydberg-constant",
        "bohr-radius",
        "compton-wavelength",
    ]
    constants_index = read(SITE_ROOT / "results" / "calibration-cascade" / "constants" / "index.md")
    assert_contains(constants_index, "Calibration Cascade Constants", "constants index")
    assert_contains(constants_index, "These detail pages cover the launch set of core cascade readouts", "constants index")
    assert_contains(constants_index, "full Constants Ledger remains available", "constants index")
    assert_contains(constants_index, "Tau-effective means τ-effective", "constants index")
    assert_not_contains(constants_index, "Numerical Physics Ledger PDF artifact", "constants index")
    for slug in expected_constants:
        source_page = read(SITE_ROOT / "results" / "calibration-cascade" / "constants" / slug / "index.md")
        assert_contains(source_page, "layout: \"calibration-constant-page\"", f"constant page {slug}")
        assert_contains(source_page, "formula_text:", f"constant page {slug}")
        assert_contains(source_page, "diagram_svg_status: \"rendered\"", f"constant page {slug}")
        assert_contains(source_page, "diagram_mmd_source:", f"constant page {slug}")
        assert_contains(source_page, "flowchart", f"constant page {slug}")
        assert_contains(source_page, "render_status: \"rendered\"", f"constant page {slug}")
        assert_not_contains(source_page, "Numerical Physics Ledger PDF artifact", f"constant page {slug}")

    bridge = read(SITE_ROOT / "results" / "physics" / "cascade" / "index.md")
    assert_contains(bridge, "/results/calibration-cascade/", "compatibility bridge")
    assert_not_contains(bridge, "Every SI value derives", "compatibility bridge")
    assert_not_contains(bridge, "SI-derived", "compatibility bridge")

    if BUILD_ROOT.exists():
        built = read(BUILD_ROOT / "results" / "calibration-cascade" / "index.html")
        assert_contains(built, "Calibration Cascade", "built route")
        assert_contains(built, "Directed Acyclic Cascade", "built route")
        assert_contains(built, "Cascade overview", "built route")
        assert_contains(built, "ι_τ = 2/(π+e)", "built route")
        assert_contains(built, "Follow the cascade", "built route")
        assert_contains(built, "Key constant cascades", "built route")
        assert_contains(built, "Dependency edge table", "built route")
        assert_contains(built, "Mass-Ratio Chain", "built route")
        assert_contains(built, "<details", "built route")
        assert_contains(built, "scope group", "built route")
        assert_contains(built, "CODATA 2018", "built route")
        assert_contains(built, "SI readout / unit realization", "built route")
        assert_contains(built, "Bohr radius", "built route")
        assert_contains(built, "Tau-effective means τ-effective", "built route")
        assert_contains(built, "The page does not recompute CODATA 2022 values or change the existing numerical prediction artifact.", "built route")
        assert_not_contains(built, "force-directed", "built route")
        assert_not_contains(built, "draggable", "built route")
        assert_not_contains(built, "Every SI value derives", "built route")
        assert_not_contains(built, "Numerical Physics Ledger PDF artifact", "built route")
        assert_not_contains(built, "Numerical Physics Ledger Artifact", "built route")
        assert_not_contains(built, "old Physics Ledger ontology", "built route")
        assert_not_contains(built, "calibration-layer-grid", "built route")
        if re.search(r"(?<![A-Za-z0-9])a_0(?!\^\{Bohr\})", built):
            raise SystemExit("built route contains bare a_0")
        built_index = read(BUILD_ROOT / "results" / "calibration-cascade" / "constants" / "index.html")
        assert_contains(built_index, "Calibration Cascade Constants", "built constants index")
        assert_contains(built_index, "launch set of core cascade readouts", "built constants index")
        for slug in expected_constants:
            built_page = read(BUILD_ROOT / "results" / "calibration-cascade" / "constants" / slug / "index.html")
            assert_contains(built_page, "Plain-text fallback", f"built constant page {slug}")
            assert_contains(built_page, "Dependency Diagram", f"built constant page {slug}")
            assert_contains(built_page, "<img", f"built constant page {slug}")
            assert_contains(built_page, "Tau-effective means τ-effective", f"built constant page {slug}")
            assert_not_contains(built_page, "Numerical Physics Ledger PDF artifact", f"built constant page {slug}")

    nav = read(SITE_ROOT / "_data" / "nav.yml")
    nav_section = nav[nav.find('title: "Falsifiable predictions"') :]
    assert_contains(nav_section, 'title: "Numerical Predictions"', "Results nav")
    assert_contains(nav_section, 'title: "Calibration Cascade"', "Results nav")
    assert_contains(nav_section, 'url: "/results/calibration-cascade/"', "Results nav")

    nav = read(SITE_ROOT / "_data" / "nav.yml")
    nav_section = nav[nav.find('title: "Falsifiable predictions"') :]
    assert_contains(nav_section, 'title: "Numerical Predictions"', "Results nav")
    assert_contains(nav_section, 'title: "Calibration Cascade"', "Results nav")
    assert_contains(nav_section, 'url: "/results/calibration-cascade/"', "Results nav")

    print("Calibration Cascade site projection assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
