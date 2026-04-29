---
{
  "projection_kind": "taulib_declaration",
  "title": "ChowlaSelbergTerms",
  "permalink": "/verify/taulib/docs/book-iv-calibration-epstein-zeta/chowla-selberg-terms/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.EpsteinZeta`.",
  "declaration_id": "TauLib.BookIV.Calibration.EpsteinZeta::ChowlaSelbergTerms",
  "declaration_slug": "chowla-selberg-terms",
  "kind": "structure",
  "name": "ChowlaSelbergTerms",
  "module_name": "TauLib.BookIV.Calibration.EpsteinZeta",
  "module_url": "/verify/taulib/docs/book-iv-calibration-epstein-zeta/",
  "source_line_start": 105,
  "source_line_end": 114,
  "registry_ids": [
    "IV.D41"
  ],
  "related_registry_items": [
    {
      "id": "IV.D41",
      "title": "Chowla-Selberg Decomposition",
      "url": "/registry/object/IV.D41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/EpsteinZeta.lean#L105-L114",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.EpsteinZeta",
        "url": "/verify/taulib/docs/book-iv-calibration-epstein-zeta/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/EpsteinZeta.lean#L105-L114",
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

- Module: [TauLib.BookIV.Calibration.EpsteinZeta](/verify/taulib/docs/book-iv-calibration-epstein-zeta/)
- Source path: [`TauLib/BookIV/Calibration/EpsteinZeta.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/EpsteinZeta.lean#L105-L114)
- Source range: L105-L114
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D41` — Chowla-Selberg Decomposition

## Immediate Comment / Docstring

```lean
/-- [IV.D41] The three terms of the Chowla-Selberg decomposition.

    Z(s; iι_τ) = Term1 + Term2 + Term3

    Term1 = 2ζ(2s)              (constant, negligible at large s)
    Term2 = C(s)·ι_τ^(1-2s)    (leading power-law term)
    Term3 = Bessel_sum           (exponentially suppressed) -/
```

## Source Excerpt

```lean
structure ChowlaSelbergTerms where
  /-- Evaluation point s. -/
  s : Nat
  /-- Leading exponent: 1 - 2s. -/
  leading_exp : Int
  /-- Leading exponent equals 1 - 2s. -/
  exp_formula : leading_exp = 1 - 2 * (s : Int)
  /-- The constant term 2ζ(2s) is negligible for s ≥ 2. -/
  constant_negligible : s ≥ 2
  deriving Repr
```
