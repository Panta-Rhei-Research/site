---
{
  "projection_kind": "taulib_declaration",
  "title": "DownTypeSectorComplete",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/down-type-sector-complete/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::DownTypeSectorComplete",
  "declaration_slug": "down-type-sector-complete",
  "kind": "structure",
  "name": "DownTypeSectorComplete",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2904,
  "source_line_end": 2919,
  "registry_ids": [
    "IV.R434"
  ],
  "related_registry_items": [
    {
      "id": "IV.R434",
      "title": "Down-Type Sector Exponent Completeness",
      "url": "/registry/object/IV.R434/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2904-L2919",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2904-L2919",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2904-L2919)
- Source range: L2904-L2919
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R434` — Down-Type Sector Exponent Completeness

## Immediate Comment / Docstring

```lean
/-- [IV.R434] Down-type sector exponent completeness. -/
```

## Source Excerpt

```lean
structure DownTypeSectorComplete where
  /-- β(t/b) numerator. -/
  tb_num : Int := -45
  /-- β(t/b) denominator. -/
  tb_den : Nat := 13
  /-- β(s/b) numerator. -/
  sb_num : Nat := 53
  /-- β(s/b) denominator. -/
  sb_den : Nat := 15
  /-- β(d/s) numerator. -/
  ds_num : Nat := 64
  /-- β(d/s) denominator. -/
  ds_den : Nat := 23
  /-- Worst-case ppm. -/
  worst_ppm : Int := 1559
  deriving Repr
```
