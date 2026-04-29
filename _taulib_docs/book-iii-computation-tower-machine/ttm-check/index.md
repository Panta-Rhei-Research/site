---
{
  "projection_kind": "taulib_declaration",
  "title": "ttm_check",
  "permalink": "/verify/taulib/docs/book-iii-computation-tower-machine/ttm-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.TowerMachine`.",
  "declaration_id": "TauLib.BookIII.Computation.TowerMachine::ttm_check",
  "declaration_slug": "ttm-check",
  "kind": "def",
  "name": "ttm_check",
  "module_name": "TauLib.BookIII.Computation.TowerMachine",
  "module_url": "/verify/taulib/docs/book-iii-computation-tower-machine/",
  "source_line_start": 78,
  "source_line_end": 99,
  "registry_ids": [
    "III.D51"
  ],
  "related_registry_items": [
    {
      "id": "III.D51",
      "title": "τ-Tower Machine",
      "url": "/registry/object/III.D51/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L78-L99",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.TowerMachine",
        "url": "/verify/taulib/docs/book-iii-computation-tower-machine/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L78-L99",
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

- Module: [TauLib.BookIII.Computation.TowerMachine](/verify/taulib/docs/book-iii-computation-tower-machine/)
- Source path: [`TauLib/BookIII/Computation/TowerMachine.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L78-L99)
- Source range: L78-L99
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D51` — τ-Tower Machine

## Immediate Comment / Docstring

```lean
/-- [III.D51] TTM check: transitions preserve validity (registers stay
    within primorial range). -/
```

## Source Excerpt

```lean
def ttm_check (bound db : TauIdx) : Bool :=
  go 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
where
  go (a b k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if a > bound then true
    else if b > bound then go (a + 1) 0 1 (fuel - 1)
    else if k > db then go a (b + 1) 1 (fuel - 1)
    else
      let pk := primorial k
      if pk == 0 then go a b (k + 1) (fuel - 1)
      else
        let cfg := TTMConfig.mk 0 (a % pk) (b % pk) k
        let cfg' := ttm_step cfg
        -- Registers stay in range
        let valid := cfg'.reg_a < pk && cfg'.reg_b < pk
        -- Boundary wraparound: test at pk-1 edge
        let cfg_edge := TTMConfig.mk 0 (pk - 1) (pk - 1) k
        let cfg_edge' := ttm_step cfg_edge
        let edge_ok := cfg_edge'.reg_a < pk && cfg_edge'.reg_b < pk
        valid && edge_ok && go a b (k + 1) (fuel - 1)
  termination_by fuel
```
