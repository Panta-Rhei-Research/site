---
{
  "projection_kind": "taulib_declaration",
  "title": "reionization_z_structural",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/reionization-z-structural/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::reionization_z_structural",
  "declaration_slug": "reionization-z-structural",
  "kind": "theorem",
  "name": "reionization_z_structural",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 399,
  "source_line_end": 400,
  "registry_ids": [
    "V.P139"
  ],
  "related_registry_items": [
    {
      "id": "V.P139",
      "title": "Reionization Optical Depth from z_reion = 8",
      "url": "/registry/object/V.P139/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L399-L400",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L399-L400",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L399-L400)
- Source range: L399-L400
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P139` — Reionization Optical Depth from z_reion = 8

## Immediate Comment / Docstring

```lean
/-- [V.P139] Reionisation Optical Depth from z_reion = 8.
    z_reion = a₃ − W₃(4) = 13 − 5 = 8. τ_reion ≈ 0.059.
    Planck: 0.054±0.007. Within 1σ. -/
```

## Source Excerpt

```lean
theorem reionization_z_structural :
    13 - 5 = (8 : Nat) := by native_decide
```
