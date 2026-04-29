---
{
  "projection_kind": "taulib_declaration",
  "title": "UncertaintyProduct",
  "permalink": "/verify/taulib/docs/book-iv-physics-planck-character/uncertainty-product/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Physics.PlanckCharacter`.",
  "declaration_id": "TauLib.BookIV.Physics.PlanckCharacter::UncertaintyProduct",
  "declaration_slug": "uncertainty-product",
  "kind": "structure",
  "name": "UncertaintyProduct",
  "module_name": "TauLib.BookIV.Physics.PlanckCharacter",
  "module_url": "/verify/taulib/docs/book-iv-physics-planck-character/",
  "source_line_start": 182,
  "source_line_end": 194,
  "registry_ids": [
    "IV.D14"
  ],
  "related_registry_items": [
    {
      "id": "IV.D14",
      "title": "Uncertainty Product",
      "url": "/registry/object/IV.D14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/PlanckCharacter.lean#L182-L194",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.PlanckCharacter",
        "url": "/verify/taulib/docs/book-iv-physics-planck-character/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/PlanckCharacter.lean#L182-L194",
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

- Module: [TauLib.BookIV.Physics.PlanckCharacter](/verify/taulib/docs/book-iv-physics-planck-character/)
- Source path: [`TauLib/BookIV/Physics/PlanckCharacter.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/PlanckCharacter.lean#L182-L194)
- Source range: L182-L194
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D14` — Uncertainty Product

## Immediate Comment / Docstring

```lean
/-- [IV.D14] Uncertainty product template: the product Δx · Δp
    (or Δt · ΔE) that must satisfy the τ-Heisenberg inequality.

    The uncertainty arises from **incompatible address constraints**
    in τ-NF, NOT from measurement disturbance.

    Δx_n(x) = tau-position = rad(U_n(β_n(x)))
    Δp_n(x) = tau-momentum = min{t | Π^ph_n(x;t) exists} -/
```

## Source Excerpt

```lean
structure UncertaintyProduct where
  /-- Position/time resolution numerator. -/
  delta_x_numer : Nat
  /-- Position/time resolution denominator. -/
  delta_x_denom : Nat
  /-- Momentum/energy resolution numerator. -/
  delta_p_numer : Nat
  /-- Momentum/energy resolution denominator. -/
  delta_p_denom : Nat
  /-- Both denominators positive. -/
  denom_pos_x : delta_x_denom > 0
  denom_pos_p : delta_p_denom > 0
  deriving Repr
```
