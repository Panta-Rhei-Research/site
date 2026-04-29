---
{
  "projection_kind": "taulib_declaration",
  "title": "RelationalQuantity",
  "permalink": "/verify/taulib/docs/book-iv-calibration-calibration-anchor/relational-quantity/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.CalibrationAnchor`.",
  "declaration_id": "TauLib.BookIV.Calibration.CalibrationAnchor::RelationalQuantity",
  "declaration_slug": "relational-quantity",
  "kind": "structure",
  "name": "RelationalQuantity",
  "module_name": "TauLib.BookIV.Calibration.CalibrationAnchor",
  "module_url": "/verify/taulib/docs/book-iv-calibration-calibration-anchor/",
  "source_line_start": 165,
  "source_line_end": 172,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L165-L172",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L165-L172",
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

- Module: [TauLib.BookIV.Calibration.CalibrationAnchor](/verify/taulib/docs/book-iv-calibration-calibration-anchor/)
- Source path: [`TauLib/BookIV/Calibration/CalibrationAnchor.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L165-L172)
- Source range: L165-L172
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A relational quantity with its collapse status. -/
```

## Source Excerpt

```lean
structure RelationalQuantity where
  /-- Symbol used in the paper (M, L, H, Q, R). -/
  symbol : String
  /-- Physical meaning. -/
  meaning : String
  /-- Collapse status. -/
  status : RelationalStatus
  deriving Repr
```
