---
{
  "projection_kind": "taulib_declaration",
  "title": "WeinbergNearMatch",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/weinberg-near-match/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.DimensionlessNearMatch`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionlessNearMatch::WeinbergNearMatch",
  "declaration_slug": "weinberg-near-match",
  "kind": "structure",
  "name": "WeinbergNearMatch",
  "module_name": "TauLib.BookIV.Calibration.DimensionlessNearMatch",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/",
  "source_line_start": 50,
  "source_line_end": 56,
  "registry_ids": [
    "IV.D28"
  ],
  "related_registry_items": [
    {
      "id": "IV.D28",
      "title": "Weinberg Near-Match",
      "url": "/registry/object/IV.D28/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L50-L56",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L50-L56",
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
- Source path: [`TauLib/BookIV/Calibration/DimensionlessNearMatch.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L50-L56)
- Source range: L50-L56
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D28` — Weinberg Near-Match

## Immediate Comment / Docstring

```lean
/-- [IV.D28] Weinberg angle near-match: κ(A,D) = ι_τ(1−ι_τ) vs sin²θ_W.

    τ-derived: κ(A,D) ≈ 0.2249
    Experimental: sin²θ_W = 0.23121(4) (on-shell, CODATA 2022)
    Deviation: ~2.7% -/
```

## Source Excerpt

```lean
structure WeinbergNearMatch where
  /-- τ-derived coupling formula. -/
  tau_coupling : CouplingFormula := kappa_AD
  /-- SI reference value. -/
  si_value : SIConstant := si_weinberg_sin2
  /-- Scope: established (near-match with range proof). -/
  scope : String := "established"
```
