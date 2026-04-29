---
{
  "projection_kind": "taulib_declaration",
  "title": "subsystem_horizon",
  "permalink": "/verify/taulib/docs/book-iv-arena-refinement-tower/subsystem-horizon/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Arena.RefinementTower`.",
  "declaration_id": "TauLib.BookIV.Arena.RefinementTower::subsystem_horizon",
  "declaration_slug": "subsystem-horizon",
  "kind": "theorem",
  "name": "subsystem_horizon",
  "module_name": "TauLib.BookIV.Arena.RefinementTower",
  "module_url": "/verify/taulib/docs/book-iv-arena-refinement-tower/",
  "source_line_start": 87,
  "source_line_end": 87,
  "registry_ids": [
    "IV.P147"
  ],
  "related_registry_items": [
    {
      "id": "IV.P147",
      "title": "Subsystem Horizon",
      "url": "/registry/object/IV.P147/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/RefinementTower.lean#L87-L87",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/RefinementTower.lean#L87-L87",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookIV/Arena/RefinementTower.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/RefinementTower.lean#L87-L87)
- Source range: L87-L87
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P147` — Subsystem Horizon

## Immediate Comment / Docstring

```lean
/-- [IV.P147] Subsystem horizon: every finite subsystem can only
    observe finitely many orbit levels. The profinite limit captures all.
    Formalized as: for any finite bound B, there exist levels beyond B. -/
```

## Source Excerpt

```lean
theorem subsystem_horizon (B : Nat) : ∃ n : Nat, n > B := ⟨B + 1, by omega⟩
```
