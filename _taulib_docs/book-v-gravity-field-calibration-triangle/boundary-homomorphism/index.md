---
{
  "projection_kind": "taulib_declaration",
  "title": "BoundaryHomomorphism",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-calibration-triangle/boundary-homomorphism/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.CalibrationTriangle`.",
  "declaration_id": "TauLib.BookV.GravityField.CalibrationTriangle::BoundaryHomomorphism",
  "declaration_slug": "boundary-homomorphism",
  "kind": "structure",
  "name": "BoundaryHomomorphism",
  "module_name": "TauLib.BookV.GravityField.CalibrationTriangle",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-calibration-triangle/",
  "source_line_start": 150,
  "source_line_end": 157,
  "registry_ids": [
    "V.D80"
  ],
  "related_registry_items": [
    {
      "id": "V.D80",
      "title": "Ring Homomorphism Phi_p,n",
      "url": "/registry/object/V.D80/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/CalibrationTriangle.lean#L150-L157",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.CalibrationTriangle",
        "url": "/verify/taulib/docs/book-v-gravity-field-calibration-triangle/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/CalibrationTriangle.lean#L150-L157",
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

- Module: [TauLib.BookV.GravityField.CalibrationTriangle](/verify/taulib/docs/book-v-gravity-field-calibration-triangle/)
- Source path: [`TauLib/BookV/GravityField/CalibrationTriangle.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/CalibrationTriangle.lean#L150-L157)
- Source range: L150-L157
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D80` — Ring Homomorphism Phi_p,n

## Immediate Comment / Docstring

```lean
/-- [V.D80] Boundary homomorphism: the map from tau-internal
    quantities to SI units.

    Phi: tau-quantities -> SI quantities

    Requires:
    1. ONE experimental anchor (m_n in kg)
    2. iota_tau (from tau axioms)

    All other SI constants are DERIVED. -/
```

## Source Excerpt

```lean
structure BoundaryHomomorphism where
  /-- The calibration constant Xi_tau. -/
  xi : CalibrationConstant
  /-- Whether the homomorphism is complete (covers all SI constants). -/
  is_complete : Bool := true
  /-- Whether it preserves the sector structure. -/
  preserves_sectors : Bool := true
  deriving Repr
```
