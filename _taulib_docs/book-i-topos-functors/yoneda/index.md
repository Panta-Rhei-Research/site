---
{
  "projection_kind": "taulib_declaration",
  "title": "yoneda",
  "permalink": "/verify/taulib/docs/book-i-topos-functors/yoneda/",
  "summary_short": "`def` declaration in `TauLib.BookI.Topos.Functors`.",
  "declaration_id": "TauLib.BookI.Topos.Functors::yoneda",
  "declaration_slug": "yoneda",
  "kind": "def",
  "name": "yoneda",
  "module_name": "TauLib.BookI.Topos.Functors",
  "module_url": "/verify/taulib/docs/book-i-topos-functors/",
  "source_line_start": 123,
  "source_line_end": 124,
  "registry_ids": [
    "I.D54"
  ],
  "related_registry_items": [
    {
      "id": "I.D54",
      "title": "Yoneda Embedding",
      "url": "/registry/object/I.D54/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/Functors.lean#L123-L124",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/Functors.lean#L123-L124",
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
- Source path: [`TauLib/BookI/Topos/Functors.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/Functors.lean#L123-L124)
- Source range: L123-L124
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D54` — Yoneda Embedding

## Immediate Comment / Docstring

```lean
/-- [I.D54] The Yoneda embedding y: Cat_τ → PSh(Cat_τ).
    Sends X to Hom(-, X), modeled as a presheaf. -/
```

## Source Excerpt

```lean
def yoneda (x : TauIdx) : Presheaf :=
  ⟨fun _ => true⟩  -- In thin Cat_τ, all hom-sets are singletons
```
