---
{
  "projection_kind": "taulib_declaration",
  "title": "NFEinsteinIteration",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/nfeinstein-iteration/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.NonlinearEinstein`.",
  "declaration_id": "TauLib.BookV.GravityField.NonlinearEinstein::NFEinsteinIteration",
  "declaration_slug": "nfeinstein-iteration",
  "kind": "structure",
  "name": "NFEinsteinIteration",
  "module_name": "TauLib.BookV.GravityField.NonlinearEinstein",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/",
  "source_line_start": 124,
  "source_line_end": 133,
  "registry_ids": [
    "V.D55"
  ],
  "related_registry_items": [
    {
      "id": "V.D55",
      "title": "tau-NF Einstein iteration",
      "url": "/registry/object/V.D55/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L124-L133",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.NonlinearEinstein",
        "url": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L124-L133",
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

- Module: [TauLib.BookV.GravityField.NonlinearEinstein](/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/)
- Source path: [`TauLib/BookV/GravityField/NonlinearEinstein.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L124-L133)
- Source range: L124-L133
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D55` — tau-NF Einstein iteration

## Immediate Comment / Docstring

```lean
/-- [V.D55] Normal-form Einstein iteration: iterative procedure
    solving the full nonlinear τ-Einstein equation.

    The iteration starts from an initial guess S₀ and converges
    to the unique fixed point S_ω with minimal cocycle defect.

    Properties:
    - Monotone defect decrease at each step
    - Convergence to unique fixed point
    - Fixed point has zero cocycle defect
    - Solution is the minimal-defect configuration -/
```

## Source Excerpt

```lean
structure NFEinsteinIteration where
  /-- Current iteration depth (number of NF steps). -/
  depth : Nat
  /-- Cocycle defect at the current step. -/
  current_defect : CocycleDefect
  /-- Whether the iteration has converged (defect = 0). -/
  converged : Bool
  /-- If converged, defect must be zero. -/
  convergence_check : converged = true → current_defect.defect_numer = 0
  deriving Repr
```
