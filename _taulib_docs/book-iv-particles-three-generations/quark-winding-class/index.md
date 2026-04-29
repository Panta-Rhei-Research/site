---
{
  "projection_kind": "taulib_declaration",
  "title": "QuarkWindingClass",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/quark-winding-class/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::QuarkWindingClass",
  "declaration_slug": "quark-winding-class",
  "kind": "structure",
  "name": "QuarkWindingClass",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 147,
  "source_line_end": 160,
  "registry_ids": [
    "IV.D197"
  ],
  "related_registry_items": [
    {
      "id": "IV.D197",
      "title": "Quark winding classes",
      "url": "/registry/object/IV.D197/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L147-L160",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L147-L160",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L147-L160)
- Source range: L147-L160
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D197` — Quark winding classes

## Immediate Comment / Docstring

```lean
/-- [IV.D197] Quark winding classes on T² with shape ratio ι_τ.
    The six quarks are assigned to three winding classes:
    - Class (1,0): Gen 1 (u, d), eigenvalue β = 1
    - Class (0,1): Gen 2 (c, s), eigenvalue β = ι_τ⁻¹
    - Class (1,1): Gen 3 (t, b), eigenvalue β = ι_τ⁻² -/
```

## Source Excerpt

```lean
structure QuarkWindingClass where
  /-- Winding pair (m, n) on T². -/
  winding_m : Nat
  /-- Winding pair (m, n) on T². -/
  winding_n : Nat
  /-- Generation number. -/
  generation : Nat
  /-- Up-type quark name. -/
  up_type : String
  /-- Down-type quark name. -/
  down_type : String
  /-- Eigenvalue exponent: β = ι_τ^(-exponent). -/
  eigenvalue_exp : Nat
  deriving Repr
```
