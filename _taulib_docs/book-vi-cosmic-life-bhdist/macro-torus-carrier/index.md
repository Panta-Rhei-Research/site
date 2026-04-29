---
{
  "projection_kind": "taulib_declaration",
  "title": "MacroTorusCarrier",
  "permalink": "/verify/taulib/docs/book-vi-cosmic-life-bhdist/macro-torus-carrier/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.CosmicLife.BHDist`.",
  "declaration_id": "TauLib.BookVI.CosmicLife.BHDist::MacroTorusCarrier",
  "declaration_slug": "macro-torus-carrier",
  "kind": "structure",
  "name": "MacroTorusCarrier",
  "module_name": "TauLib.BookVI.CosmicLife.BHDist",
  "module_url": "/verify/taulib/docs/book-vi-cosmic-life-bhdist/",
  "source_line_start": 56,
  "source_line_end": 67,
  "registry_ids": [
    "VI.D54"
  ],
  "related_registry_items": [
    {
      "id": "VI.D54",
      "title": "Macro-Torus Carrier T(H_BH)",
      "url": "/registry/object/VI.D54/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHDist.lean#L56-L67",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHDist.lean#L56-L67",
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
- Source path: [`TauLib/BookVI/CosmicLife/BHDist.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHDist.lean#L56-L67)
- Source range: L56-L67
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D54` — Macro-Torus Carrier T(H_BH)

## Immediate Comment / Docstring

```lean
/-- [VI.D54] Macro-torus carrier: BH carrier with T² boundary.
    Components: T² boundary topology, multipole refinement tower,
    Kerr holonomy, and carrier type. -/
```

## Source Excerpt

```lean
structure MacroTorusCarrier where
  /-- Horizon has T² topology (from V.T109). -/
  t2_boundary : Bool := true
  /-- Refinement tower: multipole moments through order 2^n. -/
  multipole_tower : Bool := true
  /-- Boundary holonomy: frame-dragging algebra from Kerr. -/
  kerr_holonomy : Bool := true
  /-- Carrier type identifier. -/
  carrier_type : String := "macro-torus"
  /-- Horizon dimension = 2 (torus). -/
  horizon_dim : Nat := horizon_topology
  deriving Repr
```
