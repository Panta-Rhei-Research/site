---
{
  "projection_kind": "taulib_declaration",
  "title": "beta_as_derivative",
  "permalink": "/verify/taulib/docs/book-iv-calibration-running-regime/beta-as-derivative/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.RunningRegime`.",
  "declaration_id": "TauLib.BookIV.Calibration.RunningRegime::beta_as_derivative",
  "declaration_slug": "beta-as-derivative",
  "kind": "theorem",
  "name": "beta_as_derivative",
  "module_name": "TauLib.BookIV.Calibration.RunningRegime",
  "module_url": "/verify/taulib/docs/book-iv-calibration-running-regime/",
  "source_line_start": 95,
  "source_line_end": 97,
  "registry_ids": [
    "IV.P169"
  ],
  "related_registry_items": [
    {
      "id": "IV.P169",
      "title": "Beta Function as Readout Derivative",
      "url": "/registry/object/IV.P169/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L95-L97",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.RunningRegime",
        "url": "/verify/taulib/docs/book-iv-calibration-running-regime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L95-L97",
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

- Module: [TauLib.BookIV.Calibration.RunningRegime](/verify/taulib/docs/book-iv-calibration-running-regime/)
- Source path: [`TauLib/BookIV/Calibration/RunningRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L95-L97)
- Source range: L95-L97
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P169` — Beta Function as Readout Derivative

## Immediate Comment / Docstring

```lean
/-- [IV.P169] The orthodox beta function is the logarithmic derivative
    of the readout functor: β(α_X) = κ(X;d)·dR_μ/d(ln μ).
    Since κ(X;d) is constant, all "running" resides in R_μ. -/
```

## Source Excerpt

```lean
theorem beta_as_derivative :
    -- Ontic coupling is constant → β = 0 at ontic level
    (BetaFunction.mk .D true rfl true).ontic_beta_zero = true := rfl
```
