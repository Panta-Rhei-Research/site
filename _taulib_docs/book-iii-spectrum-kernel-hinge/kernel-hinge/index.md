---
{
  "projection_kind": "taulib_declaration",
  "title": "KernelHinge",
  "permalink": "/verify/taulib/docs/book-iii-spectrum-kernel-hinge/kernel-hinge/",
  "summary_short": "`structure` declaration in `TauLib.BookIII.Spectrum.KernelHinge`.",
  "declaration_id": "TauLib.BookIII.Spectrum.KernelHinge::KernelHinge",
  "declaration_slug": "kernel-hinge",
  "kind": "structure",
  "name": "KernelHinge",
  "module_name": "TauLib.BookIII.Spectrum.KernelHinge",
  "module_url": "/verify/taulib/docs/book-iii-spectrum-kernel-hinge/",
  "source_line_start": 59,
  "source_line_end": 85,
  "registry_ids": [
    "I.D74"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/KernelHinge.lean#L59-L85",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectrum.KernelHinge",
        "url": "/verify/taulib/docs/book-iii-spectrum-kernel-hinge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/KernelHinge.lean#L59-L85",
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

- Module: [TauLib.BookIII.Spectrum.KernelHinge](/verify/taulib/docs/book-iii-spectrum-kernel-hinge/)
- Source path: [`TauLib/BookIII/Spectrum/KernelHinge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/KernelHinge.lean#L59-L85)
- Source range: L59-L85
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.D74] The kernel hinge diagram: a structured witness that
    all of Book I's infrastructure is earned from the axioms.

    Layer 1: The coherence kernel (generators + axioms)
    Layer 2: The Three Keys (number system, boundary, holomorphy)
    Layer 3: Categorical infrastructure (category, topos, bi-monoidal)
    Layer 4: The culmination (Global Hartogs, boundary-interior) -/
```

## Source Excerpt

```lean
structure KernelHinge where
  -- Layer 1: The coherence kernel
  generators_count : Nat
  generators_are_five : generators_count = 5

  -- Layer 2: The Three Keys
  -- KEY 1: Number system (profinite integers, earned in Parts VIII-IX)
  key1_number_system : Type := TauIdx
  -- KEY 2: Algebraic boundary (lemniscate, earned in Parts VI-VII)
  key2_boundary : Type := TauIdx
  -- KEY 3: Holomorphic functions (HolFun, earned in Part XII)
  key3_holomorphy : Type := HolFun

  -- Layer 3: Categorical infrastructure
  earned_category : CatTau
  earned_topos : EarnedTopos

  -- Layer 4: The culmination
  -- The identity theorem (I.T21)
  identity_theorem : ∀ f₁ f₂ : StageFun,
    TowerCoherent f₁ → TowerCoherent f₂ →
    ∀ d₀, (∀ n, agree_at f₁ f₂ n d₀) →
    ∀ n k, k ≤ d₀ → agree_at f₁ f₂ n k
  -- The subobject classifier has exactly 4 values
  four_valued_classifier : ∀ v : Tau.Logic.Omega_tau,
    v = Tau.Logic.Truth4.T ∨ v = Tau.Logic.Truth4.F ∨
    v = Tau.Logic.Truth4.B ∨ v = Tau.Logic.Truth4.N
```
