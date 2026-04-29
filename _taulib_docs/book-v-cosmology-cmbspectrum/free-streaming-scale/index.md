---
{
  "projection_kind": "taulib_declaration",
  "title": "free_streaming_scale",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/free-streaming-scale/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::free_streaming_scale",
  "declaration_slug": "free-streaming-scale",
  "kind": "def",
  "name": "free_streaming_scale",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 235,
  "source_line_end": 237,
  "registry_ids": [
    "V.D249"
  ],
  "related_registry_items": [
    {
      "id": "V.D249",
      "title": "Neutrino Free-Streaming Scale from σ-Polarity Masses",
      "url": "/registry/object/V.D249/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L235-L237",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L235-L237",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L235-L237)
- Source range: L235-L237
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.D249` — Neutrino Free-Streaming Scale from σ-Polarity Masses

## Immediate Comment / Docstring

```lean
/-- [V.D249] Neutrino Free-Streaming Scale.
    k_fs = 0.018·Ω_m^{1/2}·(m/eV)·h [Mpc⁻¹].
    f_ν = ω_ν/ω_m = Σm_ν/(94.07·ω_m) = 0.00643. -/
```

## Source Excerpt

```lean
def free_streaming_scale : String :=
  "k_fs(m₃) = 3.63×10⁻⁴ Mpc⁻¹ (dominant). " ++
  "f_ν = 0.00643 for M3h (Σm_ν = 0.089 eV)."
```
