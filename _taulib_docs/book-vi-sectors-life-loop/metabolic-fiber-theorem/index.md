---
{
  "projection_kind": "taulib_declaration",
  "title": "MetabolicFiberTheorem",
  "permalink": "/verify/taulib/docs/book-vi-sectors-life-loop/metabolic-fiber-theorem/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Sectors.LifeLoop`.",
  "declaration_id": "TauLib.BookVI.Sectors.LifeLoop::MetabolicFiberTheorem",
  "declaration_slug": "metabolic-fiber-theorem",
  "kind": "structure",
  "name": "MetabolicFiberTheorem",
  "module_name": "TauLib.BookVI.Sectors.LifeLoop",
  "module_url": "/verify/taulib/docs/book-vi-sectors-life-loop/",
  "source_line_start": 67,
  "source_line_end": 72,
  "registry_ids": [
    "VI.T05"
  ],
  "related_registry_items": [
    {
      "id": "VI.T05",
      "title": "Metabolic Fiber Theorem",
      "url": "/registry/object/VI.T05/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/LifeLoop.lean#L67-L72",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/LifeLoop.lean#L67-L72",
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
- Source path: [`TauLib/BookVI/Sectors/LifeLoop.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/LifeLoop.lean#L67-L72)
- Source range: L67-L72
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T05` — Metabolic Fiber Theorem

## Immediate Comment / Docstring

```lean
/-- [VI.T05] Metabolic Fiber Theorem: every Life loop factors through
    Loop_src × Loop_rec × Loop_base. -/
```

## Source Excerpt

```lean
structure MetabolicFiberTheorem where
  factor_count : Nat
  count_eq : factor_count = 3
  src_nontrivial : Bool := true
  rec_nontrivial : Bool := true
  deriving Repr
```
