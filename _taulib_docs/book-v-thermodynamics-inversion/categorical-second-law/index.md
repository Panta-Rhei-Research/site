---
{
  "projection_kind": "taulib_declaration",
  "title": "CategoricalSecondLaw",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-inversion/categorical-second-law/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.Inversion`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.Inversion::CategoricalSecondLaw",
  "declaration_slug": "categorical-second-law",
  "kind": "structure",
  "name": "CategoricalSecondLaw",
  "module_name": "TauLib.BookV.Thermodynamics.Inversion",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-inversion/",
  "source_line_start": 89,
  "source_line_end": 100,
  "registry_ids": [
    "V.T55"
  ],
  "related_registry_items": [
    {
      "id": "V.T55",
      "title": "The Categorical Second Law",
      "url": "/registry/object/V.T55/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L89-L100",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.Inversion",
        "url": "/verify/taulib/docs/book-v-thermodynamics-inversion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L89-L100",
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

- Module: [TauLib.BookV.Thermodynamics.Inversion](/verify/taulib/docs/book-v-thermodynamics-inversion/)
- Source path: [`TauLib/BookV/Thermodynamics/Inversion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L89-L100)
- Source range: L89-L100
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T55` — The Categorical Second Law

## Immediate Comment / Docstring

```lean
/-- [V.T55] The Categorical Second Law.

    Along the alpha-orbit on base tau^1, defect entropy is
    monotonically non-increasing. The contraction factor is
    (1 - iota_tau) = kappa(D;1), the gravitational self-coupling.

    This inverts the classical second law: classical entropy increases,
    but defect entropy (the physically meaningful component) decreases. -/
```

## Source Excerpt

```lean
structure CategoricalSecondLaw where
  /-- Contraction factor numerator (1 - iota_tau). -/
  contraction_factor_numer : Nat
  /-- Contraction factor denominator. -/
  contraction_factor_denom : Nat
  /-- Denominator positive. -/
  denom_pos : contraction_factor_denom > 0
  /-- The contraction factor is strictly less than 1. -/
  strict_contraction : contraction_factor_numer < contraction_factor_denom
  /-- Scope: tau-effective. -/
  scope : String := "tau-effective"
  deriving Repr
```
