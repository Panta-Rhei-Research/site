---
{
  "projection_kind": "taulib_declaration",
  "title": "ParityBridgeTheorem",
  "permalink": "/verify/taulib/docs/book-vi-life-core-parity-bridge/parity-bridge-theorem/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.LifeCore.ParityBridge`.",
  "declaration_id": "TauLib.BookVI.LifeCore.ParityBridge::ParityBridgeTheorem",
  "declaration_slug": "parity-bridge-theorem",
  "kind": "structure",
  "name": "ParityBridgeTheorem",
  "module_name": "TauLib.BookVI.LifeCore.ParityBridge",
  "module_url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/",
  "source_line_start": 73,
  "source_line_end": 79,
  "registry_ids": [
    "VI.T01"
  ],
  "related_registry_items": [
    {
      "id": "VI.T01",
      "title": "Parity Bridge Theorem",
      "url": "/registry/object/VI.T01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L73-L79",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.LifeCore.ParityBridge",
        "url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L73-L79",
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

- Module: [TauLib.BookVI.LifeCore.ParityBridge](/verify/taulib/docs/book-vi-life-core-parity-bridge/)
- Source path: [`TauLib/BookVI/LifeCore/ParityBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L73-L79)
- Source range: L73-L79
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T01` — Parity Bridge Theorem

## Immediate Comment / Docstring

```lean
/-- [VI.T01] Parity Bridge Theorem: E₁→E₂ factors uniquely through weak sector.
    E₁ →[P_weak] 2_τ →[SelfDesc] E₂. -/
```

## Source Excerpt

```lean
structure ParityBridgeTheorem where
  path_count : Nat
  unique_path : path_count = 1
  source_layer : String := "E1"
  target_layer : String := "E2"
  mediating_sector : String := "weak"
  deriving Repr
```
