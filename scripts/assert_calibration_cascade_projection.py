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
        "coupling_ledger.yml",
        "mass_ratio_chain.yml",
        "constants_ledger.yml",
        "g_alpha_bridge.yml",
        "verification_comparisons.yml",
    ]
    for filename in required_data:
        read(data_root / filename)
    for filename in ("index.json", "constants-ledger.json", "coupling-ledger.json", "ui-groups.json"):
        read(asset_root / filename)

    route = read(SITE_ROOT / "results" / "calibration-cascade" / "index.md")
    assert_contains(route, "Calibration Cascade", "source route")
    assert_contains(route, "directed acyclic dependency structure", "source route")
    assert_contains(route, "calibration-dag", "source route")
    assert_contains(route, "<details", "source route")
    assert_contains(route, "<summary", "source route")
    assert_contains(route, "Mass-Ratio Chain", "source route")
    assert_contains(route, "constants ledger table records source outputs", "source route")
    assert_contains(route, "SI readout / unit realization", "source route")
    assert_contains(route, "CODATA 2018", "source route")
    assert_contains(route, "Bohr radius", "source route")
    assert_contains(route, "Text equivalent", "source route")
    assert_not_contains(route, "force-directed", "source route")
    assert_not_contains(route, "draggable", "source route")
    assert_not_contains(route, "Every SI value derives", "source route")
    if re.search(r"(?<![A-Za-z0-9])a_0(?!\^\{Bohr\})", route):
        raise SystemExit("source route contains bare a_0")

    bridge = read(SITE_ROOT / "results" / "physics" / "cascade" / "index.md")
    assert_contains(bridge, "/results/calibration-cascade/", "compatibility bridge")
    assert_not_contains(bridge, "Every SI value derives", "compatibility bridge")
    assert_not_contains(bridge, "SI-derived", "compatibility bridge")

    if BUILD_ROOT.exists():
        built = read(BUILD_ROOT / "results" / "calibration-cascade" / "index.html")
        assert_contains(built, "Calibration Cascade", "built route")
        assert_contains(built, "Directed Acyclic Cascade", "built route")
        assert_contains(built, "Mass-Ratio Chain", "built route")
        assert_contains(built, "<details", "built route")
        assert_contains(built, "CODATA 2018", "built route")
        assert_contains(built, "SI readout / unit realization", "built route")
        assert_contains(built, "Bohr radius", "built route")
        assert_not_contains(built, "force-directed", "built route")
        assert_not_contains(built, "draggable", "built route")
        assert_not_contains(built, "Every SI value derives", "built route")
        if re.search(r"(?<![A-Za-z0-9])a_0(?!\^\{Bohr\})", built):
            raise SystemExit("built route contains bare a_0")

    print("Calibration Cascade site projection assertions passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
