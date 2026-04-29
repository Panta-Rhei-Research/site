---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L420",
  "permalink": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/eval-l420/",
  "summary_short": "`eval` declaration in `TauLib.BookIV.Calibration.CalibrationAnchorExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.CalibrationAnchorExt::#eval:420",
  "declaration_slug": "eval-l420",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookIV.Calibration.CalibrationAnchorExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/",
  "source_line_start": 420,
  "source_line_end": 420,
  "registry_ids": [
    "IV.R262",
    "IV.R263",
    "IV.R264",
    "IV.R265",
    "IV.R266",
    "IV.R267"
  ],
  "related_registry_items": [
    {
      "id": "IV.R262",
      "title": "What the paper got right",
      "url": "/registry/object/IV.R262/"
    },
    {
      "id": "IV.R263",
      "title": "Not a numerical fit",
      "url": "/registry/object/IV.R263/"
    },
    {
      "id": "IV.R264",
      "title": "The Planck mass in tau-physics",
      "url": "/registry/object/IV.R264/"
    },
    {
      "id": "IV.R265",
      "title": "One input, not zero",
      "url": "/registry/object/IV.R265/"
    },
    {
      "id": "IV.R266",
      "title": "Lean formalization",
      "url": "/registry/object/IV.R266/"
    },
    {
      "id": "IV.R267",
      "title": "Falsifiability",
      "url": "/registry/object/IV.R267/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L420-L420",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.CalibrationAnchorExt",
        "url": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L420-L420",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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

- Module: [TauLib.BookIV.Calibration.CalibrationAnchorExt](/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/)
- Source path: [`TauLib/BookIV/Calibration/CalibrationAnchorExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L420-L420)
- Source range: L420-L420
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- `IV.R262` — What the paper got right
- `IV.R263` — Not a numerical fit
- `IV.R264` — The Planck mass in tau-physics
- `IV.R265` — One input, not zero
- `IV.R266` — Lean formalization
- `IV.R267` — Falsifiability

## Immediate Comment / Docstring

```lean
-- ============================================================
-- REMARKS (comment-only)
-- ============================================================

-- [IV.R262] What the paper got right: the Springer Nature paper
-- (Dec 2024) correctly identified 5 relational units (M, L, H, Q, R)
-- and the structural formulas c = L·H, h = M·L²·H, etc.
-- What the τ-framework adds: collapsing 5 → 1 via ι_τ.

-- [IV.R263] Not a numerical fit: the mass ratio R is DERIVED from
-- spectral geometry (Epstein zeta, lemniscate 3-fold, holonomy),
-- not fitted to CODATA. Zero free parameters in the R formula.

-- [IV.R264] The Planck mass in τ-physics: m_P is NOT fundamental.
-- It is a dimensional combination m_P = √(ℏc/G), fourth in
-- ontological priority: n → p → e⁻ → m_P.

-- [IV.R265] One input, not zero: the τ-framework is NOT a Theory
-- of Everything that predicts all constants from pure mathematics.
-- It reduces ~26 Standard Model parameters to 1 anchor + ι_τ.

-- [IV.R266] Lean formalization: every formalizable claim in ch12
-- has a corresponding Lean 4 theorem in CalibrationAnchor.lean and
-- CalibrationAnchorExt.lean, with ZERO sorry.

-- [IV.R267] Falsifiability: the R formula R = ι_τ^(-7) − (√3+π³α²)·ι_τ^(-2)
-- predicts m_e = 0.510998937 MeV to 0.025 ppm. Any future measurement
-- outside this range would falsify the formula. The formula is NOT
-- adjustable — there are no tunable parameters.

-- ============================================================
-- SMOKE TESTS
-- ============================================================

-- Relational units
```

## Source Excerpt

```lean
#eval five_relational_units.length                                -- 5
```
