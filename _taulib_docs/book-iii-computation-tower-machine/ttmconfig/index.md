---
{
  "projection_kind": "taulib_declaration",
  "title": "TTMConfig",
  "permalink": "/verify/taulib/docs/book-iii-computation-tower-machine/ttmconfig/",
  "summary_short": "`structure` declaration in `TauLib.BookIII.Computation.TowerMachine`.",
  "declaration_id": "TauLib.BookIII.Computation.TowerMachine::TTMConfig",
  "declaration_slug": "ttmconfig",
  "kind": "structure",
  "name": "TTMConfig",
  "module_name": "TauLib.BookIII.Computation.TowerMachine",
  "module_url": "/verify/taulib/docs/book-iii-computation-tower-machine/",
  "source_line_start": 43,
  "source_line_end": 48,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L43-L48",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L43-L48",
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

- Module: [TauLib.BookIII.Computation.TowerMachine](/verify/taulib/docs/book-iii-computation-tower-machine/)
- Source path: [`TauLib/BookIII/Computation/TowerMachine.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L43-L48)
- Source range: L43-L48
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `III.D51` — τ-Tower Machine

## Immediate Comment / Docstring

```lean
/-- [III.D51] TTM configuration at E₂ level: state + register values at
    primorial depth k. The registers hold τ-addresses. -/
```

## Source Excerpt

```lean
structure TTMConfig where
  state : TauIdx        -- current state (< num_states)
  reg_a : TauIdx        -- register A value
  reg_b : TauIdx        -- register B value
  depth : TauIdx        -- primorial depth of operation
  deriving Repr, DecidableEq, BEq
```
