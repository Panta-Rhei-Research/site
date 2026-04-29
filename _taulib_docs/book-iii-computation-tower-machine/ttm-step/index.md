---
{
  "projection_kind": "taulib_declaration",
  "title": "ttm_step",
  "permalink": "/verify/taulib/docs/book-iii-computation-tower-machine/ttm-step/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.TowerMachine`.",
  "declaration_id": "TauLib.BookIII.Computation.TowerMachine::ttm_step",
  "declaration_slug": "ttm-step",
  "kind": "def",
  "name": "ttm_step",
  "module_name": "TauLib.BookIII.Computation.TowerMachine",
  "module_url": "/verify/taulib/docs/book-iii-computation-tower-machine/",
  "source_line_start": 52,
  "source_line_end": 65,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L52-L65",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L52-L65",
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
- Source path: [`TauLib/BookIII/Computation/TowerMachine.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L52-L65)
- Source range: L52-L65
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D51` — τ-Tower Machine

## Immediate Comment / Docstring

```lean
/-- [III.D51] TTM transition: one step of computation at primorial level k.
    The transition is a modular operation determined by the state. -/
```

## Source Excerpt

```lean
def ttm_step (cfg : TTMConfig) : TTMConfig :=
  let pk := primorial cfg.depth
  if pk == 0 then cfg
  else
    -- Transition rule based on state (mod 4 cycle)
    match cfg.state % 4 with
    | 0 => -- Add registers
      ⟨(cfg.state + 1) % 4, (cfg.reg_a + cfg.reg_b) % pk, cfg.reg_b, cfg.depth⟩
    | 1 => -- Multiply registers
      ⟨(cfg.state + 1) % 4, (cfg.reg_a * cfg.reg_b) % pk, cfg.reg_b, cfg.depth⟩
    | 2 => -- Swap registers
      ⟨(cfg.state + 1) % 4, cfg.reg_b, cfg.reg_a, cfg.depth⟩
    | _ => -- Reset to start
      ⟨0, cfg.reg_a, cfg.reg_b, cfg.depth⟩
```
