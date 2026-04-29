---
{
  "projection_kind": "taulib_declaration",
  "title": "SheLevequeDecomposition",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-turbulence/she-leveque-decomposition/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.Turbulence`.",
  "declaration_id": "TauLib.BookV.FluidMacro.Turbulence::SheLevequeDecomposition",
  "declaration_slug": "she-leveque-decomposition",
  "kind": "structure",
  "name": "SheLevequeDecomposition",
  "module_name": "TauLib.BookV.FluidMacro.Turbulence",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-turbulence/",
  "source_line_start": 276,
  "source_line_end": 299,
  "registry_ids": [
    "V.D309"
  ],
  "related_registry_items": [
    {
      "id": "V.D309",
      "title": "She-Lévêque τ-Decomposition",
      "url": "/registry/object/V.D309/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L276-L299",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.Turbulence",
        "url": "/verify/taulib/docs/book-v-fluid-macro-turbulence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L276-L299",
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

- Module: [TauLib.BookV.FluidMacro.Turbulence](/verify/taulib/docs/book-v-fluid-macro-turbulence/)
- Source path: [`TauLib/BookV/FluidMacro/Turbulence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L276-L299)
- Source range: L276-L299
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D309` — She-Lévêque τ-Decomposition

## Immediate Comment / Docstring

```lean
/-- [V.D309] She-Leveque τ-decomposition.

    ζ_p = p/dim(τ³)² + dim(T²)·[1 - (dim(T²)/dim(τ³))^{p/dim(τ³)}]
        = p/9 + 2[1-(2/3)^{p/3}]

    Linear term: p/9 = K41 scaling on squared dimension (intensity saturation)
    Nonlinear term: fiber-controlled intermittency
    - Prefactor 2 = dim(T²): fiber dimensions available for filaments
    - Base 2/3 = dim(T²)/dim(τ³): fiber-to-total ratio
    - Exponent p/3 = p/dim(τ³): K41 scaling -/
```

## Source Excerpt

```lean
structure SheLevequeDecomposition where
  /-- Total dimension of τ³. -/
  tau3_dim : Nat := 3
  /-- Fiber dimension (T²). -/
  fiber_dim : Nat := 2
  /-- Linear coefficient denominator: dim(τ³)² = 9. -/
  linear_denom : Nat := 9
  /-- Nonlinear prefactor: dim(T²) = 2. -/
  nonlinear_prefactor : Nat := 2
  /-- Scaling ratio numerator: dim(T²) = 2. -/
  ratio_numer : Nat := 2
  /-- Scaling ratio denominator: dim(τ³) = 3. -/
  ratio_denom : Nat := 3
  /-- Exponent denominator: dim(τ³) = 3. -/
  exp_denom : Nat := 3
  /-- Free parameters. -/
  free_params : Nat := 0
  /-- Linear denominator = τ³ dim squared. -/
  linear_check : linear_denom = tau3_dim * tau3_dim := by omega
  /-- Prefactor = fiber dimension. -/
  prefactor_check : nonlinear_prefactor = fiber_dim := by omega
  /-- Ratio = fiber/total. -/
  ratio_check : ratio_numer = fiber_dim ∧ ratio_denom = tau3_dim := by omega
  deriving Repr
```
