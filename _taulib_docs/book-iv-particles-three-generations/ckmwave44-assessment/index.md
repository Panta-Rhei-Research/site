---
{
  "projection_kind": "taulib_declaration",
  "title": "CKMWave44Assessment",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/ckmwave44-assessment/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::CKMWave44Assessment",
  "declaration_slug": "ckmwave44-assessment",
  "kind": "structure",
  "name": "CKMWave44Assessment",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2832,
  "source_line_end": 2841,
  "registry_ids": [
    "IV.R433"
  ],
  "related_registry_items": [
    {
      "id": "IV.R433",
      "title": "CKM Precision Assessment (Wave 44)",
      "url": "/registry/object/IV.R433/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2832-L2841",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.ThreeGenerations",
        "url": "/verify/taulib/docs/book-iv-particles-three-generations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2832-L2841",
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2832-L2841)
- Source range: L2832-L2841
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R433` — CKM Precision Assessment (Wave 44)

## Immediate Comment / Docstring

```lean
/-- [IV.R433] CKM precision assessment (Wave 44). -/
```

## Source Excerpt

```lean
structure CKMWave44Assessment where
  /-- A NLO ppm. -/
  a_nlo_ppm : Int := 3109
  /-- J NLO ppm. -/
  j_nlo_ppm : Int := 2624
  /-- All CKM sub-3200 ppm. -/
  all_sub_3200 : Bool := true
  /-- Free parameters. -/
  free_params : Nat := 0
  deriving Repr
```
