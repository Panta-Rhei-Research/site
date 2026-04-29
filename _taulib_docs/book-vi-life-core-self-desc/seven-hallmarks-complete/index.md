---
{
  "projection_kind": "taulib_declaration",
  "title": "SevenHallmarksComplete",
  "permalink": "/verify/taulib/docs/book-vi-life-core-self-desc/seven-hallmarks-complete/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.LifeCore.SelfDesc`.",
  "declaration_id": "TauLib.BookVI.LifeCore.SelfDesc::SevenHallmarksComplete",
  "declaration_slug": "seven-hallmarks-complete",
  "kind": "structure",
  "name": "SevenHallmarksComplete",
  "module_name": "TauLib.BookVI.LifeCore.SelfDesc",
  "module_url": "/verify/taulib/docs/book-vi-life-core-self-desc/",
  "source_line_start": 66,
  "source_line_end": 72,
  "registry_ids": [
    "VI.P04"
  ],
  "related_registry_items": [
    {
      "id": "VI.P04",
      "title": "Seven Hallmarks Complete",
      "url": "/registry/object/VI.P04/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/SelfDesc.lean#L66-L72",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.LifeCore.SelfDesc",
        "url": "/verify/taulib/docs/book-vi-life-core-self-desc/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/SelfDesc.lean#L66-L72",
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

- Module: [TauLib.BookVI.LifeCore.SelfDesc](/verify/taulib/docs/book-vi-life-core-self-desc/)
- Source path: [`TauLib/BookVI/LifeCore/SelfDesc.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/SelfDesc.lean#L66-L72)
- Source range: L66-L72
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.P04` — Seven Hallmarks Complete

## Immediate Comment / Docstring

```lean
/-- [VI.P04] Seven hallmarks complete: bijection H → F, |H| = |F| = 7. -/
```

## Source Excerpt

```lean
structure SevenHallmarksComplete where
  hallmark_count : Nat
  count_eq : hallmark_count = 7
  formal_count : Nat
  formal_eq : formal_count = 7
  is_bijection : Bool := true
  deriving Repr
```
