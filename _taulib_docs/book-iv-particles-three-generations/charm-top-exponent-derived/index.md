---
{
  "projection_kind": "taulib_declaration",
  "title": "CharmTopExponentDerived",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/charm-top-exponent-derived/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::CharmTopExponentDerived",
  "declaration_slug": "charm-top-exponent-derived",
  "kind": "structure",
  "name": "CharmTopExponentDerived",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2669,
  "source_line_end": 2688,
  "registry_ids": [
    "IV.P221"
  ],
  "related_registry_items": [
    {
      "id": "IV.P221",
      "title": "m_c/m_t Exponent from Higgs-Weighted Transition",
      "url": "/registry/object/IV.P221/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2669-L2688",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2669-L2688",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2669-L2688)
- Source range: L2669-L2688
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P221` — m_c/m_t Exponent from Higgs-Weighted Transition

## Immediate Comment / Docstring

```lean
/-- [IV.P221] m_c/m_t exponent from Higgs-weighted transition.
    β(c/t) = dim·W₃(4)·n_H/(a₃+2·W₃(4)) = 3·5·7/23 = 105/23. -/
```

## Source Excerpt

```lean
structure CharmTopExponentDerived where
  /-- Exponent numerator. -/
  exp_num : Nat := 105
  /-- Exponent denominator. -/
  exp_den : Nat := 23
  /-- dim(τ³). -/
  dim_tau3 : Nat := 3
  /-- Window value W₃(4). -/
  w34 : Nat := 5
  /-- Higgs crossing number. -/
  n_higgs : Nat := 7
  /-- CF partial quotient a₃. -/
  a3 : Nat := 13
  /-- Deviation in ppm. -/
  deviation_ppm : Int := 1150
  /-- Numerator = dim × W₃(4) × n_H. -/
  num_derivation : exp_num = dim_tau3 * w34 * n_higgs
  /-- Denominator = a₃ + 2·W₃(4). -/
  den_derivation : exp_den = a3 + 2 * w34
  deriving Repr
```
