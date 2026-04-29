---
{
  "projection_kind": "taulib_declaration",
  "title": "PentagonCPDerivation",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/pentagon-cpderivation/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::PentagonCPDerivation",
  "declaration_slug": "pentagon-cpderivation",
  "kind": "structure",
  "name": "PentagonCPDerivation",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1487,
  "source_line_end": 1494,
  "registry_ids": [
    "IV.P200"
  ],
  "related_registry_items": [
    {
      "id": "IV.P200",
      "title": "CP Violation from ω-Period Pentagon: Pentagon-Angle Derivation",
      "url": "/registry/object/IV.P200/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1487-L1494",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.ThreeGenerations",
        "url": "/verify/taulib/docs/book-iv-particles-three-generations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1487-L1494",
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1487-L1494)
- Source range: L1487-L1494
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P200` — CP Violation from ω-Period Pentagon: Pentagon-Angle Derivation

## Immediate Comment / Docstring

```lean
/-- [IV.P200] Pentagon CP derivation structure. -/
```

## Source Excerpt

```lean
structure PentagonCPDerivation where
  /-- 5 generators: {α,π,γ,η,ω}. -/
  n_generators : Nat := 5
  /-- ρ̄ denominator: 2π → multiplier 2. -/
  rho_bar_denom_multiplier : Nat := 2
  /-- Step angle 2π/5 = 72°. -/
  step_angle_degrees : Nat := 72
  deriving Repr
```
