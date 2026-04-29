---
{
  "projection_kind": "taulib_declaration",
  "title": "EtaBFormalDerivation",
  "permalink": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/eta-bformal-derivation/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BaryogenesisAsymmetry`.",
  "declaration_id": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry::EtaBFormalDerivation",
  "declaration_slug": "eta-bformal-derivation",
  "kind": "structure",
  "name": "EtaBFormalDerivation",
  "module_name": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
  "module_url": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/",
  "source_line_start": 241,
  "source_line_end": 252,
  "registry_ids": [
    "V.T188"
  ],
  "related_registry_items": [
    {
      "id": "V.T188",
      "title": "η_B Formal Derivation: α·ι_τ¹⁵·(5/6) at −10320 ppm",
      "url": "/registry/object/V.T188/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L241-L252",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
        "url": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L241-L252",
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

- Module: [TauLib.BookV.Cosmology.BaryogenesisAsymmetry](/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/)
- Source path: [`TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L241-L252)
- Source range: L241-L252
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T188` — η_B Formal Derivation: α·ι_τ¹⁵·(5/6) at −10320 ppm

## Immediate Comment / Docstring

```lean
/-- [V.T188] η_B Formal Derivation at −10320 ppm.
    η_B = α·ι_τ¹⁵·(5/6) = 6.080×10⁻¹⁰, Planck 6.104±0.058. -/
```

## Source Excerpt

```lean
structure EtaBFormalDerivation where
  /-- Exponent in ι_τ^k: k = dim(τ³) × |generators|. -/
  exponent : Nat := 15
  /-- Exponent decomposition proof. -/
  exponent_eq : exponent = 3 * 5
  /-- Coefficient numerator (non-resonant channels). -/
  coeff_numer : Nat := 5
  /-- Coefficient denominator (total channels). -/
  coeff_denom : Nat := 6
  /-- Number of σ from Planck (deviation within 1.09σ), ×100. -/
  deviation_sigma_x100 : Nat := 109
  deriving Repr
```
