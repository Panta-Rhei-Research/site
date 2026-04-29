---
{
  "projection_kind": "taulib_declaration",
  "title": "LowNoiseCarrierCondition",
  "permalink": "/verify/taulib/docs/book-vi-life-core-parity-bridge/low-noise-carrier-condition/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.LifeCore.ParityBridge`.",
  "declaration_id": "TauLib.BookVI.LifeCore.ParityBridge::LowNoiseCarrierCondition",
  "declaration_slug": "low-noise-carrier-condition",
  "kind": "structure",
  "name": "LowNoiseCarrierCondition",
  "module_name": "TauLib.BookVI.LifeCore.ParityBridge",
  "module_url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/",
  "source_line_start": 90,
  "source_line_end": 93,
  "registry_ids": [
    "VI.P01"
  ],
  "related_registry_items": [
    {
      "id": "VI.P01",
      "title": "Low-Noise Carrier Condition",
      "url": "/registry/object/VI.P01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L90-L93",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L90-L93",
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
- Source path: [`TauLib/BookVI/LifeCore/ParityBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L90-L93)
- Source range: L90-L93
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.P01` — Low-Noise Carrier Condition

## Immediate Comment / Docstring

```lean
/-- [VI.P01] Low-noise carrier condition: 3 conditions for E₁→E₂ transition. -/
```

## Source Excerpt

```lean
structure LowNoiseCarrierCondition where
  condition_count : Nat
  count_eq : condition_count = 3
  deriving Repr
```
