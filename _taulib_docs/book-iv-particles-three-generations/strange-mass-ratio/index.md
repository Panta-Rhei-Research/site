---
{
  "projection_kind": "taulib_declaration",
  "title": "StrangeMassRatio",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/strange-mass-ratio/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::StrangeMassRatio",
  "declaration_slug": "strange-mass-ratio",
  "kind": "structure",
  "name": "StrangeMassRatio",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2471,
  "source_line_end": 2486,
  "registry_ids": [
    "IV.T192"
  ],
  "related_registry_items": [
    {
      "id": "IV.T192",
      "title": "Strange Mass from τ-Chain at +1559 ppm",
      "url": "/registry/object/IV.T192/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2471-L2486",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2471-L2486",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2471-L2486)
- Source range: L2471-L2486
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T192` — Strange Mass from τ-Chain at +1559 ppm

## Immediate Comment / Docstring

```lean
/-- [IV.T192] Strange quark mass from τ-chain.

    m_s = m_b(τ) × ι_τ^(53/15) = 4174.4 × 0.02241 = 93.55 MeV.
    Exponent: 53/15 = (4·a₃ + 1) / (dim·W₃(4))
            = (4×13 + 1) / (3×5).
    At +1559 ppm from PDG 93.4 ± 0.8 MeV (0.2σ). -/
```

## Source Excerpt

```lean
structure StrangeMassRatio where
  /-- Exponent numerator: 4·a₃ + 1 = 53. -/
  exp_num : Nat := 53
  /-- Exponent denominator: dim·W₃(4) = 15. -/
  exp_den : Nat := 15
  /-- τ-predicted mass in MeV (×100 for integer). -/
  mass_x100 : Nat := 9355
  /-- PDG mass (×10). -/
  pdg_mass_x10 : Nat := 934
  /-- Deviation in ppm. -/
  deviation_ppm : Int := 1559
  /-- Numerator = 4·a₃ + 1. -/
  num_decomp : exp_num = 4 * 13 + 1
  /-- Denominator = dim × W₃(4). -/
  den_decomp : exp_den = 3 * 5
  deriving Repr
```
