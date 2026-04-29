---
{
  "projection_kind": "taulib_declaration",
  "title": "FrameClosureDefect",
  "permalink": "/verify/taulib/docs/book-vi-cosmic-life-bhdist/frame-closure-defect/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.CosmicLife.BHDist`.",
  "declaration_id": "TauLib.BookVI.CosmicLife.BHDist::FrameClosureDefect",
  "declaration_slug": "frame-closure-defect",
  "kind": "structure",
  "name": "FrameClosureDefect",
  "module_name": "TauLib.BookVI.CosmicLife.BHDist",
  "module_url": "/verify/taulib/docs/book-vi-cosmic-life-bhdist/",
  "source_line_start": 100,
  "source_line_end": 107,
  "registry_ids": [
    "VI.D56"
  ],
  "related_registry_items": [
    {
      "id": "VI.D56",
      "title": "Frame-Closure Defect",
      "url": "/registry/object/VI.D56/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHDist.lean#L100-L107",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHDist.lean#L100-L107",
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
- Source path: [`TauLib/BookVI/CosmicLife/BHDist.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHDist.lean#L100-L107)
- Source range: L100-L107
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D56` — Frame-Closure Defect

## Immediate Comment / Docstring

```lean
/-- [VI.D56] Frame-closure defect: Sobolev-norm deviation from Kerr-Newman.
    Vanishes for isolated stationary Kerr BH.
    Norm choice is conventional (any coercive norm on H^n(H) works). -/
```

## Source Excerpt

```lean
structure FrameClosureDefect where
  /-- Vanishes for ideal Kerr solution. -/
  vanishes_ideal : Bool := true
  /-- Uses Sobolev norm (conventional choice). -/
  sobolev_norm : Bool := true
  /-- Ringdown damps this defect via V.D234 QNM modes. -/
  damped_by_qnm : Bool := true
  deriving Repr
```
