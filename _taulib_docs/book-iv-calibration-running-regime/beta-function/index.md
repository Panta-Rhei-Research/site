---
{
  "projection_kind": "taulib_declaration",
  "title": "BetaFunction",
  "permalink": "/verify/taulib/docs/book-iv-calibration-running-regime/beta-function/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.RunningRegime`.",
  "declaration_id": "TauLib.BookIV.Calibration.RunningRegime::BetaFunction",
  "declaration_slug": "beta-function",
  "kind": "structure",
  "name": "BetaFunction",
  "module_name": "TauLib.BookIV.Calibration.RunningRegime",
  "module_url": "/verify/taulib/docs/book-iv-calibration-running-regime/",
  "source_line_start": 42,
  "source_line_end": 50,
  "registry_ids": [
    "IV.D299"
  ],
  "related_registry_items": [
    {
      "id": "IV.D299",
      "title": "Beta function",
      "url": "/registry/object/IV.D299/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L42-L50",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L42-L50",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookIV.Calibration.RunningRegime](/verify/taulib/docs/book-iv-calibration-running-regime/)
- Source path: [`TauLib/BookIV/Calibration/RunningRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L42-L50)
- Source range: L42-L50
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D299` — Beta function

## Immediate Comment / Docstring

```lean
/-- [IV.D299] The beta function β(α_X) = μ·d(α_X)/dμ for a coupling
    α_X(μ). In the τ-framework, the ontic coupling is FIXED and
    β ≡ 0 at the ontic level. What QFT calls "running" is the
    readout functor's scale dependence. -/
```

## Source Excerpt

```lean
structure BetaFunction where
  /-- Sector whose coupling is being examined. -/
  sector : Tau.BookIII.Sectors.Sector
  /-- Ontic beta is identically zero. -/
  ontic_beta_zero : Bool
  ontic_true : ontic_beta_zero = true
  /-- Apparent beta from readout (nonzero in general). -/
  apparent_nonzero : Bool
  deriving Repr
```
