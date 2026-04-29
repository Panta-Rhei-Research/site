---
{
  "projection_kind": "taulib_declaration",
  "title": "hartogs_flow_step",
  "permalink": "/verify/taulib/docs/book-iii-physics-hartogs-flow/hartogs-flow-step/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.HartogsFlow`.",
  "declaration_id": "TauLib.BookIII.Physics.HartogsFlow::hartogs_flow_step",
  "declaration_slug": "hartogs-flow-step",
  "kind": "def",
  "name": "hartogs_flow_step",
  "module_name": "TauLib.BookIII.Physics.HartogsFlow",
  "module_url": "/verify/taulib/docs/book-iii-physics-hartogs-flow/",
  "source_line_start": 45,
  "source_line_end": 55,
  "registry_ids": [
    "III.D40"
  ],
  "related_registry_items": [
    {
      "id": "III.D40",
      "title": "Hartogs Flow Operator",
      "url": "/registry/object/III.D40/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L45-L55",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.HartogsFlow",
        "url": "/verify/taulib/docs/book-iii-physics-hartogs-flow/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L45-L55",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookIII.Physics.HartogsFlow](/verify/taulib/docs/book-iii-physics-hartogs-flow/)
- Source path: [`TauLib/BookIII/Physics/HartogsFlow.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L45-L55)
- Source range: L45-L55
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D40` — Hartogs Flow Operator

## Immediate Comment / Docstring

```lean
/-- [III.D40] Hartogs flow step: advance fluid data from level k to k+1.
    Each cylinder's value at level k is lifted to level k+1 by CRT
    reconstruction, then re-decomposed into BNF at the new level.
    The flow preserves sector structure while refining resolution. -/
```

## Source Excerpt

```lean
def hartogs_flow_step (x k : TauIdx) : BoundaryNF :=
  let pk := primorial k
  let pk1 := primorial (k + 1)
  if pk == 0 || pk1 == 0 then ⟨0, 0, 0, k + 1⟩
  else
    -- Current value at level k
    let xk := x % pk
    -- Lift to level k+1: same residue, new depth
    let xk1 := xk % pk1
    -- Re-decompose at level k+1
    boundary_normal_form xk1 (k + 1)
```
