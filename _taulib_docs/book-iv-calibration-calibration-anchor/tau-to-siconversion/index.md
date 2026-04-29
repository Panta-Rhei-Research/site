---
{
  "projection_kind": "taulib_declaration",
  "title": "TauToSIConversion",
  "permalink": "/verify/taulib/docs/book-iv-calibration-calibration-anchor/tau-to-siconversion/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.CalibrationAnchor`.",
  "declaration_id": "TauLib.BookIV.Calibration.CalibrationAnchor::TauToSIConversion",
  "declaration_slug": "tau-to-siconversion",
  "kind": "structure",
  "name": "TauToSIConversion",
  "module_name": "TauLib.BookIV.Calibration.CalibrationAnchor",
  "module_url": "/verify/taulib/docs/book-iv-calibration-calibration-anchor/",
  "source_line_start": 102,
  "source_line_end": 113,
  "registry_ids": [
    "IV.D31"
  ],
  "related_registry_items": [
    {
      "id": "IV.D31",
      "title": "τ-to-SI Conversion",
      "url": "/registry/object/IV.D31/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L102-L113",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L102-L113",
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
- Source path: [`TauLib/BookIV/Calibration/CalibrationAnchor.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L102-L113)
- Source range: L102-L113
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D31` — τ-to-SI Conversion

## Immediate Comment / Docstring

```lean
/-- [IV.D31] τ-to-SI conversion factor.

    In τ-native units: m_n = 1 (neutron mass defines the unit).
    The conversion factor Λ_M = m_n(SI) / m_n(τ) = m_n(SI).

    All masses: m_x(SI) = Λ_M × r_x(ι_τ)
    where r_x is the τ-native mass ratio for particle x. -/
```

## Source Excerpt

```lean
structure TauToSIConversion where
  /-- Name of the dimensional quantity. -/
  name : String
  /-- Conversion factor numerator: Λ × f(ι_τ). -/
  lambda_numer : Nat
  /-- Conversion factor denominator. -/
  lambda_denom : Nat
  /-- Denominator is positive. -/
  denom_pos : lambda_denom > 0
  /-- Whether this is the anchor itself or a derived quantity. -/
  is_anchor : Bool
  deriving Repr
```
