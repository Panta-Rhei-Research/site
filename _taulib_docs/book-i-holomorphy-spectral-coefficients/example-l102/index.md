---
{
  "projection_kind": "taulib_declaration",
  "title": "example at L102",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-spectral-coefficients/example-l102/",
  "summary_short": "`example` declaration in `TauLib.BookI.Holomorphy.SpectralCoefficients`.",
  "declaration_id": "TauLib.BookI.Holomorphy.SpectralCoefficients::#eval:102",
  "declaration_slug": "example-l102",
  "kind": "example",
  "name": null,
  "module_name": "TauLib.BookI.Holomorphy.SpectralCoefficients",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-spectral-coefficients/",
  "source_line_start": 102,
  "source_line_end": 102,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/SpectralCoefficients.lean#L102-L102",
  "formal_status": "example",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.SpectralCoefficients",
        "url": "/verify/taulib/docs/book-i-holomorphy-spectral-coefficients/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/SpectralCoefficients.lean#L102-L102",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "example",
      "status": "example"
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

- Module: [TauLib.BookI.Holomorphy.SpectralCoefficients](/verify/taulib/docs/book-i-holomorphy-spectral-coefficients/)
- Source path: [`TauLib/BookI/Holomorphy/SpectralCoefficients.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/SpectralCoefficients.lean#L102-L102)
- Source range: L102-L102
- Kind: `example`
- Formal status hint: `example`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Spectral coefficients of χ₊ at input 1, stage 1. -/
```

## Source Excerpt

```lean
example : (spectral_of chi_plus_stage 1 1).b_coeff = 1 := by native_decide
```
