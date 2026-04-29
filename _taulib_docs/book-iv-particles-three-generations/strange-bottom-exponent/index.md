---
{
  "projection_kind": "taulib_declaration",
  "title": "StrangeBottomExponent",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/strange-bottom-exponent/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::StrangeBottomExponent",
  "declaration_slug": "strange-bottom-exponent",
  "kind": "structure",
  "name": "StrangeBottomExponent",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2863,
  "source_line_end": 2880,
  "registry_ids": [
    "IV.T199"
  ],
  "related_registry_items": [
    {
      "id": "IV.T199",
      "title": "m_s/m_b Exponent from Confinement-Weighted Mode Count",
      "url": "/registry/object/IV.T199/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2863-L2880",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2863-L2880",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2863-L2880)
- Source range: L2863-L2880
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T199` — m_s/m_b Exponent from Confinement-Weighted Mode Count

## Immediate Comment / Docstring

```lean
/-- [IV.T199] m_s/m_b exponent from confinement-weighted mode count.
    β(s/b) = (lobes² · a₃ + λ(1,0)) / (dim · W₃(4)) = 53/15. -/
```

## Source Excerpt

```lean
structure StrangeBottomExponent where
  /-- Numerator: lobes² · a₃ + 1. -/
  exp_num : Nat := 53
  /-- Denominator: dim · W₃(4). -/
  exp_den : Nat := 15
  /-- lobes² factor. -/
  lobes_sq : Nat := 4
  /-- CF resonance a₃. -/
  a3 : Nat := 13
  /-- Ground-state eigenvalue λ(1,0). -/
  lambda_10 : Nat := 1
  /-- Deviation from PDG (ppm). -/
  deviation_ppm : Int := 1559
  /-- Numerator check: lobes² × a₃ + λ(1,0). -/
  num_check : lobes_sq * a3 + lambda_10 = exp_num := by decide
  /-- Denominator check: dim × W₃(4). -/
  den_check : 3 * 5 = exp_den := by decide
  deriving Repr
```
