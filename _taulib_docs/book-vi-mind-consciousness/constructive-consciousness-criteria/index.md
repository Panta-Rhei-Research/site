---
{
  "projection_kind": "taulib_declaration",
  "title": "ConstructiveConsciousnessCriteria",
  "permalink": "/verify/taulib/docs/book-vi-mind-consciousness/constructive-consciousness-criteria/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Mind.Consciousness`.",
  "declaration_id": "TauLib.BookVI.Mind.Consciousness::ConstructiveConsciousnessCriteria",
  "declaration_slug": "constructive-consciousness-criteria",
  "kind": "structure",
  "name": "ConstructiveConsciousnessCriteria",
  "module_name": "TauLib.BookVI.Mind.Consciousness",
  "module_url": "/verify/taulib/docs/book-vi-mind-consciousness/",
  "source_line_start": 142,
  "source_line_end": 151,
  "registry_ids": [
    "VI.D86"
  ],
  "related_registry_items": [
    {
      "id": "VI.D86",
      "title": "Constructive Consciousness Criteria",
      "url": "/registry/object/VI.D86/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Consciousness.lean#L142-L151",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Consciousness.lean#L142-L151",
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
- Source path: [`TauLib/BookVI/Mind/Consciousness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Consciousness.lean#L142-L151)
- Source range: L142-L151
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D86` — Constructive Consciousness Criteria

## Immediate Comment / Docstring

```lean
/-- [VI.D86] Constructive Consciousness Criteria.
    Three testable conditions extracted from VI.T38 + VI.D68 + VI.D69:
    (CC1) Consumer-sector topology realized: the system instantiates
      mixed-sector structure (π',π'' pairing) with genuine feedback loops.
    (CC2) Eval² loop closed: the system supports second-order
      self-evaluation (evaluator evaluates its own evaluation).
    (CC3) Structural self-model maintained: the system maintains a
      dynamically coherent self-model satisfying VI.D68's 3 conditions.
    Scope: τ-effective. -/
```

## Source Excerpt

```lean
structure ConstructiveConsciousnessCriteria where
  /-- (CC1) Mixed-sector topology (π',π'') realized. -/
  consumer_topology_realized : Bool := true
  /-- (CC2) Eval² = Eval ∘ Eval loop closed. -/
  eval_squared_closed : Bool := true
  /-- (CC3) Structural self-model (VI.D68) maintained. -/
  self_model_maintained : Bool := true
  /-- All three required. -/
  scope : String := "tau-effective"
  deriving Repr
```
