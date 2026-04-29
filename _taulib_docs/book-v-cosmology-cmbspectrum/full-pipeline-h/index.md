---
{
  "projection_kind": "taulib_declaration",
  "title": "full_pipeline_h",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/full-pipeline-h/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::full_pipeline_h",
  "declaration_slug": "full-pipeline-h",
  "kind": "def",
  "name": "full_pipeline_h",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 384,
  "source_line_end": 386,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L384-L386",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L384-L386",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L384-L386)
- Source range: L384-L386
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.T197` — Full CMB Pipeline with Structural h

## Immediate Comment / Docstring

```lean
/-- [V.T197] Full CMB Pipeline with Structural h.
    M3h+h_τ: ℓ₁=220.63 (+2863 ppm). DE+h_τ: ℓ₁=221.52 (+6925 ppm).
    Zero free parameters beyond ι_τ and T_CMB. -/
```

## Source Excerpt

```lean
def full_pipeline_h : String :=
  "Full pipeline (M3h+h_τ): ℓ₁=220.63 (+2863), ℓ₂=529.75, ℓ₃=796.74. " ++
  "Peak ratios ℓ₂/ℓ₁=2.401, ℓ₃/ℓ₁=3.611 are universal (phase-shift determined)."
```
