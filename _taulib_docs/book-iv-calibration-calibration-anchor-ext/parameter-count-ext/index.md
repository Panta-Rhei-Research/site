---
{
  "projection_kind": "taulib_declaration",
  "title": "parameter_count_ext",
  "permalink": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/parameter-count-ext/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.CalibrationAnchorExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.CalibrationAnchorExt::parameter_count_ext",
  "declaration_slug": "parameter-count-ext",
  "kind": "theorem",
  "name": "parameter_count_ext",
  "module_name": "TauLib.BookIV.Calibration.CalibrationAnchorExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/",
  "source_line_start": 343,
  "source_line_end": 348,
  "registry_ids": [
    "IV.T111"
  ],
  "related_registry_items": [
    {
      "id": "IV.T111",
      "title": "Parameter Count",
      "url": "/registry/object/IV.T111/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L343-L348",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L343-L348",
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
- Source path: [`TauLib/BookIV/Calibration/CalibrationAnchorExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L343-L348)
- Source range: L343-L348
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T111` — Parameter Count

## Immediate Comment / Docstring

```lean
/-- [IV.T111] The τ-framework has exactly ONE free parameter.

    All dimensionless quantities are fixed by ι_τ = 2/(π+e).
    The single free parameter is the neutron mass m_n
    (the calibration anchor). -/
```

## Source Excerpt

```lean
theorem parameter_count_ext :
    -- Exactly 1 free unit
    (collapsed_units.filter (·.status == .Free)).length = 1 ∧
    -- The anchor is sole
    anchor_ext.sole_anchor = true := by
  native_decide
```
