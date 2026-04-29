---
{
  "projection_kind": "taulib_declaration",
  "title": "DiscriminatorTable",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/discriminator-table/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::DiscriminatorTable",
  "declaration_slug": "discriminator-table",
  "kind": "structure",
  "name": "DiscriminatorTable",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1277,
  "source_line_end": 1286,
  "registry_ids": [
    "V.R401"
  ],
  "related_registry_items": [
    {
      "id": "V.R401",
      "title": "τ-vs-ΛCDM Discriminator Table",
      "url": "/registry/object/V.R401/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1277-L1286",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1277-L1286",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1277-L1286)
- Source range: L1277-L1286
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.R401` — τ-vs-ΛCDM Discriminator Table

## Immediate Comment / Docstring

```lean
/-- [V.R401] τ-vs-ΛCDM Discriminator Table.
    D1: r=ι_τ⁴=0.014 at 14σ (CMB-S4).
    D2: Σm_ν=0.089 eV at 4.5σ (DESI).
    D3: Null DM direct detection.
    D4: Structural H₀ tension resolution.
    D5: w(z) deviation at z>1 (DESI Y5/Y10). -/
```

## Source Excerpt

```lean
structure DiscriminatorTable where
  /-- Most decisive: CMB-S4 significance for r. -/
  cmbs4_r_sigma : Nat := 14
  /-- DESI significance for Σm_ν. -/
  desi_mnu_sigma_x10 : Nat := 45
  /-- DM detection: 0 = null prediction. -/
  dm_detection_null : Nat := 0
  /-- H₀ tension: 1 = structurally resolved. -/
  h0_resolved : Nat := 1
  deriving Repr
```
