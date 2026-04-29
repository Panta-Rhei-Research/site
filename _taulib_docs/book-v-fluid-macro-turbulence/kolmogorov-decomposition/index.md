---
{
  "projection_kind": "taulib_declaration",
  "title": "KolmogorovDecomposition",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-turbulence/kolmogorov-decomposition/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.Turbulence`.",
  "declaration_id": "TauLib.BookV.FluidMacro.Turbulence::KolmogorovDecomposition",
  "declaration_slug": "kolmogorov-decomposition",
  "kind": "structure",
  "name": "KolmogorovDecomposition",
  "module_name": "TauLib.BookV.FluidMacro.Turbulence",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-turbulence/",
  "source_line_start": 379,
  "source_line_end": 396,
  "registry_ids": [
    "V.D310"
  ],
  "related_registry_items": [
    {
      "id": "V.D310",
      "title": "Kolmogorov Exponent Decomposition",
      "url": "/registry/object/V.D310/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L379-L396",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L379-L396",
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
- Source path: [`TauLib/BookV/FluidMacro/Turbulence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L379-L396)
- Source range: L379-L396
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D310` — Kolmogorov Exponent Decomposition

## Immediate Comment / Docstring

```lean
/-- [V.D310] Kolmogorov exponent decomposition.

    5/3 = (|gen| + dim(T²)) / dim(τ³) = (3 + 2) / 3

    Numerator 5 = 3 generation modes + 2 fiber directions.
    Denominator 3 = dim(τ³). -/
```

## Source Excerpt

```lean
structure KolmogorovDecomposition where
  /-- Number of generations. -/
  n_gen : Nat := 3
  /-- Fiber dimension. -/
  fiber_dim : Nat := 2
  /-- Total dimension. -/
  tau3_dim : Nat := 3
  /-- Numerator = gen + fiber. -/
  numer : Nat := 5
  /-- Denominator = total dim. -/
  denom : Nat := 3
  /-- Numerator decomposition. -/
  numer_eq : numer = n_gen + fiber_dim := by omega
  /-- Denominator is τ³ dim. -/
  denom_eq : denom = tau3_dim := by omega
  /-- Free parameters. -/
  free_params : Nat := 0
  deriving Repr
```
