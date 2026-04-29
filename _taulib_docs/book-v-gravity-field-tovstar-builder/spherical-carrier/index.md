---
{
  "projection_kind": "taulib_declaration",
  "title": "SphericalCarrier",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/spherical-carrier/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.TOVStarBuilder`.",
  "declaration_id": "TauLib.BookV.GravityField.TOVStarBuilder::SphericalCarrier",
  "declaration_slug": "spherical-carrier",
  "kind": "structure",
  "name": "SphericalCarrier",
  "module_name": "TauLib.BookV.GravityField.TOVStarBuilder",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/",
  "source_line_start": 69,
  "source_line_end": 80,
  "registry_ids": [
    "V.D66"
  ],
  "related_registry_items": [
    {
      "id": "V.D66",
      "title": "Spherical carrier predicate",
      "url": "/registry/object/V.D66/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L69-L80",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TOVStarBuilder",
        "url": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L69-L80",
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

- Module: [TauLib.BookV.GravityField.TOVStarBuilder](/verify/taulib/docs/book-v-gravity-field-tovstar-builder/)
- Source path: [`TauLib/BookV/GravityField/TOVStarBuilder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L69-L80)
- Source range: L69-L80
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D66` — Spherical carrier predicate

## Immediate Comment / Docstring

```lean
/-- [V.D66] Spherical carrier predicate: a ball-like region in the
    tau-arena that can host a gravitational defect bundle. -/
```

## Source Excerpt

```lean
structure SphericalCarrier where
  /-- Radius index numerator. -/
  radius_numer : Nat
  /-- Radius index denominator. -/
  radius_denom : Nat
  /-- Denominator positive. -/
  denom_pos : radius_denom > 0
  /-- Radius is positive. -/
  radius_positive : radius_numer > 0
  /-- Whether the carrier has spherical symmetry. -/
  is_spherical : Bool := true
  deriving Repr
```
