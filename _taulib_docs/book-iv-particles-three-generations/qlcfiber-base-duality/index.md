---
{
  "projection_kind": "taulib_declaration",
  "title": "QLCFiberBaseDuality",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/qlcfiber-base-duality/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::QLCFiberBaseDuality",
  "declaration_slug": "qlcfiber-base-duality",
  "kind": "structure",
  "name": "QLCFiberBaseDuality",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2324,
  "source_line_end": 2335,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2324-L2335",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2324-L2335",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2324-L2335)
- Source range: L2324-L2335
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [IV.P189/T175 upgrade] QLC from fiber-base duality.

    θ₁₂^{PMNS} + θ_C^{CKM} ≈ π/4 + O(ι_τ²)

    Proof structure:
    - On T² (fiber): quark mixing is small:
      θ_C = arcsin(ι_τ·κ_D) ≈ 0.222 rad
    - On τ¹ (base): the complementary angle is π/4 − θ_C
      because T² × τ¹ → τ³ imposes that the total mixing
      angle in the product is π/4 (quarter-turn on combined space)
    - Correction: ι_τ²·κ_ω arises from ω-sector (Higgs) coupling
      between fiber and base

    Physical: quarks (on T²) and leptons (on τ¹) have
    complementary mixing because the product structure
    τ³ = τ¹ ×_f T² constrains total mixing. -/
```

## Source Excerpt

```lean
structure QLCFiberBaseDuality where
  /-- Fiber dimension: T² (quarks). -/
  fiber_dim : Nat := 2
  /-- Base dimension: τ¹ (leptons). -/
  base_dim : Nat := 1
  /-- Total quarter-turn angle (degrees): π/4 = 45°. -/
  quarter_turn_degrees : Nat := 45
  /-- Higgs correction power: ι_τ² order. -/
  higgs_correction_power : Nat := 2
  /-- QLC deviation in degrees (×10): 1.4° → 14. -/
  deviation_deg_x10 : Nat := 14
  deriving Repr
```
