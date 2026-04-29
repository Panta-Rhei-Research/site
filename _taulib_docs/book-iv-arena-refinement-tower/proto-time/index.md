---
{
  "projection_kind": "taulib_declaration",
  "title": "ProtoTime",
  "permalink": "/verify/taulib/docs/book-iv-arena-refinement-tower/proto-time/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Arena.RefinementTower`.",
  "declaration_id": "TauLib.BookIV.Arena.RefinementTower::ProtoTime",
  "declaration_slug": "proto-time",
  "kind": "structure",
  "name": "ProtoTime",
  "module_name": "TauLib.BookIV.Arena.RefinementTower",
  "module_url": "/verify/taulib/docs/book-iv-arena-refinement-tower/",
  "source_line_start": 96,
  "source_line_end": 108,
  "registry_ids": [
    "IV.D251"
  ],
  "related_registry_items": [
    {
      "id": "IV.D251",
      "title": "Proto-Time t_p",
      "url": "/registry/object/IV.D251/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/RefinementTower.lean#L96-L108",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/RefinementTower.lean#L96-L108",
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
- Source path: [`TauLib/BookIV/Arena/RefinementTower.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/RefinementTower.lean#L96-L108)
- Source range: L96-L108
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D251` — Proto-Time t_p

## Immediate Comment / Docstring

```lean
/-- [IV.D251] Proto-time: the ordering on α-orbit levels that defines
    temporal succession before any metric. Earlier levels (smaller depth)
    precede later levels (larger depth). -/
```

## Source Excerpt

```lean
structure ProtoTime where
  /-- Current depth in the tower. -/
  tick : Nat
  /-- Tick is positive. -/
  tick_pos : tick > 0
  deriving Repr, DecidableEq

/-- Proto-time ordering: earlier ticks precede later ticks. -/
instance : LT ProtoTime where
  lt a b := a.tick < b.tick

instance : DecidableRel (α := ProtoTime) (· < ·) :=
  fun a b => inferInstanceAs (Decidable (a.tick < b.tick))
```
