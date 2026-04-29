---
{
  "projection_kind": "taulib_declaration",
  "title": "NeuralArchitecture",
  "permalink": "/verify/taulib/docs/book-vi-consumer-neural/neural-architecture/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Consumer.Neural`.",
  "declaration_id": "TauLib.BookVI.Consumer.Neural::NeuralArchitecture",
  "declaration_slug": "neural-architecture",
  "kind": "structure",
  "name": "NeuralArchitecture",
  "module_name": "TauLib.BookVI.Consumer.Neural",
  "module_url": "/verify/taulib/docs/book-vi-consumer-neural/",
  "source_line_start": 48,
  "source_line_end": 59,
  "registry_ids": [
    "VI.D52"
  ],
  "related_registry_items": [
    {
      "id": "VI.D52",
      "title": "Neural Architecture as τ³ Computer",
      "url": "/registry/object/VI.D52/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L48-L59",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Consumer.Neural",
        "url": "/verify/taulib/docs/book-vi-consumer-neural/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L48-L59",
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

- Module: [TauLib.BookVI.Consumer.Neural](/verify/taulib/docs/book-vi-consumer-neural/)
- Source path: [`TauLib/BookVI/Consumer/Neural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L48-L59)
- Source range: L48-L59
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D52` — Neural Architecture as τ³ Computer

## Immediate Comment / Docstring

```lean
/-- [VI.D52] Neural Architecture as τ³ Computer.
    Three node types: sensory (input), inter (processing), motor (output).
    Weighted directed edges. The architecture mirrors the τ³ fibration
    (Book II, Part II): base τ¹ = temporal sequencing,
    fiber T² = parallel feature processing. -/
```

## Source Excerpt

```lean
structure NeuralArchitecture where
  /-- Number of fundamental node types. -/
  node_types : Nat
  /-- Exactly 3 types: sensory, inter, motor. -/
  types_eq : node_types = 3
  /-- Edges carry weights. -/
  weighted_edges : Bool := true
  /-- Network is directed (sensory → inter → motor). -/
  directed : Bool := true
  /-- Architecture mirrors τ³ structure. -/
  tau3_computer : Bool := true
  deriving Repr
```
