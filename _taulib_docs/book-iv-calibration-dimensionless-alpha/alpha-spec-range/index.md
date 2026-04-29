---
{
  "projection_kind": "taulib_declaration",
  "title": "alpha_spec_range",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/alpha-spec-range/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.DimensionlessAlpha`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionlessAlpha::alpha_spec_range",
  "declaration_slug": "alpha-spec-range",
  "kind": "theorem",
  "name": "alpha_spec_range",
  "module_name": "TauLib.BookIV.Calibration.DimensionlessAlpha",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/",
  "source_line_start": 41,
  "source_line_end": 44,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L41-L44",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.DimensionlessAlpha",
        "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L41-L44",
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

- Module: [TauLib.BookIV.Calibration.DimensionlessAlpha](/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/)
- Source path: [`TauLib/BookIV/Calibration/DimensionlessAlpha.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L41-L44)
- Source range: L41-L44
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The spectral formula gives 1/α between 137 and 139. -/
```

## Source Excerpt

```lean
theorem alpha_spec_range :
    alpha_spec_denom > 137 * alpha_spec_numer ∧
    alpha_spec_denom < 139 * alpha_spec_numer :=
  alpha_inverse_correct_ballpark
```
