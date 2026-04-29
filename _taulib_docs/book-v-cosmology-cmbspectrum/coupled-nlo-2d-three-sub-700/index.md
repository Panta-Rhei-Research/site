---
{
  "projection_kind": "taulib_declaration",
  "title": "coupled_nlo_2d_three_sub_700",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/coupled-nlo-2d-three-sub-700/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::coupled_nlo_2d_three_sub_700",
  "declaration_slug": "coupled-nlo-2d-three-sub-700",
  "kind": "theorem",
  "name": "coupled_nlo_2d_three_sub_700",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1769,
  "source_line_end": 1773,
  "registry_ids": [
    "V.P183"
  ],
  "related_registry_items": [
    {
      "id": "V.P183",
      "title": "Multi-Observable Consistency",
      "url": "/registry/object/V.P183/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1769-L1773",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1769-L1773",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1769-L1773)
- Source range: L1769-L1773
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P183` — Multi-Observable Consistency

## Immediate Comment / Docstring

```lean
/-- [V.P183] Three observables simultaneously sub-700 ppm. -/
```

## Source Excerpt

```lean
theorem coupled_nlo_2d_three_sub_700 :
    coupled_nlo_2d_data.omega_b_ppm < 700 ∧
    coupled_nlo_2d_data.ell1_ppm < 700 ∧
    coupled_nlo_2d_data.ell2_ppm < 700 := by
  native_decide
```
