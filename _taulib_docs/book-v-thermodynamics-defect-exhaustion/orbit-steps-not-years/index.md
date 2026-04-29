---
{
  "projection_kind": "taulib_declaration",
  "title": "OrbitStepsNotYears",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/orbit-steps-not-years/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.DefectExhaustion`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.DefectExhaustion::OrbitStepsNotYears",
  "declaration_slug": "orbit-steps-not-years",
  "kind": "structure",
  "name": "OrbitStepsNotYears",
  "module_name": "TauLib.BookV.Thermodynamics.DefectExhaustion",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/",
  "source_line_start": 331,
  "source_line_end": 336,
  "registry_ids": [
    "V.R124"
  ],
  "related_registry_items": [
    {
      "id": "V.R124",
      "title": "Orbit steps are not years",
      "url": "/registry/object/V.R124/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L331-L336",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L331-L336",
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
- Source path: [`TauLib/BookV/Thermodynamics/DefectExhaustion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L331-L336)
- Source range: L331-L336
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.R124` — Orbit steps are not years

## Immediate Comment / Docstring

```lean
-- [V.R124] Orbit steps are not years:
```

## Source Excerpt

```lean
structure OrbitStepsNotYears where
  /-- n_coh upper bound (orbit steps). -/
  orbit_bound : Nat
  /-- Physical duration is calibration-dependent. -/
  calibration_dependent : Bool := true
  deriving Repr
```
