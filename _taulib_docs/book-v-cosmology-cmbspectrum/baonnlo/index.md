---
{
  "projection_kind": "taulib_declaration",
  "title": "BAONNLO",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/baonnlo/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::BAONNLO",
  "declaration_slug": "baonnlo",
  "kind": "structure",
  "name": "BAONNLO",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1944,
  "source_line_end": 1961,
  "registry_ids": [
    "V.D331"
  ],
  "related_registry_items": [
    {
      "id": "V.D331",
      "title": "BAO NNLO Distance Table",
      "url": "/registry/object/V.D331/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1944-L1961",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1944-L1961",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1944-L1961)
- Source range: L1944-L1961
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D331` — BAO NNLO Distance Table

## Immediate Comment / Docstring

```lean
/-- [V.D331] BAO NNLO distance table.
    D_V/r_d at 5 DESI Y1 bins: all sub-1300 ppm from Planck ΛCDM.
    Mean |Δ| = 1145 ppm. NLO→NNLO improvement 21×.
    Scope: τ-effective (Wave 42B). -/
```

## Source Excerpt

```lean
structure BAONNLO where
  /-- D_V/r_d ppm at z=0.51 (LRG1). -/
  dv_rd_ppm_z051 : Nat := 1201
  /-- D_V/r_d ppm at z=0.71 (LRG2). -/
  dv_rd_ppm_z071 : Nat := 1174
  /-- D_V/r_d ppm at z=0.93 (LRG3+ELG1). -/
  dv_rd_ppm_z093 : Nat := 1150
  /-- D_V/r_d ppm at z=1.32 (ELG2). -/
  dv_rd_ppm_z132 : Nat := 1120
  /-- D_V/r_d ppm at z=2.33 (QSO). -/
  dv_rd_ppm_z233 : Nat := 1079
  /-- NLO mean |ppm|. -/
  nlo_mean_ppm : Nat := 23489
  /-- NNLO mean |ppm|. -/
  nnlo_mean_ppm : Nat := 1145
  /-- r_d(NNLO) in units of 0.01 Mpc. -/
  rd_nnlo_x100 : Nat := 14690
  deriving Repr
```
