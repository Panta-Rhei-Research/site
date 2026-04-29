---
{
  "projection_kind": "taulib_declaration",
  "title": "MinimalConsciousAgent",
  "permalink": "/verify/taulib/docs/book-vi-mind-consciousness/minimal-conscious-agent/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Mind.Consciousness`.",
  "declaration_id": "TauLib.BookVI.Mind.Consciousness::MinimalConsciousAgent",
  "declaration_slug": "minimal-conscious-agent",
  "kind": "structure",
  "name": "MinimalConsciousAgent",
  "module_name": "TauLib.BookVI.Mind.Consciousness",
  "module_url": "/verify/taulib/docs/book-vi-mind-consciousness/",
  "source_line_start": 72,
  "source_line_end": 83,
  "registry_ids": [
    "VI.D69"
  ],
  "related_registry_items": [
    {
      "id": "VI.D69",
      "title": "Minimal Conscious Agent",
      "url": "/registry/object/VI.D69/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Consciousness.lean#L72-L83",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Consciousness.lean#L72-L83",
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
- Source path: [`TauLib/BookVI/Mind/Consciousness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Consciousness.lean#L72-L83)
- Source range: L72-L83
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D69` — Minimal Conscious Agent

## Immediate Comment / Docstring

```lean
/-- [VI.D69] Minimal Conscious Agent: three requirements.
    (i) Consumer sector (mixed, VI.D46): requires both fiber generators
    (ii) Centralized integration: global workspace binding
    (iii) Recurrent self-representation: Eval² = Eval ∘ Eval (VI.L07)
    Primitive sectors cannot satisfy (i) or (iii). -/
```

## Source Excerpt

```lean
structure MinimalConsciousAgent where
  /-- Number of requirements. -/
  condition_count : Nat
  /-- Exactly 3 requirements. -/
  count_eq : condition_count = 3
  /-- (i) Must be in consumer (mixed) sector. -/
  consumer_sector : Bool := true
  /-- (ii) Centralized integration (global workspace). -/
  centralized_integration : Bool := true
  /-- (iii) Recurrent self-representation (Eval²). -/
  recurrent_self_representation : Bool := true
  deriving Repr
```
