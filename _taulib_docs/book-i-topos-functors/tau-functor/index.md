---
{
  "projection_kind": "taulib_declaration",
  "title": "TauFunctor",
  "permalink": "/verify/taulib/docs/book-i-topos-functors/tau-functor/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Topos.Functors`.",
  "declaration_id": "TauLib.BookI.Topos.Functors::TauFunctor",
  "declaration_slug": "tau-functor",
  "kind": "structure",
  "name": "TauFunctor",
  "module_name": "TauLib.BookI.Topos.Functors",
  "module_url": "/verify/taulib/docs/book-i-topos-functors/",
  "source_line_start": 45,
  "source_line_end": 47,
  "registry_ids": [
    "I.D52"
  ],
  "related_registry_items": [
    {
      "id": "I.D52",
      "title": "Tau-Functor",
      "url": "/registry/object/I.D52/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/Functors.lean#L45-L47",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/Functors.lean#L45-L47",
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
- Source path: [`TauLib/BookI/Topos/Functors.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/Functors.lean#L45-L47)
- Source range: L45-L47
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D52` — Tau-Functor

## Immediate Comment / Docstring

```lean
/-- [I.D52] A τ-functor maps objects to objects and respects composition.
    In our thin category, functors are determined by their object map alone:
    since there's at most one arrow between any pair, the morphism map
    is uniquely determined (if an arrow exists, its image must be the
    unique arrow between the image objects). -/
```

## Source Excerpt

```lean
structure TauFunctor where
  /-- Object map: where each τ-index goes. -/
  obj_map : TauIdx → TauIdx
```
