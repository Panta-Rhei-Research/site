---
{
  "projection_kind": "taulib_declaration",
  "title": "NeuralDefectTower",
  "permalink": "/verify/taulib/docs/book-vi-consumer-neural/neural-defect-tower/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Consumer.Neural`.",
  "declaration_id": "TauLib.BookVI.Consumer.Neural::NeuralDefectTower",
  "declaration_slug": "neural-defect-tower",
  "kind": "structure",
  "name": "NeuralDefectTower",
  "module_name": "TauLib.BookVI.Consumer.Neural",
  "module_url": "/verify/taulib/docs/book-vi-consumer-neural/",
  "source_line_start": 138,
  "source_line_end": 151,
  "registry_ids": [
    "VI.D88"
  ],
  "related_registry_items": [
    {
      "id": "VI.D88",
      "title": "Neural Defect Tower",
      "url": "/registry/object/VI.D88/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L138-L151",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L138-L151",
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
- Source path: [`TauLib/BookVI/Consumer/Neural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L138-L151)
- Source range: L138-L151
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D88` — Neural Defect Tower

## Immediate Comment / Docstring

```lean
/-- [VI.D88] Neural Defect Tower: multi-level defect accumulation
    specialized to the neural architecture (VI.D52). Each level i has
    a defect functional Δᵢ(n) that is monotonically increasing with
    refinement step n (specialization of VI.D43). Levels cascade:
    when Level i defect exceeds a threshold, Level i+1 defect
    accumulation accelerates.
    Scope: τ-effective. -/
```

## Source Excerpt

```lean
structure NeuralDefectTower where
  /-- Number of hierarchical levels. -/
  level_count : Nat
  /-- Exactly 4 levels. -/
  count_eq : level_count = 4
  /-- Each level's defect is monotonically increasing (VI.D43). -/
  monotone_per_level : Bool := true
  /-- Levels cascade: Level i overflow accelerates Level i+1. -/
  inter_level_cascade : Bool := true
  /-- Specialization of aging defect (VI.D43). -/
  specializes_aging_defect : Bool := true
  /-- Scope: τ-effective. -/
  scope : String := "tau-effective"
  deriving Repr
```
