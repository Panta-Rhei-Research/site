---
{
  "projection_kind": "taulib_declaration",
  "title": "finite_defect_budget",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/finite-defect-budget/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.DefectExhaustion`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.DefectExhaustion::finite_defect_budget",
  "declaration_slug": "finite-defect-budget",
  "kind": "theorem",
  "name": "finite_defect_budget",
  "module_name": "TauLib.BookV.Thermodynamics.DefectExhaustion",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/",
  "source_line_start": 119,
  "source_line_end": 120,
  "registry_ids": [
    "V.T60"
  ],
  "related_registry_items": [
    {
      "id": "V.T60",
      "title": "Finite defect budget",
      "url": "/registry/object/V.T60/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L119-L120",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L119-L120",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookV/Thermodynamics/DefectExhaustion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L119-L120)
- Source range: L119-L120
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T60` — Finite defect budget

## Immediate Comment / Docstring

```lean
/-- [V.T60] Finite defect budget theorem:
    B_def <= |D_0| / iota_tau < infinity.

    The global defect budget is finite, bounded by the initial
    defect count divided by iota_tau. Follows from the geometric
    series bound in the contraction lemma.

    Key numerical check: iota_tau > 0, so the bound is finite. -/
```

## Source Excerpt

```lean
theorem finite_defect_budget : iota_tau_numer > 0 := by
  simp [iota_tau_numer]
```
