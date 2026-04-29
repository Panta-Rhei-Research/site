---
{
  "projection_kind": "taulib_declaration",
  "title": "InternalIdentity",
  "permalink": "/verify/taulib/docs/book-iv-physics-internal-equations/internal-identity/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Physics.InternalEquations`.",
  "declaration_id": "TauLib.BookIV.Physics.InternalEquations::InternalIdentity",
  "declaration_slug": "internal-identity",
  "kind": "structure",
  "name": "InternalIdentity",
  "module_name": "TauLib.BookIV.Physics.InternalEquations",
  "module_url": "/verify/taulib/docs/book-iv-physics-internal-equations/",
  "source_line_start": 82,
  "source_line_end": 95,
  "registry_ids": [
    "IV.D323"
  ],
  "related_registry_items": [
    {
      "id": "IV.D323",
      "title": "Internal Identity",
      "url": "/registry/object/IV.D323/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/InternalEquations.lean#L82-L95",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.InternalEquations",
        "url": "/verify/taulib/docs/book-iv-physics-internal-equations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/InternalEquations.lean#L82-L95",
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

- Module: [TauLib.BookIV.Physics.InternalEquations](/verify/taulib/docs/book-iv-physics-internal-equations/)
- Source path: [`TauLib/BookIV/Physics/InternalEquations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/InternalEquations.lean#L82-L95)
- Source range: L82-L95
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D323` — Internal Identity

## Immediate Comment / Docstring

```lean
/-- [IV.D323] An internal identity: a named equation between categorical
    objects at a specific ontological layer.

    At Layer 1, the `source_sector` and `target_sector` identify which
    sector subcategories the domain and codomain live in.
    The `is_dimensionless` flag asserts the equation involves only
    same-sector morphisms (a ratio, not a cross-sector bridge). -/
```

## Source Excerpt

```lean
structure InternalIdentity where
  /-- Name of the identity (for documentation). -/
  name : String
  /-- Which ontological layer this identity belongs to. -/
  layer : EquationLayer
  /-- Source sector (domain of the morphism). -/
  source_sector : Sector
  /-- Target sector (codomain of the morphism). -/
  target_sector : Sector
  /-- Whether the identity is dimensionless (same-sector ratio). -/
  is_dimensionless : Bool
  /-- Whether this identity is derivable from ι_τ alone (no free parameters). -/
  from_iota_alone : Bool
  deriving Repr
```
