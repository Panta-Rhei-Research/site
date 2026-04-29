---
{
  "projection_kind": "taulib_declaration",
  "title": "YonedaSelfImage",
  "permalink": "/verify/taulib/docs/book-iv-arena-boundary-holonomy/yoneda-self-image/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Arena.BoundaryHolonomy`.",
  "declaration_id": "TauLib.BookIV.Arena.BoundaryHolonomy::YonedaSelfImage",
  "declaration_slug": "yoneda-self-image",
  "kind": "structure",
  "name": "YonedaSelfImage",
  "module_name": "TauLib.BookIV.Arena.BoundaryHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-arena-boundary-holonomy/",
  "source_line_start": 42,
  "source_line_end": 49,
  "registry_ids": [
    "IV.D258"
  ],
  "related_registry_items": [
    {
      "id": "IV.D258",
      "title": "Yoneda self-image",
      "url": "/registry/object/IV.D258/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L42-L49",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.BoundaryHolonomy",
        "url": "/verify/taulib/docs/book-iv-arena-boundary-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L42-L49",
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

- Module: [TauLib.BookIV.Arena.BoundaryHolonomy](/verify/taulib/docs/book-iv-arena-boundary-holonomy/)
- Source path: [`TauLib/BookIV/Arena/BoundaryHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L42-L49)
- Source range: L42-L49
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D258` — Yoneda self-image

## Immediate Comment / Docstring

```lean
/-- [IV.D258] The Yoneda self-image y(τ³): the representation of τ³
    as a presheaf on itself. Encodes τ³'s complete self-description.
    At E₁, this is the arena's "internal mirror". -/
```

## Source Excerpt

```lean
structure YonedaSelfImage where
  /-- The arena being represented. -/
  arena_dim : Nat
  arena_eq : arena_dim = 5
  /-- Self-description is complete (all sectors visible). -/
  complete : Bool
  complete_true : complete = true
  deriving Repr
```
