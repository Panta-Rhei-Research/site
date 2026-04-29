---
{
  "projection_kind": "taulib_declaration",
  "title": "bhs_universality",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-bipolar-holonomy/bhs-universality/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.BipolarHolonomy`.",
  "declaration_id": "TauLib.BookV.GravityField.BipolarHolonomy::bhs_universality",
  "declaration_slug": "bhs-universality",
  "kind": "theorem",
  "name": "bhs_universality",
  "module_name": "TauLib.BookV.GravityField.BipolarHolonomy",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-bipolar-holonomy/",
  "source_line_start": 142,
  "source_line_end": 143,
  "registry_ids": [
    "V.T86"
  ],
  "related_registry_items": [
    {
      "id": "V.T86",
      "title": "Chandrasekhar Mass from tau-Framework --- V.T38",
      "url": "/registry/object/V.T86/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/BipolarHolonomy.lean#L142-L143",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/BipolarHolonomy.lean#L142-L143",
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

- Module: [TauLib.BookV.GravityField.BipolarHolonomy](/verify/taulib/docs/book-v-gravity-field-bipolar-holonomy/)
- Source path: [`TauLib/BookV/GravityField/BipolarHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/BipolarHolonomy.lean#L142-L143)
- Source range: L142-L143
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T86` — Chandrasekhar Mass from tau-Framework --- V.T38

## Immediate Comment / Docstring

```lean
/-- [V.T86] Universal coefficient theorem: b¹ = b₁ when H₁ is free.

    For τ³ with H₁(τ³; ℤ) ≅ ℤ³ (free abelian), the UCT gives:
    H¹(τ³; ℤ) ≅ Hom(H₁(τ³; ℤ), ℤ) ⊕ Ext¹(H₀(τ³; ℤ), ℤ)

    Since both H₁ and H₀ are free, Ext¹ = 0, and
    Hom(ℤ³, ℤ) ≅ ℤ³, giving b¹ = b₁ = 3.

    This is the key algebraic topology fact that makes
    b₁_arena = b1_arena in the BHS. -/
```

## Source Excerpt

```lean
theorem bhs_universality :
    canonical_bhs.b₁_arena = canonical_bhs.b1_arena := by rfl
```
