---
{
  "projection_kind": "taulib_declaration",
  "title": "TowerLevel",
  "permalink": "/verify/taulib/docs/book-iv-arena-refinement-tower/tower-level/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Arena.RefinementTower`.",
  "declaration_id": "TauLib.BookIV.Arena.RefinementTower::TowerLevel",
  "declaration_slug": "tower-level",
  "kind": "structure",
  "name": "TowerLevel",
  "module_name": "TauLib.BookIV.Arena.RefinementTower",
  "module_url": "/verify/taulib/docs/book-iv-arena-refinement-tower/",
  "source_line_start": 38,
  "source_line_end": 43,
  "registry_ids": [
    "IV.D249"
  ],
  "related_registry_items": [
    {
      "id": "IV.D249",
      "title": "Refinement Tower mathcalR",
      "url": "/registry/object/IV.D249/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/RefinementTower.lean#L38-L43",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.RefinementTower",
        "url": "/verify/taulib/docs/book-iv-arena-refinement-tower/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/RefinementTower.lean#L38-L43",
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

- Module: [TauLib.BookIV.Arena.RefinementTower](/verify/taulib/docs/book-iv-arena-refinement-tower/)
- Source path: [`TauLib/BookIV/Arena/RefinementTower.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/RefinementTower.lean#L38-L43)
- Source range: L38-L43
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D249` — Refinement Tower mathcalR

## Immediate Comment / Docstring

```lean
/-- [IV.D249] A level in the refinement tower: quotient at depth n.
    Each level captures the observable physics up to that resolution. -/
```

## Source Excerpt

```lean
structure TowerLevel where
  /-- Depth index (positive natural). -/
  depth : Nat
  /-- Depth is positive (meaningful orbit level). -/
  depth_pos : depth > 0
  deriving Repr
```
