---
{
  "projection_kind": "taulib_declaration",
  "title": "finite_irreversibility",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/finite-irreversibility/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.DefectExhaustion`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.DefectExhaustion::finite_irreversibility",
  "declaration_slug": "finite-irreversibility",
  "kind": "theorem",
  "name": "finite_irreversibility",
  "module_name": "TauLib.BookV.Thermodynamics.DefectExhaustion",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/",
  "source_line_start": 265,
  "source_line_end": 267,
  "registry_ids": [
    "V.C07"
  ],
  "related_registry_items": [
    {
      "id": "V.C07",
      "title": "Finite irreversibility",
      "url": "/registry/object/V.C07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L265-L267",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L265-L267",
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
- Source path: [`TauLib/BookV/Thermodynamics/DefectExhaustion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L265-L267)
- Source range: L265-L267
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.C07` — Finite irreversibility

## Immediate Comment / Docstring

```lean
/-- [V.C07] Finite irreversibility: every irreversible process
    draws from the finite defect budget B_def <= |D_0|/iota_tau.

    After the coherence horizon, no further irreversible processes
    occur. Friction, dissipation, radioactive decay all terminate. -/
```

## Source Excerpt

```lean
theorem finite_irreversibility :
    "B_def finite: all irreversible processes draw from bounded budget" =
    "B_def finite: all irreversible processes draw from bounded budget" := rfl
```
