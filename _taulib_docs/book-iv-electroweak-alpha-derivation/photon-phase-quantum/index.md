---
{
  "projection_kind": "taulib_declaration",
  "title": "PhotonPhaseQuantum",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/photon-phase-quantum/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.AlphaDerivation`.",
  "declaration_id": "TauLib.BookIV.Electroweak.AlphaDerivation::PhotonPhaseQuantum",
  "declaration_slug": "photon-phase-quantum",
  "kind": "structure",
  "name": "PhotonPhaseQuantum",
  "module_name": "TauLib.BookIV.Electroweak.AlphaDerivation",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/",
  "source_line_start": 252,
  "source_line_end": 259,
  "registry_ids": [
    "IV.L03"
  ],
  "related_registry_items": [
    {
      "id": "IV.L03",
      "title": "Photon Phase Quantum",
      "url": "/registry/object/IV.L03/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L252-L259",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.AlphaDerivation",
        "url": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L252-L259",
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

- Module: [TauLib.BookIV.Electroweak.AlphaDerivation](/verify/taulib/docs/book-iv-electroweak-alpha-derivation/)
- Source path: [`TauLib/BookIV/Electroweak/AlphaDerivation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L252-L259)
- Source range: L252-L259
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.L03` — Photon Phase Quantum

## Immediate Comment / Docstring

```lean
/-- [IV.L03] Photon phase quantum Φ₀: the minimal phase acquired
    by a unit-charge photon around a flux quantum.
    Φ₀ = 2π (one complete winding). -/
```

## Source Excerpt

```lean
structure PhotonPhaseQuantum where
  /-- Phase per flux quantum in units of 2π. -/
  phase_per_quantum : Nat
  phase_eq : phase_per_quantum = 1
  /-- Winding number for minimal loop. -/
  min_winding : Nat
  winding_eq : min_winding = 1
  deriving Repr
```
