---
{
  "projection_kind": "taulib_declaration",
  "title": "dimensional_bridge_complete",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-calibration-triangle/dimensional-bridge-complete/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.CalibrationTriangle`.",
  "declaration_id": "TauLib.BookV.GravityField.CalibrationTriangle::dimensional_bridge_complete",
  "declaration_slug": "dimensional-bridge-complete",
  "kind": "theorem",
  "name": "dimensional_bridge_complete",
  "module_name": "TauLib.BookV.GravityField.CalibrationTriangle",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-calibration-triangle/",
  "source_line_start": 178,
  "source_line_end": 181,
  "registry_ids": [
    "V.T50"
  ],
  "related_registry_items": [
    {
      "id": "V.T50",
      "title": "Complete Dimensional Bridge",
      "url": "/registry/object/V.T50/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/CalibrationTriangle.lean#L178-L181",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/CalibrationTriangle.lean#L178-L181",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookV/GravityField/CalibrationTriangle.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/CalibrationTriangle.lean#L178-L181)
- Source range: L178-L181
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T50` — Complete Dimensional Bridge

## Immediate Comment / Docstring

```lean
/-- [V.T50] Complete dimensional bridge: one experimental input
    plus one derived constant determines all SI constants.

    Structural: the triangle has 1 input + 2 derived = 3 vertices. -/
```

## Source Excerpt

```lean
theorem dimensional_bridge_complete :
    calibration_triangle.experimental_inputs +
    calibration_triangle.derived_count =
    calibration_triangle.vertex_count := by rfl
```
