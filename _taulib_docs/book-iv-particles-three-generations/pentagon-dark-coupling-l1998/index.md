---
{
  "projection_kind": "taulib_declaration",
  "title": "PentagonDarkCoupling",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/pentagon-dark-coupling-l1998/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::PentagonDarkCoupling",
  "declaration_slug": "pentagon-dark-coupling-l1998",
  "kind": "structure",
  "name": "PentagonDarkCoupling",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1998,
  "source_line_end": 2007,
  "registry_ids": [
    "IV.D364"
  ],
  "related_registry_items": [
    {
      "id": "IV.D364",
      "title": "Pentagon Dark Coupling: κ_D Exponent 5/4 = |gen|/(2·|lobes|)",
      "url": "/registry/object/IV.D364/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1998-L2007",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1998-L2007",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1998-L2007)
- Source range: L1998-L2007
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D364` — Pentagon Dark Coupling: κ_D Exponent 5/4 = |gen|/(2·|lobes|)

## Immediate Comment / Docstring

```lean
/-- [IV.D364] Pentagon dark coupling structure (formalized). -/
```

## Source Excerpt

```lean
structure PentagonDarkCoupling where
  /-- Exponent numerator: 5 = |generators|. -/
  exponent_numer : Nat := 5
  /-- Exponent denominator: 4 = 2 × lobes. -/
  exponent_denom : Nat := 4
  /-- Number of generators. -/
  n_generators : Nat := 5
  /-- Number of lobes. -/
  n_lobes : Nat := 2
  deriving Repr
```
