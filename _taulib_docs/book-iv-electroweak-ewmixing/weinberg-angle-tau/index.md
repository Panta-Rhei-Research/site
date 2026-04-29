---
{
  "projection_kind": "taulib_declaration",
  "title": "WeinbergAngleTau",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewmixing/weinberg-angle-tau/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.EWMixing`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWMixing::WeinbergAngleTau",
  "declaration_slug": "weinberg-angle-tau",
  "kind": "structure",
  "name": "WeinbergAngleTau",
  "module_name": "TauLib.BookIV.Electroweak.EWMixing",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewmixing/",
  "source_line_start": 150,
  "source_line_end": 158,
  "registry_ids": [
    "IV.D130"
  ],
  "related_registry_items": [
    {
      "id": "IV.D130",
      "title": "Weinberg Angle",
      "url": "/registry/object/IV.D130/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L150-L158",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.EWMixing",
        "url": "/verify/taulib/docs/book-iv-electroweak-ewmixing/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L150-L158",
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

- Module: [TauLib.BookIV.Electroweak.EWMixing](/verify/taulib/docs/book-iv-electroweak-ewmixing/)
- Source path: [`TauLib/BookIV/Electroweak/EWMixing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L150-L158)
- Source range: L150-L158
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D130` — Weinberg Angle

## Immediate Comment / Docstring

```lean
/-- [IV.D130] The Weinberg angle (weak mixing angle) θ_W.
    In the τ-framework: sin²(θ_W) = κ(A,D) = ι_τ(1−ι_τ).

    τ-prediction: sin²(θ_W) ≈ 0.2249
    Experimental (Z pole, MS-bar): sin²(θ_W) ≈ 0.2312

    Numerator/denominator encode the τ-predicted value. -/
```

## Source Excerpt

```lean
structure WeinbergAngleTau where
  /-- sin²(θ_W) numerator = κ(A,D) numerator. -/
  sin2_numer : Nat
  /-- sin²(θ_W) denominator = κ(A,D) denominator. -/
  sin2_denom : Nat
  /-- Denominator positive. -/
  denom_pos : sin2_denom > 0
  /-- This equals the (A,D) cross-coupling. -/
  equals_kappaAD : sin2_numer = kappa_AD.numer ∧ sin2_denom = kappa_AD.denom
```
