---
{
  "projection_kind": "taulib_declaration",
  "title": "EMEnergyTransport",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-heat-em/emenergy-transport/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.HeatEM`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.HeatEM::EMEnergyTransport",
  "declaration_slug": "emenergy-transport",
  "kind": "structure",
  "name": "EMEnergyTransport",
  "module_name": "TauLib.BookV.Thermodynamics.HeatEM",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/",
  "source_line_start": 90,
  "source_line_end": 101,
  "registry_ids": [
    "V.D91"
  ],
  "related_registry_items": [
    {
      "id": "V.D91",
      "title": "EM energy transport",
      "url": "/registry/object/V.D91/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L90-L101",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.HeatEM",
        "url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L90-L101",
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

- Module: [TauLib.BookV.Thermodynamics.HeatEM](/verify/taulib/docs/book-v-thermodynamics-heat-em/)
- Source path: [`TauLib/BookV/Thermodynamics/HeatEM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L90-L101)
- Source range: L90-L101
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D91` — EM energy transport

## Immediate Comment / Docstring

```lean
/-- [V.D91] EM energy transport: a change in the CR-tension distribution
    on tau^3 mediated by the B-sector of H_partial[omega].

    Energy: Delta E = integral of <B-component, delta_tension> over tau^3.
    All three modes (radiation, conduction, convection) are B-sector. -/
```

## Source Excerpt

```lean
structure EMEnergyTransport where
  /-- The transport mode. -/
  mode : TransportMode
  /-- Energy numerator (scaled). -/
  energy_numer : Nat
  /-- Energy denominator. -/
  energy_denom : Nat
  /-- Denominator positive. -/
  denom_pos : energy_denom > 0
  /-- The mediating sector is always B. -/
  mediating_sector : Sector := .B
  deriving Repr
```
