---
{
  "projection_kind": "taulib_declaration",
  "title": "FullCMBPipeline",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/full-cmbpipeline/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::FullCMBPipeline",
  "declaration_slug": "full-cmbpipeline",
  "kind": "structure",
  "name": "FullCMBPipeline",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 618,
  "source_line_end": 625,
  "registry_ids": [
    "V.T197"
  ],
  "related_registry_items": [
    {
      "id": "V.T197",
      "title": "Full CMB Pipeline with Structural h",
      "url": "/registry/object/V.T197/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L618-L625",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L618-L625",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L618-L625)
- Source range: L618-L625
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T197` — Full CMB Pipeline with Structural h

## Immediate Comment / Docstring

```lean
/-- [V.T197] Full CMB Pipeline.
    M3h + h_τ: ℓ₁ = 220.63 (+2863 ppm). Zero free parameters. -/
```

## Source Excerpt

```lean
structure FullCMBPipeline where
  /-- Number of pipeline stages. -/
  n_stages : Nat := 6
  /-- Number of free parameters beyond ι_τ and T_CMB. -/
  free_params : Nat := 0
  /-- Number of independent inputs (single ι_τ). -/
  n_inputs : Nat := 1
  deriving Repr
```
