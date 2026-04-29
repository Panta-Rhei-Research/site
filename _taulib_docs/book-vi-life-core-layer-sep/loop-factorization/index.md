---
{
  "projection_kind": "taulib_declaration",
  "title": "LoopFactorization",
  "permalink": "/verify/taulib/docs/book-vi-life-core-layer-sep/loop-factorization/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.LifeCore.LayerSep`.",
  "declaration_id": "TauLib.BookVI.LifeCore.LayerSep::LoopFactorization",
  "declaration_slug": "loop-factorization",
  "kind": "structure",
  "name": "LoopFactorization",
  "module_name": "TauLib.BookVI.LifeCore.LayerSep",
  "module_url": "/verify/taulib/docs/book-vi-life-core-layer-sep/",
  "source_line_start": 59,
  "source_line_end": 63,
  "registry_ids": [
    "VI.L03"
  ],
  "related_registry_items": [
    {
      "id": "VI.L03",
      "title": "Loop Factorization",
      "url": "/registry/object/VI.L03/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/LayerSep.lean#L59-L63",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.LifeCore.LayerSep",
        "url": "/verify/taulib/docs/book-vi-life-core-layer-sep/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/LayerSep.lean#L59-L63",
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

- Module: [TauLib.BookVI.LifeCore.LayerSep](/verify/taulib/docs/book-vi-life-core-layer-sep/)
- Source path: [`TauLib/BookVI/LifeCore/LayerSep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/LayerSep.lean#L59-L63)
- Source range: L59-L63
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.L03` — Loop Factorization

## Immediate Comment / Docstring

```lean
/-- [VI.L03] Loop factorization: every metabolic cycle γ decomposes as
    γ_src ∗ γ_rec ∗ γ_base via π₁(τ³). -/
```

## Source Excerpt

```lean
structure LoopFactorization where
  factor_count : Nat
  count_eq : factor_count = 3
  is_unique : Bool := true
  deriving Repr
```
