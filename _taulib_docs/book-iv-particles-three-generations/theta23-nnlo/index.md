---
{
  "projection_kind": "taulib_declaration",
  "title": "Theta23NNLO",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/theta23-nnlo/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::Theta23NNLO",
  "declaration_slug": "theta23-nnlo",
  "kind": "structure",
  "name": "Theta23NNLO",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 3028,
  "source_line_end": 3043,
  "registry_ids": [
    "IV.T206"
  ],
  "related_registry_items": [
    {
      "id": "IV.T206",
      "title": "θ₂₃ NNLO from Holonomy-at-Window-Squared",
      "url": "/registry/object/IV.T206/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L3028-L3043",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L3028-L3043",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L3028-L3043)
- Source range: L3028-L3043
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T206` — θ₂₃ NNLO from Holonomy-at-Window-Squared

## Immediate Comment / Docstring

```lean
/-- [IV.T206] θ₂₃ NNLO from holonomy-at-window-squared.
    sin(θ₂₃) = (1−ι_τ⁵)/(1+ι_τ) × (1−ι_τ²/W₃(4)²)
              = (1−ι_τ⁵)/(1+ι_τ) × (1−ι_τ²/25)
    sin²θ₂₃ = 0.5457 at −494 ppm from PDG 0.546.
    94% improvement from NLO (+8604 ppm).
    Universal NNLO pattern: W₃(4)²=25 denominator shared with m_μ/m_e. -/
```

## Source Excerpt

```lean
structure Theta23NNLO where
  /-- NNLO correction denominator = W₃(4)². -/
  nnlo_denom : Nat := 25
  /-- Holonomy power in correction (ι_τ²). -/
  holonomy_power : Nat := 2
  /-- sin²θ₂₃ × 10000. -/
  sin2_x10000 : Nat := 5457
  /-- PDG sin²θ₂₃ × 10000. -/
  pdg_x10000 : Nat := 5460
  /-- Deviation in ppm (signed). -/
  deviation_ppm : Int := -494
  /-- NLO deviation was. -/
  nlo_ppm : Int := 8604
  /-- Improvement factor (%). -/
  improvement_pct : Nat := 94
  deriving Repr
```
