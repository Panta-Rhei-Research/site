---
{
  "projection_kind": "taulib_declaration",
  "title": "HolonomyCorrectionDetail",
  "permalink": "/verify/taulib/docs/book-iv-mass-derivation-holonomy-detail/holonomy-correction-detail/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.MassDerivation.HolonomyDetail`.",
  "declaration_id": "TauLib.BookIV.MassDerivation.HolonomyDetail::HolonomyCorrectionDetail",
  "declaration_slug": "holonomy-correction-detail",
  "kind": "structure",
  "name": "HolonomyCorrectionDetail",
  "module_name": "TauLib.BookIV.MassDerivation.HolonomyDetail",
  "module_url": "/verify/taulib/docs/book-iv-mass-derivation-holonomy-detail/",
  "source_line_start": 153,
  "source_line_end": 170,
  "registry_ids": [
    "IV.D315"
  ],
  "related_registry_items": [
    {
      "id": "IV.D315",
      "title": "Holonomy Correction Data --- IV.D45",
      "url": "/registry/object/IV.D315/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L153-L170",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L153-L170",
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
- Source path: [`TauLib/BookIV/MassDerivation/HolonomyDetail.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L153-L170)
- Source range: L153-L170
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D315` — Holonomy Correction Data --- IV.D45

## Immediate Comment / Docstring

```lean
/-- [IV.D315] Holonomy correction data: the three components that
    make up the Level 1+ correction π³α²·ι_τ^(-2).

    1. π³ from triple holonomy (31.006)
    2. α² from charge conjugation (5.3 × 10⁻⁵)
    3. ι_τ^(-2) from breathing operator scale (8.58)

    The combined correction π³α²·ι_τ^(-2) ≈ 0.014 refines the mass
    ratio from Level 0 (7.7 ppm) to Level 1+ (0.025 ppm). -/
```

## Source Excerpt

```lean
structure HolonomyCorrectionDetail where
  /-- π³ numerator. -/
  pi3_numer : Nat
  /-- π³ denominator. -/
  pi3_denom : Nat
  /-- α² numerator. -/
  alpha2_numer : Nat
  /-- α² denominator. -/
  alpha2_denom : Nat
  /-- ι_τ^(-2) numerator. -/
  iota_neg2_n : Nat
  /-- ι_τ^(-2) denominator. -/
  iota_neg2_d : Nat
  /-- All denominators positive. -/
  pi3_denom_pos : pi3_denom > 0
  alpha2_denom_pos : alpha2_denom > 0
  iota_neg2_denom_pos : iota_neg2_d > 0
  deriving Repr
```
