---
{
  "projection_kind": "taulib_declaration",
  "title": "FiniteInitialDefectCount",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/finite-initial-defect-count/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.DefectExhaustion`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.DefectExhaustion::FiniteInitialDefectCount",
  "declaration_slug": "finite-initial-defect-count",
  "kind": "structure",
  "name": "FiniteInitialDefectCount",
  "module_name": "TauLib.BookV.Thermodynamics.DefectExhaustion",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/",
  "source_line_start": 71,
  "source_line_end": 78,
  "registry_ids": [
    "V.P30"
  ],
  "related_registry_items": [
    {
      "id": "V.P30",
      "title": "Finite initial defect count",
      "url": "/registry/object/V.P30/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L71-L78",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L71-L78",
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
- Source path: [`TauLib/BookV/Thermodynamics/DefectExhaustion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L71-L78)
- Source range: L71-L78
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P30` — Finite initial defect count

## Immediate Comment / Docstring

```lean
/-- [V.P30] Finite initial defect count: at orbit depth n = 0,
    the number of defect sites is bounded by the finite lattice
    at the coarsest refinement level.

    |D_0| <= |Lambda_CR^(0)| < infinity

    The lattice is a quotient of Z^2 by T^2 periodicity, reduced
    modulo the coarsest prime power. -/
```

## Source Excerpt

```lean
structure FiniteInitialDefectCount where
  /-- Initial defect count |D_0|. -/
  d_0 : Nat
  /-- Upper bound from coarsest lattice. -/
  lattice_bound : Nat
  /-- The count is bounded. -/
  bounded : d_0 ≤ lattice_bound
  deriving Repr
```
