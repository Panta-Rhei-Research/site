---
{
  "projection_kind": "taulib_declaration",
  "title": "TemperatureNotFundamental",
  "permalink": "/verify/taulib/docs/book-iv-particles-spectrum-complete/temperature-not-fundamental/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.SpectrumComplete`.",
  "declaration_id": "TauLib.BookIV.Particles.SpectrumComplete::TemperatureNotFundamental",
  "declaration_slug": "temperature-not-fundamental",
  "kind": "structure",
  "name": "TemperatureNotFundamental",
  "module_name": "TauLib.BookIV.Particles.SpectrumComplete",
  "module_url": "/verify/taulib/docs/book-iv-particles-spectrum-complete/",
  "source_line_start": 210,
  "source_line_end": 219,
  "registry_ids": [
    "IV.R154"
  ],
  "related_registry_items": [
    {
      "id": "IV.R154",
      "title": "Temperature is not fundamental",
      "url": "/registry/object/IV.R154/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SpectrumComplete.lean#L210-L219",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SpectrumComplete.lean#L210-L219",
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
- Source path: [`TauLib/BookIV/Particles/SpectrumComplete.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SpectrumComplete.lean#L210-L219)
- Source range: L210-L219
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R154` — Temperature is not fundamental

## Immediate Comment / Docstring

```lean
/-- [IV.R154] Temperature is not fundamental in Category τ but a readout:
    the gradient of the defect functional with respect to the entropy
    component. Part VII will use the defect functional as organizing
    variable with temperature as derived quantity. -/
```

## Source Excerpt

```lean
structure TemperatureNotFundamental where
  /-- Temperature is derived. -/
  derived : Bool := true
  /-- Derivation: gradient of defect functional. -/
  derivation : String := "gradient of defect functional w.r.t. entropy"
  /-- Fundamental variable: defect functional. -/
  fundamental : String := "defect functional"
  /-- Part VII uses this. -/
  used_in_part_vii : Bool := true
  deriving Repr
```
