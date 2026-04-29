---
{
  "projection_kind": "taulib_declaration",
  "title": "CalibrationAnchorExt",
  "permalink": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/calibration-anchor-ext/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.CalibrationAnchorExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.CalibrationAnchorExt::CalibrationAnchorExt",
  "declaration_slug": "calibration-anchor-ext",
  "kind": "structure",
  "name": "CalibrationAnchorExt",
  "module_name": "TauLib.BookIV.Calibration.CalibrationAnchorExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/",
  "source_line_start": 305,
  "source_line_end": 316,
  "registry_ids": [
    "IV.D291"
  ],
  "related_registry_items": [
    {
      "id": "IV.D291",
      "title": "Calibration Anchor",
      "url": "/registry/object/IV.D291/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L305-L316",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L305-L316",
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
- Source path: [`TauLib/BookIV/Calibration/CalibrationAnchorExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L305-L316)
- Source range: L305-L316
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D291` — Calibration Anchor

## Immediate Comment / Docstring

```lean
/-- [IV.D291] Extended calibration anchor with explicit CODATA values.

    The neutron mass m_n = 1.674 927 500 × 10⁻²⁷ kg (rounded to
    10-digit numer for the extension), with uncertainty ~50 ppb. -/
```

## Source Excerpt

```lean
structure CalibrationAnchorExt where
  /-- Neutron mass numerator (SI kg): 1674927500. -/
  neutron_mass_kg_numer : Nat
  /-- Neutron mass denominator (SI kg): 10^36. -/
  neutron_mass_kg_denom : Nat
  /-- Denominator is positive. -/
  denom_pos : neutron_mass_kg_denom > 0
  /-- Uncertainty in parts per billion. -/
  uncertainty_ppb : Nat
  /-- This is the sole anchor (one free parameter). -/
  sole_anchor : Bool
  deriving Repr
```
