---
{
  "projection_kind": "taulib_declaration",
  "title": "TauEulerFlow",
  "permalink": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/tau-euler-flow/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.FluidRegimes`.",
  "declaration_id": "TauLib.BookIV.ManyBody.FluidRegimes::TauEulerFlow",
  "declaration_slug": "tau-euler-flow",
  "kind": "structure",
  "name": "TauEulerFlow",
  "module_name": "TauLib.BookIV.ManyBody.FluidRegimes",
  "module_url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/",
  "source_line_start": 64,
  "source_line_end": 77,
  "registry_ids": [
    "IV.D231"
  ],
  "related_registry_items": [
    {
      "id": "IV.D231",
      "title": "tau-Euler flow",
      "url": "/registry/object/IV.D231/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L64-L77",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L64-L77",
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
- Source path: [`TauLib/BookIV/ManyBody/FluidRegimes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L64-L77)
- Source range: L64-L77
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D231` — tau-Euler flow

## Immediate Comment / Docstring

```lean
/-- [IV.D231] A tau-Euler flow is a sequence of tau-admissible configurations
    {d_n} satisfying: mobility bound mu(d_n) <= mu_crit, budget conservation
    mu + nu + kappa + theta = const, and Kelvin invariance of circulation.

    This is the tau-native formulation of incompressible inviscid flow. -/
```

## Source Excerpt

```lean
structure TauEulerFlow where
  /-- Number of bounded tuple components (mu, nu, kappa, theta all bounded). -/
  n_bounded_components : Nat := 4
  /-- Number of conservation laws (budget conservation). -/
  n_conservation_laws : Nat := 1
  /-- Number of circulation invariants (Kelvin). -/
  n_invariants : Nat := 1
  /-- Compressibility degree (kappa = 0 means incompressible). -/
  kappa_degree : Nat := 0
  /-- Number of primorial stages computed. -/
  stages : Nat
  /-- All four tuple components are bounded. -/
  all_bounded : n_bounded_components = 4
  deriving Repr
```
