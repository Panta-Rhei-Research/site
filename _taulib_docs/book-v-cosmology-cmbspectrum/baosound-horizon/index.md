---
{
  "projection_kind": "taulib_declaration",
  "title": "BAOSoundHorizon",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/baosound-horizon/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::BAOSoundHorizon",
  "declaration_slug": "baosound-horizon",
  "kind": "structure",
  "name": "BAOSoundHorizon",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1489,
  "source_line_end": 1502,
  "registry_ids": [
    "V.D318"
  ],
  "related_registry_items": [
    {
      "id": "V.D318",
      "title": "NLO Sound Horizon at Drag Epoch",
      "url": "/registry/object/V.D318/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1489-L1502",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1489-L1502",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1489-L1502)
- Source range: L1489-L1502
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D318` — NLO Sound Horizon at Drag Epoch

## Immediate Comment / Docstring

```lean
/-- [V.D318] NLO Sound Horizon at Drag Epoch.
    r_d(NLO) = 149.04 Mpc. Planck: 147.09 ± 0.26.
    Scope: τ-effective (Wave 38B). -/
```

## Source Excerpt

```lean
structure BAOSoundHorizon where
  /-- r_d NLO × 100 (Mpc). -/
  r_d_nlo_x100 : Nat := 14904
  /-- r_d LO × 100 (Mpc). -/
  r_d_lo_x100 : Nat := 14975
  /-- Planck r_d × 100 (Mpc). -/
  r_d_planck_x100 : Nat := 14709
  /-- NLO deviation ppm. -/
  nlo_deviation_ppm : Nat := 13280
  /-- LO deviation ppm. -/
  lo_deviation_ppm : Nat := 18063
  /-- Free parameters. -/
  free_params : Nat := 0
  deriving Repr
```
