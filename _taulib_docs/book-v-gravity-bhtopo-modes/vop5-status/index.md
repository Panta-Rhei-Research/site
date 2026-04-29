---
{
  "projection_kind": "taulib_declaration",
  "title": "VOP5Status",
  "permalink": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/vop5-status/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Gravity.BHTopoModes`.",
  "declaration_id": "TauLib.BookV.Gravity.BHTopoModes::VOP5Status",
  "declaration_slug": "vop5-status",
  "kind": "structure",
  "name": "VOP5Status",
  "module_name": "TauLib.BookV.Gravity.BHTopoModes",
  "module_url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/",
  "source_line_start": 453,
  "source_line_end": 462,
  "registry_ids": [
    "V.R380"
  ],
  "related_registry_items": [
    {
      "id": "V.R380",
      "title": "V.OP5 Status: SOLVED via Sprint 7E Observational Suite",
      "url": "/registry/object/V.R380/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L453-L462",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.BHTopoModes",
        "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L453-L462",
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

- Module: [TauLib.BookV.Gravity.BHTopoModes](/verify/taulib/docs/book-v-gravity-bhtopo-modes/)
- Source path: [`TauLib/BookV/Gravity/BHTopoModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L453-L462)
- Source range: L453-L462
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.R380` — V.OP5 Status: SOLVED via Sprint 7E Observational Suite

## Immediate Comment / Docstring

```lean
/-- [V.R380] Structure capturing V.OP5 solution status. -/
```

## Source Excerpt

```lean
structure VOP5Status where
  /-- Number of independent observational channels. -/
  n_observational_channels : Nat := 3
  /-- Number of input constants (just ι_τ). -/
  n_input_constants : Nat := 1
  /-- Number of independent cross-checks (entropy ratio). -/
  n_cross_checks : Nat := 1
  /-- Number of free parameters. -/
  free_parameters : Nat := 0
  deriving Repr
```
