---
{
  "projection_kind": "taulib_declaration",
  "title": "n_e_nnlo_structural",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/n-e-nnlo-structural/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::n_e_nnlo_structural",
  "declaration_slug": "n-e-nnlo-structural",
  "kind": "theorem",
  "name": "n_e_nnlo_structural",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1881,
  "source_line_end": 1882,
  "registry_ids": [
    "V.D328"
  ],
  "related_registry_items": [
    {
      "id": "V.D328",
      "title": "ω_m NNLO Correction Space",
      "url": "/registry/object/V.D328/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1881-L1882",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1881-L1882",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1881-L1882)
- Source range: L1881-L1882
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.D328` — ω_m NNLO Correction Space

## Immediate Comment / Docstring

```lean
/-- [V.D328] N_e = dim × W₅(3) = 3 × 19 (NNLO context). -/
```

## Source Excerpt

```lean
theorem n_e_nnlo_structural :
    omega_m_nnlo_data.n_e = 3 * 19 := by native_decide
```
