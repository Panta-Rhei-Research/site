---
{
  "projection_kind": "taulib_declaration",
  "title": "SectorLift",
  "permalink": "/verify/taulib/docs/book-iv-physics-planck-character/sector-lift/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Physics.PlanckCharacter`.",
  "declaration_id": "TauLib.BookIV.Physics.PlanckCharacter::SectorLift",
  "declaration_slug": "sector-lift",
  "kind": "structure",
  "name": "SectorLift",
  "module_name": "TauLib.BookIV.Physics.PlanckCharacter",
  "module_url": "/verify/taulib/docs/book-iv-physics-planck-character/",
  "source_line_start": 101,
  "source_line_end": 114,
  "registry_ids": [
    "IV.D15"
  ],
  "related_registry_items": [
    {
      "id": "IV.D15",
      "title": "Sector Lift Functor",
      "url": "/registry/object/IV.D15/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/PlanckCharacter.lean#L101-L114",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/PlanckCharacter.lean#L101-L114",
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
- Source path: [`TauLib/BookIV/Physics/PlanckCharacter.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/PlanckCharacter.lean#L101-L114)
- Source range: L101-L114
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D15` — Sector Lift Functor

## Immediate Comment / Docstring

```lean
/-- [IV.D15] Sector lift functor: Lift_S : H_fix[ω] → H_fix[ω].

    Each sector S has a unique unpolarized field endomorphism that
    maps ι_τ to the sector-specific physical constant:
    Lift_S(ι_τ) = c_S

    Key properties:
    - Ring homomorphism (preserves 0, 1, +, ×)
    - σ-equivariant (preserves lobe swap)
    - Uniquely determined by sector saturation chain -/
```

## Source Excerpt

```lean
structure SectorLift where
  /-- Source sector for this lift. -/
  source_sector : Sector
  /-- Lift_S(ι_τ) numerator — the sector-specific constant. -/
  target_numer : Nat
  /-- Lift_S(ι_τ) denominator. -/
  target_denom : Nat
  /-- Denominator is positive. -/
  denom_pos : target_denom > 0
  /-- All physical sector lifts are σ-equivariant. -/
  preserves_sigma : Bool := true
  /-- Sector lifts are ring homomorphisms. -/
  is_ring_hom : Bool := true
  deriving Repr
```
