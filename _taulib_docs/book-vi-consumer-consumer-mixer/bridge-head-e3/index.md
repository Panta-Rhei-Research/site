---
{
  "projection_kind": "taulib_declaration",
  "title": "BridgeHeadE3",
  "permalink": "/verify/taulib/docs/book-vi-consumer-consumer-mixer/bridge-head-e3/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Consumer.ConsumerMixer`.",
  "declaration_id": "TauLib.BookVI.Consumer.ConsumerMixer::BridgeHeadE3",
  "declaration_slug": "bridge-head-e3",
  "kind": "structure",
  "name": "BridgeHeadE3",
  "module_name": "TauLib.BookVI.Consumer.ConsumerMixer",
  "module_url": "/verify/taulib/docs/book-vi-consumer-consumer-mixer/",
  "source_line_start": 115,
  "source_line_end": 124,
  "registry_ids": [
    "VI.L07"
  ],
  "related_registry_items": [
    {
      "id": "VI.L07",
      "title": "Consumer as Bridge-Head to E₃",
      "url": "/registry/object/VI.L07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/ConsumerMixer.lean#L115-L124",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Consumer.ConsumerMixer",
        "url": "/verify/taulib/docs/book-vi-consumer-consumer-mixer/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/ConsumerMixer.lean#L115-L124",
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

- Module: [TauLib.BookVI.Consumer.ConsumerMixer](/verify/taulib/docs/book-vi-consumer-consumer-mixer/)
- Source path: [`TauLib/BookVI/Consumer/ConsumerMixer.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/ConsumerMixer.lean#L115-L124)
- Source range: L115-L124
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.L07` — Consumer as Bridge-Head to E₃

## Immediate Comment / Docstring

```lean
/-- [VI.L07] Consumer as Bridge-Head to E₃.
    Only the mixed sector supports Eval² = Eval ∘ Eval
    (second-order self-description). This opens the bridge
    from E₂ (life) to E₃ (consciousness/mind).
    Primitive sectors have Eval¹ only. -/
```

## Source Excerpt

```lean
structure BridgeHeadE3 where
  /-- Evaluator order (2 = second-order self-description). -/
  eval_order : Nat
  /-- Exactly order 2. -/
  order_eq : eval_order = 2
  /-- Only mixed sector reaches E₃. -/
  only_mixed_sector : Bool := true
  /-- Opens enrichment layer E₃. -/
  opens_e3 : Bool := true
  deriving Repr
```
