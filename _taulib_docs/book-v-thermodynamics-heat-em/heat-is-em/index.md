---
{
  "projection_kind": "taulib_declaration",
  "title": "HeatIsEM",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-heat-em/heat-is-em/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.HeatEM`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.HeatEM::HeatIsEM",
  "declaration_slug": "heat-is-em",
  "kind": "structure",
  "name": "HeatIsEM",
  "module_name": "TauLib.BookV.Thermodynamics.HeatEM",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/",
  "source_line_start": 244,
  "source_line_end": 252,
  "registry_ids": [
    "V.T64"
  ],
  "related_registry_items": [
    {
      "id": "V.T64",
      "title": "Heat is electromagnetism",
      "url": "/registry/object/V.T64/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L244-L252",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L244-L252",
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
- Source path: [`TauLib/BookV/Thermodynamics/HeatEM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L244-L252)
- Source range: L244-L252
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T64` — Heat is electromagnetism

## Immediate Comment / Docstring

```lean
/-- [V.T64] Heat is electromagnetism: all macroscopic energy transport
    at E1 is mediated by the B-sector of the boundary holonomy algebra.

    Q-dot = integral over boundary of B-component flux.

    There is no separate "heat force" -- heat is the macroscopic
    manifestation of the B-sector (electromagnetic) boundary exchange. -/
```

## Source Excerpt

```lean
structure HeatIsEM where
  /-- The mediating sector is always B (EM). -/
  sector : Sector := .B
  /-- There is no separate heat force. -/
  no_separate_force : Bool := true
  /-- All three transport modes are unified. -/
  transport_modes : List TransportMode :=
    [.Radiation, .Conduction, .Convection]
  deriving Repr
```
