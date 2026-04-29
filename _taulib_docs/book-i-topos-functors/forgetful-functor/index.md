---
{
  "projection_kind": "taulib_declaration",
  "title": "forgetful_functor",
  "permalink": "/verify/taulib/docs/book-i-topos-functors/forgetful-functor/",
  "summary_short": "`def` declaration in `TauLib.BookI.Topos.Functors`.",
  "declaration_id": "TauLib.BookI.Topos.Functors::forgetful_functor",
  "declaration_slug": "forgetful-functor",
  "kind": "def",
  "name": "forgetful_functor",
  "module_name": "TauLib.BookI.Topos.Functors",
  "module_url": "/verify/taulib/docs/book-i-topos-functors/",
  "source_line_start": 101,
  "source_line_end": 101,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/Functors.lean#L101-L101",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/Functors.lean#L101-L101",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookI/Topos/Functors.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/Functors.lean#L101-L101)
- Source range: L101-L101
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The forgetful functor from Cat_τ to itself (identity on objects).
    In a richer setting, this would forget the holomorphic structure. -/
```

## Source Excerpt

```lean
def forgetful_functor : TauFunctor := TauFunctor.id
```
