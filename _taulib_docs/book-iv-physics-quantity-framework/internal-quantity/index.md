---
{
  "projection_kind": "taulib_declaration",
  "title": "InternalQuantity",
  "permalink": "/verify/taulib/docs/book-iv-physics-quantity-framework/internal-quantity/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Physics.QuantityFramework`.",
  "declaration_id": "TauLib.BookIV.Physics.QuantityFramework::InternalQuantity",
  "declaration_slug": "internal-quantity",
  "kind": "structure",
  "name": "InternalQuantity",
  "module_name": "TauLib.BookIV.Physics.QuantityFramework",
  "module_url": "/verify/taulib/docs/book-iv-physics-quantity-framework/",
  "source_line_start": 264,
  "source_line_end": 279,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/QuantityFramework.lean#L264-L279",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/QuantityFramework.lean#L264-L279",
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
- Source path: [`TauLib/BookIV/Physics/QuantityFramework.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/QuantityFramework.lean#L264-L279)
- Source range: L264-L279
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [IV.D321a] An internal quantity as a categorical object.
    Each quantity IS its generator action — a functor from a sector
    subcategory of τ³ to its internal hom. This replaces the metadata-level
    PhysicalQuantity with a definitional categorical characterization.

    The `generator` field names the τ-generator whose minimal endomorphism
    defines this quantity. The `carrier_space` identifies whether the
    endomorphism acts on base τ¹, fiber T², or the crossing L. -/
```

## Source Excerpt

```lean
structure InternalQuantity where
  /-- The primary invariant this quantity instantiates. -/
  invariant : PrimaryInvariant
  /-- The τ-generator whose action defines this quantity.
      α=gravity, π=time, γ=energy, η=mass, ω=entropy. -/
  generator : String
  /-- Where the generator acts: "End(τ¹)" for base, "End(T²)" for fiber,
      "Aut(L)" for crossing. -/
  endomorphism_type : String
  /-- Governing sector. -/
  sector : Sector
  /-- Carrier type. -/
  carrier : CarrierType
  /-- Whether the quantity is conserved. -/
  is_conserved : Bool
  deriving Repr
```
