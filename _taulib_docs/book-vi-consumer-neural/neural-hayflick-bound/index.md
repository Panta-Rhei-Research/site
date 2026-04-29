---
{
  "projection_kind": "taulib_declaration",
  "title": "NeuralHayflickBound",
  "permalink": "/verify/taulib/docs/book-vi-consumer-neural/neural-hayflick-bound/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Consumer.Neural`.",
  "declaration_id": "TauLib.BookVI.Consumer.Neural::NeuralHayflickBound",
  "declaration_slug": "neural-hayflick-bound",
  "kind": "structure",
  "name": "NeuralHayflickBound",
  "module_name": "TauLib.BookVI.Consumer.Neural",
  "module_url": "/verify/taulib/docs/book-vi-consumer-neural/",
  "source_line_start": 372,
  "source_line_end": 385,
  "registry_ids": [
    "VI.D91"
  ],
  "related_registry_items": [
    {
      "id": "VI.D91",
      "title": "Neural Hayflick Bound",
      "url": "/registry/object/VI.D91/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L372-L385",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L372-L385",
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
- Source path: [`TauLib/BookVI/Consumer/Neural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L372-L385)
- Source range: L372-L385
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D91` — Neural Hayflick Bound

## Immediate Comment / Docstring

```lean
/-- [VI.D91] Neural Hayflick Bound: maximum cognitive lifespan at
    each defect level, derived from finite repair budget (VI.P16)
    applied to the NeuralDefectTower (VI.D88).
    H_i = R_max(i) / r_i, where R_max(i) is the repair budget
    allocated to Level i and r_i is the defect accumulation rate.
    Overall cognitive Hayflick bound: H_neural = min(H₁,H₂,H₃,H₄).
    Connects to Book V: the geometric decay rate (1−ι_τ)^n (V.T62)
    governs the baseline defect accumulation at each level.
    Scope: τ-effective. -/
```

## Source Excerpt

```lean
structure NeuralHayflickBound where
  /-- Number of levels with individual bounds. -/
  level_count : Nat
  /-- 4 individual bounds. -/
  count_eq : level_count = 4
  /-- Each level has a finite Hayflick bound H_i. -/
  finite_per_level : Bool := true
  /-- Overall bound is min of level bounds. -/
  overall_is_min : Bool := true
  /-- Connects to Book V defect exhaustion (V.T62). -/
  connects_to_book_v : Bool := true
  /-- Scope: τ-effective. -/
  scope : String := "tau-effective"
  deriving Repr
```
