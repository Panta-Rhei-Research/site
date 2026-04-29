---
{
  "projection_kind": "taulib_declaration",
  "title": "CarrierType",
  "permalink": "/verify/taulib/docs/book-iv-physics-quantity-framework/carrier-type/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.Physics.QuantityFramework`.",
  "declaration_id": "TauLib.BookIV.Physics.QuantityFramework::CarrierType",
  "declaration_slug": "carrier-type",
  "kind": "inductive",
  "name": "CarrierType",
  "module_name": "TauLib.BookIV.Physics.QuantityFramework",
  "module_url": "/verify/taulib/docs/book-iv-physics-quantity-framework/",
  "source_line_start": 74,
  "source_line_end": 81,
  "registry_ids": [
    "IV.D10"
  ],
  "related_registry_items": [
    {
      "id": "IV.D10",
      "title": "Carrier Type",
      "url": "/registry/object/IV.D10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/QuantityFramework.lean#L74-L81",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.QuantityFramework",
        "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/QuantityFramework.lean#L74-L81",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookIV.Physics.QuantityFramework](/verify/taulib/docs/book-iv-physics-quantity-framework/)
- Source path: [`TauLib/BookIV/Physics/QuantityFramework.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/QuantityFramework.lean#L74-L81)
- Source range: L74-L81
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `IV.D10` — Carrier Type

## Immediate Comment / Docstring

```lean
/-- [IV.D10] Carrier type for physical quantities in the τ³ = τ¹ ×_f T² fibration.
    Every physical quantity lives on exactly one of three carriers. -/
```

## Source Excerpt

```lean
inductive CarrierType where
  /-- Lives on the fiber T² (spatial/microcosm = Book IV). -/
  | Fiber
  /-- Lives on the base τ¹ (temporal/macrocosm = Book V). -/
  | Base
  /-- Lives at the lemniscate crossing point L = S¹ ∨ S¹ (unpolarized). -/
  | Crossing
  deriving Repr, DecidableEq, BEq, Inhabited
```
