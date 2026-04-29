---
{
  "projection_kind": "taulib_declaration",
  "title": "NeutronRole",
  "permalink": "/verify/taulib/docs/book-iv-physics-mass-energy/neutron-role/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Physics.MassEnergy`.",
  "declaration_id": "TauLib.BookIV.Physics.MassEnergy::NeutronRole",
  "declaration_slug": "neutron-role",
  "kind": "structure",
  "name": "NeutronRole",
  "module_name": "TauLib.BookIV.Physics.MassEnergy",
  "module_url": "/verify/taulib/docs/book-iv-physics-mass-energy/",
  "source_line_start": 201,
  "source_line_end": 208,
  "registry_ids": [
    "IV.R04"
  ],
  "related_registry_items": [
    {
      "id": "IV.R04",
      "title": "Neutron First Ontic Particle",
      "url": "/registry/object/IV.R04/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/MassEnergy.lean#L201-L208",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.MassEnergy",
        "url": "/verify/taulib/docs/book-iv-physics-mass-energy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/MassEnergy.lean#L201-L208",
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

- Module: [TauLib.BookIV.Physics.MassEnergy](/verify/taulib/docs/book-iv-physics-mass-energy/)
- Source path: [`TauLib/BookIV/Physics/MassEnergy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/MassEnergy.lean#L201-L208)
- Source range: L201-L208
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R04` — Neutron First Ontic Particle

## Immediate Comment / Docstring

```lean
/-- [IV.R04] The neutron is the first ontic particle: the minimal
    mass-bearing defect bundle in τ.

    Properties:
    - Toroidal defect bundle on τ¹ (the "micro-donut")
    - Beta decay: neutron → proton + electron + ν_e
      (shedding subsidiary defect modes)
    - Stable in bound states; β-decay only when free

    This structure records the neutron's structural role.
    The numerical mass comes from the calibration cascade (Part VII). -/
```

## Source Excerpt

```lean
structure NeutronRole where
  /-- Neutron mass index (first/minimal). -/
  mass : MassIndex
  /-- The neutron is ontic (persistent T² fiber). -/
  is_ontic : mass.is_persistent = true ∧ mass.carrier = .Fiber
  /-- The neutron mass is positive. -/
  mass_positive : mass.numer > 0
  deriving Repr
```
