---
{
  "projection_kind": "taulib_declaration",
  "title": "peak_ratio_nlo_improvement",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/peak-ratio-nlo-improvement/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::peak_ratio_nlo_improvement",
  "declaration_slug": "peak-ratio-nlo-improvement",
  "kind": "theorem",
  "name": "peak_ratio_nlo_improvement",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1635,
  "source_line_end": 1638,
  "registry_ids": [
    "V.T261"
  ],
  "related_registry_items": [
    {
      "id": "V.T261",
      "title": "Peak-Ratio NLO Improvement",
      "url": "/registry/object/V.T261/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1635-L1638",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1635-L1638",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1635-L1638)
- Source range: L1635-L1638
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T261` — Peak-Ratio NLO Improvement

## Immediate Comment / Docstring

```lean
/-- [V.T261] Peak ratios improve dramatically at NLO. -/
```

## Source Excerpt

```lean
theorem peak_ratio_nlo_improvement :
    peak_ratio_nlo_data.ell2_nlo_ppm < peak_ratio_nlo_data.ell2_prev_ppm ∧
    peak_ratio_nlo_data.ell3_nlo_ppm < peak_ratio_nlo_data.ell3_prev_ppm := by
  native_decide
```
