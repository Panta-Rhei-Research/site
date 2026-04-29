---
{
  "projection_kind": "taulib_declaration",
  "title": "RefinementTower",
  "permalink": "/verify/taulib/docs/book-iv-arena-refinement-tower/refinement-tower/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Arena.RefinementTower`.",
  "declaration_id": "TauLib.BookIV.Arena.RefinementTower::RefinementTower",
  "declaration_slug": "refinement-tower",
  "kind": "structure",
  "name": "RefinementTower",
  "module_name": "TauLib.BookIV.Arena.RefinementTower",
  "module_url": "/verify/taulib/docs/book-iv-arena-refinement-tower/",
  "source_line_start": 47,
  "source_line_end": 51,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/RefinementTower.lean#L47-L51",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/RefinementTower.lean#L47-L51",
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
- Source path: [`TauLib/BookIV/Arena/RefinementTower.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/RefinementTower.lean#L47-L51)
- Source range: L47-L51
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D249` — Refinement Tower mathcalR

## Immediate Comment / Docstring

```lean
/-- [IV.D249] The refinement tower R: a sequence of levels ordered by depth.
    R = lim←_n (τ/τ_n) — the profinite inverse limit. -/
```

## Source Excerpt

```lean
structure RefinementTower where
  /-- Level accessor. -/
  level : Nat → TowerLevel
  /-- Levels are indexed consecutively starting at 1. -/
  level_depth : ∀ n : Nat, n > 0 → (level n).depth = n
```
