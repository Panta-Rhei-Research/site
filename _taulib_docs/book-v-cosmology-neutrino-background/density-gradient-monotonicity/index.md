---
{
  "projection_kind": "taulib_declaration",
  "title": "DensityGradientMonotonicity",
  "permalink": "/verify/taulib/docs/book-v-cosmology-neutrino-background/density-gradient-monotonicity/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.NeutrinoBackground`.",
  "declaration_id": "TauLib.BookV.Cosmology.NeutrinoBackground::DensityGradientMonotonicity",
  "declaration_slug": "density-gradient-monotonicity",
  "kind": "structure",
  "name": "DensityGradientMonotonicity",
  "module_name": "TauLib.BookV.Cosmology.NeutrinoBackground",
  "module_url": "/verify/taulib/docs/book-v-cosmology-neutrino-background/",
  "source_line_start": 91,
  "source_line_end": 102,
  "registry_ids": [
    "V.T152"
  ],
  "related_registry_items": [
    {
      "id": "V.T152",
      "title": "Density Gradient Monotonicity",
      "url": "/registry/object/V.T152/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L91-L102",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.NeutrinoBackground",
        "url": "/verify/taulib/docs/book-v-cosmology-neutrino-background/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L91-L102",
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

- Module: [TauLib.BookV.Cosmology.NeutrinoBackground](/verify/taulib/docs/book-v-cosmology-neutrino-background/)
- Source path: [`TauLib/BookV/Cosmology/NeutrinoBackground.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L91-L102)
- Source range: L91-L102
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T152` — Density Gradient Monotonicity

## Immediate Comment / Docstring

```lean
/-- [V.T152] Density gradient monotonicity: after neutrino decoupling,
    the CνB energy density decreases monotonically.

    - Follows from directed α-orbit (temporal monotonicity)
    - ρ_ν ∝ a⁻⁴ (relativistic) transitioning to ρ_ν ∝ a⁻³ (non-rel)
    - Monotonicity is structural (not contingent on initial conditions)
    - Gradient ∂ρ_ν/∂t < 0 for all t > t_dec -/
```

## Source Excerpt

```lean
structure DensityGradientMonotonicity where
  /-- Density decreases after decoupling. -/
  density_decreasing : Bool := true
  /-- Follows from directed α-orbit. -/
  from_alpha_orbit : Bool := true
  /-- Structural (not initial-condition dependent). -/
  is_structural : Bool := true
  /-- Relativistic scaling exponent (ρ ∝ a⁻⁴). -/
  relativistic_exp : Nat := 4
  /-- Non-relativistic scaling exponent (ρ ∝ a⁻³). -/
  nonrelativistic_exp : Nat := 3
  deriving Repr
```
