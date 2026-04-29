---
{
  "projection_kind": "taulib_declaration",
  "title": "LinearizedEinstein",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-linear-einstein/linearized-einstein/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.LinearEinstein`.",
  "declaration_id": "TauLib.BookV.GravityField.LinearEinstein::LinearizedEinstein",
  "declaration_slug": "linearized-einstein",
  "kind": "structure",
  "name": "LinearizedEinstein",
  "module_name": "TauLib.BookV.GravityField.LinearEinstein",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-linear-einstein/",
  "source_line_start": 82,
  "source_line_end": 93,
  "registry_ids": [
    "V.D52"
  ],
  "related_registry_items": [
    {
      "id": "V.D52",
      "title": "Linearized tau-Einstein equation",
      "url": "/registry/object/V.D52/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L82-L93",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.LinearEinstein",
        "url": "/verify/taulib/docs/book-v-gravity-field-linear-einstein/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L82-L93",
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

- Module: [TauLib.BookV.GravityField.LinearEinstein](/verify/taulib/docs/book-v-gravity-field-linear-einstein/)
- Source path: [`TauLib/BookV/GravityField/LinearEinstein.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean#L82-L93)
- Source range: L82-L93
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D52` — Linearized tau-Einstein equation

## Immediate Comment / Docstring

```lean
/-- [V.D52] Linearized τ-Einstein equation: weak-field approximation
    of R^H = κ_τ · T^mat.

    In the weak-field regime, the curvature character is small
    and the equation linearizes. This is the structural origin
    of Newtonian gravity and the classical GR tests.

    The perturbation order tracks the approximation level:
    - order 0: flat (Minkowski)
    - order 1: Newtonian + classical tests
    - order 2+: post-Newtonian corrections -/
```

## Source Excerpt

```lean
structure LinearizedEinstein where
  /-- Perturbation order (1 = first order, 2 = second order, etc.). -/
  order : Nat
  /-- Order must be at least 1 (order 0 = flat, trivial). -/
  order_pos : order > 0
  /-- The gravitational coupling κ_τ used. -/
  kappa : GravitationalCoupling
  /-- Chart dimension (must be 4). -/
  chart_dim : Nat
  /-- Chart is 4-dimensional. -/
  dim_is_four : chart_dim = 4
  deriving Repr
```
