---
{
  "projection_kind": "taulib_declaration",
  "title": "MassEnergyRelation",
  "permalink": "/verify/taulib/docs/book-iv-physics-mass-energy/mass-energy-relation/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Physics.MassEnergy`.",
  "declaration_id": "TauLib.BookIV.Physics.MassEnergy::MassEnergyRelation",
  "declaration_slug": "mass-energy-relation",
  "kind": "structure",
  "name": "MassEnergyRelation",
  "module_name": "TauLib.BookIV.Physics.MassEnergy",
  "module_url": "/verify/taulib/docs/book-iv-physics-mass-energy/",
  "source_line_start": 151,
  "source_line_end": 162,
  "registry_ids": [
    "IV.D23"
  ],
  "related_registry_items": [
    {
      "id": "IV.D23",
      "title": "Mass-Energy Relation",
      "url": "/registry/object/IV.D23/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/MassEnergy.lean#L151-L162",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/MassEnergy.lean#L151-L162",
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
- Source path: [`TauLib/BookIV/Physics/MassEnergy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/MassEnergy.lean#L151-L162)
- Source range: L151-L162
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D23` — Mass-Energy Relation

## Immediate Comment / Docstring

```lean
/-- [IV.D23] Mass-energy relation template: E = m · c²_τ.

    This is a structural identity relating the mass index to the
    energy index via the τ-derived speed constant. The relation
    holds as a cross-multiplication equality on scaled rationals:

    energy/1 = mass × c² means:
    E_numer · m_denom · c_denom = m_numer · E_denom · c_numer -/
```

## Source Excerpt

```lean
structure MassEnergyRelation where
  /-- Mass index. -/
  mass : MassIndex
  /-- Energy index. -/
  energy : EnergyIndex
  /-- Speed constant c²_τ. -/
  speed : SpeedConstant
  /-- The structural identity: E = m · c². -/
  relation :
    energy.numer * mass.denom * speed.c_sq_denom =
    mass.numer * energy.denom * speed.c_sq_numer
  deriving Repr
```
