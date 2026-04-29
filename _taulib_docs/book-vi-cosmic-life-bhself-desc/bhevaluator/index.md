---
{
  "projection_kind": "taulib_declaration",
  "title": "BHEvaluator",
  "permalink": "/verify/taulib/docs/book-vi-cosmic-life-bhself-desc/bhevaluator/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.CosmicLife.BHSelfDesc`.",
  "declaration_id": "TauLib.BookVI.CosmicLife.BHSelfDesc::BHEvaluator",
  "declaration_slug": "bhevaluator",
  "kind": "structure",
  "name": "BHEvaluator",
  "module_name": "TauLib.BookVI.CosmicLife.BHSelfDesc",
  "module_url": "/verify/taulib/docs/book-vi-cosmic-life-bhself-desc/",
  "source_line_start": 89,
  "source_line_end": 96,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L89-L96",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L89-L96",
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
- Source path: [`TauLib/BookVI/CosmicLife/BHSelfDesc.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L89-L96)
- Source range: L89-L96
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The BH evaluator is physically realized by T² torus ringdown.
    QNM frequencies from V.D234 determine the evaluation timescale.
    Fundamental ratio f(0,1)/f(1,0) = ι_τ⁻¹ (V.T168). -/
```

## Source Excerpt

```lean
structure BHEvaluator where
  /-- Evaluator mechanism: torus QNM ringdown. -/
  mechanism : String := "T2_QNM_ringdown"
  /-- Number of primitive torus modes (from BookV). -/
  mode_count : Nat := primitiveTorusModes.length
  /-- QNM ratio is ι_τ⁻¹ > 1 (from BookV). -/
  ratio_exceeds_one : Bool := true
  deriving Repr
```
