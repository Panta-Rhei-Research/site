---
{
  "projection_kind": "taulib_declaration",
  "title": "HolonomyFormulaExact",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/holonomy-formula-exact/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.AlphaDerivation`.",
  "declaration_id": "TauLib.BookIV.Electroweak.AlphaDerivation::HolonomyFormulaExact",
  "declaration_slug": "holonomy-formula-exact",
  "kind": "structure",
  "name": "HolonomyFormulaExact",
  "module_name": "TauLib.BookIV.Electroweak.AlphaDerivation",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/",
  "source_line_start": 165,
  "source_line_end": 177,
  "registry_ids": [
    "IV.T49"
  ],
  "related_registry_items": [
    {
      "id": "IV.T49",
      "title": "Holonomy Formula for alpha_em",
      "url": "/registry/object/IV.T49/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L165-L177",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L165-L177",
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
- Source path: [`TauLib/BookIV/Electroweak/AlphaDerivation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L165-L177)
- Source range: L165-L177
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T49` — Holonomy Formula for alpha_em

## Immediate Comment / Docstring

```lean
/-- [IV.T49] The holonomy formula α = (π³/16)·Q⁴/(M²H³L⁶) is exact.
    The π³ factor arises from three independent U(1) circles in τ³.
    The denominator encodes the relational units from the calibration
    cascade, all determined by ι_τ. -/
```

## Source Excerpt

```lean
structure HolonomyFormulaExact where
  /-- The formula is exact (not approximate). -/
  is_exact : Bool := true
  /-- π³ = 31.006... from three circles. -/
  pi_cubed_approx : Nat
  pi_cubed_eq : pi_cubed_approx = 31
  /-- Denominator factor 16. -/
  denom_factor : Nat
  factor_eq : denom_factor = 16
  /-- Number of relational unit types in formula. -/
  unit_types : Nat
  types_eq : unit_types = 4  -- Q, M, H, L
  deriving Repr
```
