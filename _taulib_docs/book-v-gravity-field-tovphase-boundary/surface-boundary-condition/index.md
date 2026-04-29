---
{
  "projection_kind": "taulib_declaration",
  "title": "SurfaceBoundaryCondition",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/surface-boundary-condition/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.TOVPhaseBoundary`.",
  "declaration_id": "TauLib.BookV.GravityField.TOVPhaseBoundary::SurfaceBoundaryCondition",
  "declaration_slug": "surface-boundary-condition",
  "kind": "structure",
  "name": "SurfaceBoundaryCondition",
  "module_name": "TauLib.BookV.GravityField.TOVPhaseBoundary",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/",
  "source_line_start": 175,
  "source_line_end": 184,
  "registry_ids": [
    "V.L01"
  ],
  "related_registry_items": [
    {
      "id": "V.L01",
      "title": "Surface Matter Bound",
      "url": "/registry/object/V.L01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L175-L184",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TOVPhaseBoundary",
        "url": "/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L175-L184",
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

- Module: [TauLib.BookV.GravityField.TOVPhaseBoundary](/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/)
- Source path: [`TauLib/BookV/GravityField/TOVPhaseBoundary.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L175-L184)
- Source range: L175-L184
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.L01` — Surface Matter Bound

## Immediate Comment / Docstring

```lean
/-- [V.L01] Surface matter character boundary condition:
    T^mat(R_surface) = 0.

    At the stellar surface, the matter character drops to zero.
    This determines the stellar radius as a function of total mass.

    In the tau-framework, this is not an arbitrary boundary condition
    but follows from the vanishing of the matter sector contributions
    at the boundary of the defect bundle. -/
```

## Source Excerpt

```lean
structure SurfaceBoundaryCondition where
  /-- Surface radius numerator. -/
  surface_radius_numer : Nat
  /-- Surface radius denominator. -/
  surface_radius_denom : Nat
  /-- Denominator positive. -/
  denom_pos : surface_radius_denom > 0
  /-- Matter character at surface is zero. -/
  matter_zero_at_surface : Bool := true
  deriving Repr
```
