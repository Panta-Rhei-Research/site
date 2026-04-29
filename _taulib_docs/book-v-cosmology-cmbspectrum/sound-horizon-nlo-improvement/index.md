---
{
  "projection_kind": "taulib_declaration",
  "title": "sound_horizon_nlo_improvement",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/sound-horizon-nlo-improvement/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::sound_horizon_nlo_improvement",
  "declaration_slug": "sound-horizon-nlo-improvement",
  "kind": "theorem",
  "name": "sound_horizon_nlo_improvement",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1703,
  "source_line_end": 1705,
  "registry_ids": [
    "V.P181"
  ],
  "related_registry_items": [
    {
      "id": "V.P181",
      "title": "Sound Horizon Improvement",
      "url": "/registry/object/V.P181/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1703-L1705",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1703-L1705",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1703-L1705)
- Source range: L1703-L1705
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P181` — Sound Horizon Improvement

## Immediate Comment / Docstring

```lean
/-- [V.P181] r_d improves at NLO (modest). -/
```

## Source Excerpt

```lean
theorem sound_horizon_nlo_improvement :
    baryon_nlo_data.rd_nlo_ppm < baryon_nlo_data.rd_lo_ppm := by
  native_decide
```
