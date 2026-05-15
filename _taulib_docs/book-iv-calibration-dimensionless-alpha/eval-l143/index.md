---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L143",
  "permalink": "/corpus/taulib/docs/book-iv-calibration-dimensionless-alpha/eval-l143/",
  "summary_short": "`eval` declaration in `TauLib.BookIV.Calibration.DimensionlessAlpha`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionlessAlpha::#eval:143",
  "declaration_slug": "eval-l143",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookIV.Calibration.DimensionlessAlpha",
  "module_url": "/corpus/taulib/docs/book-iv-calibration-dimensionless-alpha/",
  "source_line_start": 143,
  "source_line_end": 143,
  "registry_ids": [
    "IV.R260"
  ],
  "related_registry_items": [
    {
      "id": "IV.R260",
      "title": "The value of being wrong",
      "url": "/registry/object/IV.R260/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L143-L143",
  "formal_status": "computed",
  "declaration_role": "computed check",
  "formal_status_label": "computed check",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.DimensionlessAlpha",
        "url": "/corpus/taulib/docs/book-iv-calibration-dimensionless-alpha/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L143-L143",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "role": "computed check",
      "status": "computed check"
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

- Module: [TauLib.BookIV.Calibration.DimensionlessAlpha](/corpus/taulib/docs/book-iv-calibration-dimensionless-alpha/)
- Source path: [`TauLib/BookIV/Calibration/DimensionlessAlpha.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L143-L143)
- Source range: L143-L143
- Kind: `eval`
- Public role: `computed check`
- Formal status hint: `computed check`

## Registry Links

- `IV.R260` — The value of being wrong

## Immediate Comment / Docstring

```lean
-- [IV.R260] Recording the correction of the 1st Edition wrong formula
-- demonstrates internal falsifiability. (Structural remark)

-- ============================================================
-- SMOKE TESTS
-- ============================================================
```

## Source Excerpt

```lean
#eval alpha_inverse_float           -- ≈ 137.9 (spectral)
```
