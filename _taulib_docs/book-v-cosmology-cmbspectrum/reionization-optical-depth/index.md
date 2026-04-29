---
{
  "projection_kind": "taulib_declaration",
  "title": "ReionizationOpticalDepth",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/reionization-optical-depth/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::ReionizationOpticalDepth",
  "declaration_slug": "reionization-optical-depth",
  "kind": "structure",
  "name": "ReionizationOpticalDepth",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 714,
  "source_line_end": 725,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L714-L725",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L714-L725",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L714-L725)
- Source range: L714-L725
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P139` — Reionization Optical Depth from z_reion = 8

## Immediate Comment / Docstring

```lean
/-- [V.P139] Reionisation Optical Depth.
    z_reion = a₃ − W₃(4) = 13 − 5 = 8.
    τ_reion ≈ 0.059. Planck: 0.054 ± 0.007. -/
```

## Source Excerpt

```lean
structure ReionizationOpticalDepth where
  /-- a₃ = 13 (3rd CF partial quotient). -/
  a3 : Nat := 13
  /-- W₃(4) = 5. -/
  w34 : Nat := 5
  /-- z_reion = a₃ − W₃(4). -/
  z_reion : Nat := 8
  /-- Structural: z_reion = a₃ − W₃(4). -/
  z_decomp : z_reion = a3 - w34
  /-- Sigma deviation ×10 from Planck (0.7σ → 7). -/
  sigma_deviation_x10 : Nat := 7
  deriving Repr
```
