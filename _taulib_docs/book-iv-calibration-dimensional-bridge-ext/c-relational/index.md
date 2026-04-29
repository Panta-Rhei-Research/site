---
{
  "projection_kind": "taulib_declaration",
  "title": "c_relational",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/c-relational/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Calibration.DimensionalBridgeExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionalBridgeExt::c_relational",
  "declaration_slug": "c-relational",
  "kind": "def",
  "name": "c_relational",
  "module_name": "TauLib.BookIV.Calibration.DimensionalBridgeExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/",
  "source_line_start": 89,
  "source_line_end": 95,
  "registry_ids": [
    "IV.D293"
  ],
  "related_registry_items": [
    {
      "id": "IV.D293",
      "title": "Speed of light in relational units",
      "url": "/registry/object/IV.D293/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L89-L95",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L89-L95",
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
- Source path: [`TauLib/BookIV/Calibration/DimensionalBridgeExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L89-L95)
- Source range: L89-L95
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D293` — Speed of light in relational units

## Immediate Comment / Docstring

```lean
/-- [IV.D293] Speed of light in relational units: c = L · H.
    Prefactor = 1, exponents M⁰ L¹ H¹ Q⁰. -/
```

## Source Excerpt

```lean
def c_relational : RelationalFormula where
  formula_label := "c = L * H"
  exponents := ⟨0, 1, 1, 0⟩
  prefactor_numer := 1
  prefactor_denom := 1
  denom_pos := by omega
  prefactor_label := "1"
```
