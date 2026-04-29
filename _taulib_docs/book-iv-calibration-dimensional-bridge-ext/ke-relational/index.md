---
{
  "projection_kind": "taulib_declaration",
  "title": "ke_relational",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/ke-relational/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Calibration.DimensionalBridgeExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionalBridgeExt::ke_relational",
  "declaration_slug": "ke-relational",
  "kind": "def",
  "name": "ke_relational",
  "module_name": "TauLib.BookIV.Calibration.DimensionalBridgeExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/",
  "source_line_start": 118,
  "source_line_end": 124,
  "registry_ids": [
    "IV.D295"
  ],
  "related_registry_items": [
    {
      "id": "IV.D295",
      "title": "Coulomb constant in relational units",
      "url": "/registry/object/IV.D295/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L118-L124",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L118-L124",
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
- Source path: [`TauLib/BookIV/Calibration/DimensionalBridgeExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L118-L124)
- Source range: L118-L124
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D295` — Coulomb constant in relational units

## Immediate Comment / Docstring

```lean
/-- [IV.D295] Coulomb constant in relational units:
    k_e = (π²/32) · Q²/(M · H · L³).
    Prefactor = π²/32, exponents M⁻¹ L⁻³ H⁻¹ Q². -/
```

## Source Excerpt

```lean
def ke_relational : RelationalFormula where
  formula_label := "k_e = (pi^2/32) * Q^2/(M*H*L^3)"
  exponents := ⟨-1, -3, -1, 2⟩
  prefactor_numer := 1
  prefactor_denom := 32
  denom_pos := by omega
  prefactor_label := "pi_sq_over_32"
```
