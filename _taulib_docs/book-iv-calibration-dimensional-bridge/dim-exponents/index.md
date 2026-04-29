---
{
  "projection_kind": "taulib_declaration",
  "title": "DimExponents",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge/dim-exponents/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.DimensionalBridge`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionalBridge::DimExponents",
  "declaration_slug": "dim-exponents",
  "kind": "structure",
  "name": "DimExponents",
  "module_name": "TauLib.BookIV.Calibration.DimensionalBridge",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge/",
  "source_line_start": 64,
  "source_line_end": 69,
  "registry_ids": [
    "IV.D32"
  ],
  "related_registry_items": [
    {
      "id": "IV.D32",
      "title": "Tau Physical Scale",
      "url": "/registry/object/IV.D32/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L64-L69",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.DimensionalBridge",
        "url": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L64-L69",
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

- Module: [TauLib.BookIV.Calibration.DimensionalBridge](/verify/taulib/docs/book-iv-calibration-dimensional-bridge/)
- Source path: [`TauLib/BookIV/Calibration/DimensionalBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L64-L69)
- Source range: L64-L69
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D32` — Tau Physical Scale

## Immediate Comment / Docstring

```lean
/-- [IV.D32] Dimensional exponent vector: M^a · L^b · H^c · Q^d. -/
```

## Source Excerpt

```lean
structure DimExponents where
  M : Int
  L : Int
  H : Int
  Q : Int
  deriving Repr, DecidableEq
```
