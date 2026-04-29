---
{
  "projection_kind": "taulib_declaration",
  "title": "e2_agent_check",
  "permalink": "/verify/taulib/docs/book-iii-computation-e2-agent/e2-agent-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.E2Agent`.",
  "declaration_id": "TauLib.BookIII.Computation.E2Agent::e2_agent_check",
  "declaration_slug": "e2-agent-check",
  "kind": "def",
  "name": "e2_agent_check",
  "module_name": "TauLib.BookIII.Computation.E2Agent",
  "module_url": "/verify/taulib/docs/book-iii-computation-e2-agent/",
  "source_line_start": 64,
  "source_line_end": 85,
  "registry_ids": [
    "III.D49"
  ],
  "related_registry_items": [
    {
      "id": "III.D49",
      "title": "E₂ Computational Agent",
      "url": "/registry/object/III.D49/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Agent.lean#L64-L85",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Agent.lean#L64-L85",
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
- Source path: [`TauLib/BookIII/Computation/E2Agent.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Agent.lean#L64-L85)
- Source range: L64-L85
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D49` — E₂ Computational Agent

## Immediate Comment / Docstring

```lean
/-- [III.D49] Agent well-formedness: code and decoder are valid addresses
    (within primorial range). -/
```

## Source Excerpt

```lean
def e2_agent_check (bound db : TauIdx) : Bool :=
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
        let agent := E2Agent.mk (c % pk) (d % pk) k
        -- Step output is valid (within range)
        let result := agent_step agent
        let valid := result < pk
        -- Orbit test: step(step(x)) is also valid (2-step closure)
        let agent2 := E2Agent.mk result (d % pk) k
        let result2 := agent_step agent2
        let orbit_ok := result2 < pk
        valid && orbit_ok && go c d (k + 1) (fuel - 1)
  termination_by fuel
```
