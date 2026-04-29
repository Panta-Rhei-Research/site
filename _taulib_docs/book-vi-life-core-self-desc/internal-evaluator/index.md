---
{
  "projection_kind": "taulib_declaration",
  "title": "InternalEvaluator",
  "permalink": "/verify/taulib/docs/book-vi-life-core-self-desc/internal-evaluator/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.LifeCore.SelfDesc`.",
  "declaration_id": "TauLib.BookVI.LifeCore.SelfDesc::InternalEvaluator",
  "declaration_slug": "internal-evaluator",
  "kind": "structure",
  "name": "InternalEvaluator",
  "module_name": "TauLib.BookVI.LifeCore.SelfDesc",
  "module_url": "/verify/taulib/docs/book-vi-life-core-self-desc/",
  "source_line_start": 38,
  "source_line_end": 42,
  "registry_ids": [
    "VI.D09"
  ],
  "related_registry_items": [
    {
      "id": "VI.D09",
      "title": "Internal Evaluator",
      "url": "/registry/object/VI.D09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/SelfDesc.lean#L38-L42",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/SelfDesc.lean#L38-L42",
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
- Source path: [`TauLib/BookVI/LifeCore/SelfDesc.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/SelfDesc.lean#L38-L42)
- Source range: L38-L42
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D09` — Internal Evaluator

## Immediate Comment / Docstring

```lean
/-- [VI.D09] Internal evaluator: morphism in End(X), no oracle needed. -/
```

## Source Excerpt

```lean
structure InternalEvaluator where
  is_endomorphism : Bool := true
  domain_in_carrier : Bool := true
  no_oracle : Bool := true
  deriving Repr
```
