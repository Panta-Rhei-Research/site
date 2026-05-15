---
{
  "projection_kind": "taulib_declaration",
  "title": "weak_coupling_value",
  "permalink": "/corpus/taulib/docs/book-iv-calibration-dimensionless-couplings/weak-coupling-value/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.DimensionlessCouplings`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionlessCouplings::weak_coupling_value",
  "declaration_slug": "weak-coupling-value",
  "kind": "theorem",
  "name": "weak_coupling_value",
  "module_name": "TauLib.BookIV.Calibration.DimensionlessCouplings",
  "module_url": "/corpus/taulib/docs/book-iv-calibration-dimensionless-couplings/",
  "source_line_start": 57,
  "source_line_end": 68,
  "registry_ids": [
    "IV.D277",
    "IV.P161"
  ],
  "related_registry_items": [
    {
      "id": "IV.D277",
      "title": "Electromagnetic self-coupling",
      "url": "/registry/object/IV.D277/"
    },
    {
      "id": "IV.P161",
      "title": "Numerical value",
      "url": "/registry/object/IV.P161/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessCouplings.lean#L57-L68",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.DimensionlessCouplings",
        "url": "/corpus/taulib/docs/book-iv-calibration-dimensionless-couplings/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessCouplings.lean#L57-L68",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookIV.Calibration.DimensionlessCouplings](/corpus/taulib/docs/book-iv-calibration-dimensionless-couplings/)
- Source path: [`TauLib/BookIV/Calibration/DimensionlessCouplings.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessCouplings.lean#L57-L68)
- Source range: L57-L68
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `IV.D277` — Electromagnetic self-coupling
- `IV.P161` — Numerical value

## Immediate Comment / Docstring

```lean
/-- [IV.P161] Numerical value: κ(A;1) is in (341, 342)/1000. -/
```

## Source Excerpt

```lean
theorem weak_coupling_value :
    weak_self_coupling.numer * 1000 > 341 * weak_self_coupling.denom ∧
    weak_self_coupling.numer * 1000 < 342 * weak_self_coupling.denom := by
  constructor <;> native_decide

-- ============================================================
-- EM SELF-COUPLING [IV.D277]
-- ============================================================

/-- [IV.D277] Electromagnetic self-coupling κ(B;2) = ι_τ² ≈ 0.116594.
    Depth 2, χ₊-dominant. -/
abbrev em_self_coupling := kappa_BB
```
