---
{
  "projection_kind": "taulib_declaration",
  "title": "HorizonComparison",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-ehtreread/horizon-comparison/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.EHTReread`.",
  "declaration_id": "TauLib.BookV.Astrophysics.EHTReread::HorizonComparison",
  "declaration_slug": "horizon-comparison",
  "kind": "structure",
  "name": "HorizonComparison",
  "module_name": "TauLib.BookV.Astrophysics.EHTReread",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/",
  "source_line_start": 191,
  "source_line_end": 204,
  "registry_ids": [
    "V.D139"
  ],
  "related_registry_items": [
    {
      "id": "V.D139",
      "title": "Polarization Handedness Signature",
      "url": "/registry/object/V.D139/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L191-L204",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.EHTReread",
        "url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L191-L204",
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

- Module: [TauLib.BookV.Astrophysics.EHTReread](/verify/taulib/docs/book-v-astrophysics-ehtreread/)
- Source path: [`TauLib/BookV/Astrophysics/EHTReread.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L191-L204)
- Source range: L191-L204
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D139` — Polarization Handedness Signature

## Immediate Comment / Docstring

```lean
/-- [V.D139] Tau vs GR horizon comparison: side-by-side comparison
    of the two frameworks' predictions near the horizon. -/
```

## Source Excerpt

```lean
structure HorizonComparison where
  /-- GR prediction: event horizon, information lost, singularity. -/
  gr_has_singularity : Bool := true
  /-- GR prediction: information is lost. -/
  gr_information_lost : Bool := true
  /-- τ prediction: topology crossing, information preserved, no singularity. -/
  tau_has_singularity : Bool := false
  /-- τ prediction: information is preserved. -/
  tau_information_preserved : Bool := true
  /-- Shadow prediction: identical (differences below photon sphere). -/
  shadow_identical : Bool := true
  /-- Photon ring: identical (differences below photon sphere). -/
  photon_ring_identical : Bool := true
  deriving Repr
```
