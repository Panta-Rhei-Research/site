---
{
  "projection_kind": "taulib_declaration",
  "title": "NeutronMinimality",
  "permalink": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/neutron-minimality/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.CalibrationAnchorExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.CalibrationAnchorExt::NeutronMinimality",
  "declaration_slug": "neutron-minimality",
  "kind": "structure",
  "name": "NeutronMinimality",
  "module_name": "TauLib.BookIV.Calibration.CalibrationAnchorExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/",
  "source_line_start": 272,
  "source_line_end": 281,
  "registry_ids": [
    "IV.P166"
  ],
  "related_registry_items": [
    {
      "id": "IV.P166",
      "title": "Neutron Minimality",
      "url": "/registry/object/IV.P166/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L272-L281",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.CalibrationAnchorExt",
        "url": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L272-L281",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookIV.Calibration.CalibrationAnchorExt](/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/)
- Source path: [`TauLib/BookIV/Calibration/CalibrationAnchorExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L272-L281)
- Source range: L272-L281
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P166` — Neutron Minimality

## Immediate Comment / Docstring

```lean
/-- [IV.P166] Neutron Minimality: the neutron is the minimal stable
    unpolarized T² defect bundle.

    "Minimal" means: among all unpolarized defect bundles on T²,
    the neutron has the lowest mass (= smallest defect functional).
    This is WHY it serves as the calibration anchor — it is the
    FIRST stable particle the τ-framework produces. -/
```

## Source Excerpt

```lean
structure NeutronMinimality where
  /-- The neutron is unpolarized. -/
  bundle : UnpolarizedDefectBundle
  /-- The bundle is indeed unpolarized. -/
  is_unpol : is_unpolarized bundle = true
  /-- The neutron is the lightest (minimal mass among unpolarized). -/
  is_minimal : Bool
  /-- The neutron is stable (lifetime > universe age). -/
  is_stable : Bool
  deriving Repr
```
