---
{
  "projection_kind": "taulib_declaration",
  "title": "r0_gt_1837",
  "permalink": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/r0-gt-1837/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.MassRatioFormula`.",
  "declaration_id": "TauLib.BookIV.Calibration.MassRatioFormula::r0_gt_1837",
  "declaration_slug": "r0-gt-1837",
  "kind": "theorem",
  "name": "r0_gt_1837",
  "module_name": "TauLib.BookIV.Calibration.MassRatioFormula",
  "module_url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/",
  "source_line_start": 189,
  "source_line_end": 192,
  "registry_ids": [
    "IV.T14"
  ],
  "related_registry_items": [
    {
      "id": "IV.T14",
      "title": "Level 0 Range",
      "url": "/registry/object/IV.T14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L189-L192",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.MassRatioFormula",
        "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L189-L192",
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

- Module: [TauLib.BookIV.Calibration.MassRatioFormula](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/)
- Source path: [`TauLib/BookIV/Calibration/MassRatioFormula.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L189-L192)
- Source range: L189-L192
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T14` — Level 0 Range

## Immediate Comment / Docstring

```lean
/-- [IV.T14] The Level 0 formula R₀ = ι_τ^(-7) − √3·ι_τ^(-2) is in range.

    R₀ > 1837: the formula gives a value > 1837.
    Proof strategy: bulk > correction + 1837, which avoids Nat subtraction.
    bulk_numer × correction0_denom > correction0_numer × bulk_denom + 1837 × bulk_denom × correction0_denom -/
```

## Source Excerpt

```lean
theorem r0_gt_1837 :
    bulk_numer * correction0_denom >
    correction0_numer * bulk_denom + 1837 * bulk_denom * correction0_denom := by
  native_decide
```
