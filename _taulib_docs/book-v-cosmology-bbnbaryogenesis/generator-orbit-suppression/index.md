---
{
  "projection_kind": "taulib_declaration",
  "title": "GeneratorOrbitSuppression",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/generator-orbit-suppression/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BBNBaryogenesis`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNBaryogenesis::GeneratorOrbitSuppression",
  "declaration_slug": "generator-orbit-suppression",
  "kind": "structure",
  "name": "GeneratorOrbitSuppression",
  "module_name": "TauLib.BookV.Cosmology.BBNBaryogenesis",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/",
  "source_line_start": 369,
  "source_line_end": 382,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L369-L382",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BBNBaryogenesis",
        "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L369-L382",
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

- Module: [TauLib.BookV.Cosmology.BBNBaryogenesis](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/)
- Source path: [`TauLib/BookV/Cosmology/BBNBaryogenesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L369-L382)
- Source range: L369-L382
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.P130 upgrade] SA-i mod-5 generator orbit: the 5-generator orbit
    of σ-involution on H_∂[ω] produces exactly ι_τ¹⁵ suppression.

    Proof structure:
    1. Each generator g_k ∈ {α,π,γ,η,ω} contributes one holonomy factor
       ι_τ^{dim(τ³)} = ι_τ³ from the 3-dimensional τ³
    2. The generators act cyclically (ℤ/5ℤ) on the boundary character
    3. The full orbit traverses all 5 generators: total suppression
       ι_τ^{3×5} = ι_τ¹⁵
    4. Geometric series S₅ = Σ_{k=0}^{4} ι_τ^{3k} = (1−ι_τ¹⁵)/(1−ι_τ³)
    5. Parallel: SA-i mod-3 (3 colors) → θ_QCD=0; SA-i mod-5 → η_B -/
```

## Source Excerpt

```lean
structure GeneratorOrbitSuppression where
  /-- Number of generators in the orbit. -/
  n_generators : Nat := 5
  /-- Dimension of τ³. -/
  tau3_dim : Nat := 3
  /-- Each generator contributes ι_τ^{dim(τ³)}. -/
  per_generator_power : Nat := 3
  /-- Total suppression exponent. -/
  total_exponent : Nat := 15
  /-- The orbit is cyclic (ℤ/5ℤ). -/
  cyclic_orbit : Bool := true
  /-- Exponent = generators × per-generator power. -/
  exponent_decomp : total_exponent = n_generators * per_generator_power
  deriving Repr
```
