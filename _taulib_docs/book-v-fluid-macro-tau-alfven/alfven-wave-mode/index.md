---
{
  "projection_kind": "taulib_declaration",
  "title": "AlfvenWaveMode",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-wave-mode/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.TauAlfven`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauAlfven::AlfvenWaveMode",
  "declaration_slug": "alfven-wave-mode",
  "kind": "structure",
  "name": "AlfvenWaveMode",
  "module_name": "TauLib.BookV.FluidMacro.TauAlfven",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/",
  "source_line_start": 82,
  "source_line_end": 95,
  "registry_ids": [
    "V.D111"
  ],
  "related_registry_items": [
    {
      "id": "V.D111",
      "title": "Mixed-sector mode",
      "url": "/registry/object/V.D111/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L82-L95",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.TauAlfven",
        "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L82-L95",
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

- Module: [TauLib.BookV.FluidMacro.TauAlfven](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/)
- Source path: [`TauLib/BookV/FluidMacro/TauAlfven.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L82-L95)
- Source range: L82-L95
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D111` — Mixed-sector mode

## Immediate Comment / Docstring

```lean
/-- [V.D111] Alfven wave mode: transverse oscillation of the magnetic
    field and plasma, propagating along B at the Alfven speed v_A.

    v_A = B / √(μ₀ ρ)

    Shear Alfven waves are incompressible and carry energy along B. -/
```

## Source Excerpt

```lean
structure AlfvenWaveMode where
  /-- Polarization type. -/
  polarization : MHDPolarization
  /-- Alfven speed numerator (scaled). -/
  speed_numer : Nat
  /-- Alfven speed denominator. -/
  speed_denom : Nat
  /-- Denominator positive. -/
  speed_denom_pos : speed_denom > 0
  /-- Propagation angle θ relative to B (in degrees, scaled by 10). -/
  angle_deg_scaled : Nat
  /-- Whether the wave is incompressible. -/
  is_incompressible : Bool
  deriving Repr
```
