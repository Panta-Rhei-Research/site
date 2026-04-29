---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L224",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-calibration-triangle/eval-l224/",
  "summary_short": "`eval` declaration in `TauLib.BookV.GravityField.CalibrationTriangle`.",
  "declaration_id": "TauLib.BookV.GravityField.CalibrationTriangle::#eval:224",
  "declaration_slug": "eval-l224",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookV.GravityField.CalibrationTriangle",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-calibration-triangle/",
  "source_line_start": 224,
  "source_line_end": 224,
  "registry_ids": [
    "V.R100",
    "V.R101",
    "V.R102"
  ],
  "related_registry_items": [
    {
      "id": "V.R100",
      "title": "No SI units enter Xi_tau",
      "url": "/registry/object/V.R100/"
    },
    {
      "id": "V.R101",
      "title": "The delta_A thread through the triangle",
      "url": "/registry/object/V.R101/"
    },
    {
      "id": "V.R102",
      "title": "The unit problem in orthodox physics",
      "url": "/registry/object/V.R102/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/CalibrationTriangle.lean#L224-L224",
  "formal_status": "computed",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/CalibrationTriangle.lean#L224-L224",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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
- Source path: [`TauLib/BookV/GravityField/CalibrationTriangle.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/CalibrationTriangle.lean#L224-L224)
- Source range: L224-L224
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- `V.R100` — No SI units enter Xi_tau
- `V.R101` — The delta_A thread through the triangle
- `V.R102` — The unit problem in orthodox physics

## Immediate Comment / Docstring

```lean
-- ============================================================
-- REMARKS (comment-only)
-- ============================================================

-- [V.R100] No Kilograms Needed: the tau-framework does not need
-- the kilogram -- only the neutron mass COUNT (how many neutrons).
-- The conversion to kg is a final readout step.
-- [V.R101] delta_A Threading: the proton-neutron mass difference
-- delta_A threads through the calibration triangle as a weak-sector
-- correction, not a separate input.
-- [V.R102] Orthodox Three-Input Requirement: orthodox physics requires
-- three independent experimental inputs (c, h, G or equivalent).
-- The tau-framework collapses this to one input (m_n) plus iota_tau.

-- ============================================================
-- SMOKE TESTS
-- ============================================================
```

## Source Excerpt

```lean
#eval calibration_triangle.vertex_count
```
