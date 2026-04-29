---
{
  "projection_kind": "taulib_declaration",
  "title": "coupled_nlo_2d_ell1_sub_200",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/coupled-nlo-2d-ell1-sub-200/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::coupled_nlo_2d_ell1_sub_200",
  "declaration_slug": "coupled-nlo-2d-ell1-sub-200",
  "kind": "theorem",
  "name": "coupled_nlo_2d_ell1_sub_200",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1759,
  "source_line_end": 1761,
  "registry_ids": [
    "V.T264"
  ],
  "related_registry_items": [
    {
      "id": "V.T264",
      "title": "Coupled NLO Optimum: δ_h = κ_D/N_e",
      "url": "/registry/object/V.T264/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1759-L1761",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1759-L1761",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1759-L1761)
- Source range: L1759-L1761
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T264` — Coupled NLO Optimum: δ_h = κ_D/N_e

## Immediate Comment / Docstring

```lean
/-- [V.T264] Coupled NLO achieves ℓ₁ sub-200 ppm. -/
```

## Source Excerpt

```lean
theorem coupled_nlo_2d_ell1_sub_200 :
    coupled_nlo_2d_data.ell1_ppm < 200 := by
  native_decide
```
