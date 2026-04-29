---
{
  "projection_kind": "taulib_declaration",
  "title": "neff_consistency",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/neff-consistency/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::neff_consistency",
  "declaration_slug": "neff-consistency",
  "kind": "theorem",
  "name": "neff_consistency",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1417,
  "source_line_end": 1419,
  "registry_ids": [
    "V.P175"
  ],
  "related_registry_items": [
    {
      "id": "V.P175",
      "title": "Peak Ratio Consistency Check",
      "url": "/registry/object/V.P175/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1417-L1419",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1417-L1419",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1417-L1419)
- Source range: L1417-L1419
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P175` — Peak Ratio Consistency Check

## Immediate Comment / Docstring

```lean
/-- [V.P175] N_eff = 3 from H₁(τ³) ≅ ℤ³ matches Planck N_eff = 2.99 ± 0.17. -/
```

## Source Excerpt

```lean
theorem neff_consistency :
    peak_height_ratios_data.n_eff_predicted = 3 := by
  native_decide
```
