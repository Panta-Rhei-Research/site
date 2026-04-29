---
{
  "projection_kind": "taulib_declaration",
  "title": "weinberg_undershoots",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/weinberg-undershoots/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.DimensionlessNearMatch`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionlessNearMatch::weinberg_undershoots",
  "declaration_slug": "weinberg-undershoots",
  "kind": "theorem",
  "name": "weinberg_undershoots",
  "module_name": "TauLib.BookIV.Calibration.DimensionlessNearMatch",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/",
  "source_line_start": 64,
  "source_line_end": 66,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L64-L66",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L64-L66",
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
- Source path: [`TauLib/BookIV/Calibration/DimensionlessNearMatch.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L64-L66)
- Source range: L64-L66
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- κ(A,D) < sin²θ_W: the τ-approximation undershoots the experimental value. -/
```

## Source Excerpt

```lean
theorem weinberg_undershoots :
    kappa_AD.numer * si_weinberg_sin2.denom <
    si_weinberg_sin2.numer * kappa_AD.denom := by native_decide
```
