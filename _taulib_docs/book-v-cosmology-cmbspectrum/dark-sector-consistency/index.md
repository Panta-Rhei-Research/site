---
{
  "projection_kind": "taulib_declaration",
  "title": "DarkSectorConsistency",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/dark-sector-consistency/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::DarkSectorConsistency",
  "declaration_slug": "dark-sector-consistency",
  "kind": "structure",
  "name": "DarkSectorConsistency",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1245,
  "source_line_end": 1258,
  "registry_ids": [
    "V.T215"
  ],
  "related_registry_items": [
    {
      "id": "V.T215",
      "title": "Dark Sector Consistency Theorem",
      "url": "/registry/object/V.T215/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1245-L1258",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1245-L1258",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1245-L1258)
- Source range: L1245-L1258
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T215` — Dark Sector Consistency Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T215] Dark Sector Consistency Theorem.
    The τ-framework explains rotation curves + lensing + Hubble diagram +
    CMB + BAO with ONE parameter set from ι_τ = 2/(π+e):
    Ω_Λ=0.6849, Ω_m=0.3151, h=0.6735, r=ι_τ⁴=0.014,
    Σm_ν=0.089 eV, M_eff/M_p=6.65. No free parameters. -/
```

## Source Excerpt

```lean
structure DarkSectorConsistency where
  /-- Number of observational pillars explained. -/
  pillars : Nat := 5
  /-- Number of free parameters. -/
  free_params : Nat := 0
  /-- Number of decisive discriminators vs ΛCDM. -/
  discriminators : Nat := 5
  /-- M_eff/M_p × 100 = 665. -/
  mass_ratio_x100 : Nat := 665
  /-- r × 10000 = 140 (= ι_τ⁴). -/
  r_tensor_x10000 : Nat := 140
  /-- Σm_ν × 1000 in eV = 89. -/
  sum_mnu_x1000 : Nat := 89
  deriving Repr
```
