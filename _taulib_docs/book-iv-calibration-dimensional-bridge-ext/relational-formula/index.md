---
{
  "projection_kind": "taulib_declaration",
  "title": "RelationalFormula",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/relational-formula/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.DimensionalBridgeExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionalBridgeExt::RelationalFormula",
  "declaration_slug": "relational-formula",
  "kind": "structure",
  "name": "RelationalFormula",
  "module_name": "TauLib.BookIV.Calibration.DimensionalBridgeExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/",
  "source_line_start": 68,
  "source_line_end": 81,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L68-L81",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L68-L81",
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
- Source path: [`TauLib/BookIV/Calibration/DimensionalBridgeExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L68-L81)
- Source range: L68-L81
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A relational-unit formula for an SI constant:
    formula_label × DimExponents × prefactor_label. -/
```

## Source Excerpt

```lean
structure RelationalFormula where
  /-- Human-readable formula string. -/
  formula_label : String
  /-- Dimensional exponents M^a · L^b · H^c · Q^d (Int for negative). -/
  exponents : DimExponents
  /-- Prefactor numerator (rational part). -/
  prefactor_numer : Nat
  /-- Prefactor denominator (rational part). -/
  prefactor_denom : Nat
  /-- Denominator is positive. -/
  denom_pos : prefactor_denom > 0
  /-- Symbolic label for the prefactor (e.g., "1", "pi_sq_over_32"). -/
  prefactor_label : String
  deriving Repr
```
