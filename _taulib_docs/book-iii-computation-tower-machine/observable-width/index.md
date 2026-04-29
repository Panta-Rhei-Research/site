---
{
  "projection_kind": "taulib_declaration",
  "title": "observable_width",
  "permalink": "/verify/taulib/docs/book-iii-computation-tower-machine/observable-width/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.TowerMachine`.",
  "declaration_id": "TauLib.BookIII.Computation.TowerMachine::observable_width",
  "declaration_slug": "observable-width",
  "kind": "def",
  "name": "observable_width",
  "module_name": "TauLib.BookIII.Computation.TowerMachine",
  "module_url": "/verify/taulib/docs/book-iii-computation-tower-machine/",
  "source_line_start": 139,
  "source_line_end": 139,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L139-L139",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L139-L139",
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
- Source path: [`TauLib/BookIII/Computation/TowerMachine.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L139-L139)
- Source range: L139-L139
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D52` — Observable Transition

## Immediate Comment / Docstring

```lean
/-- [III.D52] Observable width: the number of register bits visible at
    each step. W = 1 + m where m = number of registers (here m = 2). -/
```

## Source Excerpt

```lean
def observable_width : TauIdx := 3  -- 1 state + 2 registers
```
