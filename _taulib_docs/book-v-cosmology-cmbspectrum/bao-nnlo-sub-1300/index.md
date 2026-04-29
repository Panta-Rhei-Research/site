---
{
  "projection_kind": "taulib_declaration",
  "title": "bao_nnlo_sub_1300",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/bao-nnlo-sub-1300/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::bao_nnlo_sub_1300",
  "declaration_slug": "bao-nnlo-sub-1300",
  "kind": "theorem",
  "name": "bao_nnlo_sub_1300",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1966,
  "source_line_end": 1972,
  "registry_ids": [
    "V.T267"
  ],
  "related_registry_items": [
    {
      "id": "V.T267",
      "title": "BAO Sub-1300 ppm at NNLO",
      "url": "/registry/object/V.T267/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1966-L1972",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1966-L1972",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1966-L1972)
- Source range: L1966-L1972
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T267` — BAO Sub-1300 ppm at NNLO

## Immediate Comment / Docstring

```lean
/-- [V.T267] All 5 DESI bins sub-1300 ppm at NNLO. -/
```

## Source Excerpt

```lean
theorem bao_nnlo_sub_1300 :
    bao_nnlo_data.dv_rd_ppm_z051 < 1300 ∧
    bao_nnlo_data.dv_rd_ppm_z071 < 1300 ∧
    bao_nnlo_data.dv_rd_ppm_z093 < 1300 ∧
    bao_nnlo_data.dv_rd_ppm_z132 < 1300 ∧
    bao_nnlo_data.dv_rd_ppm_z233 < 1300 := by
  native_decide
```
