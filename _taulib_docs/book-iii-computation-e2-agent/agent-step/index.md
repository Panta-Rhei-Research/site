---
{
  "projection_kind": "taulib_declaration",
  "title": "agent_step",
  "permalink": "/verify/taulib/docs/book-iii-computation-e2-agent/agent-step/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.E2Agent`.",
  "declaration_id": "TauLib.BookIII.Computation.E2Agent::agent_step",
  "declaration_slug": "agent-step",
  "kind": "def",
  "name": "agent_step",
  "module_name": "TauLib.BookIII.Computation.E2Agent",
  "module_url": "/verify/taulib/docs/book-iii-computation-e2-agent/",
  "source_line_start": 45,
  "source_line_end": 48,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Agent.lean#L45-L48",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Agent.lean#L45-L48",
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
- Source path: [`TauLib/BookIII/Computation/E2Agent.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Agent.lean#L45-L48)
- Source range: L45-L48
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D49` — E₂ Computational Agent

## Immediate Comment / Docstring

```lean
/-- [III.D49] Apply the decoder to the code: D(C) at primorial level k.
    The decoder operates by modular arithmetic on the code. -/
```

## Source Excerpt

```lean
def agent_step (a : E2Agent) : TauIdx :=
  let pk := primorial a.depth
  if pk == 0 then 0
  else (a.code + a.decoder) % pk
```
