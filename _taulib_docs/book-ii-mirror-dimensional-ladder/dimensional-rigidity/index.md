---
{
  "projection_kind": "taulib_declaration",
  "title": "DimensionalRigidity",
  "permalink": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/dimensional-rigidity/",
  "summary_short": "`structure` declaration in `TauLib.BookII.Mirror.DimensionalLadder`.",
  "declaration_id": "TauLib.BookII.Mirror.DimensionalLadder::DimensionalRigidity",
  "declaration_slug": "dimensional-rigidity",
  "kind": "structure",
  "name": "DimensionalRigidity",
  "module_name": "TauLib.BookII.Mirror.DimensionalLadder",
  "module_url": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/",
  "source_line_start": 356,
  "source_line_end": 365,
  "registry_ids": [
    "II.D76"
  ],
  "related_registry_items": [
    {
      "id": "II.D76",
      "title": "Dimensional Rigidity",
      "url": "/registry/object/II.D76/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L356-L365",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Mirror.DimensionalLadder",
        "url": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L356-L365",
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

- Module: [TauLib.BookII.Mirror.DimensionalLadder](/verify/taulib/docs/book-ii-mirror-dimensional-ladder/)
- Source path: [`TauLib/BookII/Mirror/DimensionalLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L356-L365)
- Source range: L356-L365
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `II.D76` — Dimensional Rigidity

## Immediate Comment / Docstring

```lean
/-- [II.D76] Dimensional rigidity: τ admits exactly one holomorphic structure
    with fixed fibration index and refinement dimension. -/
```

## Source Excerpt

```lean
structure DimensionalRigidity where
  /-- Fibration index = 3 (1 base + 2 fiber). -/
  fibration_index : Nat
  /-- Refinement dimension = 4 (A, B, C, D rays). -/
  refinement_dim : Nat
  /-- Base factors = 1 (τ¹). -/
  base_factors : Nat
  /-- Fiber factors = 2 (T²). -/
  fiber_factors : Nat
  deriving Repr
```
