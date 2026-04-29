---
{
  "projection_kind": "taulib_declaration",
  "title": "RegimeTransition",
  "permalink": "/verify/taulib/docs/book-iv-calibration-running-regime/regime-transition/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.RunningRegime`.",
  "declaration_id": "TauLib.BookIV.Calibration.RunningRegime::RegimeTransition",
  "declaration_slug": "regime-transition",
  "kind": "structure",
  "name": "RegimeTransition",
  "module_name": "TauLib.BookIV.Calibration.RunningRegime",
  "module_url": "/verify/taulib/docs/book-iv-calibration-running-regime/",
  "source_line_start": 137,
  "source_line_end": 145,
  "registry_ids": [
    "IV.D303"
  ],
  "related_registry_items": [
    {
      "id": "IV.D303",
      "title": "Regime transition",
      "url": "/registry/object/IV.D303/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L137-L145",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L137-L145",
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
- Source path: [`TauLib/BookIV/Calibration/RunningRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L137-L145)
- Source range: L137-L145
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D303` — Regime transition

## Immediate Comment / Docstring

```lean
/-- [IV.D303] A regime transition at scale μ_*: a discontinuity in the
    entropy splitting where S_vis jumps as a new sector becomes visible. -/
```

## Source Excerpt

```lean
structure RegimeTransition where
  /-- Transition scale (encoded as scaled Nat). -/
  scale_numer : Nat
  /-- Sectors involved in the transition. -/
  sector_from : Tau.BookIII.Sectors.Sector
  sector_to : Tau.BookIII.Sectors.Sector
  /-- Different sectors. -/
  distinct : sector_from ≠ sector_to
  deriving Repr
```
