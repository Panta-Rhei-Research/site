---
{
  "projection_kind": "taulib_declaration",
  "title": "SourceSubClass",
  "permalink": "/verify/taulib/docs/book-vi-sectors-life-loop/source-sub-class/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Sectors.LifeLoop`.",
  "declaration_id": "TauLib.BookVI.Sectors.LifeLoop::SourceSubClass",
  "declaration_slug": "source-sub-class",
  "kind": "structure",
  "name": "SourceSubClass",
  "module_name": "TauLib.BookVI.Sectors.LifeLoop",
  "module_url": "/verify/taulib/docs/book-vi-sectors-life-loop/",
  "source_line_start": 54,
  "source_line_end": 57,
  "registry_ids": [
    "VI.D13"
  ],
  "related_registry_items": [
    {
      "id": "VI.D13",
      "title": "Source Sub-Class (Loop_src)",
      "url": "/registry/object/VI.D13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/LifeLoop.lean#L54-L57",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Sectors.LifeLoop",
        "url": "/verify/taulib/docs/book-vi-sectors-life-loop/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/LifeLoop.lean#L54-L57",
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

- Module: [TauLib.BookVI.Sectors.LifeLoop](/verify/taulib/docs/book-vi-sectors-life-loop/)
- Source path: [`TauLib/BookVI/Sectors/LifeLoop.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/LifeLoop.lean#L54-L57)
- Source range: L54-L57
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D13` — Source Sub-Class (Loop_src)

## Immediate Comment / Docstring

```lean
/-- [VI.D13] Source sub-class: loops with dominant π'-winding. -/
```

## Source Excerpt

```lean
structure SourceSubClass where
  generator : String := "pi_prime"
  archetype : String := "plants"
  deriving Repr
```
