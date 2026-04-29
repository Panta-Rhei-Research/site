---
{
  "projection_kind": "taulib_declaration",
  "title": "PropagationOp",
  "permalink": "/verify/taulib/docs/book-iv-arena-actors-dynamics/propagation-op/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Arena.ActorsDynamics`.",
  "declaration_id": "TauLib.BookIV.Arena.ActorsDynamics::PropagationOp",
  "declaration_slug": "propagation-op",
  "kind": "structure",
  "name": "PropagationOp",
  "module_name": "TauLib.BookIV.Arena.ActorsDynamics",
  "module_url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/",
  "source_line_start": 147,
  "source_line_end": 152,
  "registry_ids": [
    "IV.D272"
  ],
  "related_registry_items": [
    {
      "id": "IV.D272",
      "title": "Propagation operator",
      "url": "/registry/object/IV.D272/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/ActorsDynamics.lean#L147-L152",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.ActorsDynamics",
        "url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/ActorsDynamics.lean#L147-L152",
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

- Module: [TauLib.BookIV.Arena.ActorsDynamics](/verify/taulib/docs/book-iv-arena-actors-dynamics/)
- Source path: [`TauLib/BookIV/Arena/ActorsDynamics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/ActorsDynamics.lean#L147-L152)
- Source range: L147-L152
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D272` — Propagation operator

## Immediate Comment / Docstring

```lean
/-- [IV.D272] Propagation operator: governs defect evolution in the arena.
    Fiber modes → quantum propagation; base modes → classical propagation. -/
```

## Source Excerpt

```lean
structure PropagationOp where
  /-- Operates on fiber (quantum) or base (classical). -/
  domain : CarrierType
  /-- Time evolution is unitary on fiber. -/
  unitary_on_fiber : Bool
  deriving Repr
```
