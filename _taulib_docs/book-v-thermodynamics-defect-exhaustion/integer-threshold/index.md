---
{
  "projection_kind": "taulib_declaration",
  "title": "IntegerThreshold",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/integer-threshold/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.DefectExhaustion`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.DefectExhaustion::IntegerThreshold",
  "declaration_slug": "integer-threshold",
  "kind": "structure",
  "name": "IntegerThreshold",
  "module_name": "TauLib.BookV.Thermodynamics.DefectExhaustion",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/",
  "source_line_start": 133,
  "source_line_end": 140,
  "registry_ids": [
    "V.L03"
  ],
  "related_registry_items": [
    {
      "id": "V.L03",
      "title": "Integer threshold",
      "url": "/registry/object/V.L03/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L133-L140",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L133-L140",
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
- Source path: [`TauLib/BookV/Thermodynamics/DefectExhaustion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L133-L140)
- Source range: L133-L140
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.L03` — Integer threshold

## Immediate Comment / Docstring

```lean
/-- [V.L03] Integer threshold lemma: for a non-increasing sequence
    of non-negative integers satisfying a_{n+1} <= floor((1-iota_tau) a_n),
    starting from a_0 = N, there exists finite n_0 <= N/iota_tau
    such that a_{n_0} = 0.

    The integer floor operation makes the sequence strictly decreasing
    whenever a_n > 0, ensuring finite termination. -/
```

## Source Excerpt

```lean
structure IntegerThreshold where
  /-- Starting value a_0. -/
  a_0 : Nat
  /-- Threshold depth n_0 where a_{n_0} = 0. -/
  n_0 : Nat
  /-- The threshold is bounded: n_0 * iota_tau_numer <= a_0 * contraction_denom. -/
  bounded : n_0 * iota_tau_numer ≤ a_0 * contraction_denom
  deriving Repr
```
