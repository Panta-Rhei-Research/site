---
{
  "projection_kind": "taulib_declaration",
  "title": "calibration_triangle",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-calibration-triangle/calibration-triangle-l128/",
  "summary_short": "`def` declaration in `TauLib.BookV.GravityField.CalibrationTriangle`.",
  "declaration_id": "TauLib.BookV.GravityField.CalibrationTriangle::calibration_triangle",
  "declaration_slug": "calibration-triangle-l128",
  "kind": "def",
  "name": "calibration_triangle",
  "module_name": "TauLib.BookV.GravityField.CalibrationTriangle",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-calibration-triangle/",
  "source_line_start": 128,
  "source_line_end": 134,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/CalibrationTriangle.lean#L128-L134",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/CalibrationTriangle.lean#L128-L134",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookV/GravityField/CalibrationTriangle.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/CalibrationTriangle.lean#L128-L134)
- Source range: L128-L134
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The canonical calibration triangle. -/
```

## Source Excerpt

```lean
def calibration_triangle : CalibrationTriangle where
  vertex_count := 3
  is_triangle := by rfl
  experimental_inputs := 1
  one_input := by rfl
  derived_count := 2
  two_derived := by rfl
```
