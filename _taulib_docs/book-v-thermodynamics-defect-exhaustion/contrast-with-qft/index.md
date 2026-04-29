---
{
  "projection_kind": "taulib_declaration",
  "title": "contrast_with_qft",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/contrast-with-qft/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.DefectExhaustion`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.DefectExhaustion::contrast_with_qft",
  "declaration_slug": "contrast-with-qft",
  "kind": "theorem",
  "name": "contrast_with_qft",
  "module_name": "TauLib.BookV.Thermodynamics.DefectExhaustion",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/",
  "source_line_start": 326,
  "source_line_end": 328,
  "registry_ids": [
    "V.R123"
  ],
  "related_registry_items": [
    {
      "id": "V.R123",
      "title": "Contrast with QFT",
      "url": "/registry/object/V.R123/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L326-L328",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.DefectExhaustion",
        "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L326-L328",
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

- Module: [TauLib.BookV.Thermodynamics.DefectExhaustion](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/)
- Source path: [`TauLib/BookV/Thermodynamics/DefectExhaustion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L326-L328)
- Source range: L326-L328
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R123` — Contrast with QFT

## Immediate Comment / Docstring

```lean
-- ============================================================
-- REMARKS
-- ============================================================

-- [V.R123] Contrast with QFT: in QFT, mode count is infinite
-- (UV catastrophe, vacuum divergence). In tau, mode count is
-- finite at every orbit depth.
```

## Source Excerpt

```lean
theorem contrast_with_qft :
    "QFT: infinite modes -> divergence; tau: finite modes -> no divergence" =
    "QFT: infinite modes -> divergence; tau: finite modes -> no divergence" := rfl
```
