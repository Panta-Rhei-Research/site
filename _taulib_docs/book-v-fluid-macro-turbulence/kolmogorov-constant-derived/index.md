---
{
  "projection_kind": "taulib_declaration",
  "title": "KolmogorovConstantDerived",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-turbulence/kolmogorov-constant-derived/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.Turbulence`.",
  "declaration_id": "TauLib.BookV.FluidMacro.Turbulence::KolmogorovConstantDerived",
  "declaration_slug": "kolmogorov-constant-derived",
  "kind": "structure",
  "name": "KolmogorovConstantDerived",
  "module_name": "TauLib.BookV.FluidMacro.Turbulence",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-turbulence/",
  "source_line_start": 424,
  "source_line_end": 437,
  "registry_ids": [
    "V.T251"
  ],
  "related_registry_items": [
    {
      "id": "V.T251",
      "title": "C_K = 3/2",
      "url": "/registry/object/V.T251/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L424-L437",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L424-L437",
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
- Source path: [`TauLib/BookV/FluidMacro/Turbulence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L424-L437)
- Source range: L424-L437
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T251` — C_K = 3/2

## Immediate Comment / Docstring

```lean
/-- [V.T251] Kolmogorov constant C_K = dim(τ³)/dim(T²) = 3/2 = 1.5.

    Exact match to Sreenivasan 1995 experimental value C_K = 1.5 ± 0.1.
    Zero free parameters. -/
```

## Source Excerpt

```lean
structure KolmogorovConstantDerived where
  /-- τ³ dimension (numerator). -/
  tau3_dim : Nat := 3
  /-- T² dimension (denominator). -/
  fiber_dim : Nat := 2
  /-- C_K × 10. -/
  ck_x10 : Nat := 15
  /-- Experimental C_K × 10 (central value). -/
  ck_expt_x10 : Nat := 15
  /-- Deviation = 0. -/
  deviation_ppm : Nat := 0
  /-- C_K × 10 = tau3_dim × 10 / fiber_dim. -/
  ck_check : ck_x10 * fiber_dim = tau3_dim * 10 := by omega
  deriving Repr
```
