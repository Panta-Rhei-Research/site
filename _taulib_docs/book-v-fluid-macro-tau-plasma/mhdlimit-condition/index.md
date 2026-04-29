---
{
  "projection_kind": "taulib_declaration",
  "title": "MHDLimitCondition",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-plasma/mhdlimit-condition/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.TauPlasma`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauPlasma::MHDLimitCondition",
  "declaration_slug": "mhdlimit-condition",
  "kind": "structure",
  "name": "MHDLimitCondition",
  "module_name": "TauLib.BookV.FluidMacro.TauPlasma",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-plasma/",
  "source_line_start": 276,
  "source_line_end": 285,
  "registry_ids": [
    "V.D106"
  ],
  "related_registry_items": [
    {
      "id": "V.D106",
      "title": "MHD limit",
      "url": "/registry/object/V.D106/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L276-L285",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.TauPlasma",
        "url": "/verify/taulib/docs/book-v-fluid-macro-tau-plasma/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L276-L285",
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

- Module: [TauLib.BookV.FluidMacro.TauPlasma](/verify/taulib/docs/book-v-fluid-macro-tau-plasma/)
- Source path: [`TauLib/BookV/FluidMacro/TauPlasma.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L276-L285)
- Source range: L276-L285
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D106` — MHD limit

## Immediate Comment / Docstring

```lean
/-- [V.D106] MHD limit: the magnetohydrodynamic regime of a τ-plasma.
    Conditions: charge separation < λ_D, timescales > ω_p⁻¹,
    spatial scales > λ_D.

    The plasma is described as a single conducting fluid with
    frozen-flux constraint. -/
```

## Source Excerpt

```lean
structure MHDLimitCondition where
  /-- Charge separation below Debye length. -/
  charge_separation_ok : Bool := true
  /-- Timescale exceeds inverse plasma frequency. -/
  timescale_ok : Bool := true
  /-- Spatial scale exceeds Debye length. -/
  spatial_scale_ok : Bool := true
  /-- Frozen flux condition holds. -/
  frozen_flux : Bool := true
  deriving Repr
```
