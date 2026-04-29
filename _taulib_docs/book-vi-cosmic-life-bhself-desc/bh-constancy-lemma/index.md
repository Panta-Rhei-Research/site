---
{
  "projection_kind": "taulib_declaration",
  "title": "bh_constancy_lemma",
  "permalink": "/verify/taulib/docs/book-vi-cosmic-life-bhself-desc/bh-constancy-lemma/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.CosmicLife.BHSelfDesc`.",
  "declaration_id": "TauLib.BookVI.CosmicLife.BHSelfDesc::bh_constancy_lemma",
  "declaration_slug": "bh-constancy-lemma",
  "kind": "theorem",
  "name": "bh_constancy_lemma",
  "module_name": "TauLib.BookVI.CosmicLife.BHSelfDesc",
  "module_url": "/verify/taulib/docs/book-vi-cosmic-life-bhself-desc/",
  "source_line_start": 78,
  "source_line_end": 80,
  "registry_ids": [
    "VI.L10"
  ],
  "related_registry_items": [
    {
      "id": "VI.L10",
      "title": "BH Constancy Lemma",
      "url": "/registry/object/VI.L10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L78-L80",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L78-L80",
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

- Module: [TauLib.BookVI.CosmicLife.BHSelfDesc](/verify/taulib/docs/book-vi-cosmic-life-bhself-desc/)
- Source path: [`TauLib/BookVI/CosmicLife/BHSelfDesc.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L78-L80)
- Source range: L78-L80
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VI.L10` — BH Constancy Lemma

## Immediate Comment / Docstring

```lean
/-- [VI.L10] BH constancy: same code for all n ≥ 0.
    Code is independent of blueprint ball radius. -/
```

## Source Excerpt

```lean
theorem bh_constancy_lemma :
    bh_horizon.constant_code = true ∧
    bh_horizon.stabilization_depth = 1 := ⟨rfl, rfl⟩
```
