---
{
  "projection_kind": "taulib_declaration",
  "title": "de_closure_omega_lambda",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/de-closure-omega-lambda/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::de_closure_omega_lambda",
  "declaration_slug": "de-closure-omega-lambda",
  "kind": "def",
  "name": "de_closure_omega_lambda",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 362,
  "source_line_end": 363,
  "registry_ids": [
    "V.D252"
  ],
  "related_registry_items": [
    {
      "id": "V.D252",
      "title": "DE-Closure Matter Density ω_m from Ω_Λ and h",
      "url": "/registry/object/V.D252/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L362-L363",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L362-L363",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L362-L363)
- Source range: L362-L363
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.D252` — DE-Closure Matter Density ω_m from Ω_Λ and h

## Immediate Comment / Docstring

```lean
/-- [V.D252] DE-Closure Matter Density.
    Ω_Λ = κ_D·(1+ι_τ³) = 0.6849.
    ω_m = (1−Ω_Λ−Ω_r)·h² = 0.1429. Planck: 0.1430 (−674 ppm). -/
```

## Source Excerpt

```lean
def de_closure_omega_lambda : Float :=
  kappa_D * (1.0 + iota_float * iota_float * iota_float)
```
