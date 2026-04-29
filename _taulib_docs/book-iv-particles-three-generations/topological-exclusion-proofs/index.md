---
{
  "projection_kind": "taulib_declaration",
  "title": "TopologicalExclusionProofs",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/topological-exclusion-proofs/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::TopologicalExclusionProofs",
  "declaration_slug": "topological-exclusion-proofs",
  "kind": "structure",
  "name": "TopologicalExclusionProofs",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1711,
  "source_line_end": 1720,
  "registry_ids": [
    "IV.T171"
  ],
  "related_registry_items": [
    {
      "id": "IV.T171",
      "title": "Fourth Generation Excluded (Topological)",
      "url": "/registry/object/IV.T171/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1711-L1720",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1711-L1720",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1711-L1720)
- Source range: L1711-L1720
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T171` — Fourth Generation Excluded (Topological)

## Immediate Comment / Docstring

```lean
/-- [IV.T171] Three independent proofs of |gen|=3 (formalized). -/
```

## Source Excerpt

```lean
structure TopologicalExclusionProofs where
  /-- Number of independent proofs. -/
  n_independent_proofs : Nat := 3
  /-- Proof 1: H₁(τ³;ℤ) rank. -/
  h1_rank : Nat := 3
  /-- Proof 2: primitive winding classes on T². -/
  primitive_winding_classes : Nat := 3
  /-- Proof 3: lemniscate topological regions. -/
  lemniscate_regions : Nat := 3
  deriving Repr
```
