---
{
  "projection_kind": "taulib_declaration",
  "title": "NeuralDefectLevel",
  "permalink": "/verify/taulib/docs/book-vi-consumer-neural/neural-defect-level/",
  "summary_short": "`inductive` declaration in `TauLib.BookVI.Consumer.Neural`.",
  "declaration_id": "TauLib.BookVI.Consumer.Neural::NeuralDefectLevel",
  "declaration_slug": "neural-defect-level",
  "kind": "inductive",
  "name": "NeuralDefectLevel",
  "module_name": "TauLib.BookVI.Consumer.Neural",
  "module_url": "/verify/taulib/docs/book-vi-consumer-neural/",
  "source_line_start": 120,
  "source_line_end": 125,
  "registry_ids": [
    "VI.D87"
  ],
  "related_registry_items": [
    {
      "id": "VI.D87",
      "title": "Neural Defect Level",
      "url": "/registry/object/VI.D87/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L120-L125",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L120-L125",
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

- Module: [TauLib.BookVI.Consumer.Neural](/verify/taulib/docs/book-vi-consumer-neural/)
- Source path: [`TauLib/BookVI/Consumer/Neural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L120-L125)
- Source range: L120-L125
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `VI.D87` — Neural Defect Level

## Immediate Comment / Docstring

```lean
/-- [VI.D87] Neural Defect Level: 4 hierarchical levels of neural
    defect accumulation, specializing VI.D43 (AgingDefect) to the
    neural architecture (VI.D52).
    Level 1 — Molecular: protein misfolding, aggregation (amyloid-β,
      α-synuclein, tau tangles). Defect = deviation from native fold.
    Level 2 — Synaptic: synapse loss, neurotransmitter depletion,
      receptor downregulation. Defect = edge degradation in τ³-computer.
    Level 3 — Circuit: dopaminergic/serotonergic/cholinergic pathway
      degradation. Defect = subgraph integrity loss in τ³-computer.
    Level 4 — Network: large-scale connectivity loss, white matter
      degeneration. Defect = global topology disruption in τ³-computer.
    Scope: τ-effective. -/
```

## Source Excerpt

```lean
inductive NeuralDefectLevel where
  | molecular   -- Level 1: protein misfolding, aggregation
  | synaptic    -- Level 2: synapse loss, receptor downregulation
  | circuit     -- Level 3: pathway integrity loss
  | network     -- Level 4: global connectivity disruption
  deriving Repr, BEq
```
