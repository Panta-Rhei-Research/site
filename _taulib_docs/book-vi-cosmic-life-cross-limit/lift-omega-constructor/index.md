---
{
  "projection_kind": "taulib_declaration",
  "title": "LiftOmegaConstructor",
  "permalink": "/verify/taulib/docs/book-vi-cosmic-life-cross-limit/lift-omega-constructor/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.CosmicLife.CrossLimit`.",
  "declaration_id": "TauLib.BookVI.CosmicLife.CrossLimit::LiftOmegaConstructor",
  "declaration_slug": "lift-omega-constructor",
  "kind": "structure",
  "name": "LiftOmegaConstructor",
  "module_name": "TauLib.BookVI.CosmicLife.CrossLimit",
  "module_url": "/verify/taulib/docs/book-vi-cosmic-life-cross-limit/",
  "source_line_start": 67,
  "source_line_end": 78,
  "registry_ids": [
    "VI.D61"
  ],
  "related_registry_items": [
    {
      "id": "VI.D61",
      "title": "Lift_ω Constructor",
      "url": "/registry/object/VI.D61/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/CrossLimit.lean#L67-L78",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.CosmicLife.CrossLimit",
        "url": "/verify/taulib/docs/book-vi-cosmic-life-cross-limit/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/CrossLimit.lean#L67-L78",
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

- Module: [TauLib.BookVI.CosmicLife.CrossLimit](/verify/taulib/docs/book-vi-cosmic-life-cross-limit/)
- Source path: [`TauLib/BookVI/CosmicLife/CrossLimit.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/CrossLimit.lean#L67-L78)
- Source range: L67-L78
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D61` — Lift_ω Constructor

## Immediate Comment / Docstring

```lean
/-- [VI.D61] Lift_ω constructor: recursive builder from bipolar seed
    through primorial ladder P_k = 2, 6, 30, 210, 2310, ...
    Converges superexponentially to ι_τ. -/
```

## Source Excerpt

```lean
structure LiftOmegaConstructor where
  /-- Recursive construction. -/
  recursive : Bool := true
  /-- Uses primorial ladder. -/
  primorial_ladder : Bool := true
  /-- Converges to ι_τ = 2/(π+e). -/
  converges_to_iota : Bool := true
  /-- Convergence rate is superexponential. -/
  superexponential : Bool := true
  /-- Well-definedness requires ι_τ irrational. -/
  iota_irrational : Bool := true
  deriving Repr
```
