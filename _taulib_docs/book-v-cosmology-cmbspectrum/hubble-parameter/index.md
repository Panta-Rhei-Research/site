---
{
  "projection_kind": "taulib_declaration",
  "title": "HubbleParameter",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/hubble-parameter/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::HubbleParameter",
  "declaration_slug": "hubble-parameter",
  "kind": "structure",
  "name": "HubbleParameter",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 599,
  "source_line_end": 606,
  "registry_ids": [
    "V.T196"
  ],
  "related_registry_items": [
    {
      "id": "V.T196",
      "title": "Hubble Parameter from τ: h at −120 ppm",
      "url": "/registry/object/V.T196/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L599-L606",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L599-L606",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L599-L606)
- Source range: L599-L606
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T196` — Hubble Parameter from τ: h at −120 ppm

## Immediate Comment / Docstring

```lean
/-- [V.T196] Hubble Parameter from τ at −120 ppm.
    h = 2/3 + ι_τ²/W₃(3) = 2/3 + ι_τ²/17 = 0.67352.
    Base: 2/3 = EdS exponent. Correction: κ_B/17. -/
```

## Source Excerpt

```lean
structure HubbleParameter where
  /-- W₃(3) = 17 from CF window. -/
  w33 : Nat := 17
  /-- Correction power (ι_τ² → 2). -/
  correction_power : Nat := 2
  /-- Number of free parameters. -/
  free_params : Nat := 0
  deriving Repr
```
