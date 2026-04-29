---
{
  "projection_kind": "taulib_declaration",
  "title": "hubble_from_tau",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/hubble-from-tau/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::hubble_from_tau",
  "declaration_slug": "hubble-from-tau",
  "kind": "def",
  "name": "hubble_from_tau",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 377,
  "source_line_end": 379,
  "registry_ids": [
    "V.T196"
  ],
  "related_registry_items": [
    {
      "id": "V.T196",
      "title": "Hubble Parameter from τ: h at −120 ppm",
      "url": "/registry/object/V.T196/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L377-L379",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L377-L379",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L377-L379)
- Source range: L377-L379
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.T196` — Hubble Parameter from τ: h at −120 ppm

## Immediate Comment / Docstring

```lean
/-- [V.T196] Hubble Parameter from τ: h at −120 ppm.
    h = 2/3 + ι_τ²/17 = 0.67352. Planck h = 0.6736. -/
```

## Source Excerpt

```lean
def hubble_from_tau : String :=
  "h = 2/3 + ι_τ²/17 = 0.67352, Planck 0.6736, deviation −120 ppm. " ++
  "2/3 = EdS exponent; ι_τ²/17 = EM correction / dominant CF window."
```
