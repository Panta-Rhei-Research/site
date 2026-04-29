---
{
  "projection_kind": "taulib_declaration",
  "title": "density_sector_sub_1300",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/density-sector-sub-1300/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::density_sector_sub_1300",
  "declaration_slug": "density-sector-sub-1300",
  "kind": "theorem",
  "name": "density_sector_sub_1300",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 2016,
  "source_line_end": 2020,
  "registry_ids": [
    "V.P186"
  ],
  "related_registry_items": [
    {
      "id": "V.P186",
      "title": "Density-Sector Sub-1300 ppm Consistency",
      "url": "/registry/object/V.P186/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L2016-L2020",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L2016-L2020",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L2016-L2020)
- Source range: L2016-L2020
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P186` — Density-Sector Sub-1300 ppm Consistency

## Immediate Comment / Docstring

```lean
/-- [V.P186] All ω_m-sensitive observables sub-1300 ppm. -/
```

## Source Excerpt

```lean
theorem density_sector_sub_1300 :
    density_closure_data.omega_m_ppm < 1300 ∧
    density_closure_data.rd_ppm < 1300 ∧
    density_closure_data.bao_max_ppm < 1300 := by
  native_decide
```
