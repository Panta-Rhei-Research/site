---
{
  "projection_kind": "taulib_declaration",
  "title": "cycle_detection_check",
  "permalink": "/verify/taulib/docs/book-iii-computation-e2-agent/cycle-detection-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.E2Agent`.",
  "declaration_id": "TauLib.BookIII.Computation.E2Agent::cycle_detection_check",
  "declaration_slug": "cycle-detection-check",
  "kind": "def",
  "name": "cycle_detection_check",
  "module_name": "TauLib.BookIII.Computation.E2Agent",
  "module_url": "/verify/taulib/docs/book-iii-computation-e2-agent/",
  "source_line_start": 121,
  "source_line_end": 138,
  "registry_ids": [
    "III.D50"
  ],
  "related_registry_items": [
    {
      "id": "III.D50",
      "title": "Operational Closure",
      "url": "/registry/object/III.D50/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Agent.lean#L121-L138",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.E2Agent",
        "url": "/verify/taulib/docs/book-iii-computation-e2-agent/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Agent.lean#L121-L138",
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

- Module: [TauLib.BookIII.Computation.E2Agent](/verify/taulib/docs/book-iii-computation-e2-agent/)
- Source path: [`TauLib/BookIII/Computation/E2Agent.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Agent.lean#L121-L138)
- Source range: L121-L138
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D50` — Operational Closure

## Immediate Comment / Docstring

```lean
/-- [III.D50] Cycle detection: agent iteration eventually returns to start
    (finite state space). -/
```

## Source Excerpt

```lean
def cycle_detection_check (bound db : TauIdx) : Bool :=
  go 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
where
  go (c d k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if c > bound then true
    else if d > bound then go (c + 1) 0 1 (fuel - 1)
    else if k > db then go c (d + 1) 1 (fuel - 1)
    else
      let pk := primorial k
      if pk == 0 then go c d (k + 1) (fuel - 1)
      else
        -- After at most pk steps, must return to start (pigeonhole)
        let start := c % pk
        let final := agent_iterate (E2Agent.mk start (d % pk) k) pk
        let cycled := final == start
        cycled && go c d (k + 1) (fuel - 1)
  termination_by fuel
```
