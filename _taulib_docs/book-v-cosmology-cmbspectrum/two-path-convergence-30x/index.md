---
{
  "projection_kind": "taulib_declaration",
  "title": "two_path_convergence_30x",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/two-path-convergence-30x/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::two_path_convergence_30x",
  "declaration_slug": "two-path-convergence-30x",
  "kind": "theorem",
  "name": "two_path_convergence_30x",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1889,
  "source_line_end": 1890,
  "registry_ids": [
    "V.R466"
  ],
  "related_registry_items": [
    {
      "id": "V.R466",
      "title": "Two-Path Convergence at NNLO",
      "url": "/registry/object/V.R466/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1889-L1890",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1889-L1890",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1889-L1890)
- Source range: L1889-L1890
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R466` — Two-Path Convergence at NNLO

## Immediate Comment / Docstring

```lean
/-- [V.R466] Two-path convergence: 30× improvement (was 52280 ppm). -/
```

## Source Excerpt

```lean
theorem two_path_convergence_30x :
    omega_m_nnlo_data.two_path_gap_ppm * 30 < 52280 := by native_decide
```
