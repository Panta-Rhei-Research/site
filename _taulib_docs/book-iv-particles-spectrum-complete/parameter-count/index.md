---
{
  "projection_kind": "taulib_declaration",
  "title": "ParameterCount",
  "permalink": "/verify/taulib/docs/book-iv-particles-spectrum-complete/parameter-count/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.SpectrumComplete`.",
  "declaration_id": "TauLib.BookIV.Particles.SpectrumComplete::ParameterCount",
  "declaration_slug": "parameter-count",
  "kind": "structure",
  "name": "ParameterCount",
  "module_name": "TauLib.BookIV.Particles.SpectrumComplete",
  "module_url": "/verify/taulib/docs/book-iv-particles-spectrum-complete/",
  "source_line_start": 104,
  "source_line_end": 115,
  "registry_ids": [
    "IV.R149"
  ],
  "related_registry_items": [
    {
      "id": "IV.R149",
      "title": "Parameter count",
      "url": "/registry/object/IV.R149/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SpectrumComplete.lean#L104-L115",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.SpectrumComplete",
        "url": "/verify/taulib/docs/book-iv-particles-spectrum-complete/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SpectrumComplete.lean#L104-L115",
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

- Module: [TauLib.BookIV.Particles.SpectrumComplete](/verify/taulib/docs/book-iv-particles-spectrum-complete/)
- Source path: [`TauLib/BookIV/Particles/SpectrumComplete.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SpectrumComplete.lean#L104-L115)
- Source range: L104-L115
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R149` — Parameter count

## Immediate Comment / Docstring

```lean
/-- [IV.R149] Across all 25+ results of Part VI:
    - 1 dimensionless constant: ι_τ = 2/(π+e), derived from K0-K6
    - 1 dimensional anchor: m_n = 939.565421 MeV
    - 0 fitting parameters, effective couplings, or ad hoc mass ratios -/
```

## Source Excerpt

```lean
structure ParameterCount where
  /-- Dimensionless constants. -/
  dimensionless : Nat := 1
  /-- Dimensional anchors. -/
  anchors : Nat := 1
  /-- Fitting parameters. -/
  fitting : Nat := 0
  /-- Effective couplings. -/
  effective : Nat := 0
  /-- Ad hoc mass ratios. -/
  ad_hoc : Nat := 0
  deriving Repr
```
