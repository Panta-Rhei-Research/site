---
{
  "projection_kind": "taulib_declaration",
  "title": "RefinedCoherenceHorizon",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/refined-coherence-horizon/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.DefectExhaustion`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.DefectExhaustion::RefinedCoherenceHorizon",
  "declaration_slug": "refined-coherence-horizon",
  "kind": "structure",
  "name": "RefinedCoherenceHorizon",
  "module_name": "TauLib.BookV.Thermodynamics.DefectExhaustion",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/",
  "source_line_start": 182,
  "source_line_end": 193,
  "registry_ids": [
    "V.D89"
  ],
  "related_registry_items": [
    {
      "id": "V.D89",
      "title": "Coherence horizon---refined",
      "url": "/registry/object/V.D89/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L182-L193",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L182-L193",
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
- Source path: [`TauLib/BookV/Thermodynamics/DefectExhaustion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L182-L193)
- Source range: L182-L193
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D89` — Coherence horizon---refined

## Immediate Comment / Docstring

```lean
/-- [V.D89] Coherence horizon (refined): the smallest orbit depth
    at which the defect set is empty.

    n_coh = min{n in N : |D_n| = 0}

    By the Global Defect Exhaustion Theorem, this minimum exists
    and is finite. For |D_0| ~ 10^100, n_coh <= 441 orbit steps. -/
```

## Source Excerpt

```lean
structure RefinedCoherenceHorizon where
  /-- Initial defect count. -/
  d_0 : Nat
  /-- The exact coherence horizon. -/
  n_coh : Nat
  /-- n_coh is the minimum (defect count is zero at n_coh). -/
  is_minimum : Bool := true
  /-- Upper bound from the exhaustion theorem. -/
  upper_bound : Nat
  /-- n_coh does not exceed the upper bound. -/
  within_bound : n_coh ≤ upper_bound
  deriving Repr
```
