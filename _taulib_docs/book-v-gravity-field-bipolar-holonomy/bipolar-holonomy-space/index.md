---
{
  "projection_kind": "taulib_declaration",
  "title": "BipolarHolonomySpace",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-bipolar-holonomy/bipolar-holonomy-space/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.BipolarHolonomy`.",
  "declaration_id": "TauLib.BookV.GravityField.BipolarHolonomy::BipolarHolonomySpace",
  "declaration_slug": "bipolar-holonomy-space",
  "kind": "structure",
  "name": "BipolarHolonomySpace",
  "module_name": "TauLib.BookV.GravityField.BipolarHolonomy",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-bipolar-holonomy/",
  "source_line_start": 60,
  "source_line_end": 69,
  "registry_ids": [
    "V.D101"
  ],
  "related_registry_items": [
    {
      "id": "V.D101",
      "title": "Macro charge",
      "url": "/registry/object/V.D101/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/BipolarHolonomy.lean#L60-L69",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.BipolarHolonomy",
        "url": "/verify/taulib/docs/book-v-gravity-field-bipolar-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/BipolarHolonomy.lean#L60-L69",
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

- Module: [TauLib.BookV.GravityField.BipolarHolonomy](/verify/taulib/docs/book-v-gravity-field-bipolar-holonomy/)
- Source path: [`TauLib/BookV/GravityField/BipolarHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/BipolarHolonomy.lean#L60-L69)
- Source range: L60-L69
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D101` — Macro charge

## Immediate Comment / Docstring

```lean
/-- [V.D101] The Bipolar Holonomy Space of (τ³, L).

    BHS(τ³, L) := H₁(τ³; ℤ) ⊗ H¹(τ³; ℤ) ⊗ H₁(L; ℤ)

    The three Betti numbers:
    - b₁_arena = rank H₁(τ³; ℤ): independent 1-cycles in τ³
    - b1_arena = rank H¹(τ³; ℤ): independent characters on τ³
    - b₁_boundary = rank H₁(L; ℤ): independent loops in L = S¹ ∨ S¹ -/
```

## Source Excerpt

```lean
structure BipolarHolonomySpace where
  /-- b₁(τ³): first Betti number of the arena (homology). -/
  b₁_arena : Nat
  /-- b¹(τ³): first Betti number of the arena (cohomology). -/
  b1_arena : Nat
  /-- b₁(L): first Betti number of the boundary lemniscate. -/
  b₁_boundary : Nat
  /-- The dimension of the tensor product BHS. -/
  dim : Nat := b₁_arena * b1_arena * b₁_boundary
  deriving Repr
```
