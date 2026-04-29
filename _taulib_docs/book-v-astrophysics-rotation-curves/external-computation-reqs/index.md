---
{
  "projection_kind": "taulib_declaration",
  "title": "ExternalComputationReqs",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/external-computation-reqs/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::ExternalComputationReqs",
  "declaration_slug": "external-computation-reqs",
  "kind": "structure",
  "name": "ExternalComputationReqs",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 1062,
  "source_line_end": 1071,
  "registry_ids": [
    "V.P192"
  ],
  "related_registry_items": [
    {
      "id": "V.P192",
      "title": "External Computation Requirements for v(r)",
      "url": "/registry/object/V.P192/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L1062-L1071",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.RotationCurves",
        "url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L1062-L1071",
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

- Module: [TauLib.BookV.Astrophysics.RotationCurves](/verify/taulib/docs/book-v-astrophysics-rotation-curves/)
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L1062-L1071)
- Source range: L1062-L1071
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P192` — External Computation Requirements for v(r)

## Immediate Comment / Docstring

```lean
/-- [V.P192] External computation requirements for full v(r). -/
```

## Source Excerpt

```lean
structure ExternalComputationReqs where
  /-- Modified Poisson solver needed. -/
  needs_poisson_solver : Bool := true
  /-- Mesh resolution in pc. -/
  mesh_resolution_pc : Nat := 100
  /-- τ-Einstein is metric theory (no extra fields). -/
  is_metric_theory : Bool := true
  /-- TeVeS needs 3 additional fields. -/
  teves_extra_fields : Nat := 3
  deriving Repr
```
