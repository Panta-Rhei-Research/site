---
{
  "projection_kind": "taulib_declaration",
  "title": "power_hierarchy_ch10",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensionless-couplings2/power-hierarchy-ch10/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.DimensionlessCouplings2`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionlessCouplings2::power_hierarchy_ch10",
  "declaration_slug": "power-hierarchy-ch10",
  "kind": "theorem",
  "name": "power_hierarchy_ch10",
  "module_name": "TauLib.BookIV.Calibration.DimensionlessCouplings2",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensionless-couplings2/",
  "source_line_start": 90,
  "source_line_end": 97,
  "registry_ids": [
    "IV.T106"
  ],
  "related_registry_items": [
    {
      "id": "IV.T106",
      "title": "Power Hierarchy",
      "url": "/registry/object/IV.T106/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessCouplings2.lean#L90-L97",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.DimensionlessCouplings2",
        "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-couplings2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessCouplings2.lean#L90-L97",
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

- Module: [TauLib.BookIV.Calibration.DimensionlessCouplings2](/verify/taulib/docs/book-iv-calibration-dimensionless-couplings2/)
- Source path: [`TauLib/BookIV/Calibration/DimensionlessCouplings2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessCouplings2.lean#L90-L97)
- Source range: L90-L97
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T106` — Power Hierarchy

## Immediate Comment / Docstring

```lean
/-- [IV.T106] Power hierarchy: κ(B;2) = κ(A;1)² and κ(A,C) = κ(A;1)·κ(C;3).
    The EM coupling is the square of the weak coupling; weak-strong is
    the multiplicative closure of weak × strong. -/
```

## Source Excerpt

```lean
theorem power_hierarchy_ch10 :
    -- κ(B;2) = κ(A;1)²
    kappa_BB.numer * (kappa_AA.denom * kappa_AA.denom) =
    (kappa_AA.numer * kappa_AA.numer) * kappa_BB.denom ∧
    -- κ(A,C) = κ(A;1)·κ(C;3) (multiplicative closure)
    kappa_AC.numer * (kappa_AA.denom * kappa_CC.denom) =
    (kappa_AA.numer * kappa_CC.numer) * kappa_AC.denom :=
  ⟨em_is_weak_squared, weak_strong_is_multiplicative⟩
```
