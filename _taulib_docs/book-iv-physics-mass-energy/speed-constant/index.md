---
{
  "projection_kind": "taulib_declaration",
  "title": "SpeedConstant",
  "permalink": "/verify/taulib/docs/book-iv-physics-mass-energy/speed-constant/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Physics.MassEnergy`.",
  "declaration_id": "TauLib.BookIV.Physics.MassEnergy::SpeedConstant",
  "declaration_slug": "speed-constant",
  "kind": "structure",
  "name": "SpeedConstant",
  "module_name": "TauLib.BookIV.Physics.MassEnergy",
  "module_url": "/verify/taulib/docs/book-iv-physics-mass-energy/",
  "source_line_start": 126,
  "source_line_end": 133,
  "registry_ids": [
    "IV.D22"
  ],
  "related_registry_items": [
    {
      "id": "IV.D22",
      "title": "Speed Constant",
      "url": "/registry/object/IV.D22/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/MassEnergy.lean#L126-L133",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/MassEnergy.lean#L126-L133",
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
- Source path: [`TauLib/BookIV/Physics/MassEnergy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/MassEnergy.lean#L126-L133)
- Source range: L126-L133
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D22` — Speed Constant

## Immediate Comment / Docstring

```lean
/-- [IV.D22] Speed-of-light constant c²_τ: the τ-derived structural
    constant relating mass and energy indices.

    c²_τ is not postulated but earned from the τ-kernel as the
    canonical conversion factor between defect-bundle mass indices
    and coherence cost indices. -/
```

## Source Excerpt

```lean
structure SpeedConstant where
  /-- c² numerator (scaled). -/
  c_sq_numer : Nat
  /-- c² denominator. -/
  c_sq_denom : Nat
  /-- Denominator is positive. -/
  denom_pos : c_sq_denom > 0
  deriving Repr
```
