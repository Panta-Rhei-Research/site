---
{
  "projection_kind": "taulib_declaration",
  "title": "StrongNearMatch",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/strong-near-match/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.DimensionlessNearMatch`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionlessNearMatch::StrongNearMatch",
  "declaration_slug": "strong-near-match",
  "kind": "structure",
  "name": "StrongNearMatch",
  "module_name": "TauLib.BookIV.Calibration.DimensionlessNearMatch",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/",
  "source_line_start": 85,
  "source_line_end": 93,
  "registry_ids": [
    "IV.D29"
  ],
  "related_registry_items": [
    {
      "id": "IV.D29",
      "title": "Strong Near-Match",
      "url": "/registry/object/IV.D29/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L85-L93",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.DimensionlessNearMatch",
        "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L85-L93",
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

- Module: [TauLib.BookIV.Calibration.DimensionlessNearMatch](/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/)
- Source path: [`TauLib/BookIV/Calibration/DimensionlessNearMatch.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L85-L93)
- Source range: L85-L93
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D29` — Strong Near-Match

## Immediate Comment / Docstring

```lean
/-- [IV.D29] Strong coupling near-match: 2·κ(C,C) vs α_s(M_Z).

    τ-derived: 2·κ(C) = 2·ι_τ³/(1−ι_τ) ≈ 0.1208
    Experimental: α_s(M_Z) = 0.1180(9)
    Deviation: ~2.4% -/
```

## Source Excerpt

```lean
structure StrongNearMatch where
  /-- τ-derived coupling formula (doubled). -/
  tau_coupling : CouplingFormula := kappa_CC
  /-- Multiplication factor. -/
  factor : Nat := 2
  /-- SI reference value. -/
  si_value : SIConstant := si_strong_coupling
  /-- Scope: established (near-match with range proof). -/
  scope : String := "established"
```
