---
{
  "projection_kind": "taulib_declaration",
  "title": "omega_coupling_value",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensionless-couplings/omega-coupling-value/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.DimensionlessCouplings`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionlessCouplings::omega_coupling_value",
  "declaration_slug": "omega-coupling-value",
  "kind": "theorem",
  "name": "omega_coupling_value",
  "module_name": "TauLib.BookIV.Calibration.DimensionlessCouplings",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensionless-couplings/",
  "source_line_start": 99,
  "source_line_end": 118,
  "registry_ids": [
    "IV.D280",
    "IV.P164",
    "IV.R247",
    "IV.R248"
  ],
  "related_registry_items": [
    {
      "id": "IV.D280",
      "title": "Weak--gravity cross-coupling",
      "url": "/registry/object/IV.D280/"
    },
    {
      "id": "IV.P164",
      "title": "Numerical value",
      "url": "/registry/object/IV.P164/"
    },
    {
      "id": "IV.R247",
      "title": "Origin of the No Knobs Principle",
      "url": "/registry/object/IV.R247/"
    },
    {
      "id": "IV.R248",
      "title": "Lean verification",
      "url": "/registry/object/IV.R248/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessCouplings.lean#L99-L118",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessCouplings.lean#L99-L118",
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
- Source path: [`TauLib/BookIV/Calibration/DimensionlessCouplings.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessCouplings.lean#L99-L118)
- Source range: L99-L118
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.D280` — Weak--gravity cross-coupling
- `IV.P164` — Numerical value
- `IV.R247` — Origin of the No Knobs Principle
- `IV.R248` — Lean verification

## Immediate Comment / Docstring

```lean
/-- [IV.P164] Numerical value: κ(ω) is in (29, 30)/1000. -/
```

## Source Excerpt

```lean
theorem omega_coupling_value :
    omega_self_coupling.numer * 1000 > 29 * omega_self_coupling.denom ∧
    omega_self_coupling.numer * 1000 < 30 * omega_self_coupling.denom := by
  constructor <;> native_decide

-- [IV.R247] The No Knobs Principle (III.T42) was proved in Book III
-- as a structural consequence of the enrichment ladder.
-- (Structural remark)

-- [IV.R248] The strict ordering κ_D > κ_A > κ_B > κ_C > κ_ω is
-- verified in TauLib.BookIV.Sectors.CouplingFormulas.
-- (Structural remark)

-- ============================================================
-- WEAK-GRAVITY CROSS-COUPLING [IV.D280]
-- ============================================================

/-- [IV.D280] Weak-gravity cross-coupling κ(A,D) = ι_τ(1−ι_τ) ≈ 0.2249.
    Both sectors on base τ¹. Near sin²θ_W = 0.2312. -/
abbrev weak_grav_cross := kappa_AD
```
