---
{
  "projection_kind": "taulib_declaration",
  "title": "CalibrationAnchor",
  "permalink": "/verify/taulib/docs/book-iv-calibration-calibration-anchor/calibration-anchor/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.CalibrationAnchor`.",
  "declaration_id": "TauLib.BookIV.Calibration.CalibrationAnchor::CalibrationAnchor",
  "declaration_slug": "calibration-anchor",
  "kind": "structure",
  "name": "CalibrationAnchor",
  "module_name": "TauLib.BookIV.Calibration.CalibrationAnchor",
  "module_url": "/verify/taulib/docs/book-iv-calibration-calibration-anchor/",
  "source_line_start": 64,
  "source_line_end": 75,
  "registry_ids": [
    "IV.D30"
  ],
  "related_registry_items": [
    {
      "id": "IV.D30",
      "title": "Calibration Anchor",
      "url": "/registry/object/IV.D30/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L64-L75",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.CalibrationAnchor",
        "url": "/verify/taulib/docs/book-iv-calibration-calibration-anchor/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L64-L75",
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

- Module: [TauLib.BookIV.Calibration.CalibrationAnchor](/verify/taulib/docs/book-iv-calibration-calibration-anchor/)
- Source path: [`TauLib/BookIV/Calibration/CalibrationAnchor.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L64-L75)
- Source range: L64-L75
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D30` — Calibration Anchor

## Immediate Comment / Docstring

```lean
/-- [IV.D30] The calibration anchor: the neutron mass as the single
    experimental input that pins the τ-to-SI conversion.

    In τ-native units, the neutron mass defines the unit (m_n(τ) = 1).
    In SI, m_n = 1.674 927 498 04(95) × 10⁻²⁷ kg (CODATA 2022). -/
```

## Source Excerpt

```lean
structure CalibrationAnchor where
  /-- Neutron mass in SI: numer/denom kg. -/
  mass_numer : Nat
  /-- Denominator for mass scaling. -/
  mass_denom : Nat
  /-- Denominator is positive. -/
  denom_pos : mass_denom > 0
  /-- The SI reference constant this anchors to. -/
  si_ref : SIConstant
  /-- This is the ONLY free dimensional parameter. -/
  is_sole_anchor : Bool
  deriving Repr
```
