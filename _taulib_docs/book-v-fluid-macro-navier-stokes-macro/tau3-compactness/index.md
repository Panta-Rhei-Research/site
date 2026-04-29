---
{
  "projection_kind": "taulib_declaration",
  "title": "Tau3Compactness",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/tau3-compactness/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.NavierStokesMacro`.",
  "declaration_id": "TauLib.BookV.FluidMacro.NavierStokesMacro::Tau3Compactness",
  "declaration_slug": "tau3-compactness",
  "kind": "structure",
  "name": "Tau3Compactness",
  "module_name": "TauLib.BookV.FluidMacro.NavierStokesMacro",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/",
  "source_line_start": 120,
  "source_line_end": 132,
  "registry_ids": [
    "V.P42"
  ],
  "related_registry_items": [
    {
      "id": "V.P42",
      "title": "Compactness of tau^3",
      "url": "/registry/object/V.P42/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L120-L132",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.NavierStokesMacro",
        "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L120-L132",
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

- Module: [TauLib.BookV.FluidMacro.NavierStokesMacro](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/)
- Source path: [`TauLib/BookV/FluidMacro/NavierStokesMacro.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L120-L132)
- Source range: L120-L132
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P42` — Compactness of tau^3

## Immediate Comment / Docstring

```lean
/-- [V.P42] Compactness of τ³: the fibered product τ³ = τ¹ ×_f T² is
    compact in the profinite topology.

    Consequences:
    - Every continuous function on τ³ is bounded
    - Every sequence of τ-admissible configurations has convergent subsequence
    - All defect-tuple components are bounded -/
```

## Source Excerpt

```lean
structure Tau3Compactness where
  /-- Upper bound on mobility component. -/
  mobility_bound : Nat
  /-- Upper bound on vorticity component. -/
  vorticity_bound : Nat
  /-- Upper bound on compression component. -/
  compression_bound : Nat
  /-- Upper bound on topological component. -/
  topological_bound : Nat
  /-- All bounds are positive. -/
  bounds_positive : mobility_bound > 0 ∧ vorticity_bound > 0 ∧
    compression_bound > 0 ∧ topological_bound > 0
  deriving Repr
```
