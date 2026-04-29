---
{
  "projection_kind": "taulib_declaration",
  "title": "EvolutionOptimization",
  "permalink": "/verify/taulib/docs/book-vi-consumer-evolution/evolution-optimization/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Consumer.Evolution`.",
  "declaration_id": "TauLib.BookVI.Consumer.Evolution::EvolutionOptimization",
  "declaration_slug": "evolution-optimization",
  "kind": "structure",
  "name": "EvolutionOptimization",
  "module_name": "TauLib.BookVI.Consumer.Evolution",
  "module_url": "/verify/taulib/docs/book-vi-consumer-evolution/",
  "source_line_start": 56,
  "source_line_end": 71,
  "registry_ids": [
    "VI.T27"
  ],
  "related_registry_items": [
    {
      "id": "VI.T27",
      "title": "Evolution as Optimization",
      "url": "/registry/object/VI.T27/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Evolution.lean#L56-L71",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Consumer.Evolution",
        "url": "/verify/taulib/docs/book-vi-consumer-evolution/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Evolution.lean#L56-L71",
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

- Module: [TauLib.BookVI.Consumer.Evolution](/verify/taulib/docs/book-vi-consumer-evolution/)
- Source path: [`TauLib/BookVI/Consumer/Evolution.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Evolution.lean#L56-L71)
- Source range: L56-L71
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T27` — Evolution as Optimization

## Immediate Comment / Docstring

```lean
/-- [VI.T27] Evolution as Optimization: NP-hard → polynomial.
    Four evolutionary forces: mutation, selection, drift, migration.
    Together they implement the PPAS protocol (Book III, Part IX, III.T33)
    that reduces NP-hard search to polynomial convergence. -/
```

## Source Excerpt

```lean
structure EvolutionOptimization where
  /-- Number of evolutionary forces. -/
  force_count : Nat
  /-- Exactly 4 forces. -/
  count_eq : force_count = 4
  /-- Force 1: mutation (variation generator). -/
  mutation : Bool := true
  /-- Force 2: selection (fitness filter). -/
  selection : Bool := true
  /-- Force 3: genetic drift (stochastic sampling). -/
  drift : Bool := true
  /-- Force 4: migration (gene flow). -/
  migration : Bool := true
  /-- Convergence in polynomial generations. -/
  convergence : Bool := true
  deriving Repr
```
