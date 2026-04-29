---
{
  "projection_kind": "taulib_declaration",
  "title": "TauTurbulentFlow",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-turbulence/tau-turbulent-flow/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.Turbulence`.",
  "declaration_id": "TauLib.BookV.FluidMacro.Turbulence::TauTurbulentFlow",
  "declaration_slug": "tau-turbulent-flow",
  "kind": "structure",
  "name": "TauTurbulentFlow",
  "module_name": "TauLib.BookV.FluidMacro.Turbulence",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-turbulence/",
  "source_line_start": 77,
  "source_line_end": 90,
  "registry_ids": [
    "V.D99"
  ],
  "related_registry_items": [
    {
      "id": "V.D99",
      "title": "tau-turbulent flow",
      "url": "/registry/object/V.D99/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L77-L90",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L77-L90",
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
- Source path: [`TauLib/BookV/FluidMacro/Turbulence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L77-L90)
- Source range: L77-L90
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D99` — tau-turbulent flow

## Immediate Comment / Docstring

```lean
/-- [V.D99] Tau-turbulent flow: a macro tau-NS flow with Re >> 1,
    non-monotonic defect budget across primorial levels, and
    structured variation balanced by injection from the source.

    Turbulence is deterministic but structurally complex. -/
```

## Source Excerpt

```lean
structure TauTurbulentFlow where
  /-- Underlying macro tau-NS flow. -/
  flow : MacroTauNSFlow
  /-- Reynolds number (ratio form). -/
  reynolds : MacroReynoldsNumber
  /-- Injection level (energy enters here). -/
  level_inj : Nat
  /-- Dissipation level (energy leaves here). -/
  level_diss : Nat
  /-- Injection level < dissipation level. -/
  inj_lt_diss : level_inj < level_diss
  /-- Reynolds number is large (Re > threshold). -/
  reynolds_large : reynolds.mobility_numer > 100 * reynolds.viscosity_denom
  deriving Repr
```
