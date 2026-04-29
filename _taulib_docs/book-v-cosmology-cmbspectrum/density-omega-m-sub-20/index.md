---
{
  "projection_kind": "taulib_declaration",
  "title": "density_omega_m_sub_20",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/density-omega-m-sub-20/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::density_omega_m_sub_20",
  "declaration_slug": "density-omega-m-sub-20",
  "kind": "theorem",
  "name": "density_omega_m_sub_20",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1918,
  "source_line_end": 1919,
  "registry_ids": [
    "V.D329"
  ],
  "related_registry_items": [
    {
      "id": "V.D329",
      "title": "ω_m–Peaks Pareto Barrier",
      "url": "/registry/object/V.D329/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1918-L1919",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1918-L1919",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1918-L1919)
- Source range: L1918-L1919
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.D329` — ω_m–Peaks Pareto Barrier

## Immediate Comment / Docstring

```lean
/-- [V.D329] Density regime: ω_m sub-20 ppm. -/
```

## Source Excerpt

```lean
theorem density_omega_m_sub_20 :
    pareto_barrier_data.density_omega_m_ppm < 20 := by native_decide
```
