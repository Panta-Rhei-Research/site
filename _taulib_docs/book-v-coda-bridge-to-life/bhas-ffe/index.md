---
{
  "projection_kind": "taulib_declaration",
  "title": "BHAsFFE",
  "permalink": "/verify/taulib/docs/book-v-coda-bridge-to-life/bhas-ffe/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Coda.BridgeToLife`.",
  "declaration_id": "TauLib.BookV.Coda.BridgeToLife::BHAsFFE",
  "declaration_slug": "bhas-ffe",
  "kind": "structure",
  "name": "BHAsFFE",
  "module_name": "TauLib.BookV.Coda.BridgeToLife",
  "module_url": "/verify/taulib/docs/book-v-coda-bridge-to-life/",
  "source_line_start": 520,
  "source_line_end": 533,
  "registry_ids": [
    "V.P118"
  ],
  "related_registry_items": [
    {
      "id": "V.P118",
      "title": "Black holes as far-from-equilibrium patterns",
      "url": "/registry/object/V.P118/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/BridgeToLife.lean#L520-L533",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Coda.BridgeToLife",
        "url": "/verify/taulib/docs/book-v-coda-bridge-to-life/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/BridgeToLife.lean#L520-L533",
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

- Module: [TauLib.BookV.Coda.BridgeToLife](/verify/taulib/docs/book-v-coda-bridge-to-life/)
- Source path: [`TauLib/BookV/Coda/BridgeToLife.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/BridgeToLife.lean#L520-L533)
- Source range: L520-L533
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P118` — Black holes as far-from-equilibrium patterns

## Immediate Comment / Docstring

```lean
/-- [V.P118] Black holes as far-from-equilibrium (FFE) patterns.

    Every BH satisfies the 3 FFE conditions:
    1. Bounded S_def (entropy splitting, not thermal equilibrium)
    2. Boundary flux (accretion disk, jets, Hawking-like readout)
    3. Internal circulation via frame-dragging (Kerr-like torus flow)

    BHs are NOT dead endpoints — they are active, self-maintaining
    topological patterns on L. -/
```

## Source Excerpt

```lean
structure BHAsFFE where
  /-- Number of FFE conditions satisfied. -/
  ffe_conditions : Nat
  /-- All 3 satisfied. -/
  conditions_eq : ffe_conditions = 3
  /-- Bounded S_def. -/
  bounded_s_def : Bool := true
  /-- Boundary flux present. -/
  boundary_flux : Bool := true
  /-- Internal circulation. -/
  internal_circulation : Bool := true
  /-- FFE label count (bounded + flux + circulation). -/
  ffe_label_count : Nat := 3
  deriving Repr
```
