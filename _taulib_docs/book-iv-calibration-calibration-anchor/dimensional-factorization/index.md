---
{
  "projection_kind": "taulib_declaration",
  "title": "DimensionalFactorization",
  "permalink": "/verify/taulib/docs/book-iv-calibration-calibration-anchor/dimensional-factorization/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.CalibrationAnchor`.",
  "declaration_id": "TauLib.BookIV.Calibration.CalibrationAnchor::DimensionalFactorization",
  "declaration_slug": "dimensional-factorization",
  "kind": "structure",
  "name": "DimensionalFactorization",
  "module_name": "TauLib.BookIV.Calibration.CalibrationAnchor",
  "module_url": "/verify/taulib/docs/book-iv-calibration-calibration-anchor/",
  "source_line_start": 130,
  "source_line_end": 141,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L130-L141",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L130-L141",
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
- Source path: [`TauLib/BookIV/Calibration/CalibrationAnchor.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L130-L141)
- Source range: L130-L141
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Every dimensional constant in the τ-framework factors as:
    constant(SI) = Λ_M^a × f(ι_τ) × (geometric factors)
    where a is the mass dimension and f(ι_τ) is a rational function. -/
```

## Source Excerpt

```lean
structure DimensionalFactorization where
  /-- Name of the constant. -/
  name : String
  /-- Mass dimension (power of Λ_M). -/
  mass_dim : Int
  /-- ι_τ-dependent factor numerator. -/
  iota_factor_numer : Nat
  /-- ι_τ-dependent factor denominator. -/
  iota_factor_denom : Nat
  /-- Denominator is positive. -/
  denom_pos : iota_factor_denom > 0
  deriving Repr
```
