---
{
  "projection_kind": "taulib_declaration",
  "title": "PhysicalConstantsCore",
  "permalink": "/verify/taulib/docs/book-iv-physics-planck-character/physical-constants-core/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Physics.PlanckCharacter`.",
  "declaration_id": "TauLib.BookIV.Physics.PlanckCharacter::PhysicalConstantsCore",
  "declaration_slug": "physical-constants-core",
  "kind": "structure",
  "name": "PhysicalConstantsCore",
  "module_name": "TauLib.BookIV.Physics.PlanckCharacter",
  "module_url": "/verify/taulib/docs/book-iv-physics-planck-character/",
  "source_line_start": 219,
  "source_line_end": 228,
  "registry_ids": [
    "IV.R03"
  ],
  "related_registry_items": [
    {
      "id": "IV.R03",
      "title": "Physical Constants Core",
      "url": "/registry/object/IV.R03/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/PlanckCharacter.lean#L219-L228",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/PlanckCharacter.lean#L219-L228",
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
- Source path: [`TauLib/BookIV/Physics/PlanckCharacter.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/PlanckCharacter.lean#L219-L228)
- Source range: L219-L228
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R03` — Physical Constants Core

## Immediate Comment / Docstring

```lean
/-- [IV.R03] The physical constants core C_phys = Q(ι_τ):
    the closure of ι_τ under field operations and all sector lift functors.

    Every physical constant is an ι_τ-image:
    - ℏ_τ = Lift_QM(ι_τ)
    - κ_τ = Lift_GR(ι_τ)
    - α_EM = (8/15) · ι_τ⁴
    - All sector vacua Ω*_S = F_S(ι_τ)
    - All excitation quanta q_S[ω] = G_S(ι_τ)

    C_phys is **countably generated** by a single element (ι_τ). -/
```

## Source Excerpt

```lean
structure PhysicalConstantsCore where
  /-- The master constant ι_τ = 2/(π+e) numerator. -/
  master_numer : Nat := iota
  /-- The master constant denominator. -/
  master_denom : Nat := iotaD
  /-- Number of sector lifts (= 5). -/
  num_lifts : Nat := 5
  /-- All constants are σ-fixed (unpolarized). -/
  all_sigma_fixed : Bool := true
  deriving Repr
```
