---
{
  "projection_kind": "taulib_declaration",
  "title": "ClosingIdentity",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/closing-identity/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.DimensionalBridgeExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionalBridgeExt::ClosingIdentity",
  "declaration_slug": "closing-identity",
  "kind": "structure",
  "name": "ClosingIdentity",
  "module_name": "TauLib.BookIV.Calibration.DimensionalBridgeExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/",
  "source_line_start": 367,
  "source_line_end": 378,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L367-L378",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.DimensionalBridgeExt",
        "url": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L367-L378",
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

- Module: [TauLib.BookIV.Calibration.DimensionalBridgeExt](/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/)
- Source path: [`TauLib/BookIV/Calibration/DimensionalBridgeExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L367-L378)
- Source range: L367-L378
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The gravitational closing identity connects α_G to α through
    the lemniscate √3 factor and a first-order correction c₁ = 3/π.

    α_G = α¹⁸ · √3 · (1 − (3/π)·α)

    This structure records the key integer/rational parameters. -/
```

## Source Excerpt

```lean
structure ClosingIdentity where
  /-- Exponent of α in the leading term. -/
  alpha_exponent : Nat
  /-- The √3 comes from lemniscate geometry (3-fold sectors). -/
  sqrt3_origin : String
  /-- First-order correction numerator: 3. -/
  correction_numer : Nat
  /-- First-order correction denominator label: π. -/
  correction_denom_label : String
  /-- G deviation from CODATA at c₁ = 3/π. -/
  deviation_ppm : Nat  -- 3 ppm
  deriving Repr
```
