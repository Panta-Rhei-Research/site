---
{
  "projection_kind": "taulib_declaration",
  "title": "correction_factor",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/correction-factor-l129/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Calibration.DimensionlessAlpha`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionlessAlpha::correction_factor",
  "declaration_slug": "correction-factor-l129",
  "kind": "def",
  "name": "correction_factor",
  "module_name": "TauLib.BookIV.Calibration.DimensionlessAlpha",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/",
  "source_line_start": 129,
  "source_line_end": 134,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L129-L134",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.DimensionlessAlpha",
        "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L129-L134",
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

- Module: [TauLib.BookIV.Calibration.DimensionlessAlpha](/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/)
- Source path: [`TauLib/BookIV/Calibration/DimensionlessAlpha.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L129-L134)
- Source range: L129-L134
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The canonical correction factor. -/
```

## Source Excerpt

```lean
def correction_factor : CorrectionFactor where
  near_unity_numer := 1006  -- R ≈ 1.006
  near_unity_denom := 1000
  denom_pos := by omega
  pi_cubed_approx := 31
  pi_cubed_eq := rfl
```
