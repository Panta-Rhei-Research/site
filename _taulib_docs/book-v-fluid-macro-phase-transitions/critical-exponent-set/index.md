---
{
  "projection_kind": "taulib_declaration",
  "title": "CriticalExponentSet",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/critical-exponent-set/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.PhaseTransitions`.",
  "declaration_id": "TauLib.BookV.FluidMacro.PhaseTransitions::CriticalExponentSet",
  "declaration_slug": "critical-exponent-set",
  "kind": "structure",
  "name": "CriticalExponentSet",
  "module_name": "TauLib.BookV.FluidMacro.PhaseTransitions",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/",
  "source_line_start": 155,
  "source_line_end": 182,
  "registry_ids": [
    "V.D115"
  ],
  "related_registry_items": [
    {
      "id": "V.D115",
      "title": "First-order macro transition",
      "url": "/registry/object/V.D115/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L155-L182",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.PhaseTransitions",
        "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L155-L182",
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

- Module: [TauLib.BookV.FluidMacro.PhaseTransitions](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/)
- Source path: [`TauLib/BookV/FluidMacro/PhaseTransitions.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L155-L182)
- Source range: L155-L182
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D115` — First-order macro transition

## Immediate Comment / Docstring

```lean
/-- [V.D115] Critical exponent set: the six canonical critical exponents
    near a continuous phase transition.

    All exponents are encoded as (numerator, denominator) rationals.
    Scaling relations must hold. -/
```

## Source Excerpt

```lean
structure CriticalExponentSet where
  /-- α exponent: specific heat (numer, denom). -/
  alpha_n : Int
  alpha_d : Nat
  alpha_d_pos : alpha_d > 0
  /-- β exponent: order parameter (numer, denom). -/
  beta_n : Nat
  beta_d : Nat
  beta_d_pos : beta_d > 0
  /-- γ exponent: susceptibility (numer, denom). -/
  gamma_n : Nat
  gamma_d : Nat
  gamma_d_pos : gamma_d > 0
  /-- ν exponent: correlation length (numer, denom). -/
  nu_n : Nat
  nu_d : Nat
  nu_d_pos : nu_d > 0
  /-- η exponent: anomalous dimension (numer, denom). -/
  eta_n : Nat
  eta_d : Nat
  eta_d_pos : eta_d > 0
  /-- δ exponent: critical isotherm (numer, denom). -/
  delta_n : Nat
  delta_d : Nat
  delta_d_pos : delta_d > 0
  /-- Spatial dimension. -/
  dim : Nat
  deriving Repr
```
