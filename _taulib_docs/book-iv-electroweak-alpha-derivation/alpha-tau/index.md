---
{
  "projection_kind": "taulib_declaration",
  "title": "AlphaTau",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/alpha-tau/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.AlphaDerivation`.",
  "declaration_id": "TauLib.BookIV.Electroweak.AlphaDerivation::AlphaTau",
  "declaration_slug": "alpha-tau",
  "kind": "structure",
  "name": "AlphaTau",
  "module_name": "TauLib.BookIV.Electroweak.AlphaDerivation",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/",
  "source_line_start": 68,
  "source_line_end": 83,
  "registry_ids": [
    "IV.D104"
  ],
  "related_registry_items": [
    {
      "id": "IV.D104",
      "title": "tau-Native Fine-Structure Constant",
      "url": "/registry/object/IV.D104/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L68-L83",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L68-L83",
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
- Source path: [`TauLib/BookIV/Electroweak/AlphaDerivation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L68-L83)
- Source range: L68-L83
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D104` — tau-Native Fine-Structure Constant

## Immediate Comment / Docstring

```lean
/-- [IV.D104] The τ-native fine-structure constant α_τ.
    Two equivalent formulas:
    - Spectral: α_spec = (8/15)·ι_τ⁴ (leading order, 0.6% off)
    - Holonomy: α = (π³/16)·Q⁴/(M²H³L⁶) (exact)
    Both are fully determined by ι_τ = 2/(π+e). -/
```

## Source Excerpt

```lean
structure AlphaTau where
  /-- Spectral formula numerator (8·ι_τ⁴). -/
  spectral_numer : Nat
  /-- Spectral formula denominator (15·D⁴). -/
  spectral_denom : Nat
  denom_pos : spectral_denom > 0
  /-- 1/α lies in [137, 139] for spectral formula. -/
  inverse_lower : spectral_denom > 137 * spectral_numer
  inverse_upper : spectral_denom < 139 * spectral_numer
  /-- Number of holonomy circles (π³ origin). -/
  holonomy_circles : Nat
  circles_eq : holonomy_circles = 3
  /-- Number of relational units in denominator. -/
  relational_units : Nat
  units_eq : relational_units = 4  -- Q, M, H, L
  deriving Repr
```
