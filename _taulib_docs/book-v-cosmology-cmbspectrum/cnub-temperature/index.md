---
{
  "projection_kind": "taulib_declaration",
  "title": "cnub_temperature",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/cnub-temperature/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::cnub_temperature",
  "declaration_slug": "cnub-temperature",
  "kind": "def",
  "name": "cnub_temperature",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 242,
  "source_line_end": 242,
  "registry_ids": [
    "V.D250"
  ],
  "related_registry_items": [
    {
      "id": "V.D250",
      "title": "CνB Temperature Chain",
      "url": "/registry/object/V.D250/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L242-L242",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L242-L242",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L242-L242)
- Source range: L242-L242
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.D250` — CνB Temperature Chain

## Immediate Comment / Docstring

```lean
/-- [V.D250] CνB Temperature Chain (established).
    T_CνB = (4/11)^{1/3}·T_CMB = 1.9454 K.
    T_dec ≈ 1.37 MeV, z_ν ≈ 5.8×10⁹. -/
```

## Source Excerpt

```lean
def cnub_temperature : Float := 1.9454
```
