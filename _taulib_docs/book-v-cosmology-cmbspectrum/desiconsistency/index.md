---
{
  "projection_kind": "taulib_declaration",
  "title": "DESIConsistency",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/desiconsistency/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::DESIConsistency",
  "declaration_slug": "desiconsistency",
  "kind": "structure",
  "name": "DESIConsistency",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1222,
  "source_line_end": 1227,
  "registry_ids": [
    "V.T214"
  ],
  "related_registry_items": [
    {
      "id": "V.T214",
      "title": "DESI Consistency Check",
      "url": "/registry/object/V.T214/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1222-L1227",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1222-L1227",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1222-L1227)
- Source range: L1222-L1227
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T214` — DESI Consistency Check

## Immediate Comment / Docstring

```lean
/-- [V.T214] DESI Consistency Check.
    τ-native D_V/r_d matches Planck-ΛCDM at z = 0.51–2.33.
    q₀ = −0.527 confirms accelerating expansion. -/
```

## Source Excerpt

```lean
structure DESIConsistency where
  /-- Number of DESI redshift bins checked. -/
  desi_bins : Nat := 5
  /-- All bins consistent (1 = yes). -/
  all_consistent : Nat := 1
  deriving Repr
```
