---
{
  "projection_kind": "taulib_declaration",
  "title": "ttm_nativity_check",
  "permalink": "/verify/taulib/docs/book-iii-computation-tower-machine/ttm-nativity-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.TowerMachine`.",
  "declaration_id": "TauLib.BookIII.Computation.TowerMachine::ttm_nativity_check",
  "declaration_slug": "ttm-nativity-check",
  "kind": "def",
  "name": "ttm_nativity_check",
  "module_name": "TauLib.BookIII.Computation.TowerMachine",
  "module_url": "/verify/taulib/docs/book-iii-computation-tower-machine/",
  "source_line_start": 108,
  "source_line_end": 131,
  "registry_ids": [
    "III.T30"
  ],
  "related_registry_items": [
    {
      "id": "III.T30",
      "title": "TTM τ-Nativity",
      "url": "/registry/object/III.T30/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L108-L131",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L108-L131",
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
- Source path: [`TauLib/BookIII/Computation/TowerMachine.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L108-L131)
- Source range: L108-L131
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T30` — TTM τ-Nativity

## Immediate Comment / Docstring

```lean
/-- [III.T30] TTM τ-nativity check: program IS τ-address. The machine's
    transition function is determined by the registers themselves (no
    external instruction tape). Code = data. -/
```

## Source Excerpt

```lean
def ttm_nativity_check (bound db : TauIdx) : Bool :=
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
        -- The code x determines the computation (symmetric init)
        let cfg := TTMConfig.mk 0 (x % pk) (x % pk) k
        let cfg' := ttm_step cfg
        -- Output is also a τ-address at same depth
        let native := cfg'.reg_a < pk && cfg'.reg_b < pk
        -- Asymmetric init: (x, 0) and (0, x) give different results
        let cfg_a := TTMConfig.mk 0 (x % pk) 0 k
        let cfg_b := TTMConfig.mk 0 0 (x % pk) k
        let cfg_a' := ttm_step cfg_a
        let cfg_b' := ttm_step cfg_b
        let asym_ok := cfg_a'.reg_a < pk && cfg_b'.reg_a < pk
        native && asym_ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
