---
{
  "projection_kind": "taulib_declaration",
  "title": "peaks_ell1_sub_200",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/peaks-ell1-sub-200/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::peaks_ell1_sub_200",
  "declaration_slug": "peaks-ell1-sub-200",
  "kind": "theorem",
  "name": "peaks_ell1_sub_200",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1922,
  "source_line_end": 1923,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1922-L1923",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1922-L1923",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1922-L1923)
- Source range: L1922-L1923
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.D329` — ω_m–Peaks Pareto Barrier

## Immediate Comment / Docstring

```lean
/-- [V.D329] Peaks regime: ℓ₁ sub-200 ppm. -/
```

## Source Excerpt

```lean
theorem peaks_ell1_sub_200 :
    pareto_barrier_data.peaks_ell1_ppm < 200 := by native_decide
```
