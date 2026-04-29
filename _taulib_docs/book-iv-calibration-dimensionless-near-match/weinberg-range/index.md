---
{
  "projection_kind": "taulib_declaration",
  "title": "weinberg_range",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/weinberg-range/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.DimensionlessNearMatch`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionlessNearMatch::weinberg_range",
  "declaration_slug": "weinberg-range",
  "kind": "theorem",
  "name": "weinberg_range",
  "module_name": "TauLib.BookIV.Calibration.DimensionlessNearMatch",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/",
  "source_line_start": 59,
  "source_line_end": 61,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L59-L61",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L59-L61",
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
- Source path: [`TauLib/BookIV/Calibration/DimensionlessNearMatch.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean#L59-L61)
- Source range: L59-L61
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- κ(A,D) is in the range (0.224, 0.226). -/
```

## Source Excerpt

```lean
theorem weinberg_range :
    kappa_AD.numer * 1000 > 224 * kappa_AD.denom ∧
    kappa_AD.numer * 1000 < 226 * kappa_AD.denom := by native_decide
```
