---
{
  "projection_kind": "taulib_declaration",
  "title": "BottomMass",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/bottom-mass/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::BottomMass",
  "declaration_slug": "bottom-mass",
  "kind": "structure",
  "name": "BottomMass",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2497,
  "source_line_end": 2512,
  "registry_ids": [
    "IV.T193"
  ],
  "related_registry_items": [
    {
      "id": "IV.T193",
      "title": "Bottom Mass from τ-Chain at −1351 ppm",
      "url": "/registry/object/IV.T193/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2497-L2512",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2497-L2512",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2497-L2512)
- Source range: L2497-L2512
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T193` — Bottom Mass from τ-Chain at −1351 ppm

## Immediate Comment / Docstring

```lean
/-- [IV.T193] Bottom quark mass from τ-chain.

    m_b = (17/20)·ι_τ^(-20/13)·m_n = 4174.4 MeV.
    Combined exponent: -20/13 = -lobes²·W₃(4)/a₃ = -4×5/13.
    At -1351 ppm from PDG 4180 ± 7 MeV (0.8σ). -/
```

## Source Excerpt

```lean
structure BottomMass where
  /-- Combined exponent numerator (absolute). -/
  exp_num : Nat := 20
  /-- Combined exponent denominator. -/
  exp_den : Nat := 13
  /-- τ-predicted mass (×10). -/
  mass_x10 : Nat := 41744
  /-- PDG mass. -/
  pdg_mass : Nat := 4180
  /-- Deviation in ppm. -/
  deviation_ppm : Int := -1351
  /-- Numerator = lobes² × W₃(4). -/
  num_decomp : exp_num = 4 * 5
  /-- Denominator = a₃. -/
  den_is_a3 : exp_den = 13
  deriving Repr
```
