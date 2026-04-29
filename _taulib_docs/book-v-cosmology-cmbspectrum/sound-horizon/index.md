---
{
  "projection_kind": "taulib_declaration",
  "title": "SoundHorizon",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/sound-horizon/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::SoundHorizon",
  "declaration_slug": "sound-horizon",
  "kind": "structure",
  "name": "SoundHorizon",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 123,
  "source_line_end": 128,
  "registry_ids": [
    "V.T191"
  ],
  "related_registry_items": [
    {
      "id": "V.T191",
      "title": "Sound Horizon from τ-Native Inputs",
      "url": "/registry/object/V.T191/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L123-L128",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L123-L128",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L123-L128)
- Source range: L123-L128
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T191` — Sound Horizon from τ-Native Inputs

## Immediate Comment / Docstring

```lean
/-- [V.T191] Sound Horizon from τ-Native Inputs.
    r_s = 143.18 Mpc. Planck: 147.09±0.26 Mpc. −2.66%. -/
```

## Source Excerpt

```lean
structure SoundHorizon where
  /-- Number of τ-native inputs (ω_b, ω_m). -/
  n_native_inputs : Nat := 2
  /-- Number of holonomy components used. -/
  n_holonomy_components : Nat := 1
  deriving Repr
```
