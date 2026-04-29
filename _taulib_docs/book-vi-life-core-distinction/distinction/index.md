---
{
  "projection_kind": "taulib_declaration",
  "title": "Distinction",
  "permalink": "/verify/taulib/docs/book-vi-life-core-distinction/distinction/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.LifeCore.Distinction`.",
  "declaration_id": "TauLib.BookVI.LifeCore.Distinction::Distinction",
  "declaration_slug": "distinction",
  "kind": "structure",
  "name": "Distinction",
  "module_name": "TauLib.BookVI.LifeCore.Distinction",
  "module_url": "/verify/taulib/docs/book-vi-life-core-distinction/",
  "source_line_start": 27,
  "source_line_end": 35,
  "registry_ids": [
    "VI.D04"
  ],
  "related_registry_items": [
    {
      "id": "VI.D04",
      "title": "τ-Distinction",
      "url": "/registry/object/VI.D04/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/Distinction.lean#L27-L35",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.LifeCore.Distinction",
        "url": "/verify/taulib/docs/book-vi-life-core-distinction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/Distinction.lean#L27-L35",
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

- Module: [TauLib.BookVI.LifeCore.Distinction](/verify/taulib/docs/book-vi-life-core-distinction/)
- Source path: [`TauLib/BookVI/LifeCore/Distinction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/Distinction.lean#L27-L35)
- Source range: L27-L35
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D04` — τ-Distinction

## Immediate Comment / Docstring

```lean
/-- [VI.D04] τ-Distinction predicate: D: X → 2_τ satisfying 5 conditions.
    1. Clopen partition  2. Refinement-coherent  3. Eventually stable
    4. Law-stable  5. H_∂-equivariant -/
```

## Source Excerpt

```lean
structure Distinction where
  condition_count : Nat
  count_eq : condition_count = 5
  clopen : Bool := true
  refinement_coherent : Bool := true
  eventually_stable : Bool := true
  law_stable : Bool := true
  equivariant : Bool := true
  deriving Repr
```
