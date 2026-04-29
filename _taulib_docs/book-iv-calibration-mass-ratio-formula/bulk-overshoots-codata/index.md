---
{
  "projection_kind": "taulib_declaration",
  "title": "bulk_overshoots_codata",
  "permalink": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-overshoots-codata/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.MassRatioFormula`.",
  "declaration_id": "TauLib.BookIV.Calibration.MassRatioFormula::bulk_overshoots_codata",
  "declaration_slug": "bulk-overshoots-codata",
  "kind": "theorem",
  "name": "bulk_overshoots_codata",
  "module_name": "TauLib.BookIV.Calibration.MassRatioFormula",
  "module_url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/",
  "source_line_start": 176,
  "source_line_end": 178,
  "registry_ids": [
    "IV.T13"
  ],
  "related_registry_items": [
    {
      "id": "IV.T13",
      "title": "Bulk Overshoots",
      "url": "/registry/object/IV.T13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L176-L178",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L176-L178",
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
- Source path: [`TauLib/BookIV/Calibration/MassRatioFormula.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L176-L178)
- Source range: L176-L178
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T13` — Bulk Overshoots

## Immediate Comment / Docstring

```lean
/-- [IV.T13] The bulk term ι_τ^(-7) overshoots R_CODATA.

    Even with the 6-digit approximation, ι_τ^(-7) ≈ 1847.5 > 1838.68 = R.
    This proves the correction term has the right SIGN (must be subtracted). -/
```

## Source Excerpt

```lean
theorem bulk_overshoots_codata :
    bulk_numer * si_mass_ratio.denom > si_mass_ratio.numer * bulk_denom := by
  native_decide
```
