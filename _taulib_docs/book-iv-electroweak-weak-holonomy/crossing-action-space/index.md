---
{
  "projection_kind": "taulib_declaration",
  "title": "CrossingActionSpace",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/crossing-action-space/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.WeakHolonomy`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakHolonomy::CrossingActionSpace",
  "declaration_slug": "crossing-action-space",
  "kind": "structure",
  "name": "CrossingActionSpace",
  "module_name": "TauLib.BookIV.Electroweak.WeakHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/",
  "source_line_start": 42,
  "source_line_end": 49,
  "registry_ids": [
    "IV.D115"
  ],
  "related_registry_items": [
    {
      "id": "IV.D115",
      "title": "Crossing-Point Action Space",
      "url": "/registry/object/IV.D115/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L42-L49",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakHolonomy",
        "url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L42-L49",
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

- Module: [TauLib.BookIV.Electroweak.WeakHolonomy](/verify/taulib/docs/book-iv-electroweak-weak-holonomy/)
- Source path: [`TauLib/BookIV/Electroweak/WeakHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L42-L49)
- Source range: L42-L49
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D115` — Crossing-Point Action Space

## Immediate Comment / Docstring

```lean
/-- [IV.D115] The crossing-point action space: the tangent space at
    the omega-crossing of L (lemniscate), where the A-sector holonomy
    is concentrated. The crossing point is where both lobes meet,
    giving SU(2) its non-abelian structure. -/
```

## Source Excerpt

```lean
structure CrossingActionSpace where
  /-- Real dimension of the tangent space at crossing. -/
  real_dim : Nat
  dim_eq : real_dim = 3
  /-- The crossing is where both lobes are simultaneously active. -/
  both_lobes : Bool
  both_true : both_lobes = true
  deriving Repr
```
