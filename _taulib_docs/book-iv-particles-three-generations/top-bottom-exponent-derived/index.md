---
{
  "projection_kind": "taulib_declaration",
  "title": "TopBottomExponentDerived",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/top-bottom-exponent-derived/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::TopBottomExponentDerived",
  "declaration_slug": "top-bottom-exponent-derived",
  "kind": "structure",
  "name": "TopBottomExponentDerived",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2644,
  "source_line_end": 2661,
  "registry_ids": [
    "IV.T196"
  ],
  "related_registry_items": [
    {
      "id": "IV.T196",
      "title": "m_t/m_b Exponent from Winding Algebra",
      "url": "/registry/object/IV.T196/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2644-L2661",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2644-L2661",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2644-L2661)
- Source range: L2644-L2661
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T196` — m_t/m_b Exponent from Winding Algebra

## Immediate Comment / Docstring

```lean
/-- [IV.T196] m_t/m_b exponent from winding algebra.
    β(t/b) = -dim(τ³)·(a₃+|lobes|)/a₃ = -3·15/13 = -45/13.
    First quark exponent derived from T² mode-counting. -/
```

## Source Excerpt

```lean
structure TopBottomExponentDerived where
  /-- Exponent numerator (absolute). -/
  exp_num : Nat := 45
  /-- Exponent denominator. -/
  exp_den : Nat := 13
  /-- dim(τ³). -/
  dim_tau3 : Nat := 3
  /-- CF partial quotient a₃. -/
  a3 : Nat := 13
  /-- Lemniscate lobe count. -/
  lobes : Nat := 2
  /-- Deviation in ppm. -/
  deviation_ppm : Int := 99
  /-- Numerator = dim × (a₃ + lobes). -/
  num_derivation : exp_num = dim_tau3 * (a3 + lobes)
  /-- Denominator = a₃. -/
  den_derivation : exp_den = a3
  deriving Repr
```
