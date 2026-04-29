---
{
  "projection_kind": "taulib_declaration",
  "title": "QLCDerivationChain",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/qlcderivation-chain/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::QLCDerivationChain",
  "declaration_slug": "qlcderivation-chain",
  "kind": "structure",
  "name": "QLCDerivationChain",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2395,
  "source_line_end": 2408,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2395-L2408",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2395-L2408",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2395-L2408)
- Source range: L2395-L2408
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [IV.T175 upgrade] QLC constraint: θ₁₂ + θ_C = π/4.
    The fiber-base duality T²×τ¹→τ³ imposes a quarter-turn
    constraint on the sum of solar and Cabibbo angles.

    Chain: λ_C = ι_τ·(1−ι_τ) (IV.T152, τ-effective)
           → θ_C = arcsin(λ_C)
           → θ₁₂ = π/4 − θ_C + ι_τ²κ_ω (NLO correction)
           → θ₁₂ at +3106 ppm from PDG -/
```

## Source Excerpt

```lean
structure QLCDerivationChain where
  /-- Cabibbo λ_C deviation from PDG in ppm (−2327). -/
  cabibbo_deviation_ppm : Nat := 2327
  /-- Quarter-turn constraint from T²×τ¹ fiber-base duality (π/4 radians × 10000). -/
  quarter_turn_angle : Nat := 7854
  /-- NLO correction power (ι_τ²). -/
  nlo_power : Nat := 2
  /-- θ₁₂ deviation from PDG in ppm (+3106). -/
  theta12_deviation_ppm : Nat := 3106
  /-- Number of free parameters (zero: all from ι_τ). -/
  free_params : Nat := 0
  /-- Scope. -/
  scope : String := "tau-effective"
  deriving Repr
```
