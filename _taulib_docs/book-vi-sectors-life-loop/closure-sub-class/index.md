---
{
  "projection_kind": "taulib_declaration",
  "title": "ClosureSubClass",
  "permalink": "/verify/taulib/docs/book-vi-sectors-life-loop/closure-sub-class/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Sectors.LifeLoop`.",
  "declaration_id": "TauLib.BookVI.Sectors.LifeLoop::ClosureSubClass",
  "declaration_slug": "closure-sub-class",
  "kind": "structure",
  "name": "ClosureSubClass",
  "module_name": "TauLib.BookVI.Sectors.LifeLoop",
  "module_url": "/verify/taulib/docs/book-vi-sectors-life-loop/",
  "source_line_start": 60,
  "source_line_end": 63,
  "registry_ids": [
    "VI.D14"
  ],
  "related_registry_items": [
    {
      "id": "VI.D14",
      "title": "Closure Sub-Class (Loop_rec)",
      "url": "/registry/object/VI.D14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/LifeLoop.lean#L60-L63",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/LifeLoop.lean#L60-L63",
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
- Source path: [`TauLib/BookVI/Sectors/LifeLoop.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/LifeLoop.lean#L60-L63)
- Source range: L60-L63
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D14` — Closure Sub-Class (Loop_rec)

## Immediate Comment / Docstring

```lean
/-- [VI.D14] Closure sub-class: loops with dominant π''-winding. -/
```

## Source Excerpt

```lean
structure ClosureSubClass where
  generator : String := "pi_double_prime"
  archetype : String := "fungi"
  deriving Repr
```
