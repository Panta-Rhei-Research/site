---
{
  "projection_kind": "taulib_declaration",
  "title": "CKMUnitarityTriangle",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/ckmunitarity-triangle/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::CKMUnitarityTriangle",
  "declaration_slug": "ckmunitarity-triangle",
  "kind": "structure",
  "name": "CKMUnitarityTriangle",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1342,
  "source_line_end": 1351,
  "registry_ids": [
    "IV.P198"
  ],
  "related_registry_items": [
    {
      "id": "IV.P198",
      "title": "CKM Unitarity Triangle Angles from tau-Framework",
      "url": "/registry/object/IV.P198/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1342-L1351",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1342-L1351",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1342-L1351)
- Source range: L1342-L1351
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P198` — CKM Unitarity Triangle Angles from tau-Framework

## Immediate Comment / Docstring

```lean
/-- [IV.P198] CKM unitarity triangle angles from τ-framework. -/
```

## Source Excerpt

```lean
structure CKMUnitarityTriangle where
  /-- Number of triangle angles. -/
  n_angles : Nat := 3
  /-- Angles sum (degrees): α+β+γ = 180° (unitarity). -/
  angle_sum_degrees : Nat := 180
  /-- β angle from τ-parameters (degrees × 100). -/
  beta_deg_x100 : Nat := 2248
  /-- γ angle from τ-parameters (degrees × 100). -/
  gamma_deg_x100 : Nat := 6544
  deriving Repr
```
