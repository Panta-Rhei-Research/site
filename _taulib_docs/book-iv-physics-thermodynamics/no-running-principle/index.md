---
{
  "projection_kind": "taulib_declaration",
  "title": "NoRunningPrinciple",
  "permalink": "/verify/taulib/docs/book-iv-physics-thermodynamics/no-running-principle/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Physics.Thermodynamics`.",
  "declaration_id": "TauLib.BookIV.Physics.Thermodynamics::NoRunningPrinciple",
  "declaration_slug": "no-running-principle",
  "kind": "structure",
  "name": "NoRunningPrinciple",
  "module_name": "TauLib.BookIV.Physics.Thermodynamics",
  "module_url": "/verify/taulib/docs/book-iv-physics-thermodynamics/",
  "source_line_start": 140,
  "source_line_end": 151,
  "registry_ids": [
    "IV.P04"
  ],
  "related_registry_items": [
    {
      "id": "IV.P04",
      "title": "No-Running Principle",
      "url": "/registry/object/IV.P04/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/Thermodynamics.lean#L140-L151",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.Thermodynamics",
        "url": "/verify/taulib/docs/book-iv-physics-thermodynamics/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/Thermodynamics.lean#L140-L151",
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

- Module: [TauLib.BookIV.Physics.Thermodynamics](/verify/taulib/docs/book-iv-physics-thermodynamics/)
- Source path: [`TauLib/BookIV/Physics/Thermodynamics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/Thermodynamics.lean#L140-L151)
- Source range: L140-L151
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P04` — No-Running Principle

## Immediate Comment / Docstring

```lean
/-- [IV.P04] No-Running Principle: ontic coupling constants do NOT run.

    Orthodox "running couplings" (α_s(Q²), α_EM(Q²), etc.) are NOT ontic.
    The τ-kernel coupling constants are **boundary fixed-point invariants**:

    - Fixed ontic value (determined by ι_τ alone)
    - Regime-dependent readout functor
    - Apparent "running" = projection drift from different measurement scales

    The coupling value in the registry IS the fixed ontic value. -/
```

## Source Excerpt

```lean
structure NoRunningPrinciple where
  /-- Which sector this principle applies to. -/
  sector : Sector
  /-- The fixed ontic coupling for this sector. -/
  ontic_coupling_numer : Nat
  /-- The fixed ontic coupling denominator. -/
  ontic_coupling_denom : Nat
  /-- Denominator positive. -/
  denom_pos : ontic_coupling_denom > 0
  /-- The coupling is regime-independent (fixed). -/
  regime_independent : Bool := true
  deriving Repr
```
