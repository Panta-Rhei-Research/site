---
{
  "projection_kind": "taulib_declaration",
  "title": "tensor_passage_cross_check",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/tensor-passage-cross-check/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.ExponentDerivation`.",
  "declaration_id": "TauLib.BookV.GravityField.ExponentDerivation::tensor_passage_cross_check",
  "declaration_slug": "tensor-passage-cross-check",
  "kind": "theorem",
  "name": "tensor_passage_cross_check",
  "module_name": "TauLib.BookV.GravityField.ExponentDerivation",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/",
  "source_line_start": 304,
  "source_line_end": 318,
  "registry_ids": [
    "V.P111"
  ],
  "related_registry_items": [
    {
      "id": "V.P111",
      "title": "Tensor-Square Connection",
      "url": "/registry/object/V.P111/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ExponentDerivation.lean#L304-L318",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.ExponentDerivation",
        "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ExponentDerivation.lean#L304-L318",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookV.GravityField.ExponentDerivation](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/)
- Source path: [`TauLib/BookV/GravityField/ExponentDerivation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ExponentDerivation.lean#L304-L318)
- Source range: L304-L318
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P111` — Tensor-Square Connection

## Immediate Comment / Docstring

```lean
/-- [V.P111] Connection: ExponentDerivation × SpectralPage.

    The gravitational coupling α_G ∝ (121/225)^18 · ι^72:
    - 18 passages (ExponentDerivation: 2 × 3 × 3)
    - 121/225 per passage (SpectralPage: tensor-square EM density)
    - ι⁴ per passage (alpha formula)
    - Total: (121/225)^18 · ι^(4×18) = (121/225)^18 · ι^72

    Cross-multiplied Nat verification: 121^18 active mode tuples
    out of 225^18 total mode tuples, times ι^72. -/
```

## Source Excerpt

```lean
theorem tensor_passage_cross_check :
    121 * 121 = 11^2 * 11^2 ∧   -- each passage: 11² active
    225 * 225 = 15^2 * 15^2 ∧   -- each passage: 15² total
    4 * 18 = 72 := by omega      -- total iota-power

-- ============================================================
-- BHS SEMANTIC UPGRADE (see BipolarHolonomy.lean for full formalization)
-- ============================================================

/-! The exponent 18 IS dim(BHS), where BHS(τ³, L) = H₁(τ³) ⊗ H¹(τ³) ⊗ H₁(L)
    is the Bipolar Holonomy Space. This upgrades the factorization 2 × 3 × 3
    from "product of three invariants" to "dimension of a single cohomological
    object." See `TauLib.BookV.GravityField.BipolarHolonomy` for the full
    formalization. The bridge theorem `bhs_equals_exponent` verifies
    dim(BHS) = ExponentFactors.product = 18. -/
```
