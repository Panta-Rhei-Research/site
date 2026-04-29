---
{
  "projection_kind": "taulib_declaration",
  "title": "PolarityPropagation",
  "permalink": "/verify/taulib/docs/book-vi-life-core-parity-bridge/polarity-propagation/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.LifeCore.ParityBridge`.",
  "declaration_id": "TauLib.BookVI.LifeCore.ParityBridge::PolarityPropagation",
  "declaration_slug": "polarity-propagation",
  "kind": "structure",
  "name": "PolarityPropagation",
  "module_name": "TauLib.BookVI.LifeCore.ParityBridge",
  "module_url": "/verify/taulib/docs/book-vi-life-core-parity-bridge/",
  "source_line_start": 111,
  "source_line_end": 121,
  "registry_ids": [
    "VI.D71"
  ],
  "related_registry_items": [
    {
      "id": "VI.D71",
      "title": "Polarity Propagation",
      "url": "/registry/object/VI.D71/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L111-L121",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L111-L121",
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
- Source path: [`TauLib/BookVI/LifeCore/ParityBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/ParityBridge.lean#L111-L121)
- Source range: L111-L121
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D71` — Polarity Propagation

## Immediate Comment / Docstring

```lean
/-- [VI.D71] Polarity Propagation: functor mapping IV.D112 σ_A-admissibility
    through VI.T01 Parity Bridge into VI.D01 polarity functional.
    The propagation chain is: weak-sector parity violation (σ = C_τ, IV.T146)
    → Parity Bridge (VI.T01) → polarity functional P_weak (VI.D01)
    → biological chirality seed. -/
```

## Source Excerpt

```lean
structure PolarityPropagation where
  /-- Source: weak-sector parity violation. -/
  source_sector : String := "weak"
  /-- Bridge: VI.T01 unique factorization. -/
  bridge_path_count : Nat
  bridge_unique : bridge_path_count = 1
  /-- Target: polarity functional output in 2_τ. -/
  target_codomain : String := "2_tau"
  /-- Propagation preserves chirality sign. -/
  sign_preserved : Bool := true
  deriving Repr
```
