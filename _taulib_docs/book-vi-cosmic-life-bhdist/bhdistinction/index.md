---
{
  "projection_kind": "taulib_declaration",
  "title": "BHDistinction",
  "permalink": "/verify/taulib/docs/book-vi-cosmic-life-bhdist/bhdistinction/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.CosmicLife.BHDist`.",
  "declaration_id": "TauLib.BookVI.CosmicLife.BHDist::BHDistinction",
  "declaration_slug": "bhdistinction",
  "kind": "structure",
  "name": "BHDistinction",
  "module_name": "TauLib.BookVI.CosmicLife.BHDist",
  "module_url": "/verify/taulib/docs/book-vi-cosmic-life-bhdist/",
  "source_line_start": 132,
  "source_line_end": 142,
  "registry_ids": [
    "VI.T29"
  ],
  "related_registry_items": [
    {
      "id": "VI.T29",
      "title": "BH Distinction Theorem",
      "url": "/registry/object/VI.T29/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHDist.lean#L132-L142",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHDist.lean#L132-L142",
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
- Source path: [`TauLib/BookVI/CosmicLife/BHDist.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHDist.lean#L132-L142)
- Source range: L132-L142
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T29` — BH Distinction Theorem

## Immediate Comment / Docstring

```lean
/-- [VI.T29] BH Distinction Theorem: all 5 τ-Distinction conditions satisfied.
    (i) Clopen: event horizon (zero-width boundary)
    (ii) Refinement-coherent: No-Hair collapses tower
    (iii) Eventually stable: stabilizes after 1 ringdown
    (iv) Law-stable: No-Shrink Theorem (V.T114)
    (v) H∂-equivariant: axial Killing symmetry -/
```

## Source Excerpt

```lean
structure BHDistinction where
  /-- Number of conditions satisfied. -/
  conditions_satisfied : Nat
  /-- All five conditions verified. -/
  all_five : conditions_satisfied = 5
  clopen : Bool := true
  refinement_coherent : Bool := true
  eventually_stable : Bool := true
  law_stable : Bool := true        -- via V.T114 (No-Shrink)
  equivariant : Bool := true
  deriving Repr
```
