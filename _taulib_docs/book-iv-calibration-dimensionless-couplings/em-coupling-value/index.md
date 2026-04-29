---
{
  "projection_kind": "taulib_declaration",
  "title": "em_coupling_value",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensionless-couplings/em-coupling-value/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.DimensionlessCouplings`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionlessCouplings::em_coupling_value",
  "declaration_slug": "em-coupling-value",
  "kind": "theorem",
  "name": "em_coupling_value",
  "module_name": "TauLib.BookIV.Calibration.DimensionlessCouplings",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensionless-couplings/",
  "source_line_start": 71,
  "source_line_end": 82,
  "registry_ids": [
    "IV.D278",
    "IV.P162"
  ],
  "related_registry_items": [
    {
      "id": "IV.D278",
      "title": "Strong self-coupling",
      "url": "/registry/object/IV.D278/"
    },
    {
      "id": "IV.P162",
      "title": "Numerical value",
      "url": "/registry/object/IV.P162/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessCouplings.lean#L71-L82",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.DimensionlessCouplings",
        "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-couplings/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessCouplings.lean#L71-L82",
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

- Module: [TauLib.BookIV.Calibration.DimensionlessCouplings](/verify/taulib/docs/book-iv-calibration-dimensionless-couplings/)
- Source path: [`TauLib/BookIV/Calibration/DimensionlessCouplings.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessCouplings.lean#L71-L82)
- Source range: L71-L82
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.D278` — Strong self-coupling
- `IV.P162` — Numerical value

## Immediate Comment / Docstring

```lean
/-- [IV.P162] Numerical value: κ(B;2) is in (116, 117)/1000. -/
```

## Source Excerpt

```lean
theorem em_coupling_value :
    em_self_coupling.numer * 1000 > 116 * em_self_coupling.denom ∧
    em_self_coupling.numer * 1000 < 117 * em_self_coupling.denom := by
  constructor <;> native_decide

-- ============================================================
-- STRONG SELF-COUPLING [IV.D278]
-- ============================================================

/-- [IV.D278] Strong self-coupling κ(C;3) = ι_τ³/(1−ι_τ) ≈ 0.06046.
    Depth 3, χ₋-dominant. Confinement coupling. -/
abbrev strong_self_coupling := kappa_CC
```
