---
{
  "projection_kind": "taulib_declaration",
  "title": "Theta13OpenFrontier",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/theta13-open-frontier/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::Theta13OpenFrontier",
  "declaration_slug": "theta13-open-frontier",
  "kind": "structure",
  "name": "Theta13OpenFrontier",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2360,
  "source_line_end": 2367,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2360-L2367",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2360-L2367",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2360-L2367)
- Source range: L2360-L2367
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- θ₁₃ second-order mechanism: genuinely open frontier.

    Best candidates explored:
    - sin²θ₁₃ = λ_C²·(ι_τ/2) ≈ 0.00432 (too small, PDG 0.02224)
    - sin²θ₁₃ = ι_τ⁴·κ_D ≈ 0.00893 (still 2.5× too small)
    - Double winding-class crossing amplitude: gen1→gen3 skipping gen2

    Current best: 13.6% off. No viable formula at present.
    Flagged as "genuinely open frontier". -/
```

## Source Excerpt

```lean
structure Theta13OpenFrontier where
  /-- Best deviation from PDG in percent. -/
  best_deviation_percent : Nat := 14
  /-- Number of candidates explored. -/
  n_candidates_explored : Nat := 3
  /-- Number of viable formulas found. -/
  n_viable_formulas : Nat := 0
  deriving Repr
```
