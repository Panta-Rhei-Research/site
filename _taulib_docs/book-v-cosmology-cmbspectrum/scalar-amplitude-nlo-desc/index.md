---
{
  "projection_kind": "taulib_declaration",
  "title": "scalar_amplitude_nlo_desc",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/scalar-amplitude-nlo-desc/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::scalar_amplitude_nlo_desc",
  "declaration_slug": "scalar-amplitude-nlo-desc",
  "kind": "def",
  "name": "scalar_amplitude_nlo_desc",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 371,
  "source_line_end": 373,
  "registry_ids": [
    "V.D253"
  ],
  "related_registry_items": [
    {
      "id": "V.D253",
      "title": "Scalar Amplitude NLO: A_s = α_τ·ι_τ¹⁴·(1−ι_τ³/3)",
      "url": "/registry/object/V.D253/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L371-L373",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L371-L373",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L371-L373)
- Source range: L371-L373
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.D253` — Scalar Amplitude NLO: A_s = α_τ·ι_τ¹⁴·(1−ι_τ³/3)

## Immediate Comment / Docstring

```lean
/-- [V.D253] Scalar Amplitude NLO.
    A_s = (121/225)·ι_τ¹⁸·(1−ι_τ³/3) = 2.096×10⁻⁹.
    10× improvement over baseline +11425 ppm. -/
```

## Source Excerpt

```lean
def scalar_amplitude_nlo_desc : String :=
  "A_s = (121/225)·ι_τ¹⁸·(1−ι_τ³/3) = 2.096×10⁻⁹. " ++
  "NLO factor is structural (τ³ volume averaging), not slow-roll running."
```
