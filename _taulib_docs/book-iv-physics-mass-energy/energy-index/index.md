---
{
  "projection_kind": "taulib_declaration",
  "title": "EnergyIndex",
  "permalink": "/verify/taulib/docs/book-iv-physics-mass-energy/energy-index/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Physics.MassEnergy`.",
  "declaration_id": "TauLib.BookIV.Physics.MassEnergy::EnergyIndex",
  "declaration_slug": "energy-index",
  "kind": "structure",
  "name": "EnergyIndex",
  "module_name": "TauLib.BookIV.Physics.MassEnergy",
  "module_url": "/verify/taulib/docs/book-iv-physics-mass-energy/",
  "source_line_start": 101,
  "source_line_end": 110,
  "registry_ids": [
    "IV.D21"
  ],
  "related_registry_items": [
    {
      "id": "IV.D21",
      "title": "Energy Index",
      "url": "/registry/object/IV.D21/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/MassEnergy.lean#L101-L110",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/MassEnergy.lean#L101-L110",
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
- Source path: [`TauLib/BookIV/Physics/MassEnergy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/MassEnergy.lean#L101-L110)
- Source range: L101-L110
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D21` — Energy Index

## Immediate Comment / Docstring

```lean
/-- [IV.D21] Energy index: the coherence cost of maintaining a
    localized defect bundle structure.

    Energy ∝ defect-tuple magnitude × stability degree.
    Each sector provides its own excitation cost scale. -/
```

## Source Excerpt

```lean
structure EnergyIndex where
  /-- Energy value numerator (scaled). -/
  numer : Nat
  /-- Energy value denominator. -/
  denom : Nat
  /-- Denominator is positive. -/
  denom_pos : denom > 0
  /-- Which sector provides the excitation. -/
  sector : Sector
  deriving Repr
```
