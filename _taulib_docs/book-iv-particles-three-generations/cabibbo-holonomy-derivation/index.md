---
{
  "projection_kind": "taulib_declaration",
  "title": "CabibboHolonomyDerivation",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/cabibbo-holonomy-derivation/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::CabibboHolonomyDerivation",
  "declaration_slug": "cabibbo-holonomy-derivation",
  "kind": "structure",
  "name": "CabibboHolonomyDerivation",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2239,
  "source_line_end": 2250,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2239-L2250",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2239-L2250",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2239-L2250)
- Source range: L2239-L2250
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [IV.T152 upgrade] Cabibbo angle from T² holonomy transition.

    The T² fiber has two fundamental cycles γ₁, γ₂ with holonomies
    ι_τ (γ-generator, EM) and (1−ι_τ) (η-generator, Strong).

    The transition amplitude from winding class (1,0) to (0,1)
    on T² with the τ-metric is the inner product:
    ⟨e^{iγ₁}, e^{iγ₂}⟩_τ = ι_τ · (1−ι_τ) = ι_τ · κ_D

    This equals the Cabibbo angle: λ_C = ι_τ · κ_D.
    sin(θ_C) = λ_C = ι_τ · (1−ι_τ) ≈ 0.2249
    PDG: 0.22500 ± 0.00067 → deviation −2327 ppm.

    Physical interpretation: quark mixing between generations 1
    and 2 is the amplitude for a T² winding-class transition.
    This is structural: the transition amplitude is determined
    entirely by the fiber holonomy. -/
```

## Source Excerpt

```lean
structure CabibboHolonomyDerivation where
  /-- Number of T² cycles with holonomies (γ₁, γ₂). -/
  n_cycle_holonomies : Nat := 2
  /-- Number of holonomy factors in product: ι_τ · κ_D. -/
  n_holonomy_factors : Nat := 2
  /-- Deviation from PDG in ppm. -/
  deviation_ppm : Nat := 2327
  /-- Number of free parameters in derivation. -/
  n_free_params : Nat := 0
  /-- Winding class transition: gen 1 → gen 2 (index pair). -/
  transition_from_gen : Nat := 1
  deriving Repr
```
