---
{
  "projection_kind": "taulib_declaration",
  "title": "FitnessLandscapeTopology",
  "permalink": "/verify/taulib/docs/book-vi-consumer-evolution/fitness-landscape-topology/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Consumer.Evolution`.",
  "declaration_id": "TauLib.BookVI.Consumer.Evolution::FitnessLandscapeTopology",
  "declaration_slug": "fitness-landscape-topology",
  "kind": "structure",
  "name": "FitnessLandscapeTopology",
  "module_name": "TauLib.BookVI.Consumer.Evolution",
  "module_url": "/verify/taulib/docs/book-vi-consumer-evolution/",
  "source_line_start": 96,
  "source_line_end": 103,
  "registry_ids": [
    "VI.R20"
  ],
  "related_registry_items": [
    {
      "id": "VI.R20",
      "title": "Fitness Landscape Topology",
      "url": "/registry/object/VI.R20/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Evolution.lean#L96-L103",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Evolution.lean#L96-L103",
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
- Source path: [`TauLib/BookVI/Consumer/Evolution.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Evolution.lean#L96-L103)
- Source range: L96-L103
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.R20` — Fitness Landscape Topology

## Immediate Comment / Docstring

```lean
/-- [VI.R20] Fitness Landscape Topology.
    Rugged landscapes with epistatic interactions,
    NK-model structure, and multiple attractor basins.
    Speciation occurs at saddle points between basins. -/
```

## Source Excerpt

```lean
structure FitnessLandscapeTopology where
  /-- Epistatic interactions present. -/
  epistatic : Bool := true
  /-- NK-model structure. -/
  nk_model : Bool := true
  /-- Attractor basins present. -/
  attractor_basins : Bool := true
  deriving Repr
```
