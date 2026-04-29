---
{
  "projection_kind": "taulib_declaration",
  "title": "MagneticPredictionSuite",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-ehtreread/magnetic-prediction-suite/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.EHTReread`.",
  "declaration_id": "TauLib.BookV.Astrophysics.EHTReread::MagneticPredictionSuite",
  "declaration_slug": "magnetic-prediction-suite",
  "kind": "structure",
  "name": "MagneticPredictionSuite",
  "module_name": "TauLib.BookV.Astrophysics.EHTReread",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/",
  "source_line_start": 605,
  "source_line_end": 626,
  "registry_ids": [
    "V.R412"
  ],
  "related_registry_items": [
    {
      "id": "V.R412",
      "title": "Complete Magnetic Table",
      "url": "/registry/object/V.R412/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L605-L626",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.EHTReread",
        "url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L605-L626",
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

- Module: [TauLib.BookV.Astrophysics.EHTReread](/verify/taulib/docs/book-v-astrophysics-ehtreread/)
- Source path: [`TauLib/BookV/Astrophysics/EHTReread.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L605-L626)
- Source range: L605-L626
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.R412` — Complete Magnetic Table

## Immediate Comment / Docstring

```lean
/-- [V.R412] Complete T² vs S² Magnetic Prediction Suite.
    9 observables, all derived from genus(T²) = 1 and ι_τ. -/
```

## Source Excerpt

```lean
structure MagneticPredictionSuite where
  /-- EVPA winding number (T²). -/
  w_evpa : Nat := 2
  /-- RM winding number (T²). -/
  w_rm : Nat := 2
  /-- Circular pol winding number (T²). -/
  w_v : Nat := 2
  /-- B_tor/B_pol × 1000. -/
  field_ratio_x1000 : Nat := 2930
  /-- Flux through hole exists (1 = yes). -/
  flux_through_hole : Nat := 1
  /-- Jet helicity fixed by topology (1 = yes). -/
  jet_helicity_fixed : Nat := 1
  /-- Jet B_z/B_phi × 1000 at base. -/
  jet_bz_bphi_x1000 : Nat := 341
  /-- IGMF in filaments (nG × 10). -/
  igmf_fil_ng_x10 : Nat := 300
  /-- B alignment parallel (1 = yes). -/
  b_alignment_parallel : Nat := 1
  deriving Repr

instance : Inhabited MagneticPredictionSuite := ⟨{}⟩
```
