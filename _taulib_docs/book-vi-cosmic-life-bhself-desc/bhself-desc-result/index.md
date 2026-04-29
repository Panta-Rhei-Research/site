---
{
  "projection_kind": "taulib_declaration",
  "title": "BHSelfDescResult",
  "permalink": "/verify/taulib/docs/book-vi-cosmic-life-bhself-desc/bhself-desc-result/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.CosmicLife.BHSelfDesc`.",
  "declaration_id": "TauLib.BookVI.CosmicLife.BHSelfDesc::BHSelfDescResult",
  "declaration_slug": "bhself-desc-result",
  "kind": "structure",
  "name": "BHSelfDescResult",
  "module_name": "TauLib.BookVI.CosmicLife.BHSelfDesc",
  "module_url": "/verify/taulib/docs/book-vi-cosmic-life-bhself-desc/",
  "source_line_start": 113,
  "source_line_end": 123,
  "registry_ids": [
    "VI.T30"
  ],
  "related_registry_items": [
    {
      "id": "VI.T30",
      "title": "BH SelfDesc Theorem",
      "url": "/registry/object/VI.T30/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L113-L123",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.CosmicLife.BHSelfDesc",
        "url": "/verify/taulib/docs/book-vi-cosmic-life-bhself-desc/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L113-L123",
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

- Module: [TauLib.BookVI.CosmicLife.BHSelfDesc](/verify/taulib/docs/book-vi-cosmic-life-bhself-desc/)
- Source path: [`TauLib/BookVI/CosmicLife/BHSelfDesc.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L113-L123)
- Source range: L113-L123
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T30` — BH SelfDesc Theorem

## Immediate Comment / Docstring

```lean
/-- [VI.T30] BH SelfDesc Theorem: 3/3 conditions verified.
    (i) Completeness: Eval reconstructs D at every level
    (ii) Internality: code + evaluator reside within carrier
    (iii) Refinement coherence: tower stabilizes at n=1
    Conclusion: BH IS alive (same theorem as for cells). -/
```

## Source Excerpt

```lean
structure BHSelfDescResult where
  /-- Number of SelfDesc conditions satisfied. -/
  conditions_satisfied : Nat
  /-- All three conditions verified. -/
  all_three : conditions_satisfied = 3
  completeness : Bool := true
  internality : Bool := true
  refinement_coherence : Bool := true
  /-- Final verdict: BH is alive. -/
  bh_alive : Bool := true
  deriving Repr
```
