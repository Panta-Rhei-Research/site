---
{
  "projection_kind": "taulib_declaration",
  "title": "MagneticPressureTension",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/magnetic-pressure-tension/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.TauMHD`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauMHD::MagneticPressureTension",
  "declaration_slug": "magnetic-pressure-tension",
  "kind": "structure",
  "name": "MagneticPressureTension",
  "module_name": "TauLib.BookV.FluidMacro.TauMHD",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/",
  "source_line_start": 114,
  "source_line_end": 125,
  "registry_ids": [
    "V.D108"
  ],
  "related_registry_items": [
    {
      "id": "V.D108",
      "title": "Magnetic Reynolds number",
      "url": "/registry/object/V.D108/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L114-L125",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.TauMHD",
        "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L114-L125",
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

- Module: [TauLib.BookV.FluidMacro.TauMHD](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/)
- Source path: [`TauLib/BookV/FluidMacro/TauMHD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L114-L125)
- Source range: L114-L125
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D108` — Magnetic Reynolds number

## Immediate Comment / Docstring

```lean
/-- [V.D108] Magnetic pressure-tension: the magnetic field contributes
    both isotropic pressure P_B = B²/(2μ₀) and anisotropic tension
    T_B = B²/μ₀ along field lines.

    Encoded as (pressure_numer, tension_numer) with common denominator.
    Tension = 2 × Pressure (exact ratio). -/
```

## Source Excerpt

```lean
structure MagneticPressureTension where
  /-- Magnetic pressure numerator (B²/(2μ₀), scaled). -/
  pressure_numer : Nat
  /-- Magnetic tension numerator (B²/μ₀, scaled). -/
  tension_numer : Nat
  /-- Common denominator. -/
  denom : Nat
  /-- Denominator positive. -/
  denom_pos : denom > 0
  /-- Tension = 2 × pressure. -/
  tension_ratio : tension_numer = 2 * pressure_numer
  deriving Repr
```
