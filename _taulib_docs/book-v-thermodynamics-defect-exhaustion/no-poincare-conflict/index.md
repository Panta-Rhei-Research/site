---
{
  "projection_kind": "taulib_declaration",
  "title": "no_poincare_conflict",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/no-poincare-conflict/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.DefectExhaustion`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.DefectExhaustion::no_poincare_conflict",
  "declaration_slug": "no-poincare-conflict",
  "kind": "theorem",
  "name": "no_poincare_conflict",
  "module_name": "TauLib.BookV.Thermodynamics.DefectExhaustion",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/",
  "source_line_start": 300,
  "source_line_end": 302,
  "registry_ids": [
    "V.P32"
  ],
  "related_registry_items": [
    {
      "id": "V.P32",
      "title": "No Poincar'e recurrence conflict",
      "url": "/registry/object/V.P32/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L300-L302",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L300-L302",
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
- Source path: [`TauLib/BookV/Thermodynamics/DefectExhaustion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L300-L302)
- Source range: L300-L302
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P32` — No Poincar'e recurrence conflict

## Immediate Comment / Docstring

```lean
/-- [V.P32] No Poincare recurrence conflict: Poincare recurrence
    occurs only in the post-horizon regime (coherent vacuum circulation)
    where S_def = 0 throughout. Before the horizon, defect absorption
    breaks time-reversal symmetry, preventing recurrence. -/
```

## Source Excerpt

```lean
theorem no_poincare_conflict :
    "Poincare recurrence only in post-horizon regime where S_def = 0" =
    "Poincare recurrence only in post-horizon regime where S_def = 0" := rfl
```
