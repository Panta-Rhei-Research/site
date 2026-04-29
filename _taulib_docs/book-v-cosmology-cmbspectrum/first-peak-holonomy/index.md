---
{
  "projection_kind": "taulib_declaration",
  "title": "FirstPeakHolonomy",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/first-peak-holonomy/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::FirstPeakHolonomy",
  "declaration_slug": "first-peak-holonomy",
  "kind": "structure",
  "name": "FirstPeakHolonomy",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 140,
  "source_line_end": 147,
  "registry_ids": [
    "V.T192"
  ],
  "related_registry_items": [
    {
      "id": "V.T192",
      "title": "First Peak from Holonomy Matter Fraction",
      "url": "/registry/object/V.T192/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L140-L147",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L140-L147",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L140-L147)
- Source range: L140-L147
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T192` — First Peak from Holonomy Matter Fraction

## Immediate Comment / Docstring

```lean
/-- [V.T192] First Peak from Holonomy Matter Fraction.
    ℓ₁ = 220.6 at +2840 ppm from Planck 220.0±0.5. -/
```

## Source Excerpt

```lean
structure FirstPeakHolonomy where
  /-- Number of free parameters. -/
  free_params : Nat := 0
  /-- Deviation from Planck in ppm. -/
  deviation_ppm : Nat := 2840
  /-- Number of pipeline steps (Friedmann integral chain). -/
  n_pipeline_steps : Nat := 4
  deriving Repr
```
