---
{
  "projection_kind": "taulib_declaration",
  "title": "FreeStreamingSuppression",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/free-streaming-suppression/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::FreeStreamingSuppression",
  "declaration_slug": "free-streaming-suppression",
  "kind": "structure",
  "name": "FreeStreamingSuppression",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 306,
  "source_line_end": 313,
  "registry_ids": [
    "V.P137"
  ],
  "related_registry_items": [
    {
      "id": "V.P137",
      "title": "Free-Streaming Suppression from τ-Native Masses",
      "url": "/registry/object/V.P137/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L306-L313",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L306-L313",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L306-L313)
- Source range: L306-L313
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P137` — Free-Streaming Suppression from τ-Native Masses

## Immediate Comment / Docstring

```lean
/-- [V.P137] Free-Streaming Suppression from τ-Native Masses.
    ΔP/P ≈ −8f_ν = −5.14%. Detectable: DESI ~4.5σ, Euclid ~5-9σ. -/
```

## Source Excerpt

```lean
structure FreeStreamingSuppression where
  /-- Number of BES formula factors (−8f_ν). -/
  n_formula_factors : Nat := 1
  /-- DESI detection significance in σ ×10 (4.5σ → 45). -/
  desi_sigma_x10 : Nat := 45
  /-- Number of free parameters. -/
  free_params : Nat := 0
  deriving Repr
```
