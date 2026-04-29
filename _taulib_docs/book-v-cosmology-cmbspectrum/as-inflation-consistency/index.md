---
{
  "projection_kind": "taulib_declaration",
  "title": "as_inflation_consistency",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/as-inflation-consistency/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::as_inflation_consistency",
  "declaration_slug": "as-inflation-consistency",
  "kind": "def",
  "name": "as_inflation_consistency",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 391,
  "source_line_end": 394,
  "registry_ids": [
    "V.T198"
  ],
  "related_registry_items": [
    {
      "id": "V.T198",
      "title": "Scalar Amplitude NLO: Inflationary Consistency",
      "url": "/registry/object/V.T198/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L391-L394",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L391-L394",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L391-L394)
- Source range: L391-L394
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.T198` — Scalar Amplitude NLO: Inflationary Consistency

## Immediate Comment / Docstring

```lean
/-- [V.T198] Scalar Amplitude NLO: Inflationary Consistency.
    NLO factor (1−ι_τ³/3) is structural, not slow-roll.
    ε = r/16 ~ 8.5×10⁻⁴, running ~ 10⁻³ ≪ required 10⁻² (156× gap). -/
```

## Source Excerpt

```lean
def as_inflation_consistency : String :=
  "NLO factor (1−ι_τ³/3) cannot arise from slow-roll running: " ++
  "ε = r/16 ~ 8.5×10⁻⁴, required O(ι_τ³) ~ 0.040, gap 156×. " ++
  "Correction is structural (τ³ volume averaging)."
```
