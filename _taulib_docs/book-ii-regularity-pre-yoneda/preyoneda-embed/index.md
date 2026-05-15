---
{
  "projection_kind": "taulib_declaration",
  "title": "preyoneda_embed",
  "permalink": "/corpus/taulib/docs/book-ii-regularity-pre-yoneda/preyoneda-embed/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.PreYoneda`.",
  "declaration_id": "TauLib.BookII.Regularity.PreYoneda::preyoneda_embed",
  "declaration_slug": "preyoneda-embed",
  "kind": "def",
  "name": "preyoneda_embed",
  "module_name": "TauLib.BookII.Regularity.PreYoneda",
  "module_url": "/corpus/taulib/docs/book-ii-regularity-pre-yoneda/",
  "source_line_start": 59,
  "source_line_end": 60,
  "registry_ids": [
    "II.D50"
  ],
  "related_registry_items": [
    {
      "id": "II.D50",
      "title": "Pre-Yoneda Embedding",
      "url": "/registry/object/II.D50/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L59-L60",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.PreYoneda",
        "url": "/corpus/taulib/docs/book-ii-regularity-pre-yoneda/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L59-L60",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookII.Regularity.PreYoneda](/corpus/taulib/docs/book-ii-regularity-pre-yoneda/)
- Source path: [`TauLib/BookII/Regularity/PreYoneda.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L59-L60)
- Source range: L59-L60
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `II.D50` — Pre-Yoneda Embedding

## Immediate Comment / Docstring

```lean
/-- [II.D50] Pre-Yoneda embedding: maps a function f to its restriction tower.
    At stage k, the embedding reads f at the stage-k representative of x.

    preyoneda_embed(f, x, k) = f(reduce(x, k))

    This is the fundamental representable presheaf construction:
    f becomes the natural transformation Hom(-, f) restricted to the
    primorial tower. -/
```

## Source Excerpt

```lean
def preyoneda_embed (f : TauIdx → Int) (x k : TauIdx) : Int :=
  f (reduce x k)
```
