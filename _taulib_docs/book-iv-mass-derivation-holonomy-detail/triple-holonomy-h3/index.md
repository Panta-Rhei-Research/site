---
{
  "projection_kind": "taulib_declaration",
  "title": "TripleHolonomyH3",
  "permalink": "/verify/taulib/docs/book-iv-mass-derivation-holonomy-detail/triple-holonomy-h3/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.MassDerivation.HolonomyDetail`.",
  "declaration_id": "TauLib.BookIV.MassDerivation.HolonomyDetail::TripleHolonomyH3",
  "declaration_slug": "triple-holonomy-h3",
  "kind": "structure",
  "name": "TripleHolonomyH3",
  "module_name": "TauLib.BookIV.MassDerivation.HolonomyDetail",
  "module_url": "/verify/taulib/docs/book-iv-mass-derivation-holonomy-detail/",
  "source_line_start": 72,
  "source_line_end": 91,
  "registry_ids": [
    "IV.D314"
  ],
  "related_registry_items": [
    {
      "id": "IV.D314",
      "title": "Triple Holonomy --- IV.D44",
      "url": "/registry/object/IV.D314/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L72-L91",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.MassDerivation.HolonomyDetail",
        "url": "/verify/taulib/docs/book-iv-mass-derivation-holonomy-detail/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L72-L91",
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

- Module: [TauLib.BookIV.MassDerivation.HolonomyDetail](/verify/taulib/docs/book-iv-mass-derivation-holonomy-detail/)
- Source path: [`TauLib/BookIV/MassDerivation/HolonomyDetail.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L72-L91)
- Source range: L72-L91
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D314` — Triple Holonomy --- IV.D44

## Immediate Comment / Docstring

```lean
/-- [IV.D314] Triple holonomy H₃ = ∮_{T_π}·∮_{T_γ}·∮_{T_η}.

    The product of Wilson loops around the three independent U(1)
    circles in τ³ = τ¹ ×_f T². Each circle contributes one factor
    of π, giving π³ as the holonomy prefactor.

    Circle assignments:
    - T_π: base τ¹ circle (generator π, Weak/temporal sector A)
    - T_γ: first fiber circle (generator γ, EM sector B)
    - T_η: second fiber circle (generator η, Strong sector C) -/
```

## Source Excerpt

```lean
structure TripleHolonomyH3 where
  /-- Number of independent circles. -/
  circle_count : Nat
  /-- Circle count is 3. -/
  three_circles : circle_count = 3
  /-- Generator labels for the three circles. -/
  generators : List String
  /-- Generators list has correct length. -/
  gen_count : generators.length = circle_count
  /-- π exponent matches circle count. -/
  pi_exponent : Nat
  /-- Exponent = circle count. -/
  exp_eq : pi_exponent = circle_count
  /-- π³ rational approximation numerator. -/
  pi_cubed_n : Nat
  /-- π³ rational approximation denominator. -/
  pi_cubed_d : Nat
  /-- Denominator positive. -/
  denom_pos : pi_cubed_d > 0
  deriving Repr
```
