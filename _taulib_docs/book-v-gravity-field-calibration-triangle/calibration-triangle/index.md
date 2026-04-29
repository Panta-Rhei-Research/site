---
{
  "projection_kind": "taulib_declaration",
  "title": "CalibrationTriangle",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-calibration-triangle/calibration-triangle/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.CalibrationTriangle`.",
  "declaration_id": "TauLib.BookV.GravityField.CalibrationTriangle::CalibrationTriangle",
  "declaration_slug": "calibration-triangle",
  "kind": "structure",
  "name": "CalibrationTriangle",
  "module_name": "TauLib.BookV.GravityField.CalibrationTriangle",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-calibration-triangle/",
  "source_line_start": 112,
  "source_line_end": 125,
  "registry_ids": [
    "V.D79"
  ],
  "related_registry_items": [
    {
      "id": "V.D79",
      "title": "Calibration Triangle",
      "url": "/registry/object/V.D79/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/CalibrationTriangle.lean#L112-L125",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/CalibrationTriangle.lean#L112-L125",
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
- Source path: [`TauLib/BookV/GravityField/CalibrationTriangle.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/CalibrationTriangle.lean#L112-L125)
- Source range: L112-L125
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D79` — Calibration Triangle

## Immediate Comment / Docstring

```lean
/-- [V.D79] The calibration triangle: three vertices connected
    by edge ratios determined entirely by iota_tau.

    - Vertex 1: m_n (1 experimental input)
    - Vertex 2: G_tau (derived from iota_tau^2)
    - Vertex 3: alpha_em (derived from (8/15) * iota_tau^4)

    The triangle is COMPLETE: all SI physical constants can
    be expressed in terms of these three. -/
```

## Source Excerpt

```lean
structure CalibrationTriangle where
  /-- Number of vertices (always 3). -/
  vertex_count : Nat
  /-- Exactly 3 vertices. -/
  is_triangle : vertex_count = 3
  /-- Number of experimental inputs (always 1). -/
  experimental_inputs : Nat
  /-- Only 1 experimental input (m_n). -/
  one_input : experimental_inputs = 1
  /-- Number of derived constants (always 2). -/
  derived_count : Nat
  /-- Two derived constants. -/
  two_derived : derived_count = 2
  deriving Repr
```
