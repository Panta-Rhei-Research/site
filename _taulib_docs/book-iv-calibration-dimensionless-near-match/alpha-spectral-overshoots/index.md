---
{
  "projection_kind": "taulib_declaration",
  "title": "alpha_spectral_overshoots",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/alpha-spectral-overshoots/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.DimensionlessNearMatch`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionlessNearMatch::alpha_spectral_overshoots",
  "declaration_slug": "alpha-spectral-overshoots",
  "kind": "theorem",
  "name": "alpha_spectral_overshoots",
  "module_name": "TauLib.BookIV.Calibration.DimensionlessNearMatch",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/",
  "source_line_start": 120,
  "source_line_end": 122,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L120-L122",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L120-L122",
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
- Source path: [`TauLib/BookIV/Calibration/DimensionlessNearMatch.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L120-L122)
- Source range: L120-L122
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The spectral 1/α overshoots the experimental value:
    α_spectral < α_exp (i.e. 1/α_spectral > 1/α_exp).
    Spectral: 1/α ≈ 137.9, Experimental: 1/α ≈ 137.036. -/
```

## Source Excerpt

```lean
theorem alpha_spectral_overshoots :
    alpha_spectral_denom * si_alpha_inverse.denom >
    si_alpha_inverse.numer * alpha_spectral_numer := by native_decide
```
