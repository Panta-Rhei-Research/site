---
{
  "projection_kind": "taulib_declaration",
  "title": "LensingDynamicalEquality",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/lensing-dynamical-equality/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::LensingDynamicalEquality",
  "declaration_slug": "lensing-dynamical-equality",
  "kind": "structure",
  "name": "LensingDynamicalEquality",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 1013,
  "source_line_end": 1020,
  "registry_ids": [
    "V.P147"
  ],
  "related_registry_items": [
    {
      "id": "V.P147",
      "title": "Lensing–Dynamical Mass Equality",
      "url": "/registry/object/V.P147/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L1013-L1020",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L1013-L1020",
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L1013-L1020)
- Source range: L1013-L1020
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P147` — Lensing–Dynamical Mass Equality

## Immediate Comment / Docstring

```lean
/-- [V.P147] Lensing–Dynamical Mass Equality.
    M_lensing = M_dynamical = M_p + M_∂. Both probe the same
    effective metric g_∂[χ]. Key advantage over MOND. -/
```

## Source Excerpt

```lean
structure LensingDynamicalEquality where
  /-- Lensing and dynamical masses use same metric (1 = yes). -/
  same_metric : Nat := 1
  /-- MOND requires separate theory for lensing (1 = yes). -/
  mond_needs_teves : Nat := 1
  /-- Number of additional fields in TeVeS. -/
  teves_fields : Nat := 3
  deriving Repr
```
