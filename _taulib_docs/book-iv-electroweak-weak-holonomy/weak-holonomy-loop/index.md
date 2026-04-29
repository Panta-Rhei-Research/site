---
{
  "projection_kind": "taulib_declaration",
  "title": "WeakHolonomyLoop",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/weak-holonomy-loop/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.WeakHolonomy`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakHolonomy::WeakHolonomyLoop",
  "declaration_slug": "weak-holonomy-loop",
  "kind": "structure",
  "name": "WeakHolonomyLoop",
  "module_name": "TauLib.BookIV.Electroweak.WeakHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/",
  "source_line_start": 153,
  "source_line_end": 162,
  "registry_ids": [
    "IV.D119"
  ],
  "related_registry_items": [
    {
      "id": "IV.D119",
      "title": "Weak Holonomy Loop",
      "url": "/registry/object/IV.D119/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L153-L162",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L153-L162",
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
- Source path: [`TauLib/BookIV/Electroweak/WeakHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L153-L162)
- Source range: L153-L162
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D119` — Weak Holonomy Loop

## Immediate Comment / Docstring

```lean
/-- [IV.D119] A holonomy loop in the A-sector: parallel transport
    around a closed path in the weak sector produces a non-trivial
    SU(2) rotation. The non-abelian nature comes from the crossing
    point where both lobes interact. -/
```

## Source Excerpt

```lean
structure WeakHolonomyLoop where
  /-- Winding number around the crossing. -/
  winding : Nat
  /-- Non-abelian holonomy: rotation angle depends on path. -/
  non_abelian : Bool
  non_abelian_true : non_abelian = true
  /-- The holonomy group is SU(2). -/
  group_dim : Nat
  group_eq : group_dim = 3
  deriving Repr
```
