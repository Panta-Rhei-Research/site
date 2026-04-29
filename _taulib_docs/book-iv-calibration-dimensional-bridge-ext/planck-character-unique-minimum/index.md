---
{
  "projection_kind": "taulib_declaration",
  "title": "planck_character_unique_minimum",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/planck-character-unique-minimum/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.DimensionalBridgeExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionalBridgeExt::planck_character_unique_minimum",
  "declaration_slug": "planck-character-unique-minimum",
  "kind": "theorem",
  "name": "planck_character_unique_minimum",
  "module_name": "TauLib.BookIV.Calibration.DimensionalBridgeExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/",
  "source_line_start": 277,
  "source_line_end": 278,
  "registry_ids": [
    "IV.P167"
  ],
  "related_registry_items": [
    {
      "id": "IV.P167",
      "title": "Attained minimum",
      "url": "/registry/object/IV.P167/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L277-L278",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L277-L278",
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

- Module: [TauLib.BookIV.Calibration.DimensionalBridgeExt](/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/)
- Source path: [`TauLib/BookIV/Calibration/DimensionalBridgeExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L277-L278)
- Source range: L277-L278
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P167` — Attained minimum

## Immediate Comment / Docstring

```lean
/-- [IV.P167] The Planck character is the unique attained minimum of the
    sector lift functional.

    In the τ-framework, the uncertainty bound Δx·Δp ≥ ℏ_τ is achieved
    by the canonical saturating chain. This is NOT merely an infimum:
    the minimum is actually attained, distinguishing it from the
    conventional QFT treatment. -/
```

## Source Excerpt

```lean
theorem planck_character_unique_minimum :
    planck_character_ext.is_minimum = true := by rfl
```
