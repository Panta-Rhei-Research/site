---
{
  "projection_kind": "taulib_declaration",
  "title": "h_relational",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/h-relational/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Calibration.DimensionalBridgeExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionalBridgeExt::h_relational",
  "declaration_slug": "h-relational",
  "kind": "def",
  "name": "h_relational",
  "module_name": "TauLib.BookIV.Calibration.DimensionalBridgeExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/",
  "source_line_start": 103,
  "source_line_end": 109,
  "registry_ids": [
    "IV.D294"
  ],
  "related_registry_items": [
    {
      "id": "IV.D294",
      "title": "Planck's constant in relational units",
      "url": "/registry/object/IV.D294/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L103-L109",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L103-L109",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookIV/Calibration/DimensionalBridgeExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L103-L109)
- Source range: L103-L109
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D294` — Planck's constant in relational units

## Immediate Comment / Docstring

```lean
/-- [IV.D294] Planck's constant in relational units: h = M · L² · H.
    Prefactor = 1, exponents M¹ L² H¹ Q⁰. -/
```

## Source Excerpt

```lean
def h_relational : RelationalFormula where
  formula_label := "h = M * L^2 * H"
  exponents := ⟨1, 2, 1, 0⟩
  prefactor_numer := 1
  prefactor_denom := 1
  denom_pos := by omega
  prefactor_label := "1"
```
