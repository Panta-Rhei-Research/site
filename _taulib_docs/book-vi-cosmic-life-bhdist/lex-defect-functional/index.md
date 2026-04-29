---
{
  "projection_kind": "taulib_declaration",
  "title": "LexDefectFunctional",
  "permalink": "/verify/taulib/docs/book-vi-cosmic-life-bhdist/lex-defect-functional/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.CosmicLife.BHDist`.",
  "declaration_id": "TauLib.BookVI.CosmicLife.BHDist::LexDefectFunctional",
  "declaration_slug": "lex-defect-functional",
  "kind": "structure",
  "name": "LexDefectFunctional",
  "module_name": "TauLib.BookVI.CosmicLife.BHDist",
  "module_url": "/verify/taulib/docs/book-vi-cosmic-life-bhdist/",
  "source_line_start": 80,
  "source_line_end": 87,
  "registry_ids": [
    "VI.D55"
  ],
  "related_registry_items": [
    {
      "id": "VI.D55",
      "title": "Lexicographic Defect Functional",
      "url": "/registry/object/VI.D55/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHDist.lean#L80-L87",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.CosmicLife.BHDist",
        "url": "/verify/taulib/docs/book-vi-cosmic-life-bhdist/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHDist.lean#L80-L87",
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

- Module: [TauLib.BookVI.CosmicLife.BHDist](/verify/taulib/docs/book-vi-cosmic-life-bhdist/)
- Source path: [`TauLib/BookVI/CosmicLife/BHDist.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHDist.lean#L80-L87)
- Source range: L80-L87
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D55` — Lexicographic Defect Functional

## Immediate Comment / Docstring

```lean
/-- [VI.D55] Lexicographic defect: pairs frame-closure + strong-saturation.
    Ordered lexicographically: frame dominates (slow DoF first). -/
```

## Source Excerpt

```lean
structure LexDefectFunctional where
  /-- Number of defect components. -/
  component_count : Nat
  /-- Exactly 2 components: frame-closure + strong-saturation. -/
  count_eq : component_count = 2
  /-- Lexicographic ordering active. -/
  lexicographic : Bool := true
  deriving Repr
```
