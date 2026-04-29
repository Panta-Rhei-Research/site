---
{
  "projection_kind": "taulib_declaration",
  "title": "LanguageAddsTemporalization",
  "permalink": "/verify/taulib/docs/book-vii-meta-saturation/language-adds-temporalization/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Saturation`.",
  "declaration_id": "TauLib.BookVII.Meta.Saturation::LanguageAddsTemporalization",
  "declaration_slug": "language-adds-temporalization",
  "kind": "structure",
  "name": "LanguageAddsTemporalization",
  "module_name": "TauLib.BookVII.Meta.Saturation",
  "module_url": "/verify/taulib/docs/book-vii-meta-saturation/",
  "source_line_start": 607,
  "source_line_end": 614,
  "registry_ids": [
    "VII.D51"
  ],
  "related_registry_items": [
    {
      "id": "VII.D51",
      "title": "Language Adds Temporalization",
      "url": "/registry/object/VII.D51/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L607-L614",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Saturation",
        "url": "/verify/taulib/docs/book-vii-meta-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L607-L614",
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

- Module: [TauLib.BookVII.Meta.Saturation](/verify/taulib/docs/book-vii-meta-saturation/)
- Source path: [`TauLib/BookVII/Meta/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L607-L614)
- Source range: L607-L614
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D51` — Language Adds Temporalization

## Immediate Comment / Docstring

```lean
/-- [VII.D51] Language Adds Temporalization (ch59). Syntax introduces
    temporal markers (past/present/future) into the enrichment chain.
    Pre-linguistic systems process structure atemporally; language
    adds a temporal index to every predication. -/
```

## Source Excerpt

```lean
structure LanguageAddsTemporalization where
  /-- Temporal markers introduced by syntax. -/
  temporal_markers : Bool := true
  /-- Pre-linguistic = atemporal. -/
  pre_linguistic_atemporal : Bool := true
  /-- Language indexes every predication temporally. -/
  temporal_indexing : Bool := true
  deriving Repr
```
