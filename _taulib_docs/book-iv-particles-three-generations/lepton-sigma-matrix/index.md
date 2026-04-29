---
{
  "projection_kind": "taulib_declaration",
  "title": "LeptonSigmaMatrix",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/lepton-sigma-matrix/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::LeptonSigmaMatrix",
  "declaration_slug": "lepton-sigma-matrix",
  "kind": "structure",
  "name": "LeptonSigmaMatrix",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 475,
  "source_line_end": 482,
  "registry_ids": [
    "IV.D344"
  ],
  "related_registry_items": [
    {
      "id": "IV.D344",
      "title": "sigma-Equivariant Lepton Mass Matrix",
      "url": "/registry/object/IV.D344/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L475-L482",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L475-L482",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L475-L482)
- Source range: L475-L482
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D344` — sigma-Equivariant Lepton Mass Matrix

## Immediate Comment / Docstring

```lean
/-- [IV.D344] The sigma-equivariant lepton mass matrix M_ℓ = [[a,b,0],[b,c,b],[0,b,a]].
    Parameterized by effective exponents (p, q, r) such that a≈ι_τ⁻ᵖ, b≈ι_τ⁻ᵍ, c≈ι_τ⁻ʳ.
    Sigma-equivariance (rows 1 and 3 are reflections) follows from the chi_+/crossing/chi_-
    decomposition of L = S¹ ∨ S¹. -/
```

## Source Excerpt

```lean
structure LeptonSigmaMatrix where
  /-- Diagonal (lobe) exponent: a ≈ ι_τ^{-p}, close to m_μ/m_e. -/
  p : Float  -- ≈ 4.96, close to 5
  /-- Off-diagonal (mediator) exponent: b ≈ ι_τ^{-q}. -/
  q : Float  -- ≈ 5.92, close to 6
  /-- Central (crossing) exponent: c ≈ ι_τ^{-r}. -/
  r : Float  -- ≈ 7.53, close to 7.5 = 15/2
  deriving Repr
```
