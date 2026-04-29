---
{
  "projection_kind": "taulib_declaration",
  "title": "OP5Wave45Status",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/op5-wave45-status/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::OP5Wave45Status",
  "declaration_slug": "op5-wave45-status",
  "kind": "structure",
  "name": "OP5Wave45Status",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2995,
  "source_line_end": 3002,
  "registry_ids": [
    "IV.R436"
  ],
  "related_registry_items": [
    {
      "id": "IV.R436",
      "title": "IV.OP5 Status Update (Wave 45)",
      "url": "/registry/object/IV.R436/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2995-L3002",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2995-L3002",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2995-L3002)
- Source range: L2995-L3002
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R436` — IV.OP5 Status Update (Wave 45)

## Immediate Comment / Docstring

```lean
/-- [IV.R436] IV.OP5 status update (Wave 45). -/
```

## Source Excerpt

```lean
structure OP5Wave45Status where
  /-- Exponent program complete. -/
  op9_solved : Bool := true
  /-- CKM sub-3200 ppm. -/
  ckm_sub_3200 : Bool := true
  /-- Lobe-power hierarchy established. -/
  hierarchy_established : Bool := true
  deriving Repr
```
