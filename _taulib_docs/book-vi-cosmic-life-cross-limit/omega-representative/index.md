---
{
  "projection_kind": "taulib_declaration",
  "title": "OmegaRepresentative",
  "permalink": "/verify/taulib/docs/book-vi-cosmic-life-cross-limit/omega-representative/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.CosmicLife.CrossLimit`.",
  "declaration_id": "TauLib.BookVI.CosmicLife.CrossLimit::OmegaRepresentative",
  "declaration_slug": "omega-representative",
  "kind": "structure",
  "name": "OmegaRepresentative",
  "module_name": "TauLib.BookVI.CosmicLife.CrossLimit",
  "module_url": "/verify/taulib/docs/book-vi-cosmic-life-cross-limit/",
  "source_line_start": 43,
  "source_line_end": 54,
  "registry_ids": [
    "VI.D60"
  ],
  "related_registry_items": [
    {
      "id": "VI.D60",
      "title": "ω-Representative of Life",
      "url": "/registry/object/VI.D60/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/CrossLimit.lean#L43-L54",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/CrossLimit.lean#L43-L54",
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
- Source path: [`TauLib/BookVI/CosmicLife/CrossLimit.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/CrossLimit.lean#L43-L54)
- Source range: L43-L54
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D60` — ω-Representative of Life

## Immediate Comment / Docstring

```lean
/-- [VI.D60] ω-Representative: carrier at boundary of code space.
    Three conditions: code dominance, boundary saturation, crossing faithfulness.
    BHs are the unique physical ω-representatives. -/
```

## Source Excerpt

```lean
structure OmegaRepresentative where
  /-- Number of defining conditions. -/
  condition_count : Nat
  /-- Exactly 3 conditions. -/
  count_eq : condition_count = 3
  /-- Code dominance: ω-germ determines basin. -/
  code_dominance : Bool := true
  /-- Boundary saturation: maximal information density. -/
  boundary_saturation : Bool := true
  /-- Crossing faithfulness: evaluator factors through ω. -/
  crossing_faithful : Bool := true
  deriving Repr
```
