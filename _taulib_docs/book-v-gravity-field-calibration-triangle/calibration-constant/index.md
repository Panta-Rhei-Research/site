---
{
  "projection_kind": "taulib_declaration",
  "title": "CalibrationConstant",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-calibration-triangle/calibration-constant/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.CalibrationTriangle`.",
  "declaration_id": "TauLib.BookV.GravityField.CalibrationTriangle::CalibrationConstant",
  "declaration_slug": "calibration-constant",
  "kind": "structure",
  "name": "CalibrationConstant",
  "module_name": "TauLib.BookV.GravityField.CalibrationTriangle",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-calibration-triangle/",
  "source_line_start": 72,
  "source_line_end": 83,
  "registry_ids": [
    "V.D78"
  ],
  "related_registry_items": [
    {
      "id": "V.D78",
      "title": "Calibration Constant Xi_tau",
      "url": "/registry/object/V.D78/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/CalibrationTriangle.lean#L72-L83",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/CalibrationTriangle.lean#L72-L83",
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
- Source path: [`TauLib/BookV/GravityField/CalibrationTriangle.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/CalibrationTriangle.lean#L72-L83)
- Source range: L72-L83
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D78` — Calibration Constant Xi_tau

## Immediate Comment / Docstring

```lean
/-- [V.D78] Calibration constant Xi_tau: the tau-to-SI conversion
    factor determined by matching the neutron mass.

    Xi_tau is refinement-stable: it does not depend on the
    tau truncation depth beyond the iota_tau precision. -/
```

## Source Excerpt

```lean
structure CalibrationConstant where
  /-- Xi_tau numerator. -/
  xi_numer : Nat
  /-- Xi_tau denominator. -/
  xi_denom : Nat
  /-- Denominator positive. -/
  denom_pos : xi_denom > 0
  /-- Whether Xi_tau is refinement-stable. -/
  is_refinement_stable : Bool := true
  /-- Scope. -/
  scope : String := "tau-effective"
  deriving Repr
```
