---
{
  "projection_kind": "taulib_declaration",
  "title": "MassSquaredSplittings",
  "permalink": "/verify/taulib/docs/book-v-cosmology-neutrino-background/mass-squared-splittings/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.NeutrinoBackground`.",
  "declaration_id": "TauLib.BookV.Cosmology.NeutrinoBackground::MassSquaredSplittings",
  "declaration_slug": "mass-squared-splittings",
  "kind": "structure",
  "name": "MassSquaredSplittings",
  "module_name": "TauLib.BookV.Cosmology.NeutrinoBackground",
  "module_url": "/verify/taulib/docs/book-v-cosmology-neutrino-background/",
  "source_line_start": 217,
  "source_line_end": 230,
  "registry_ids": [
    "V.T269"
  ],
  "related_registry_items": [
    {
      "id": "V.T269",
      "title": "Mass-Squared Splittings from τ-Exponents",
      "url": "/registry/object/V.T269/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L217-L230",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.NeutrinoBackground",
        "url": "/verify/taulib/docs/book-v-cosmology-neutrino-background/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L217-L230",
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

- Module: [TauLib.BookV.Cosmology.NeutrinoBackground](/verify/taulib/docs/book-v-cosmology-neutrino-background/)
- Source path: [`TauLib/BookV/Cosmology/NeutrinoBackground.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L217-L230)
- Source range: L217-L230
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T269` — Mass-Squared Splittings from τ-Exponents

## Immediate Comment / Docstring

```lean
/-- [V.T269] Mass-squared splittings from τ-exponents.
    Δm²₂₁(τ) ≈ 4.66 × 10⁻⁴ eV² (NuFIT: 7.53 × 10⁻⁵, factor 6.2× off).
    |Δm²₃₂|(τ) ≈ 3.01 × 10⁻³ eV² (NuFIT: 2.453 × 10⁻³, +22.9%). -/
```

## Source Excerpt

```lean
structure MassSquaredSplittings where
  /-- Δm²₂₁ in units of 10⁻⁵ eV². -/
  dm21_sq_e5 : Float := 46.6
  /-- |Δm²₃₂| in units of 10⁻³ eV². -/
  dm32_sq_e3 : Float := 3.01
  /-- NuFIT Δm²₂₁ in units of 10⁻⁵ eV². -/
  dm21_sq_nufit : Float := 7.53
  /-- NuFIT |Δm²₃₂| in units of 10⁻³ eV². -/
  dm32_sq_nufit : Float := 2.453
  /-- Solar splitting ratio (τ/NuFIT). -/
  solar_ratio : Float := 6.19
  /-- Atmospheric deviation (%). -/
  atm_deviation_pct : Float := 22.9
  deriving Repr
```
