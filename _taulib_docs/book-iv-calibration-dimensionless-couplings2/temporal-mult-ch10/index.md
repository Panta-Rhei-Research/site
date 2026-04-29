---
{
  "projection_kind": "taulib_declaration",
  "title": "temporal_mult_ch10",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensionless-couplings2/temporal-mult-ch10/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.DimensionlessCouplings2`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionlessCouplings2::temporal_mult_ch10",
  "declaration_slug": "temporal-mult-ch10",
  "kind": "theorem",
  "name": "temporal_mult_ch10",
  "module_name": "TauLib.BookIV.Calibration.DimensionlessCouplings2",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensionless-couplings2/",
  "source_line_start": 75,
  "source_line_end": 78,
  "registry_ids": [
    "IV.T105"
  ],
  "related_registry_items": [
    {
      "id": "IV.T105",
      "title": "Temporal Multiplicative Closure",
      "url": "/registry/object/IV.T105/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessCouplings2.lean#L75-L78",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessCouplings2.lean#L75-L78",
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
- Source path: [`TauLib/BookIV/Calibration/DimensionlessCouplings2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessCouplings2.lean#L75-L78)
- Source range: L75-L78
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T105` — Temporal Multiplicative Closure

## Immediate Comment / Docstring

```lean
/-- [IV.T105] Temporal multiplicative closure: κ(A,D) = κ(A;1)·κ(D;1).
    Wraps CouplingFormulas.temporal_multiplicative. -/
```

## Source Excerpt

```lean
theorem temporal_mult_ch10 :
    kappa_AD.numer * (kappa_AA.denom * kappa_DD.denom) =
    kappa_AA.numer * kappa_DD.numer * kappa_AD.denom :=
  temporal_multiplicative
```
