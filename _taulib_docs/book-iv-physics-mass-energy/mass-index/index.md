---
{
  "projection_kind": "taulib_declaration",
  "title": "MassIndex",
  "permalink": "/verify/taulib/docs/book-iv-physics-mass-energy/mass-index/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Physics.MassEnergy`.",
  "declaration_id": "TauLib.BookIV.Physics.MassEnergy::MassIndex",
  "declaration_slug": "mass-index",
  "kind": "structure",
  "name": "MassIndex",
  "module_name": "TauLib.BookIV.Physics.MassEnergy",
  "module_url": "/verify/taulib/docs/book-iv-physics-mass-energy/",
  "source_line_start": 75,
  "source_line_end": 86,
  "registry_ids": [
    "IV.D20"
  ],
  "related_registry_items": [
    {
      "id": "IV.D20",
      "title": "Mass Index",
      "url": "/registry/object/IV.D20/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/MassEnergy.lean#L75-L86",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/MassEnergy.lean#L75-L86",
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
- Source path: [`TauLib/BookIV/Physics/MassEnergy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/MassEnergy.lean#L75-L86)
- Source range: L75-L86
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D20` — Mass Index

## Immediate Comment / Docstring

```lean
/-- [IV.D20] Mass index: the inertial invariant of a persistent
    localized defect bundle.

    Mass = boundary fixed-point of the defect bundle's coherence
    functional = α-Idx readout from NF-stabilized configuration.

    Properties:
    - Not a primitive scalar but a resistance/scale index
    - Comes with minimal carrier that can host it
    - Monotone under admissible evolution (No-Shrink for BH) -/
```

## Source Excerpt

```lean
structure MassIndex where
  /-- Mass value numerator (scaled). -/
  numer : Nat
  /-- Mass value denominator. -/
  denom : Nat
  /-- Denominator is positive. -/
  denom_pos : denom > 0
  /-- Carrier type (must be Fiber for ontic particles). -/
  carrier : CarrierType
  /-- Whether the defect bundle is persistent (stable T² fiber). -/
  is_persistent : Bool
  deriving Repr
```
