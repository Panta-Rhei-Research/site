---
{
  "projection_kind": "taulib_declaration",
  "title": "all_near_matches_in_range",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/all-near-matches-in-range/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.DimensionlessNearMatch`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionlessNearMatch::all_near_matches_in_range",
  "declaration_slug": "all-near-matches-in-range",
  "kind": "theorem",
  "name": "all_near_matches_in_range",
  "module_name": "TauLib.BookIV.Calibration.DimensionlessNearMatch",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/",
  "source_line_start": 131,
  "source_line_end": 141,
  "registry_ids": [
    "IV.P05"
  ],
  "related_registry_items": [
    {
      "id": "IV.P05",
      "title": "All Near-Matches in Range",
      "url": "/registry/object/IV.P05/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L131-L141",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L131-L141",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookIV/Calibration/DimensionlessNearMatch.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L131-L141)
- Source range: L131-L141
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P05` — All Near-Matches in Range

## Immediate Comment / Docstring

```lean
/-- [IV.P05] All three dimensionless near-matches are within their
    respective range brackets. This is a structural observation,
    NOT a proof of correctness — all three are CONJECTURAL. -/
```

## Source Excerpt

```lean
theorem all_near_matches_in_range :
    -- α: spectral 1/α between 137 and 139 (exp: 137.036)
    (alpha_spectral_denom > 137 * alpha_spectral_numer ∧
     alpha_spectral_denom < 139 * alpha_spectral_numer) ∧
    -- sin²θ_W: κ(A,D) between 0.224 and 0.226 (exp: 0.2312)
    (kappa_AD.numer * 1000 > 224 * kappa_AD.denom ∧
     kappa_AD.numer * 1000 < 226 * kappa_AD.denom) ∧
    -- α_s: 2·κ(C) between 0.119 and 0.122 (exp: 0.1180)
    (2 * kappa_CC.numer * 1000 > 119 * kappa_CC.denom ∧
     2 * kappa_CC.numer * 1000 < 122 * kappa_CC.denom) :=
  ⟨alpha_inverse_correct_ballpark, weinberg_range, strong_range⟩
```
