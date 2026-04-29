---
{
  "projection_kind": "taulib_declaration",
  "title": "SelfDescClosure",
  "permalink": "/verify/taulib/docs/book-vi-life-core-self-desc/self-desc-closure/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.LifeCore.SelfDesc`.",
  "declaration_id": "TauLib.BookVI.LifeCore.SelfDesc::SelfDescClosure",
  "declaration_slug": "self-desc-closure",
  "kind": "structure",
  "name": "SelfDescClosure",
  "module_name": "TauLib.BookVI.LifeCore.SelfDesc",
  "module_url": "/verify/taulib/docs/book-vi-life-core-self-desc/",
  "source_line_start": 51,
  "source_line_end": 55,
  "registry_ids": [
    "VI.T03"
  ],
  "related_registry_items": [
    {
      "id": "VI.T03",
      "title": "SelfDesc Closure Theorem",
      "url": "/registry/object/VI.T03/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/SelfDesc.lean#L51-L55",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/SelfDesc.lean#L51-L55",
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
- Source path: [`TauLib/BookVI/LifeCore/SelfDesc.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/SelfDesc.lean#L51-L55)
- Source range: L51-L55
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T03` — SelfDesc Closure Theorem

## Immediate Comment / Docstring

```lean
/-- [VI.T03] SelfDesc Closure: SelfDesc pair is self-maintaining. -/
```

## Source Excerpt

```lean
structure SelfDescClosure where
  basin_correction : Bool := true
  code_integrity : Bool := true
  closure_under_eval : Bool := true
  deriving Repr
```
