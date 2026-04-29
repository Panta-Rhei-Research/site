---
{
  "projection_kind": "taulib_declaration",
  "title": "WolfensteinRhoFormula",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/wolfenstein-rho-formula-l1237/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::WolfensteinRhoFormula",
  "declaration_slug": "wolfenstein-rho-formula-l1237",
  "kind": "structure",
  "name": "WolfensteinRhoFormula",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1237,
  "source_line_end": 1244,
  "registry_ids": [
    "IV.T164"
  ],
  "related_registry_items": [
    {
      "id": "IV.T164",
      "title": "rho_bar = 1/(2*pi): omega-Period Structural Derivation (tau-effective)",
      "url": "/registry/object/IV.T164/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1237-L1244",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1237-L1244",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1237-L1244)
- Source range: L1237-L1244
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T164` — rho_bar = 1/(2*pi): omega-Period Structural Derivation (tau-effective)

## Immediate Comment / Docstring

```lean
/-- [IV.T164] Wolfenstein ρ̄ formula structure (formalized). -/
```

## Source Excerpt

```lean
structure WolfensteinRhoFormula where
  /-- ω-period multiplier on ∂(τ³): 2π → 2. -/
  omega_period_multiplier : Nat := 2
  /-- Deviation from PDG in ppm. -/
  deviation_ppm : Nat := 975
  /-- τ-effective threshold in ppm. -/
  tau_eff_threshold_ppm : Nat := 5000
  deriving Repr
```
