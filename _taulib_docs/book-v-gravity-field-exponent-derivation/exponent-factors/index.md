---
{
  "projection_kind": "taulib_declaration",
  "title": "ExponentFactors",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/exponent-factors/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.ExponentDerivation`.",
  "declaration_id": "TauLib.BookV.GravityField.ExponentDerivation::ExponentFactors",
  "declaration_slug": "exponent-factors",
  "kind": "structure",
  "name": "ExponentFactors",
  "module_name": "TauLib.BookV.GravityField.ExponentDerivation",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/",
  "source_line_start": 89,
  "source_line_end": 98,
  "registry_ids": [
    "V.D100"
  ],
  "related_registry_items": [
    {
      "id": "V.D100",
      "title": "tau-enstrophy",
      "url": "/registry/object/V.D100/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ExponentDerivation.lean#L89-L98",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ExponentDerivation.lean#L89-L98",
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

- Module: [TauLib.BookV.GravityField.ExponentDerivation](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/)
- Source path: [`TauLib/BookV/GravityField/ExponentDerivation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ExponentDerivation.lean#L89-L98)
- Source range: L89-L98
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D100` — tau-enstrophy

## Immediate Comment / Docstring

```lean
/-- [V.D100] The three factors that compose the exponent 18.
    Each comes from a different structural level of τ³. -/
```

## Source Excerpt

```lean
structure ExponentFactors where
  /-- b₁(T²): first Betti number of fiber torus. -/
  betti_1_fiber : Nat
  /-- dim(τ³): dimension of fibered product. -/
  dim_tau3 : Nat
  /-- |{π,γ,η}|: cardinality of solenoidal triple. -/
  solenoidal_card : Nat
  /-- The product gives the exponent. -/
  product : Nat := betti_1_fiber * dim_tau3 * solenoidal_card
  deriving Repr
```
