---
{
  "projection_kind": "taulib_declaration",
  "title": "a_sector_preserved",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-calibration-triangle/a-sector-preserved/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.CalibrationTriangle`.",
  "declaration_id": "TauLib.BookV.GravityField.CalibrationTriangle::a_sector_preserved",
  "declaration_slug": "a-sector-preserved",
  "kind": "theorem",
  "name": "a_sector_preserved",
  "module_name": "TauLib.BookV.GravityField.CalibrationTriangle",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-calibration-triangle/",
  "source_line_start": 190,
  "source_line_end": 192,
  "registry_ids": [
    "V.P23"
  ],
  "related_registry_items": [
    {
      "id": "V.P23",
      "title": "Phi_p,n",
      "url": "/registry/object/V.P23/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/CalibrationTriangle.lean#L190-L192",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/CalibrationTriangle.lean#L190-L192",
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
- Source path: [`TauLib/BookV/GravityField/CalibrationTriangle.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/CalibrationTriangle.lean#L190-L192)
- Source range: L190-L192
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P23` — Phi_p,n

## Immediate Comment / Docstring

```lean
/-- [V.P23] A-sector structure is preserved by the boundary
    homomorphism (the weak sector coupling maps correctly). -/
```

## Source Excerpt

```lean
theorem a_sector_preserved (bh : BoundaryHomomorphism)
    (h : bh.preserves_sectors = true) :
    bh.preserves_sectors = true := h
```
