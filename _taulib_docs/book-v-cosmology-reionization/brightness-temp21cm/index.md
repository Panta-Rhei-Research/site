---
{
  "projection_kind": "taulib_declaration",
  "title": "BrightnessTemp21cm",
  "permalink": "/verify/taulib/docs/book-v-cosmology-reionization/brightness-temp21cm/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.Reionization`.",
  "declaration_id": "TauLib.BookV.Cosmology.Reionization::BrightnessTemp21cm",
  "declaration_slug": "brightness-temp21cm",
  "kind": "structure",
  "name": "BrightnessTemp21cm",
  "module_name": "TauLib.BookV.Cosmology.Reionization",
  "module_url": "/verify/taulib/docs/book-v-cosmology-reionization/",
  "source_line_start": 45,
  "source_line_end": 55,
  "registry_ids": [
    "V.D334"
  ],
  "related_registry_items": [
    {
      "id": "V.D334",
      "title": "21cm Brightness Temperature",
      "url": "/registry/object/V.D334/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/Reionization.lean#L45-L55",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.Reionization",
        "url": "/verify/taulib/docs/book-v-cosmology-reionization/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/Reionization.lean#L45-L55",
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

- Module: [TauLib.BookV.Cosmology.Reionization](/verify/taulib/docs/book-v-cosmology-reionization/)
- Source path: [`TauLib/BookV/Cosmology/Reionization.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/Reionization.lean#L45-L55)
- Source range: L45-L55
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D334` — 21cm Brightness Temperature

## Immediate Comment / Docstring

```lean
/-- 21cm brightness temperature structure [V.D334].
    Stores the τ-native cosmological parameters and computes
    the differential brightness temperature against the CMB.
    Scope: τ-effective (formula uses only τ-derived inputs). -/
```

## Source Excerpt

```lean
structure BrightnessTemp21cm where
  /-- Redshift of observation. -/
  redshift : Nat
  /-- Neutral hydrogen fraction (0 to 1000, in per-mille). -/
  x_HI_permille : Nat
  /-- Spin temperature in mK. -/
  T_S_mK : Nat
  /-- T_S > 0. -/
  T_S_pos : T_S_mK > 0
  /-- CMB temperature at redshift z in mK: 2725 × (1+z). -/
  T_CMB_mK : Nat := 2725 * (1 + redshift)
```
