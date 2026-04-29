---
{
  "projection_kind": "taulib_declaration",
  "title": "flow_stabilization_check",
  "permalink": "/verify/taulib/docs/book-iii-physics-hartogs-flow/flow-stabilization-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.HartogsFlow`.",
  "declaration_id": "TauLib.BookIII.Physics.HartogsFlow::flow_stabilization_check",
  "declaration_slug": "flow-stabilization-check",
  "kind": "def",
  "name": "flow_stabilization_check",
  "module_name": "TauLib.BookIII.Physics.HartogsFlow",
  "module_url": "/verify/taulib/docs/book-iii-physics-hartogs-flow/",
  "source_line_start": 114,
  "source_line_end": 130,
  "registry_ids": [
    "III.T24"
  ],
  "related_registry_items": [
    {
      "id": "III.T24",
      "title": "Hartogs Flow Theorem",
      "url": "/registry/object/III.T24/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L114-L130",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L114-L130",
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
- Source path: [`TauLib/BookIII/Physics/HartogsFlow.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L114-L130)
- Source range: L114-L130
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T24` — Hartogs Flow Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T24] Flow stabilization check: at each level k, the flow does
    not introduce new defects. The defect functional stays at zero
    across all levels (canonical BNF is a fixed point of the flow). -/
```

## Source Excerpt

```lean
def flow_stabilization_check (bound db : TauIdx) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let pk := primorial k
      if pk == 0 then go x (k + 1) (fuel - 1)
      else
        -- The canonical assignment is a fixed point
        let nf := boundary_normal_form (x % pk) k
        let sum := (nf.b_part + nf.c_part + nf.x_part) % pk
        -- No defect: sum = original
        sum == x % pk && go x (k + 1) (fuel - 1)
  termination_by fuel
```
