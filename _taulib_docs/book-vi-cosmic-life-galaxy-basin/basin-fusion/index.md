---
{
  "projection_kind": "taulib_declaration",
  "title": "BasinFusion",
  "permalink": "/verify/taulib/docs/book-vi-cosmic-life-galaxy-basin/basin-fusion/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.CosmicLife.GalaxyBasin`.",
  "declaration_id": "TauLib.BookVI.CosmicLife.GalaxyBasin::BasinFusion",
  "declaration_slug": "basin-fusion",
  "kind": "structure",
  "name": "BasinFusion",
  "module_name": "TauLib.BookVI.CosmicLife.GalaxyBasin",
  "module_url": "/verify/taulib/docs/book-vi-cosmic-life-galaxy-basin/",
  "source_line_start": 135,
  "source_line_end": 144,
  "registry_ids": [
    "VI.L12"
  ],
  "related_registry_items": [
    {
      "id": "VI.L12",
      "title": "Basin Fusion via SMBH Merger",
      "url": "/registry/object/VI.L12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L135-L144",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L135-L144",
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
- Source path: [`TauLib/BookVI/CosmicLife/GalaxyBasin.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L135-L144)
- Source range: L135-L144
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.L12` — Basin Fusion via SMBH Merger

## Immediate Comment / Docstring

```lean
/-- [VI.L12] Basin Fusion via SMBH Merger: galaxy merger is basin fusion.
    (i) Anchor merger produces single remnant SMBH (V.D171, V.T112)
    (ii) Code fusion: merged code via blueprint fusion
    (iii) Carrier family union (with dynamical rearrangement)
    (iv) Ladder restructuring under new gravitational potential -/
```

## Source Excerpt

```lean
structure BasinFusion where
  /-- SMBHs merge to single remnant. -/
  anchor_merges : Bool := true
  /-- Code fuses via blueprint fusion. -/
  code_fuses : Bool := true
  /-- Carrier family is union of progenitors. -/
  carrier_union : Bool := true
  /-- Ladder restructured under new potential. -/
  ladder_restructured : Bool := true
  deriving Repr
```
