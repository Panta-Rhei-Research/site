---
{
  "projection_kind": "taulib_declaration",
  "title": "StructuralSelfModel",
  "permalink": "/verify/taulib/docs/book-vi-mind-consciousness/structural-self-model/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Mind.Consciousness`.",
  "declaration_id": "TauLib.BookVI.Mind.Consciousness::StructuralSelfModel",
  "declaration_slug": "structural-self-model",
  "kind": "structure",
  "name": "StructuralSelfModel",
  "module_name": "TauLib.BookVI.Mind.Consciousness",
  "module_url": "/verify/taulib/docs/book-vi-mind-consciousness/",
  "source_line_start": 39,
  "source_line_end": 50,
  "registry_ids": [
    "VI.D68"
  ],
  "related_registry_items": [
    {
      "id": "VI.D68",
      "title": "Structural Self-Model",
      "url": "/registry/object/VI.D68/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Consciousness.lean#L39-L50",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Mind.Consciousness",
        "url": "/verify/taulib/docs/book-vi-mind-consciousness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Consciousness.lean#L39-L50",
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

- Module: [TauLib.BookVI.Mind.Consciousness](/verify/taulib/docs/book-vi-mind-consciousness/)
- Source path: [`TauLib/BookVI/Mind/Consciousness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Consciousness.lean#L39-L50)
- Source range: L39-L50
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D68` — Structural Self-Model

## Immediate Comment / Docstring

```lean
/-- [VI.D68] Structural Self-Model: three conditions.
    (i) Self-referential: model includes the modeling agent
    (ii) Reconstructive fidelity: model tracks actual state
    (iii) Dynamical coherence: model updates in real time
    A self-model is necessary but not sufficient for consciousness. -/
```

## Source Excerpt

```lean
structure StructuralSelfModel where
  /-- Number of conditions. -/
  condition_count : Nat
  /-- Exactly 3 conditions. -/
  count_eq : condition_count = 3
  /-- (i) Model includes the modeler. -/
  self_referential : Bool := true
  /-- (ii) Model tracks actual state. -/
  reconstructive_fidelity : Bool := true
  /-- (iii) Model updates dynamically. -/
  dynamical_coherence : Bool := true
  deriving Repr
```
