---
{
  "projection_kind": "taulib_declaration",
  "title": "UpQuarkDirect",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/up-quark-direct/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::UpQuarkDirect",
  "declaration_slug": "up-quark-direct",
  "kind": "structure",
  "name": "UpQuarkDirect",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2730,
  "source_line_end": 2753,
  "registry_ids": [
    "IV.T197"
  ],
  "related_registry_items": [
    {
      "id": "IV.T197",
      "title": "Up Quark Direct Mass from Exponent Duality at +395 ppm",
      "url": "/registry/object/IV.T197/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2730-L2753",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2730-L2753",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2730-L2753)
- Source range: L2730-L2753
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T197` — Up Quark Direct Mass from Exponent Duality at +395 ppm

## Immediate Comment / Docstring

```lean
/-- [IV.T197] Up quark direct mass from exponent duality.
    m_u = (17/20)·ι_τ^(11/2)·m_n = 2.161 MeV at +395 ppm. -/
```

## Source Excerpt

```lean
structure UpQuarkDirect where
  /-- Exponent numerator. -/
  exp_num : Nat := 11
  /-- Exponent denominator. -/
  exp_den : Nat := 2
  /-- Prefactor numerator (same as top quark). -/
  prefactor_num : Nat := 17
  /-- Prefactor denominator. -/
  prefactor_den : Nat := 20
  /-- Predicted mass (×1000 keV). -/
  mass_x1000 : Nat := 2161
  /-- PDG mass (×1000 keV). -/
  pdg_mass_x1000 : Nat := 2160
  /-- Deviation in ppm. -/
  deviation_ppm : Int := 395
  /-- Improvement factor over chain. -/
  chain_improvement : Nat := 79
  /-- Chain deviation (ppm). -/
  chain_deviation_ppm : Int := 31043
  /-- Geometric mean m_u·m_t (MeV²). -/
  geometric_mean : Nat := 372617
  /-- Exponent numerator = 2·W₃(4) + 1. -/
  exp_structure : exp_num = 2 * 5 + 1
  deriving Repr
```
