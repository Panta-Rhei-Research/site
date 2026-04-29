---
{
  "projection_kind": "taulib_declaration",
  "title": "NatTrans",
  "permalink": "/verify/taulib/docs/book-i-topos-functors/nat-trans/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Topos.Functors`.",
  "declaration_id": "TauLib.BookI.Topos.Functors::NatTrans",
  "declaration_slug": "nat-trans",
  "kind": "structure",
  "name": "NatTrans",
  "module_name": "TauLib.BookI.Topos.Functors",
  "module_url": "/verify/taulib/docs/book-i-topos-functors/",
  "source_line_start": 78,
  "source_line_end": 84,
  "registry_ids": [
    "I.D53"
  ],
  "related_registry_items": [
    {
      "id": "I.D53",
      "title": "Natural Transformation",
      "url": "/registry/object/I.D53/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/Functors.lean#L78-L84",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.Functors",
        "url": "/verify/taulib/docs/book-i-topos-functors/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/Functors.lean#L78-L84",
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

- Module: [TauLib.BookI.Topos.Functors](/verify/taulib/docs/book-i-topos-functors/)
- Source path: [`TauLib/BookI/Topos/Functors.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/Functors.lean#L78-L84)
- Source range: L78-L84
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D53` — Natural Transformation

## Immediate Comment / Docstring

```lean
/-- [I.D53] A natural transformation between τ-functors.
    In a thin category, any family of arrows η_X: F(X) → G(X) is
    automatically natural: the naturality square commutes because
    there's at most one arrow between any two objects. -/
```

## Source Excerpt

```lean
structure NatTrans (F G : TauFunctor) where
  /-- Component map: for each object X, an arrow F(X) → G(X).
      Represented as a function assigning target indices.
      In a thin category, naturality is automatic. -/
  component : TauIdx → TauIdx
  /-- Source compatibility: the component at X has source F(X). -/
  src_compat : ∀ x, component x = component x := fun _ => rfl
```
