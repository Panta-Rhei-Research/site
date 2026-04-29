---
{
  "projection_kind": "taulib_declaration",
  "title": "UniversalOrderParameter",
  "permalink": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/universal-order-parameter/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.FluidRegimes`.",
  "declaration_id": "TauLib.BookIV.ManyBody.FluidRegimes::UniversalOrderParameter",
  "declaration_slug": "universal-order-parameter",
  "kind": "structure",
  "name": "UniversalOrderParameter",
  "module_name": "TauLib.BookIV.ManyBody.FluidRegimes",
  "module_url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/",
  "source_line_start": 368,
  "source_line_end": 379,
  "registry_ids": [
    "IV.P142"
  ],
  "related_registry_items": [
    {
      "id": "IV.P142",
      "title": "Defect tuple as universal order parameter",
      "url": "/registry/object/IV.P142/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L368-L379",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.FluidRegimes",
        "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L368-L379",
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

- Module: [TauLib.BookIV.ManyBody.FluidRegimes](/verify/taulib/docs/book-iv-many-body-fluid-regimes/)
- Source path: [`TauLib/BookIV/ManyBody/FluidRegimes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L368-L379)
- Source range: L368-L379
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P142` — Defect tuple as universal order parameter

## Immediate Comment / Docstring

```lean
/-- [IV.P142] The defect tuple D = (mu, nu, kappa, theta) is simultaneously
    the state variable and the universal order parameter for ALL phase
    transitions. Every transition corresponds to an inequality crossing in D.

    This unifies: Landau order parameter, Ginzburg-Landau functional,
    Wilson-Fisher fixed points — all are readout-level descriptions of
    defect-tuple geometry near regime boundaries. -/
```

## Source Excerpt

```lean
structure UniversalOrderParameter where
  /-- Number of frameworks unified (3: Landau, GL, WF). -/
  n_unified_frameworks : Nat := 3
  /-- Number of components. -/
  num_components : Nat := 4
  /-- Unifies: Landau, GL, WF. -/
  unifies : List String := ["Landau", "Ginzburg-Landau", "Wilson-Fisher"]
  /-- Number of transition mechanisms (1 = inequality crossing). -/
  n_transition_mechanisms : Nat := 1
  /-- Unification count matches framework list. -/
  unification_consistent : n_unified_frameworks = 3
  deriving Repr
```
