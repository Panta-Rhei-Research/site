---
{
  "projection_kind": "taulib_declaration",
  "title": "StrongSaturationDefect",
  "permalink": "/verify/taulib/docs/book-vi-cosmic-life-bhdist/strong-saturation-defect/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.CosmicLife.BHDist`.",
  "declaration_id": "TauLib.BookVI.CosmicLife.BHDist::StrongSaturationDefect",
  "declaration_slug": "strong-saturation-defect",
  "kind": "structure",
  "name": "StrongSaturationDefect",
  "module_name": "TauLib.BookVI.CosmicLife.BHDist",
  "module_url": "/verify/taulib/docs/book-vi-cosmic-life-bhdist/",
  "source_line_start": 115,
  "source_line_end": 120,
  "registry_ids": [
    "VI.D57"
  ],
  "related_registry_items": [
    {
      "id": "VI.D57",
      "title": "Strong-Saturation Defect",
      "url": "/registry/object/VI.D57/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHDist.lean#L115-L120",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHDist.lean#L115-L120",
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
- Source path: [`TauLib/BookVI/CosmicLife/BHDist.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHDist.lean#L115-L120)
- Source range: L115-L120
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D57` — Strong-Saturation Defect

## Immediate Comment / Docstring

```lean
/-- [VI.D57] Strong-saturation defect: V^s_n ∈ [0,1].
    Measures residual strong-sector instability. -/
```

## Source Excerpt

```lean
structure StrongSaturationDefect where
  /-- Range is [0,1]. -/
  range_unit : Bool := true
  /-- BH has negligible strong-saturation defect. -/
  bh_negligible : Bool := true
  deriving Repr
```
