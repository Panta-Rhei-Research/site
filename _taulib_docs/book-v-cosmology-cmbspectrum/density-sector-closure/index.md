---
{
  "projection_kind": "taulib_declaration",
  "title": "DensitySectorClosure",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/density-sector-closure/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::DensitySectorClosure",
  "declaration_slug": "density-sector-closure",
  "kind": "structure",
  "name": "DensitySectorClosure",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1992,
  "source_line_end": 2011,
  "registry_ids": [
    "V.D332"
  ],
  "related_registry_items": [
    {
      "id": "V.D332",
      "title": "Density-Sector Observable Scorecard",
      "url": "/registry/object/V.D332/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1992-L2011",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1992-L2011",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1992-L2011)
- Source range: L1992-L2011
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D332` — Density-Sector Observable Scorecard

## Immediate Comment / Docstring

```lean
/-- [V.D332] Density-sector observable scorecard.
    All ω_m-sensitive observables sub-1300 ppm at NNLO.
    8 observables characterized. Zero free parameters.
    Scope: τ-effective (Wave 42C). -/
```

## Source Excerpt

```lean
structure DensitySectorClosure where
  /-- ω_m ppm from Planck. -/
  omega_m_ppm : Nat := 17
  /-- r_d ppm from Planck. -/
  rd_ppm : Nat := 1292
  /-- BAO D_V/r_d mean ppm. -/
  bao_mean_ppm : Nat := 1145
  /-- BAO max ppm (z=0.51). -/
  bao_max_ppm : Nat := 1201
  /-- Ω_Λ ppm from Planck. -/
  omega_lambda_ppm : Nat := 433
  /-- H₀ ppm from Planck. -/
  h0_ppm : Nat := 120
  /-- Two-path convergence ppm. -/
  two_path_ppm : Nat := 1717
  /-- Number of observables characterized. -/
  n_observables : Nat := 8
  /-- Free parameters. -/
  free_params : Nat := 0
  deriving Repr
```
