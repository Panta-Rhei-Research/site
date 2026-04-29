---
{
  "projection_kind": "taulib_declaration",
  "title": "GenMassHierarchy",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/gen-mass-hierarchy/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::GenMassHierarchy",
  "declaration_slug": "gen-mass-hierarchy",
  "kind": "structure",
  "name": "GenMassHierarchy",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1751,
  "source_line_end": 1758,
  "registry_ids": [
    "IV.T172"
  ],
  "related_registry_items": [
    {
      "id": "IV.T172",
      "title": "Generation Mass Hierarchy from Eigenvalue Ordering",
      "url": "/registry/object/IV.T172/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1751-L1758",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1751-L1758",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1751-L1758)
- Source range: L1751-L1758
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T172` — Generation Mass Hierarchy from Eigenvalue Ordering

## Immediate Comment / Docstring

```lean
/-- [IV.T172] Generation mass hierarchy structure (formalized). -/
```

## Source Excerpt

```lean
structure GenMassHierarchy where
  /-- Number of eigenvalues. -/
  n_eigenvalues : Nat := 3
  /-- Number of strict ordering relations (λ₁ < λ₂ < λ₃ → 2 relations). -/
  n_ordering_relations : Nat := 2
  /-- Lightest generation number (crossing-point mode). -/
  lightest_generation : Nat := 1
  deriving Repr
```
