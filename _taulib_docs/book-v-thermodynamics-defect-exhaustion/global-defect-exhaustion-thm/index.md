---
{
  "projection_kind": "taulib_declaration",
  "title": "GlobalDefectExhaustionThm",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/global-defect-exhaustion-thm/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.DefectExhaustion`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.DefectExhaustion::GlobalDefectExhaustionThm",
  "declaration_slug": "global-defect-exhaustion-thm",
  "kind": "structure",
  "name": "GlobalDefectExhaustionThm",
  "module_name": "TauLib.BookV.Thermodynamics.DefectExhaustion",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/",
  "source_line_start": 160,
  "source_line_end": 169,
  "registry_ids": [
    "V.T61"
  ],
  "related_registry_items": [
    {
      "id": "V.T61",
      "title": "Global Defect Exhaustion",
      "url": "/registry/object/V.T61/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L160-L169",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L160-L169",
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
- Source path: [`TauLib/BookV/Thermodynamics/DefectExhaustion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L160-L169)
- Source range: L160-L169
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T61` — Global Defect Exhaustion

## Immediate Comment / Docstring

```lean
/-- [V.T61] Global Defect Exhaustion Theorem: there exists a finite
    orbit depth n_coh < infinity such that |D_n| = 0 and S_def(n) = 0
    for all n >= n_coh.

    The coherence horizon is bounded:
    n_coh <= ceil(ln|D_0| / ln(1/(1-iota_tau))) -/
```

## Source Excerpt

```lean
structure GlobalDefectExhaustionThm where
  /-- Initial defect count. -/
  d_0 : Nat
  /-- The coherence horizon depth. -/
  n_coh : Nat
  /-- After n_coh, defect count is zero. -/
  exhausted : Bool := true
  /-- Bound on n_coh. -/
  coh_bound : n_coh * iota_tau_numer ≤ d_0 * contraction_denom
  deriving Repr
```
