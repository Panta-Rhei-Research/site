---
{
  "projection_kind": "taulib_declaration",
  "title": "GravityFrontier",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge/gravity-frontier/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.DimensionalBridge`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionalBridge::GravityFrontier",
  "declaration_slug": "gravity-frontier",
  "kind": "structure",
  "name": "GravityFrontier",
  "module_name": "TauLib.BookIV.Calibration.DimensionalBridge",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge/",
  "source_line_start": 270,
  "source_line_end": 279,
  "registry_ids": [
    "IV.R08"
  ],
  "related_registry_items": [
    {
      "id": "IV.R08",
      "title": "G Frontier",
      "url": "/registry/object/IV.R08/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L270-L279",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L270-L279",
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
- Source path: [`TauLib/BookIV/Calibration/DimensionalBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L270-L279)
- Source range: L270-L279
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R08` — G Frontier

## Immediate Comment / Docstring

```lean
/-- [IV.R08] The gravitational constant G is the remaining frontier.
    Dimensional skeleton: G = C_D · L³ H² / M
    where C_D is a base-sector geometric invariant derived in Book V.

    G requires the D-sector base geometry (τ¹ curvature analysis)
    which is outside Book IV's scope. We record the structural skeleton
    and the SI target for future cross-reference. -/
```

## Source Excerpt

```lean
structure GravityFrontier where
  /-- Dimensional exponents: M⁻¹ L³ H². -/
  exponents : DimExponents := ⟨-1, 3, 2, 0⟩
  /-- The unknown base-sector coefficient (from Book V). -/
  coeff_label : String := "C_D"
  /-- SI target for comparison. -/
  si_target : SIConstant := si_gravitational
  /-- This is deferred to Book V. -/
  deferred : Bool := true
  deriving Repr
```
