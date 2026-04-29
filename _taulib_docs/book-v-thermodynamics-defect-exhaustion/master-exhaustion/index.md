---
{
  "projection_kind": "taulib_declaration",
  "title": "MasterExhaustion",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/master-exhaustion/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.DefectExhaustion`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.DefectExhaustion::MasterExhaustion",
  "declaration_slug": "master-exhaustion",
  "kind": "structure",
  "name": "MasterExhaustion",
  "module_name": "TauLib.BookV.Thermodynamics.DefectExhaustion",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/",
  "source_line_start": 205,
  "source_line_end": 218,
  "registry_ids": [
    "V.T62"
  ],
  "related_registry_items": [
    {
      "id": "V.T62",
      "title": "Master exhaustion inequality",
      "url": "/registry/object/V.T62/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L205-L218",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.DefectExhaustion",
        "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L205-L218",
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

- Module: [TauLib.BookV.Thermodynamics.DefectExhaustion](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/)
- Source path: [`TauLib/BookV/Thermodynamics/DefectExhaustion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L205-L218)
- Source range: L205-L218
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T62` — Master exhaustion inequality

## Immediate Comment / Docstring

```lean
/-- [V.T62] Master exhaustion inequality, consolidating all three bounds:
    (i)   |D_n| <= (1-iota_tau)^n * N
    (ii)  S_def(n) <= (1-iota_tau)^n * S_def(0)
    (iii) n_coh <= ceil(ln N / ln(1/(1-iota_tau)))

    All controlled by the single parameter iota_tau. -/
```

## Source Excerpt

```lean
structure MasterExhaustion where
  /-- Initial defect count N. -/
  initial_count : Nat
  /-- Initial defect entropy (numer/denom). -/
  initial_s_def_numer : Nat
  /-- Entropy denominator. -/
  initial_s_def_denom : Nat
  /-- Entropy denominator positive. -/
  s_def_denom_pos : initial_s_def_denom > 0
  /-- The coherence horizon bound. -/
  n_coh_bound : Nat
  /-- Horizon bound satisfies constraint. -/
  horizon_valid : n_coh_bound * iota_tau_numer ≤ initial_count * contraction_denom
  deriving Repr
```
