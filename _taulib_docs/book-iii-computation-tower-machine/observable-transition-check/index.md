---
{
  "projection_kind": "taulib_declaration",
  "title": "observable_transition_check",
  "permalink": "/verify/taulib/docs/book-iii-computation-tower-machine/observable-transition-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.TowerMachine`.",
  "declaration_id": "TauLib.BookIII.Computation.TowerMachine::observable_transition_check",
  "declaration_slug": "observable-transition-check",
  "kind": "def",
  "name": "observable_transition_check",
  "module_name": "TauLib.BookIII.Computation.TowerMachine",
  "module_url": "/verify/taulib/docs/book-iii-computation-tower-machine/",
  "source_line_start": 143,
  "source_line_end": 165,
  "registry_ids": [
    "III.D52"
  ],
  "related_registry_items": [
    {
      "id": "III.D52",
      "title": "Observable Transition",
      "url": "/registry/object/III.D52/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L143-L165",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L143-L165",
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
- Source path: [`TauLib/BookIII/Computation/TowerMachine.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L143-L165)
- Source range: L143-L165
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D52` — Observable Transition

## Immediate Comment / Docstring

```lean
/-- [III.D52] Observable transition check: the observable state at each
    step is bounded by the Cook-Levin width. -/
```

## Source Excerpt

```lean
def observable_transition_check (bound db : TauIdx) : Bool :=
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
        let cfg := TTMConfig.mk 0 (x % pk) 1 k
        -- Run 4 steps (one full cycle)
        let cfg' := ttm_run cfg 4
        -- State is bounded
        let state_ok := cfg'.state < 4
        -- Registers are bounded by primorial
        let reg_ok := cfg'.reg_a < pk && cfg'.reg_b < pk
        -- Intermediate verification: after 2 steps, state and registers valid
        let cfg2 := ttm_run cfg 2
        let mid_ok := cfg2.state < 4 && cfg2.reg_a < pk && cfg2.reg_b < pk
        state_ok && reg_ok && mid_ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
