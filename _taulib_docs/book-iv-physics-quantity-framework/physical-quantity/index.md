---
{
  "projection_kind": "taulib_declaration",
  "title": "PhysicalQuantity",
  "permalink": "/verify/taulib/docs/book-iv-physics-quantity-framework/physical-quantity/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Physics.QuantityFramework`.",
  "declaration_id": "TauLib.BookIV.Physics.QuantityFramework::PhysicalQuantity",
  "declaration_slug": "physical-quantity",
  "kind": "structure",
  "name": "PhysicalQuantity",
  "module_name": "TauLib.BookIV.Physics.QuantityFramework",
  "module_url": "/verify/taulib/docs/book-iv-physics-quantity-framework/",
  "source_line_start": 90,
  "source_line_end": 103,
  "registry_ids": [
    "IV.D11"
  ],
  "related_registry_items": [
    {
      "id": "IV.D11",
      "title": "Physical Quantity Template",
      "url": "/registry/object/IV.D11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/QuantityFramework.lean#L90-L103",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/QuantityFramework.lean#L90-L103",
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

- Module: [TauLib.BookIV.Physics.QuantityFramework](/verify/taulib/docs/book-iv-physics-quantity-framework/)
- Source path: [`TauLib/BookIV/Physics/QuantityFramework.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/QuantityFramework.lean#L90-L103)
- Source range: L90-L103
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D11` — Physical Quantity Template

## Immediate Comment / Docstring

```lean
/-- [IV.D11] Physical quantity template: a τ-native physical observable
    characterized by its primary invariant, carrier, governing sector,
    and structural properties. -/
```

## Source Excerpt

```lean
structure PhysicalQuantity where
  /-- Display name. -/
  name : String
  /-- Which primary invariant this quantity belongs to. -/
  invariant : PrimaryInvariant
  /-- Where the quantity lives in τ³. -/
  carrier : CarrierType
  /-- Which holonomy sector governs this quantity. -/
  sector : Sector
  /-- Whether the quantity is σ-fixed (unpolarized, at crossing point). -/
  is_sigma_fixed : Bool
  /-- Whether the quantity is conserved under τ-admissible evolution. -/
  is_conserved : Bool
  deriving Repr
```
