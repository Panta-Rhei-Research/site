---
{
  "projection_kind": "taulib_declaration",
  "title": "SelfDescPredicate",
  "permalink": "/verify/taulib/docs/book-vi-life-core-self-desc/self-desc-predicate/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.LifeCore.SelfDesc`.",
  "declaration_id": "TauLib.BookVI.LifeCore.SelfDesc::SelfDescPredicate",
  "declaration_slug": "self-desc-predicate",
  "kind": "structure",
  "name": "SelfDescPredicate",
  "module_name": "TauLib.BookVI.LifeCore.SelfDesc",
  "module_url": "/verify/taulib/docs/book-vi-life-core-self-desc/",
  "source_line_start": 25,
  "source_line_end": 31,
  "registry_ids": [
    "VI.D08"
  ],
  "related_registry_items": [
    {
      "id": "VI.D08",
      "title": "SelfDesc Predicate",
      "url": "/registry/object/VI.D08/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/SelfDesc.lean#L25-L31",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/SelfDesc.lean#L25-L31",
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
- Source path: [`TauLib/BookVI/LifeCore/SelfDesc.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/SelfDesc.lean#L25-L31)
- Source range: L25-L31
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D08` — SelfDesc Predicate

## Immediate Comment / Docstring

```lean
/-- [VI.D08] SelfDesc predicate: internal evaluator Eval_X satisfying
    completeness, internality, refinement coherence. -/
```

## Source Excerpt

```lean
structure SelfDescPredicate where
  condition_count : Nat
  count_eq : condition_count = 3
  completeness : Bool := true
  internality : Bool := true
  refinement_coherence : Bool := true
  deriving Repr
```
