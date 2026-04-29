---
{
  "projection_kind": "taulib_declaration",
  "title": "MacroReynoldsNumber",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-reynolds-number/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.NavierStokesMacro`.",
  "declaration_id": "TauLib.BookV.FluidMacro.NavierStokesMacro::MacroReynoldsNumber",
  "declaration_slug": "macro-reynolds-number",
  "kind": "structure",
  "name": "MacroReynoldsNumber",
  "module_name": "TauLib.BookV.FluidMacro.NavierStokesMacro",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/",
  "source_line_start": 220,
  "source_line_end": 229,
  "registry_ids": [
    "V.D98"
  ],
  "related_registry_items": [
    {
      "id": "V.D98",
      "title": "Macro tau-Reynolds number",
      "url": "/registry/object/V.D98/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L220-L229",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.NavierStokesMacro",
        "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L220-L229",
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

- Module: [TauLib.BookV.FluidMacro.NavierStokesMacro](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/)
- Source path: [`TauLib/BookV/FluidMacro/NavierStokesMacro.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L220-L229)
- Source range: L220-L229
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D98` — Macro tau-Reynolds number

## Immediate Comment / Docstring

```lean
/-- [V.D98] Macro tau-Reynolds number: Re_τ^macro = μ_n^macro / η_τ^macro,
    the ratio of macro mobility to macro viscosity.

    Laminar: Re << 1, Turbulent: Re >> 1.
    Bounded above: Re_τ ≤ M·Prim(n)^{1/2} / η_τ. -/
```

## Source Excerpt

```lean
structure MacroReynoldsNumber where
  /-- Mobility numerator. -/
  mobility_numer : Nat
  /-- Viscosity denominator (nonzero). -/
  viscosity_denom : Nat
  /-- Viscosity is positive. -/
  viscosity_pos : viscosity_denom > 0
  /-- The primorial level. -/
  level : Nat
  deriving Repr
```
