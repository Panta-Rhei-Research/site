---
{
  "projection_kind": "taulib_declaration",
  "title": "BasinPredicate",
  "permalink": "/verify/taulib/docs/book-vi-cosmic-life-galaxy-basin/basin-predicate/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.CosmicLife.GalaxyBasin`.",
  "declaration_id": "TauLib.BookVI.CosmicLife.GalaxyBasin::BasinPredicate",
  "declaration_slug": "basin-predicate",
  "kind": "structure",
  "name": "BasinPredicate",
  "module_name": "TauLib.BookVI.CosmicLife.GalaxyBasin",
  "module_url": "/verify/taulib/docs/book-vi-cosmic-life-galaxy-basin/",
  "source_line_start": 80,
  "source_line_end": 93,
  "registry_ids": [
    "VI.D64"
  ],
  "related_registry_items": [
    {
      "id": "VI.D64",
      "title": "Basin Predicate",
      "url": "/registry/object/VI.D64/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L80-L93",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L80-L93",
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
- Source path: [`TauLib/BookVI/CosmicLife/GalaxyBasin.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L80-L93)
- Source range: L80-L93
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D64` — Basin Predicate

## Immediate Comment / Docstring

```lean
/-- [VI.D64] Basin Predicate: admissibility for a Life basin.
    Four conditions: (i) anchor alive, (ii) gravitational dominance,
    (iii) basin coherence (virialized), (iv) carrier support. -/
```

## Source Excerpt

```lean
structure BasinPredicate where
  /-- Number of admissibility conditions. -/
  condition_count : Nat
  /-- Exactly 4 conditions. -/
  count_eq : condition_count = 4
  /-- Anchor satisfies Distinction + SelfDesc. -/
  anchor_alive : Bool := true
  /-- Anchor is gravitationally dominant. -/
  grav_dominant : Bool := true
  /-- Basin is virialized (2K + U ≤ 0). -/
  virialized : Bool := true
  /-- At least one carrier at level n ≤ 5. -/
  carrier_support : Bool := true
  deriving Repr
```
