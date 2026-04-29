---
{
  "projection_kind": "taulib_declaration",
  "title": "Sqrt3Triad",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/sqrt3-triad/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.EWSynthesis`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWSynthesis::Sqrt3Triad",
  "declaration_slug": "sqrt3-triad",
  "kind": "structure",
  "name": "Sqrt3Triad",
  "module_name": "TauLib.BookIV.Electroweak.EWSynthesis",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/",
  "source_line_start": 202,
  "source_line_end": 213,
  "registry_ids": [
    "IV.T124"
  ],
  "related_registry_items": [
    {
      "id": "IV.T124",
      "title": "The sqrt3",
      "url": "/registry/object/IV.T124/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L202-L213",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.EWSynthesis",
        "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L202-L213",
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

- Module: [TauLib.BookIV.Electroweak.EWSynthesis](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/)
- Source path: [`TauLib/BookIV/Electroweak/EWSynthesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L202-L213)
- Source range: L202-L213
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T124` — The sqrt3

## Immediate Comment / Docstring

```lean
/-- [IV.T124] The √3 triad: the same algebraic quantity √3 = |1 − ω|
    (where ω = e^{2πi/3} is a primitive cube root of unity) appears
    in three independent physical contexts:

    1. R mass ratio correction: √3 · ι_τ^{-2} (spectral distance on L)
    2. Proton-neutron mass splitting: δ_A/m_n ≈ (√3/2) · ι_τ⁶ (isospin)
    3. Gravitational closing identity: α_G = α¹⁸ · √3 (bi-rotation)

    All three appearances trace to the SAME geometric origin: the
    three-fold structure of the lemniscate L = S¹ ∨ S¹ with its
    three sectors {Lobe₁, Lobe₂, Crossing}. -/
```

## Source Excerpt

```lean
structure Sqrt3Triad where
  /-- Context 1: R mass ratio. -/
  context_R : String := "R correction: sqrt(3) * iota_tau^(-2)"
  /-- Context 2: proton-neutron splitting. -/
  context_delta_A : String := "delta_A/m_n approx (sqrt(3)/2) * iota_tau^6"
  /-- Context 3: gravitational closing. -/
  context_alpha_G : String := "alpha_G = alpha^18 * sqrt(3) * correction"
  /-- Geometric origin. -/
  origin : String := "|1 - omega| where omega = e^(2pi*i/3)"
  /-- Number of independent appearances. -/
  appearance_count : Nat := 3
  deriving Repr
```
