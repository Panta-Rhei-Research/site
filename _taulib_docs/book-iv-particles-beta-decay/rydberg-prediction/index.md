---
{
  "projection_kind": "taulib_declaration",
  "title": "RydbergPrediction",
  "permalink": "/verify/taulib/docs/book-iv-particles-beta-decay/rydberg-prediction/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.BetaDecay`.",
  "declaration_id": "TauLib.BookIV.Particles.BetaDecay::RydbergPrediction",
  "declaration_slug": "rydberg-prediction",
  "kind": "structure",
  "name": "RydbergPrediction",
  "module_name": "TauLib.BookIV.Particles.BetaDecay",
  "module_url": "/verify/taulib/docs/book-iv-particles-beta-decay/",
  "source_line_start": 201,
  "source_line_end": 208,
  "registry_ids": [
    "IV.T86"
  ],
  "related_registry_items": [
    {
      "id": "IV.T86",
      "title": "Rydberg prediction at 0.025 ppm",
      "url": "/registry/object/IV.T86/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L201-L208",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.BetaDecay",
        "url": "/verify/taulib/docs/book-iv-particles-beta-decay/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L201-L208",
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

- Module: [TauLib.BookIV.Particles.BetaDecay](/verify/taulib/docs/book-iv-particles-beta-decay/)
- Source path: [`TauLib/BookIV/Particles/BetaDecay.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L201-L208)
- Source range: L201-L208
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T86` — Rydberg prediction at 0.025 ppm

## Immediate Comment / Docstring

```lean
/-- [IV.T86] τ-predicted R_∞ matches CODATA to ~0.026 ppm
    (seven significant figures), inheriting the 0.025 ppm
    precision of the electron mass prediction.

    R_∞^(τ) ≈ 10,973,731.29 m⁻¹ vs CODATA 10,973,731.568157 m⁻¹. -/
```

## Source Excerpt

```lean
structure RydbergPrediction where
  /-- Deviation (ppm ×1000). -/
  deviation_ppm_x1000 : Nat := 26
  /-- Significant figures matched. -/
  sig_figs : Nat := 7
  /-- Precision inherited from m_e. -/
  inherited_from : String := "m_e at 0.025 ppm"
  deriving Repr
```
