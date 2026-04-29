---
{
  "projection_kind": "taulib_declaration",
  "title": "bh_distinction_theorem",
  "permalink": "/verify/taulib/docs/book-vi-cosmic-life-bhdist/bh-distinction-theorem/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.CosmicLife.BHDist`.",
  "declaration_id": "TauLib.BookVI.CosmicLife.BHDist::bh_distinction_theorem",
  "declaration_slug": "bh-distinction-theorem",
  "kind": "theorem",
  "name": "bh_distinction_theorem",
  "module_name": "TauLib.BookVI.CosmicLife.BHDist",
  "module_url": "/verify/taulib/docs/book-vi-cosmic-life-bhdist/",
  "source_line_start": 149,
  "source_line_end": 156,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHDist.lean#L149-L156",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHDist.lean#L149-L156",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookVI/CosmicLife/BHDist.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHDist.lean#L149-L156)
- Source range: L149-L156
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VI.T29` — BH Distinction Theorem

## Immediate Comment / Docstring

```lean
/-- [VI.T29] BH Distinction Theorem: 5/5 conditions, carrier is T². -/
```

## Source Excerpt

```lean
theorem bh_distinction_theorem :
    bh_dist.conditions_satisfied = 5 ∧
    bh_dist.clopen = true ∧
    bh_dist.refinement_coherent = true ∧
    bh_dist.eventually_stable = true ∧
    bh_dist.law_stable = true ∧
    bh_dist.equivariant = true :=
  ⟨rfl, rfl, rfl, rfl, rfl, rfl⟩
```
