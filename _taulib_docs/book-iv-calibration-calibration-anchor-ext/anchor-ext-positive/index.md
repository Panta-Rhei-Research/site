---
{
  "projection_kind": "taulib_declaration",
  "title": "anchor_ext_positive",
  "permalink": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/anchor-ext-positive/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.CalibrationAnchorExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.CalibrationAnchorExt::anchor_ext_positive",
  "declaration_slug": "anchor-ext-positive",
  "kind": "theorem",
  "name": "anchor_ext_positive",
  "module_name": "TauLib.BookIV.Calibration.CalibrationAnchorExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/",
  "source_line_start": 327,
  "source_line_end": 328,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L327-L328",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L327-L328",
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
- Source path: [`TauLib/BookIV/Calibration/CalibrationAnchorExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L327-L328)
- Source range: L327-L328
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The anchor mass numerator is positive. -/
```

## Source Excerpt

```lean
theorem anchor_ext_positive :
    anchor_ext.neutron_mass_kg_numer > 0 := by native_decide
```
