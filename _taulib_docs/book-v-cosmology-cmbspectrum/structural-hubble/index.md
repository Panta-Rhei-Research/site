---
{
  "projection_kind": "taulib_declaration",
  "title": "structural_hubble",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/structural-hubble/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::structural_hubble",
  "declaration_slug": "structural-hubble",
  "kind": "def",
  "name": "structural_hubble",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 357,
  "source_line_end": 357,
  "registry_ids": [
    "V.D251"
  ],
  "related_registry_items": [
    {
      "id": "V.D251",
      "title": "Structural Hubble Parameter h = 2/3 + ι_τ²/W₃(3)",
      "url": "/registry/object/V.D251/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L357-L357",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L357-L357",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L357-L357)
- Source range: L357-L357
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.D251` — Structural Hubble Parameter h = 2/3 + ι_τ²/W₃(3)

## Immediate Comment / Docstring

```lean
/-- [V.D251] Structural Hubble Parameter h = 2/3 + ι_τ²/W₃(3).
    h = 2/3 + ι_τ²/17 = 0.67352 at −120 ppm from Planck 0.6736.
    Base: 2/3 = EdS exponent. Correction: κ_B/17. -/
```

## Source Excerpt

```lean
def structural_hubble : Float := 2.0 / 3.0 + kappa_B / 17.0
```
