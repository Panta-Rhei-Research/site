---
{
  "projection_kind": "taulib_declaration",
  "title": "HolonomyCorrectionR",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/holonomy-correction-r/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.AlphaDerivation`.",
  "declaration_id": "TauLib.BookIV.Electroweak.AlphaDerivation::HolonomyCorrectionR",
  "declaration_slug": "holonomy-correction-r",
  "kind": "structure",
  "name": "HolonomyCorrectionR",
  "module_name": "TauLib.BookIV.Electroweak.AlphaDerivation",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/",
  "source_line_start": 135,
  "source_line_end": 144,
  "registry_ids": [
    "IV.D106"
  ],
  "related_registry_items": [
    {
      "id": "IV.D106",
      "title": "Holonomy Correction Factor",
      "url": "/registry/object/IV.D106/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L135-L144",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.AlphaDerivation",
        "url": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L135-L144",
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

- Module: [TauLib.BookIV.Electroweak.AlphaDerivation](/verify/taulib/docs/book-iv-electroweak-alpha-derivation/)
- Source path: [`TauLib/BookIV/Electroweak/AlphaDerivation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L135-L144)
- Source range: L135-L144
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D106` — Holonomy Correction Factor

## Immediate Comment / Docstring

```lean
/-- [IV.D106] Holonomy correction factor R(ι_τ) relating the spectral
    and holonomy formulas: α = (8/15)·ι_τ⁴ · R(ι_τ).
    R ≈ 1.0065: the spectral formula is a 0.6% approximation.
    R encodes the detailed calibration cascade. -/
```

## Source Excerpt

```lean
structure HolonomyCorrectionR where
  /-- R numerator (scaled at 10⁶). -/
  r_numer : Nat
  /-- R denominator. -/
  r_denom : Nat
  denom_pos : r_denom > 0
  /-- R is near unity: 1.000 < R < 1.010. -/
  near_unity_lower : r_numer * 1000 > r_denom * 1000
  near_unity_upper : r_numer * 1000 < r_denom * 1010
  deriving Repr
```
