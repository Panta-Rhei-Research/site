---
{
  "projection_kind": "taulib_declaration",
  "title": "bulk_numer",
  "permalink": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-numer/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Calibration.MassRatioFormula`.",
  "declaration_id": "TauLib.BookIV.Calibration.MassRatioFormula::bulk_numer",
  "declaration_slug": "bulk-numer",
  "kind": "def",
  "name": "bulk_numer",
  "module_name": "TauLib.BookIV.Calibration.MassRatioFormula",
  "module_url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/",
  "source_line_start": 89,
  "source_line_end": 89,
  "registry_ids": [
    "IV.D46"
  ],
  "related_registry_items": [
    {
      "id": "IV.D46",
      "title": "Mass Ratio Bulk Term",
      "url": "/registry/object/IV.D46/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L89-L89",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.MassRatioFormula",
        "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L89-L89",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookIV.Calibration.MassRatioFormula](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/)
- Source path: [`TauLib/BookIV/Calibration/MassRatioFormula.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L89-L89)
- Source range: L89-L89
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `IV.D46` — Mass Ratio Bulk Term

## Immediate Comment / Docstring

```lean
/-- [IV.D46] ι_τ^(-7) numerator: (10⁶)⁷ = 10⁴². -/
```

## Source Excerpt

```lean
def bulk_numer : Nat := iotaD * iotaD * iotaD * iotaD * iotaD * iotaD * iotaD
```
