---
{
  "projection_kind": "taulib_declaration",
  "title": "S8NNLO",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-nnlo/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::S8NNLO",
  "declaration_slug": "s8-nnlo",
  "kind": "structure",
  "name": "S8NNLO",
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 647,
  "source_line_end": 672,
  "registry_ids": [
    "V.D330"
  ],
  "related_registry_items": [
    {
      "id": "V.D330",
      "title": "S₈ NNLO Density-Regime Value",
      "url": "/registry/object/V.D330/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L647-L672",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.H0TensionLCDM",
        "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L647-L672",
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

- Module: [TauLib.BookV.Astrophysics.H0TensionLCDM](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/)
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L647-L672)
- Source range: L647-L672
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D330` — S₈ NNLO Density-Regime Value

## Immediate Comment / Docstring

```lean
/-- [V.D330] S₈ NNLO density-regime value.
    At NNLO, Ω_m = 0.3155 ≈ Ω_m(Planck), so f_growth → 1.000.
    σ₈(τ,NNLO) = 0.811 × 0.913 × 1.000 × 0.997 = 0.738.
    S₈(τ,NNLO) = 0.738 × √(0.316/0.3) = 0.757.
    Scope: τ-effective (Wave 42A). -/
```

## Source Excerpt

```lean
structure S8NNLO where
  /-- σ₈(CMB, Planck) × 1000. -/
  sigma8_cmb_x1000 : Nat := 811
  /-- f_supp × 10000 (unchanged from NLO). -/
  f_supp_x10000 : Nat := 9132
  /-- f_growth(NNLO) × 10000 (≈ 1.000). -/
  f_growth_nnlo_x10000 : Nat := 10004
  /-- f_ν(NNLO) × 100000. -/
  f_nu_nnlo_x100000 : Nat := 99666
  /-- σ₈(τ,NNLO) × 10000. -/
  sigma8_nnlo_x10000 : Nat := 7380
  /-- S₈(τ,NNLO) × 10000. -/
  s8_nnlo_x10000 : Nat := 7569
  /-- Ω_m(NNLO) × 10000. -/
  omega_m_nnlo_x10000 : Nat := 3155
  /-- S₈(KiDS-1000) × 1000. -/
  s8_kids_x1000 : Nat := 759
  /-- S₈(KiDS-1000) 1σ uncertainty × 1000. -/
  s8_kids_sigma_x1000 : Nat := 24
  /-- S₈(HSC Y3) × 1000. -/
  s8_hsc_x1000 : Nat := 763
  /-- S₈(HSC Y3) 1σ uncertainty × 1000. -/
  s8_hsc_sigma_x1000 : Nat := 33
  /-- Free parameters. -/
  free_params : Nat := 0
  deriving Repr
```
