---
{
  "projection_kind": "taulib_declaration",
  "title": "bao_nnlo_improvement",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/bao-nnlo-improvement/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::bao_nnlo_improvement",
  "declaration_slug": "bao-nnlo-improvement",
  "kind": "theorem",
  "name": "bao_nnlo_improvement",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1975,
  "source_line_end": 1977,
  "registry_ids": [
    "V.P185"
  ],
  "related_registry_items": [
    {
      "id": "V.P185",
      "title": "BAO Systematic Improvement NLO→NNLO",
      "url": "/registry/object/V.P185/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1975-L1977",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.CMBSpectrum",
        "url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1975-L1977",
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

- Module: [TauLib.BookV.Cosmology.CMBSpectrum](/verify/taulib/docs/book-v-cosmology-cmbspectrum/)
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1975-L1977)
- Source range: L1975-L1977
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P185` — BAO Systematic Improvement NLO→NNLO

## Immediate Comment / Docstring

```lean
/-- [V.P185] NNLO improves over NLO by ≥20×. -/
```

## Source Excerpt

```lean
theorem bao_nnlo_improvement :
    bao_nnlo_data.nlo_mean_ppm / bao_nnlo_data.nnlo_mean_ppm ≥ 20 := by
  native_decide
```
