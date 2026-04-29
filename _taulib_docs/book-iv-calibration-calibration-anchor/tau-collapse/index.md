---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_collapse",
  "permalink": "/verify/taulib/docs/book-iv-calibration-calibration-anchor/tau-collapse/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.CalibrationAnchor`.",
  "declaration_id": "TauLib.BookIV.Calibration.CalibrationAnchor::tau_collapse",
  "declaration_slug": "tau-collapse",
  "kind": "theorem",
  "name": "tau_collapse",
  "module_name": "TauLib.BookIV.Calibration.CalibrationAnchor",
  "module_url": "/verify/taulib/docs/book-iv-calibration-calibration-anchor/",
  "source_line_start": 186,
  "source_line_end": 190,
  "registry_ids": [
    "IV.T06"
  ],
  "related_registry_items": [
    {
      "id": "IV.T06",
      "title": "τ-Collapse (5→1)",
      "url": "/registry/object/IV.T06/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L186-L190",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.CalibrationAnchor",
        "url": "/verify/taulib/docs/book-iv-calibration-calibration-anchor/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L186-L190",
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

- Module: [TauLib.BookIV.Calibration.CalibrationAnchor](/verify/taulib/docs/book-iv-calibration-calibration-anchor/)
- Source path: [`TauLib/BookIV/Calibration/CalibrationAnchor.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L186-L190)
- Source range: L186-L190
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T06` — τ-Collapse (5→1)

## Immediate Comment / Docstring

```lean
/-- [IV.T06] 5→1 collapse: of 5 relational quantities,
    exactly 1 is the anchor and 3 are ι_τ-derived
    (plus 1 SI-exact). -/
```

## Source Excerpt

```lean
theorem tau_collapse :
    relational_quantities.length = 5 ∧
    (relational_quantities.filter (·.status == .Anchor)).length = 1 ∧
    (relational_quantities.filter (·.status == .IotaDerived)).length = 3 ∧
    (relational_quantities.filter (·.status == .SIExact)).length = 1 := by native_decide
```
