---
{
  "projection_kind": "taulib_declaration",
  "title": "CharmMassRatio",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/charm-mass-ratio/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::CharmMassRatio",
  "declaration_slug": "charm-mass-ratio",
  "kind": "structure",
  "name": "CharmMassRatio",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2444,
  "source_line_end": 2459,
  "registry_ids": [
    "IV.T191"
  ],
  "related_registry_items": [
    {
      "id": "IV.T191",
      "title": "Charm Mass from τ-Chain at +1150 ppm",
      "url": "/registry/object/IV.T191/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2444-L2459",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2444-L2459",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2444-L2459)
- Source range: L2444-L2459
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T191` — Charm Mass from τ-Chain at +1150 ppm

## Immediate Comment / Docstring

```lean
/-- [IV.T191] Charm quark mass from τ-chain.

    m_c = m_t(τ) × ι_τ^(105/23) = 172440 × 0.007391 = 1274.5 MeV.
    Exponent: 105/23 = dim·W₃(4)·n_H / (a₃ + 2·W₃(4))
            = 3 × 5 × 7 / (13 + 10).
    At +1150 ppm from PDG 1273 ± 4 MeV (0.4σ). -/
```

## Source Excerpt

```lean
structure CharmMassRatio where
  /-- Exponent numerator: dim·W₃(4)·n_H = 3×5×7 = 105. -/
  exp_num : Nat := 105
  /-- Exponent denominator: a₃ + 2·W₃(4) = 13 + 10 = 23. -/
  exp_den : Nat := 23
  /-- τ-predicted mass in MeV (×10 for integer). -/
  mass_x10 : Nat := 12745
  /-- PDG mass in MeV. -/
  pdg_mass : Nat := 1273
  /-- Deviation in ppm. -/
  deviation_ppm : Int := 1150
  /-- Exponent numerator = dim × W₃(4) × n_Higgs. -/
  num_decomp : exp_num = 3 * 5 * 7
  /-- Exponent denominator = a₃ + 2·W₃(4). -/
  den_decomp : exp_den = 13 + 2 * 5
  deriving Repr
```
