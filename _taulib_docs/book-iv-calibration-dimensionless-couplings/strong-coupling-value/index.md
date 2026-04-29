---
{
  "projection_kind": "taulib_declaration",
  "title": "strong_coupling_value",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensionless-couplings/strong-coupling-value/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.DimensionlessCouplings`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionlessCouplings::strong_coupling_value",
  "declaration_slug": "strong-coupling-value",
  "kind": "theorem",
  "name": "strong_coupling_value",
  "module_name": "TauLib.BookIV.Calibration.DimensionlessCouplings",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensionless-couplings/",
  "source_line_start": 85,
  "source_line_end": 96,
  "registry_ids": [
    "IV.D279",
    "IV.P163"
  ],
  "related_registry_items": [
    {
      "id": "IV.D279",
      "title": "Omega self-coupling",
      "url": "/registry/object/IV.D279/"
    },
    {
      "id": "IV.P163",
      "title": "Numerical value",
      "url": "/registry/object/IV.P163/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessCouplings.lean#L85-L96",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessCouplings.lean#L85-L96",
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
- Source path: [`TauLib/BookIV/Calibration/DimensionlessCouplings.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessCouplings.lean#L85-L96)
- Source range: L85-L96
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.D279` — Omega self-coupling
- `IV.P163` — Numerical value

## Immediate Comment / Docstring

```lean
/-- [IV.P163] Numerical value: κ(C;3) is in (60, 61)/1000. -/
```

## Source Excerpt

```lean
theorem strong_coupling_value :
    strong_self_coupling.numer * 1000 > 60 * strong_self_coupling.denom ∧
    strong_self_coupling.numer * 1000 < 61 * strong_self_coupling.denom := by
  constructor <;> native_decide

-- ============================================================
-- OMEGA SELF-COUPLING [IV.D279]
-- ============================================================

/-- [IV.D279] Omega self-coupling κ(ω) = ι_τ³/(1+ι_τ) ≈ 0.02968.
    Crossing-point readout. The smallest primitive coupling. -/
abbrev omega_self_coupling := kappa_BC
```
