---
{
  "projection_kind": "taulib_declaration",
  "title": "exponent_unique_even_match",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/exponent-unique-even-match/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.ExponentDerivation`.",
  "declaration_id": "TauLib.BookV.GravityField.ExponentDerivation::exponent_unique_even_match",
  "declaration_slug": "exponent-unique-even-match",
  "kind": "theorem",
  "name": "exponent_unique_even_match",
  "module_name": "TauLib.BookV.GravityField.ExponentDerivation",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/",
  "source_line_start": 214,
  "source_line_end": 223,
  "registry_ids": [
    "V.T83"
  ],
  "related_registry_items": [
    {
      "id": "V.T83",
      "title": "Kepler's Second Law --- V.T35",
      "url": "/registry/object/V.T83/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ExponentDerivation.lean#L214-L223",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ExponentDerivation.lean#L214-L223",
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
- Source path: [`TauLib/BookV/GravityField/ExponentDerivation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ExponentDerivation.lean#L214-L223)
- Source range: L214-L223
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T83` — Kepler's Second Law --- V.T35

## Immediate Comment / Docstring

```lean
/-- [V.T83] 18 is the unique even exponent in {2, 4, ..., 40}
    such that the product b₁ × dim × |sol| = k where each factor
    is a structural invariant of τ³.

    Proof strategy: the factors are independently FIXED at 2, 3, 3,
    so the product is uniquely 18. There is no choice involved.

    The uniqueness is not "18 is special among integers" but
    "the three invariants force 18 uniquely."

    Additionally, the numerical constraint (CODATA matching) independently
    selects 18: among even k, only k=18 gives α^k ≈ α_G / (geometric). -/
```

## Source Excerpt

```lean
theorem exponent_unique_even_match :
    -- Factors are fixed (not chosen)
    canonical_factors.betti_1_fiber = 2 ∧
    canonical_factors.dim_tau3 = 3 ∧
    canonical_factors.solenoidal_card = 3 ∧
    -- Product is uniquely determined
    canonical_factors.product = 18 ∧
    -- 18 is even (parity constraint from squared mass ratio)
    18 % 2 = 0 := by
  exact ⟨rfl, rfl, rfl, rfl, rfl⟩
```
