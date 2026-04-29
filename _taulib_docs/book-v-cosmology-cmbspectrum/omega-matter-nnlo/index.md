---
{
  "projection_kind": "taulib_declaration",
  "title": "OmegaMatterNNLO",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/omega-matter-nnlo/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::OmegaMatterNNLO",
  "declaration_slug": "omega-matter-nnlo",
  "kind": "structure",
  "name": "OmegaMatterNNLO",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1839,
  "source_line_end": 1868,
  "registry_ids": [
    "V.D328"
  ],
  "related_registry_items": [
    {
      "id": "V.D328",
      "title": "ω_m NNLO Correction Space",
      "url": "/registry/object/V.D328/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1839-L1868",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.CMBSpectrum",
        "url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1839-L1868",
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

- Module: [TauLib.BookV.Cosmology.CMBSpectrum](/verify/taulib/docs/book-v-cosmology-cmbspectrum/)
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1839-L1868)
- Source range: L1839-L1868
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D328` — ω_m NNLO Correction Space

## Immediate Comment / Docstring

```lean
/-- [V.D328] ω_m NNLO Correction Space.
    Combined matter correction λ = (1−κ_D/57)(1−κ_D/24).
    57 = dim(τ³)·W₅(3) (inflationary e-folds).
    24 = 2^dim(τ³)·dim(τ³) (fundamental-domain vertices × dimension).
    Scope: τ-effective (Wave 41A). -/
```

## Source Excerpt

```lean
structure OmegaMatterNNLO where
  /-- κ_D/57 × 100000 (NLO holonomy correction). -/
  delta_h_x100000 : Nat := 1156
  /-- κ_D/24 × 100000 (NNLO matter correction). -/
  delta_m_x100000 : Nat := 2745
  /-- N_e = dim(τ³) × W₅(3). -/
  n_e : Nat := 57
  /-- 2^dim(τ³) × dim(τ³). -/
  fund_domain : Nat := 24
  /-- λ = (1−κ_D/57)(1−κ_D/24) × 100000. -/
  lambda_x100000 : Nat := 96132
  /-- ω_m(NNLO) × 100000. -/
  omega_m_nnlo_x100000 : Nat := 14314
  /-- ω_m ppm from Planck (absolute value). -/
  omega_m_ppm : Nat := 17
  /-- z_eq(NNLO) × 10. -/
  z_eq_x10 : Nat := 34473
  /-- z_eq(Planck) × 10. -/
  z_eq_planck_x10 : Nat := 34472
  /-- r_d(NNLO) × 100 (Mpc). -/
  rd_nnlo_x100 : Nat := 14690
  /-- r_d ppm from Planck (absolute value). -/
  rd_ppm : Nat := 1269
  /-- ω_m(DE-closure) × 100000. -/
  omega_m_de_x100000 : Nat := 14290
  /-- Two-path M3h ↔ DE gap (ppm). -/
  two_path_gap_ppm : Nat := 1717
  /-- Free parameters. -/
  free_params : Nat := 0
  deriving Repr
```
