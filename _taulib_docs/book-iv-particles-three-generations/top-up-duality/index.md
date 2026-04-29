---
{
  "projection_kind": "taulib_declaration",
  "title": "TopUpDuality",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/top-up-duality/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::TopUpDuality",
  "declaration_slug": "top-up-duality",
  "kind": "structure",
  "name": "TopUpDuality",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2714,
  "source_line_end": 2723,
  "registry_ids": [
    "IV.D380"
  ],
  "related_registry_items": [
    {
      "id": "IV.D380",
      "title": "Top–Up Exponent Duality on T²",
      "url": "/registry/object/IV.D380/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2714-L2723",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2714-L2723",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2714-L2723)
- Source range: L2714-L2723
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D380` — Top–Up Exponent Duality on T²

## Immediate Comment / Docstring

```lean
/-- [IV.D380] Top–up exponent duality on T².
    β_u + β_t = 1/|lobes| = 1/2. -/
```

## Source Excerpt

```lean
structure TopUpDuality where
  /-- β_t (×2 for integer encoding). -/
  beta_t_x2 : Int := -10
  /-- β_u (×2 for integer encoding). -/
  beta_u_x2 : Int := 11
  /-- Lobe count. -/
  lobes : Nat := 2
  /-- Duality: β_u_x2 + β_t_x2 = 2/lobes = 1. -/
  duality : beta_u_x2 + beta_t_x2 = 1
  deriving Repr
```
