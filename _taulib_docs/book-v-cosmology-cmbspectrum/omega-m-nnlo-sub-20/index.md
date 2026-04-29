---
{
  "projection_kind": "taulib_declaration",
  "title": "omega_m_nnlo_sub_20",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/omega-m-nnlo-sub-20/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::omega_m_nnlo_sub_20",
  "declaration_slug": "omega-m-nnlo-sub-20",
  "kind": "theorem",
  "name": "omega_m_nnlo_sub_20",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1873,
  "source_line_end": 1874,
  "registry_ids": [
    "V.T265"
  ],
  "related_registry_items": [
    {
      "id": "V.T265",
      "title": "ω_m Sub-20 ppm at NNLO",
      "url": "/registry/object/V.T265/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1873-L1874",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1873-L1874",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1873-L1874)
- Source range: L1873-L1874
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T265` — ω_m Sub-20 ppm at NNLO

## Immediate Comment / Docstring

```lean
/-- [V.T265] ω_m sub-20 ppm at NNLO. -/
```

## Source Excerpt

```lean
theorem omega_m_nnlo_sub_20 :
    omega_m_nnlo_data.omega_m_ppm < 20 := by native_decide
```
