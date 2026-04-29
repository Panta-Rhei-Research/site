---
{
  "projection_kind": "taulib_declaration",
  "title": "minimal_defect_solution",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/minimal-defect-solution/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.NonlinearEinstein`.",
  "declaration_id": "TauLib.BookV.GravityField.NonlinearEinstein::minimal_defect_solution",
  "declaration_slug": "minimal-defect-solution",
  "kind": "theorem",
  "name": "minimal_defect_solution",
  "module_name": "TauLib.BookV.GravityField.NonlinearEinstein",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/",
  "source_line_start": 316,
  "source_line_end": 320,
  "registry_ids": [
    "V.T35"
  ],
  "related_registry_items": [
    {
      "id": "V.T35",
      "title": "Selection",
      "url": "/registry/object/V.T35/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L316-L320",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.NonlinearEinstein",
        "url": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L316-L320",
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

- Module: [TauLib.BookV.GravityField.NonlinearEinstein](/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/)
- Source path: [`TauLib/BookV/GravityField/NonlinearEinstein.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L316-L320)
- Source range: L316-L320
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T35` — Selection

## Immediate Comment / Docstring

```lean
/-- [V.T35] The converged NF iteration yields the minimal-defect
    solution: no other admissible configuration has lower total
    cocycle defect.

    Encoded: converged solutions have zero defect (the minimum). -/
```

## Source Excerpt

```lean
theorem minimal_defect_solution (nf : NFEinsteinIteration)
    (h : nf.converged = true) :
    nf.current_defect.is_zero = true := by
  simp [CocycleDefect.is_zero]
  exact nf.convergence_check h
```
