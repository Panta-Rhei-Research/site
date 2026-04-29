---
{
  "projection_kind": "taulib_declaration",
  "title": "GeometricRelaxation",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-heat-em/geometric-relaxation/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.HeatEM`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.HeatEM::GeometricRelaxation",
  "declaration_slug": "geometric-relaxation",
  "kind": "structure",
  "name": "GeometricRelaxation",
  "module_name": "TauLib.BookV.Thermodynamics.HeatEM",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/",
  "source_line_start": 183,
  "source_line_end": 196,
  "registry_ids": [
    "V.D92"
  ],
  "related_registry_items": [
    {
      "id": "V.D92",
      "title": "Geometric relaxation",
      "url": "/registry/object/V.D92/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L183-L196",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L183-L196",
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
- Source path: [`TauLib/BookV/Thermodynamics/HeatEM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L183-L196)
- Source range: L183-L196
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D92` — Geometric relaxation

## Immediate Comment / Docstring

```lean
/-- [V.D92] Geometric relaxation: the process by which a defect bundle
    loses CR-tension through spatial redistribution on the fiber T^2.

    Driven by the fiber gradient of |dbar_b f|^2 weighted by
    iota_tau^2 (B-sector self-coupling).

    Geometric relaxation preserves topological sector. -/
```

## Source Excerpt

```lean
structure GeometricRelaxation where
  /-- Initial tension numerator. -/
  tension_initial_numer : Nat
  /-- Final tension numerator (after relaxation). -/
  tension_final_numer : Nat
  /-- Common denominator. -/
  tension_denom : Nat
  /-- Denominator positive. -/
  denom_pos : tension_denom > 0
  /-- Tension decreases. -/
  tension_decreases : tension_final_numer ≤ tension_initial_numer
  /-- Topological sector is preserved. -/
  preserves_topology : Bool := true
  deriving Repr
```
