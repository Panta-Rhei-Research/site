---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_collapse_five_to_one",
  "permalink": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/tau-collapse-five-to-one/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.CalibrationAnchorExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.CalibrationAnchorExt::tau_collapse_five_to_one",
  "declaration_slug": "tau-collapse-five-to-one",
  "kind": "theorem",
  "name": "tau_collapse_five_to_one",
  "module_name": "TauLib.BookIV.Calibration.CalibrationAnchorExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/",
  "source_line_start": 130,
  "source_line_end": 138,
  "registry_ids": [
    "IV.T108"
  ],
  "related_registry_items": [
    {
      "id": "IV.T108",
      "title": "tau-Collapse: Five to One",
      "url": "/registry/object/IV.T108/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L130-L138",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.CalibrationAnchorExt",
        "url": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L130-L138",
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

- Module: [TauLib.BookIV.Calibration.CalibrationAnchorExt](/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/)
- Source path: [`TauLib/BookIV/Calibration/CalibrationAnchorExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L130-L138)
- Source range: L130-L138
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T108` — tau-Collapse: Five to One

## Immediate Comment / Docstring

```lean
/-- [IV.T108] τ-Collapse: Five to One.

    Of 5 relational units, 4 are determined (3 by ι_τ + 1 SI-exact),
    leaving exactly 1 free parameter (the neutron mass). -/
```

## Source Excerpt

```lean
theorem tau_collapse_five_to_one :
    collapsed_units.length = 5 ∧
    (collapsed_units.filter (·.status == .Free)).length = 1 ∧
    (collapsed_units.filter (·.status == .IotaDetermined)).length = 3 ∧
    (collapsed_units.filter (·.status == .SIFixed)).length = 1 ∧
    -- The count of independently determined units is 4
    (collapsed_units.filter (·.status == .IotaDetermined)).length +
    (collapsed_units.filter (·.status == .SIFixed)).length = 4 := by
  native_decide
```
