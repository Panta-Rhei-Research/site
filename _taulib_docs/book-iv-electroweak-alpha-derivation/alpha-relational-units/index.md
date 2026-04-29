---
{
  "projection_kind": "taulib_declaration",
  "title": "AlphaRelationalUnits",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/alpha-relational-units/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.AlphaDerivation`.",
  "declaration_id": "TauLib.BookIV.Electroweak.AlphaDerivation::AlphaRelationalUnits",
  "declaration_slug": "alpha-relational-units",
  "kind": "structure",
  "name": "AlphaRelationalUnits",
  "module_name": "TauLib.BookIV.Electroweak.AlphaDerivation",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/",
  "source_line_start": 278,
  "source_line_end": 294,
  "registry_ids": [
    "IV.L04"
  ],
  "related_registry_items": [
    {
      "id": "IV.L04",
      "title": "Mediator Ratio",
      "url": "/registry/object/IV.L04/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L278-L294",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L278-L294",
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
- Source path: [`TauLib/BookIV/Electroweak/AlphaDerivation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L278-L294)
- Source range: L278-L294
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.L04` — Mediator Ratio

## Immediate Comment / Docstring

```lean
/-- [IV.L04] α = (π³/16) · Q⁴/(M²H³L⁶): the holonomy formula
    expressed in terms of the four relational units.
    The exponents (4, 2, 3, 6) are structurally determined by the
    dimension of each unit in the τ-framework. -/
```

## Source Excerpt

```lean
structure AlphaRelationalUnits where
  /-- Exponent of Q (charge unit). -/
  q_exp : Nat
  q_eq : q_exp = 4
  /-- Exponent of M (mass unit). -/
  m_exp : Nat
  m_eq : m_exp = 2
  /-- Exponent of H (frequency unit). -/
  h_exp : Nat
  h_eq : h_exp = 3
  /-- Exponent of L (length unit). -/
  l_exp : Nat
  l_eq : l_exp = 6
  /-- Sum of denominator exponents = 2 + 3 + 6 = 11. -/
  denom_total : Nat
  denom_eq : denom_total = m_exp + h_exp + l_exp
  deriving Repr
```
