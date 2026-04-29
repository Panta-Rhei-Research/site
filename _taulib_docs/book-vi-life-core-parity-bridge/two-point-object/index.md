---
{
  "projection_kind": "taulib_declaration",
  "title": "TwoPointObject",
  "permalink": "/verify/taulib/docs/book-vi-life-core-parity-bridge/two-point-object/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.LifeCore.ParityBridge`.",
  "declaration_id": "TauLib.BookVI.LifeCore.ParityBridge::TwoPointObject",
  "declaration_slug": "two-point-object",
  "kind": "structure",
  "name": "TwoPointObject",
  "module_name": "TauLib.BookVI.LifeCore.ParityBridge",
  "module_url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/",
  "source_line_start": 43,
  "source_line_end": 48,
  "registry_ids": [
    "VI.D02"
  ],
  "related_registry_items": [
    {
      "id": "VI.D02",
      "title": "Polarity-Typed Two-Point Object (2_τ)",
      "url": "/registry/object/VI.D02/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L43-L48",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L43-L48",
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
- Source path: [`TauLib/BookVI/LifeCore/ParityBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L43-L48)
- Source range: L43-L48
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D02` — Polarity-Typed Two-Point Object (2_τ)

## Immediate Comment / Docstring

```lean
/-- [VI.D02] Polarity-typed two-point object 2_τ = {+, −}.
    Split-complex idempotent structure from lemniscate boundary. -/
```

## Source Excerpt

```lean
structure TwoPointObject where
  point_count : Nat
  count_eq : point_count = 2
  split_complex : Bool := true
  from_lemniscate : Bool := true
  deriving Repr
```
