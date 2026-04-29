---
{
  "projection_kind": "taulib_declaration",
  "title": "near_match_table",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/near-match-table/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Calibration.DimensionlessNearMatch`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionlessNearMatch::near_match_table",
  "declaration_slug": "near-match-table",
  "kind": "def",
  "name": "near_match_table",
  "module_name": "TauLib.BookIV.Calibration.DimensionlessNearMatch",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/",
  "source_line_start": 158,
  "source_line_end": 171,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L158-L171",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L158-L171",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookIV/Calibration/DimensionlessNearMatch.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L158-L171)
- Source range: L158-L171
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The three dimensionless near-match entries. -/
```

## Source Excerpt

```lean
def near_match_table : List NearMatchEntry := [
  ⟨"Fine structure 1/α",
   alpha_spectral_denom, alpha_spectral_numer,  -- inverted for 1/α
   si_alpha_inverse.numer, si_alpha_inverse.denom,
   true⟩,  -- τ gives 1/α ≈ 137.9 > 137.036
  ⟨"Weinberg sin²θ_W",
   kappa_AD.numer, kappa_AD.denom,
   si_weinberg_sin2.numer, si_weinberg_sin2.denom,
   false⟩,  -- τ gives 0.2249 < 0.2312
  ⟨"Strong α_s(M_Z)",
   2 * kappa_CC.numer, kappa_CC.denom,
   si_strong_coupling.numer, si_strong_coupling.denom,
   true⟩   -- τ gives 0.1208 > 0.1180
]
```
