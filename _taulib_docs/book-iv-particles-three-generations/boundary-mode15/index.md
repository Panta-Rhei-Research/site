---
{
  "projection_kind": "taulib_declaration",
  "title": "BoundaryMode15",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/boundary-mode15/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::BoundaryMode15",
  "declaration_slug": "boundary-mode15",
  "kind": "structure",
  "name": "BoundaryMode15",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1781,
  "source_line_end": 1792,
  "registry_ids": [
    "IV.P202"
  ],
  "related_registry_items": [
    {
      "id": "IV.P202",
      "title": "15 = 3 × 5 Boundary Mode Decomposition",
      "url": "/registry/object/IV.P202/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1781-L1792",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1781-L1792",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1781-L1792)
- Source range: L1781-L1792
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P202` — 15 = 3 × 5 Boundary Mode Decomposition

## Immediate Comment / Docstring

```lean
/-- [IV.P202] 15 boundary mode decomposition structure (formalized). -/
```

## Source Excerpt

```lean
structure BoundaryMode15 where
  /-- Number of generations. -/
  n_generations : Nat := 3
  /-- Modes per generation. -/
  modes_per_gen : Nat := 5
  /-- Total boundary modes. -/
  total_modes : Nat := 15
  /-- EM-active modes. -/
  em_active : Nat := 11
  /-- EM-silent modes. -/
  em_silent : Nat := 4
  deriving Repr
```
