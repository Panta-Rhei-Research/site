---
{
  "projection_kind": "taulib_declaration",
  "title": "planck_character_sigma_fixed",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/planck-character-sigma-fixed/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.DimensionalBridgeExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionalBridgeExt::planck_character_sigma_fixed",
  "declaration_slug": "planck-character-sigma-fixed",
  "kind": "theorem",
  "name": "planck_character_sigma_fixed",
  "module_name": "TauLib.BookIV.Calibration.DimensionalBridgeExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/",
  "source_line_start": 255,
  "source_line_end": 256,
  "registry_ids": [
    "IV.T112"
  ],
  "related_registry_items": [
    {
      "id": "IV.T112",
      "title": "sigma-Fixed Planck Character",
      "url": "/registry/object/IV.T112/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L255-L256",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L255-L256",
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
- Source path: [`TauLib/BookIV/Calibration/DimensionalBridgeExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L255-L256)
- Source range: L255-L256
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T112` — sigma-Fixed Planck Character

## Immediate Comment / Docstring

```lean
/-- [IV.T112] The Planck character is σ-fixed.
    This is structural: the σ-fixed field is true by construction.
    Physically, ℏ_τ lives at the lemniscate crossing point where
    both lobes contribute equally. -/
```

## Source Excerpt

```lean
theorem planck_character_sigma_fixed :
    planck_character_ext.is_sigma_fixed = true := by rfl
```
