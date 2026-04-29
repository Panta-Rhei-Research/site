---
{
  "projection_kind": "taulib_declaration",
  "title": "SingleScaleDOF",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild-scale/single-scale-dof/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.TauSchwarzschildScale`.",
  "declaration_id": "TauLib.BookV.GravityField.TauSchwarzschildScale::SingleScaleDOF",
  "declaration_slug": "single-scale-dof",
  "kind": "structure",
  "name": "SingleScaleDOF",
  "module_name": "TauLib.BookV.GravityField.TauSchwarzschildScale",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild-scale/",
  "source_line_start": 54,
  "source_line_end": 67,
  "registry_ids": [
    "V.L4"
  ],
  "related_registry_items": [
    {
      "id": "V.L4",
      "title": "Single Scale Degree of Freedom",
      "url": "/registry/object/V.L4/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschildScale.lean#L54-L67",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TauSchwarzschildScale",
        "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild-scale/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschildScale.lean#L54-L67",
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

- Module: [TauLib.BookV.GravityField.TauSchwarzschildScale](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild-scale/)
- Source path: [`TauLib/BookV/GravityField/TauSchwarzschildScale.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschildScale.lean#L54-L67)
- Source range: L54-L67
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.L4` — Single Scale Degree of Freedom

## Immediate Comment / Docstring

```lean
/-- [V.L4] Single scale degree of freedom: τ-Schwarzschild has exactly
    one free scale parameter (linking mass M). All other quantities are
    determined by M through ι_τ.

    - Shape ratio r/R = ι_τ (fixed by axioms K0-K6)
    - Schwarzschild radius R = 2G_τ M
    - Inner radius r = ι_τ · R
    - QNM frequencies ∝ 1/R (outer) and 1/r (inner)
    - Echo times ∝ R/c and r/c

    The torus vacuum is a one-parameter family, not two-parameter. -/
```

## Source Excerpt

```lean
structure SingleScaleDOF where
  /-- Number of free scale parameters. -/
  free_params : Nat
  /-- Exactly one free parameter (M). -/
  params_eq : free_params = 1
  /-- Torus parameters (R, r). -/
  torus_params : Nat := 2
  /-- Shape constraints (r/R = ι_τ). -/
  shape_constraints : Nat := 1
  /-- Shape ratio is fixed (not free). -/
  shape_fixed : Bool := true
  /-- All derived quantities determined by M. -/
  all_determined : Bool := true
  deriving Repr
```
