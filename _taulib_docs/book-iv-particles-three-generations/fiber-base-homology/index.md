---
{
  "projection_kind": "taulib_declaration",
  "title": "FiberBaseHomology",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/fiber-base-homology/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::FiberBaseHomology",
  "declaration_slug": "fiber-base-homology",
  "kind": "structure",
  "name": "FiberBaseHomology",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1631,
  "source_line_end": 1639,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1631-L1639",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1631-L1639",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1631-L1639)
- Source range: L1631-L1639
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- H₁(τ³; ℤ) ≅ ℤ³ from fiber-base decomposition.
    rank = rank(H₁(T²)) + rank(H₁(τ¹)) = 2 + 1 = 3.
    Three generators: g₁ (meridian), g₂ (longitude), g₃ (base cycle). -/
```

## Source Excerpt

```lean
structure FiberBaseHomology where
  /-- Rank of H₁(T²) = 2 (two independent cycles on torus). -/
  rank_fiber : Nat := 2
  /-- Rank of H₁(τ¹) = 1 (one cycle on profinite solenoid). -/
  rank_base : Nat := 1
  /-- Total rank = fiber + base. -/
  rank_total : Nat := rank_fiber + rank_base
  /-- The total rank equals 3. -/
  rank_eq_three : rank_total = 3 := by native_decide
```
