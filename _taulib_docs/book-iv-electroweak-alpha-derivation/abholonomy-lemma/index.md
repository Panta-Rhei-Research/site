---
{
  "projection_kind": "taulib_declaration",
  "title": "ABHolonomyLemma",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/abholonomy-lemma/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.AlphaDerivation`.",
  "declaration_id": "TauLib.BookIV.Electroweak.AlphaDerivation::ABHolonomyLemma",
  "declaration_slug": "abholonomy-lemma",
  "kind": "structure",
  "name": "ABHolonomyLemma",
  "module_name": "TauLib.BookIV.Electroweak.AlphaDerivation",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/",
  "source_line_start": 222,
  "source_line_end": 232,
  "registry_ids": [
    "IV.L02"
  ],
  "related_registry_items": [
    {
      "id": "IV.L02",
      "title": "Holonomy Normalization",
      "url": "/registry/object/IV.L02/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L222-L232",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L222-L232",
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
- Source path: [`TauLib/BookIV/Electroweak/AlphaDerivation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L222-L232)
- Source range: L222-L232
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.L02` — Holonomy Normalization

## Immediate Comment / Docstring

```lean
/-- [IV.L02] AB holonomy around the minimal EM loop on T² equals
    the B-sector self-coupling κ(B;2) = ι_τ².
    This connects the gauge-theory holonomy to the sector coupling. -/
```

## Source Excerpt

```lean
structure ABHolonomyLemma where
  /-- The holonomy equals κ(B;2). -/
  equals_kappa_b : Bool := true
  /-- κ(B;2) = ι_τ². -/
  kappa_b_numer : Nat
  kappa_b_denom : Nat
  denom_pos : kappa_b_denom > 0
  /-- Check: numer/denom ≈ 0.1166 (ι_τ²). -/
  numer_eq : kappa_b_numer = iota_tau_numer * iota_tau_numer
  denom_eq : kappa_b_denom = iota_tau_denom * iota_tau_denom
  deriving Repr
```
