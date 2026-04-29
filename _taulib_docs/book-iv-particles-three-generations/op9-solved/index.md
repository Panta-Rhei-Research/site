---
{
  "projection_kind": "taulib_declaration",
  "title": "OP9Solved",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/op9-solved/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::OP9Solved",
  "declaration_slug": "op9-solved",
  "kind": "structure",
  "name": "OP9Solved",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2948,
  "source_line_end": 2959,
  "registry_ids": [
    "IV.R435"
  ],
  "related_registry_items": [
    {
      "id": "IV.R435",
      "title": "IV.OP9 Status: SOLVED (7/7 Exponents Derived)",
      "url": "/registry/object/IV.R435/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2948-L2959",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2948-L2959",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2948-L2959)
- Source range: L2948-L2959
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R435` — IV.OP9 Status: SOLVED (7/7 Exponents Derived)

## Immediate Comment / Docstring

```lean
/-- [IV.R435] IV.OP9 SOLVED: all 7 quark mass exponents derived. -/
```

## Source Excerpt

```lean
structure OP9Solved where
  /-- Total exponents. -/
  total : Nat := 7
  /-- Derived exponents. -/
  derived : Nat := 7
  /-- All derived. -/
  all_derived : Bool := true
  /-- Worst-case ppm. -/
  worst_ppm : Int := 1559
  /-- Free parameters. -/
  free_params : Nat := 0
  deriving Repr
```
