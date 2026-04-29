---
{
  "projection_kind": "taulib_declaration",
  "title": "ProfiniteLimit",
  "permalink": "/verify/taulib/docs/book-iv-arena-refinement-tower/profinite-limit/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Arena.RefinementTower`.",
  "declaration_id": "TauLib.BookIV.Arena.RefinementTower::ProfiniteLimit",
  "declaration_slug": "profinite-limit",
  "kind": "structure",
  "name": "ProfiniteLimit",
  "module_name": "TauLib.BookIV.Arena.RefinementTower",
  "module_url": "/verify/taulib/docs/book-iv-arena-refinement-tower/",
  "source_line_start": 66,
  "source_line_end": 72,
  "registry_ids": [
    "IV.D250"
  ],
  "related_registry_items": [
    {
      "id": "IV.D250",
      "title": "Profinite Limit hatalpha",
      "url": "/registry/object/IV.D250/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/RefinementTower.lean#L66-L72",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/RefinementTower.lean#L66-L72",
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
- Source path: [`TauLib/BookIV/Arena/RefinementTower.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/RefinementTower.lean#L66-L72)
- Source range: L66-L72
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D250` — Profinite Limit hatalpha

## Immediate Comment / Docstring

```lean
/-- [IV.D250] The profinite limit α̂ = lim←_n α_n: completion of
    the α-orbit providing the temporal substrate. Structurally,
    α̂ is the sequence of all orbit levels. -/
```

## Source Excerpt

```lean
structure ProfiniteLimit where
  /-- The generating generator (always α for temporal). -/
  seed : Generator
  /-- Seed is alpha. -/
  seed_is_alpha : seed = .alpha
  /-- The tower providing the levels. -/
  tower : RefinementTower
```
