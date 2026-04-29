---
{
  "projection_kind": "taulib_declaration",
  "title": "PlanckCharacter",
  "permalink": "/verify/taulib/docs/book-iv-physics-planck-character/planck-character/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Physics.PlanckCharacter`.",
  "declaration_id": "TauLib.BookIV.Physics.PlanckCharacter::PlanckCharacter",
  "declaration_slug": "planck-character",
  "kind": "structure",
  "name": "PlanckCharacter",
  "module_name": "TauLib.BookIV.Physics.PlanckCharacter",
  "module_url": "/verify/taulib/docs/book-iv-physics-planck-character/",
  "source_line_start": 70,
  "source_line_end": 81,
  "registry_ids": [
    "IV.D13"
  ],
  "related_registry_items": [
    {
      "id": "IV.D13",
      "title": "Planck Character",
      "url": "/registry/object/IV.D13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/PlanckCharacter.lean#L70-L81",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/PlanckCharacter.lean#L70-L81",
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
- Source path: [`TauLib/BookIV/Physics/PlanckCharacter.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/PlanckCharacter.lean#L70-L81)
- Source range: L70-L81
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D13` — Planck Character

## Immediate Comment / Docstring

```lean
/-- [IV.D13] The Planck character ℏ_τ: universal lower bound in the
    boundary holonomy algebra H_∂[ω].

    ℏ_τ = Δx_ω(x*) · Δp_ω(x*) where x* is the canonical saturating chain.
    It is the QM sector lift of the master constant ι_τ. -/
```

## Source Excerpt

```lean
structure PlanckCharacter where
  /-- ℏ_τ numerator (scaled rational representation). -/
  numer : Nat
  /-- ℏ_τ denominator (scaled rational representation). -/
  denom : Nat
  /-- Denominator is positive. -/
  denom_pos : denom > 0
  /-- ℏ_τ is σ-fixed (unpolarized, lives at lemniscate crossing point). -/
  sigma_fixed : Bool := true
  /-- ℏ_τ is the attained minimum (not merely infimum) via saturation. -/
  is_minimum : Bool := true
  deriving Repr
```
