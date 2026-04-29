---
{
  "projection_kind": "taulib_declaration",
  "title": "AdjointRep",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/adjoint-rep/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.WeakHolonomy`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakHolonomy::AdjointRep",
  "declaration_slug": "adjoint-rep",
  "kind": "structure",
  "name": "AdjointRep",
  "module_name": "TauLib.BookIV.Electroweak.WeakHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/",
  "source_line_start": 131,
  "source_line_end": 138,
  "registry_ids": [
    "IV.D118"
  ],
  "related_registry_items": [
    {
      "id": "IV.D118",
      "title": "Weak Gauge Bosons Before Mixing",
      "url": "/registry/object/IV.D118/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L131-L138",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L131-L138",
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
- Source path: [`TauLib/BookIV/Electroweak/WeakHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L131-L138)
- Source range: L131-L138
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D118` — Weak Gauge Bosons Before Mixing

## Immediate Comment / Docstring

```lean
/-- [IV.D118] The adjoint representation of SU(2): the 3-dimensional
    representation in which the gauge bosons (W+, W-, W3) live.
    dim(adjoint) = dim(SU(2)) = 3. -/
```

## Source Excerpt

```lean
structure AdjointRep where
  /-- Dimension of the adjoint representation. -/
  adj_dim : Nat
  adj_eq : adj_dim = 3
  /-- Number of gauge bosons in the adjoint. -/
  num_bosons : Nat
  bosons_eq : num_bosons = 3
  deriving Repr
```
