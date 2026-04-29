---
{
  "projection_kind": "taulib_declaration",
  "title": "horizon_consistency",
  "permalink": "/verify/taulib/docs/book-vi-cosmic-life-bhdist/horizon-consistency/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.CosmicLife.BHDist`.",
  "declaration_id": "TauLib.BookVI.CosmicLife.BHDist::horizon_consistency",
  "declaration_slug": "horizon-consistency",
  "kind": "theorem",
  "name": "horizon_consistency",
  "module_name": "TauLib.BookVI.CosmicLife.BHDist",
  "module_url": "/verify/taulib/docs/book-vi-cosmic-life-bhdist/",
  "source_line_start": 159,
  "source_line_end": 165,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHDist.lean#L159-L165",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHDist.lean#L159-L165",
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
- Source path: [`TauLib/BookVI/CosmicLife/BHDist.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHDist.lean#L159-L165)
- Source range: L159-L165
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Cross-book consistency: BH carrier uses T² from BookV, not S². -/
```

## Source Excerpt

```lean
theorem horizon_consistency :
    macro_torus.horizon_dim = 2 ∧
    horizon_topology = 2 ∧
    primitiveTorusModes.length = 3 :=
  ⟨rfl, rfl, by native_decide⟩

end Tau.BookVI.BHDist
```
