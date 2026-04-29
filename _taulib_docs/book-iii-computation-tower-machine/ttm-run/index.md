---
{
  "projection_kind": "taulib_declaration",
  "title": "ttm_run",
  "permalink": "/verify/taulib/docs/book-iii-computation-tower-machine/ttm-run/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.TowerMachine`.",
  "declaration_id": "TauLib.BookIII.Computation.TowerMachine::ttm_run",
  "declaration_slug": "ttm-run",
  "kind": "def",
  "name": "ttm_run",
  "module_name": "TauLib.BookIII.Computation.TowerMachine",
  "module_url": "/verify/taulib/docs/book-iii-computation-tower-machine/",
  "source_line_start": 68,
  "source_line_end": 74,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L68-L74",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L68-L74",
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
- Source path: [`TauLib/BookIII/Computation/TowerMachine.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L68-L74)
- Source range: L68-L74
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D51` — τ-Tower Machine

## Immediate Comment / Docstring

```lean
/-- [III.D51] TTM multi-step: run n steps from initial configuration. -/
```

## Source Excerpt

```lean
def ttm_run (cfg : TTMConfig) (n : TauIdx) : TTMConfig :=
  go cfg n
where
  go (c : TTMConfig) (fuel : Nat) : TTMConfig :=
    if fuel = 0 then c
    else go (ttm_step c) (fuel - 1)
  termination_by fuel
```
