---
{
  "projection_kind": "taulib_declaration",
  "title": "ThresholdDependentAdmissibility",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/threshold-dependent-admissibility/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BBNBaryogenesis`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNBaryogenesis::ThresholdDependentAdmissibility",
  "declaration_slug": "threshold-dependent-admissibility",
  "kind": "structure",
  "name": "ThresholdDependentAdmissibility",
  "module_name": "TauLib.BookV.Cosmology.BBNBaryogenesis",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/",
  "source_line_start": 81,
  "source_line_end": 90,
  "registry_ids": [
    "V.D197"
  ],
  "related_registry_items": [
    {
      "id": "V.D197",
      "title": "Threshold-Dependent Admissibility",
      "url": "/registry/object/V.D197/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L81-L90",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BBNBaryogenesis",
        "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L81-L90",
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

- Module: [TauLib.BookV.Cosmology.BBNBaryogenesis](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/)
- Source path: [`TauLib/BookV/Cosmology/BBNBaryogenesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L81-L90)
- Source range: L81-L90
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D197` — Threshold-Dependent Admissibility

## Immediate Comment / Docstring

```lean
/-- [V.D197] Threshold-dependent admissibility: the admissibility
    category changes at the neutron threshold L_N (depth 3).

    - Above L_N (depth < 3): PreConfinement → B-violation permitted
    - Below L_N (depth ≥ 3): PostConfinement → B absolutely conserved

    This resolves the baryogenesis tension: baryon number is not a
    fundamental symmetry but a threshold-dependent one. -/
```

## Source Excerpt

```lean
structure ThresholdDependentAdmissibility where
  /-- Confinement threshold depth (L_N = depth 3). -/
  confinement_depth : Nat := 3
  /-- Admissibility above confinement threshold. -/
  above_confinement : AdmissibilityCategory := .PreConfinement
  /-- Admissibility below confinement threshold. -/
  below_confinement : AdmissibilityCategory := .PostConfinement
  /-- The categories differ. -/
  admissibility_changes : above_confinement ≠ below_confinement
  deriving Repr
```
