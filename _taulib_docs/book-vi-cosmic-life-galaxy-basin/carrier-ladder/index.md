---
{
  "projection_kind": "taulib_declaration",
  "title": "CarrierLadder",
  "permalink": "/verify/taulib/docs/book-vi-cosmic-life-galaxy-basin/carrier-ladder/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.CosmicLife.GalaxyBasin`.",
  "declaration_id": "TauLib.BookVI.CosmicLife.GalaxyBasin::CarrierLadder",
  "declaration_slug": "carrier-ladder",
  "kind": "structure",
  "name": "CarrierLadder",
  "module_name": "TauLib.BookVI.CosmicLife.GalaxyBasin",
  "module_url": "/verify/taulib/docs/book-vi-cosmic-life-galaxy-basin/",
  "source_line_start": 50,
  "source_line_end": 57,
  "registry_ids": [
    "VI.D63"
  ],
  "related_registry_items": [
    {
      "id": "VI.D63",
      "title": "Carrier Ladder",
      "url": "/registry/object/VI.D63/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L50-L57",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.CosmicLife.GalaxyBasin",
        "url": "/verify/taulib/docs/book-vi-cosmic-life-galaxy-basin/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L50-L57",
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

- Module: [TauLib.BookVI.CosmicLife.GalaxyBasin](/verify/taulib/docs/book-vi-cosmic-life-galaxy-basin/)
- Source path: [`TauLib/BookVI/CosmicLife/GalaxyBasin.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L50-L57)
- Source range: L50-L57
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D63` — Carrier Ladder

## Immediate Comment / Docstring

```lean
/-- [VI.D63] Carrier Ladder: 7-level hierarchy from molecules to galaxies.
    X_gal[0..6] = molecular, cellular, organismal, ecosystemic,
    planetary, stellar, galactic.
    Constraints flow downward, realization flows upward. -/
```

## Source Excerpt

```lean
structure CarrierLadder where
  /-- Number of hierarchy levels. -/
  level_count : Nat
  /-- Exactly 7 levels (0 through 6). -/
  count_eq : level_count = 7
  /-- Constraints compose functorially. -/
  functorial : Bool := true
  deriving Repr
```
