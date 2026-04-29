---
{
  "projection_kind": "taulib_declaration",
  "title": "DistanceLadderRung",
  "permalink": "/verify/taulib/docs/book-v-temporal-distance-ladder/distance-ladder-rung/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.Temporal.DistanceLadder`.",
  "declaration_id": "TauLib.BookV.Temporal.DistanceLadder::DistanceLadderRung",
  "declaration_slug": "distance-ladder-rung",
  "kind": "inductive",
  "name": "DistanceLadderRung",
  "module_name": "TauLib.BookV.Temporal.DistanceLadder",
  "module_url": "/verify/taulib/docs/book-v-temporal-distance-ladder/",
  "source_line_start": 109,
  "source_line_end": 120,
  "registry_ids": [
    "V.T17"
  ],
  "related_registry_items": [
    {
      "id": "V.T17",
      "title": "Distance Ladder Translation",
      "url": "/registry/object/V.T17/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L109-L120",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.DistanceLadder",
        "url": "/verify/taulib/docs/book-v-temporal-distance-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L109-L120",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookV.Temporal.DistanceLadder](/verify/taulib/docs/book-v-temporal-distance-ladder/)
- Source path: [`TauLib/BookV/Temporal/DistanceLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L109-L120)
- Source range: L109-L120
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `V.T17` — Distance Ladder Translation

## Immediate Comment / Docstring

```lean
/-- [V.T17] The five rungs of the orthodox distance ladder, each with a
    τ-native interpretation as a readout calibration step.

    - Parallax: geometric, Earth-orbit = D-sector readout
    - Cepheid: period-luminosity from κ(D;1)/κ(B;1) ratio
    - SNIa: Chandrasekhar threshold = D-sector mass limit
    - BAO: comoving sound horizon at recombination depth n_rec
    - CMB: Σ_CMB boundary-character constraint surface -/
```

## Source Excerpt

```lean
inductive DistanceLadderRung where
  /-- Geometric parallax (kpc scale). -/
  | Parallax
  /-- Cepheid period-luminosity relation (Mpc scale). -/
  | Cepheid
  /-- Type Ia supernova standardisable candle (Gpc scale). -/
  | SNIa
  /-- Baryon acoustic oscillation standard ruler (Gpc scale). -/
  | BAO
  /-- Cosmic microwave background (horizon scale). -/
  | CMB
  deriving Repr, DecidableEq, BEq, Inhabited
```
