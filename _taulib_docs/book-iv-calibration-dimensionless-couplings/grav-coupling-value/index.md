---
{
  "projection_kind": "taulib_declaration",
  "title": "grav_coupling_value",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensionless-couplings/grav-coupling-value/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.DimensionlessCouplings`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionlessCouplings::grav_coupling_value",
  "declaration_slug": "grav-coupling-value",
  "kind": "theorem",
  "name": "grav_coupling_value",
  "module_name": "TauLib.BookIV.Calibration.DimensionlessCouplings",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensionless-couplings/",
  "source_line_start": 43,
  "source_line_end": 54,
  "registry_ids": [
    "IV.D276",
    "IV.P160"
  ],
  "related_registry_items": [
    {
      "id": "IV.D276",
      "title": "Weak self-coupling",
      "url": "/registry/object/IV.D276/"
    },
    {
      "id": "IV.P160",
      "title": "Numerical value",
      "url": "/registry/object/IV.P160/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessCouplings.lean#L43-L54",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessCouplings.lean#L43-L54",
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
- Source path: [`TauLib/BookIV/Calibration/DimensionlessCouplings.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessCouplings.lean#L43-L54)
- Source range: L43-L54
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.D276` — Weak self-coupling
- `IV.P160` — Numerical value

## Immediate Comment / Docstring

```lean
/-- [IV.P160] Numerical value: κ(D;1) is in (658, 659)/1000. -/
```

## Source Excerpt

```lean
theorem grav_coupling_value :
    grav_self_coupling.numer * 1000 > 658 * grav_self_coupling.denom ∧
    grav_self_coupling.numer * 1000 < 659 * grav_self_coupling.denom := by
  constructor <;> native_decide

-- ============================================================
-- WEAK SELF-COUPLING [IV.D276]
-- ============================================================

/-- [IV.D276] Weak self-coupling κ(A;1) = ι_τ ≈ 0.341304.
    Depth 1, balanced polarity. Equals the master constant. -/
abbrev weak_self_coupling := kappa_AA
```
