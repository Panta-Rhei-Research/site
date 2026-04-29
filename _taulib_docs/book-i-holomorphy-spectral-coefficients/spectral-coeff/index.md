---
{
  "projection_kind": "taulib_declaration",
  "title": "SpectralCoeff",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-spectral-coefficients/spectral-coeff/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Holomorphy.SpectralCoefficients`.",
  "declaration_id": "TauLib.BookI.Holomorphy.SpectralCoefficients::SpectralCoeff",
  "declaration_slug": "spectral-coeff",
  "kind": "structure",
  "name": "SpectralCoeff",
  "module_name": "TauLib.BookI.Holomorphy.SpectralCoefficients",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-spectral-coefficients/",
  "source_line_start": 37,
  "source_line_end": 41,
  "registry_ids": [
    "I.D65"
  ],
  "related_registry_items": [
    {
      "id": "I.D65",
      "title": "Spectral Coefficients",
      "url": "/registry/object/I.D65/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/SpectralCoefficients.lean#L37-L41",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/SpectralCoefficients.lean#L37-L41",
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

- Module: [TauLib.BookI.Holomorphy.SpectralCoefficients](/verify/taulib/docs/book-i-holomorphy-spectral-coefficients/)
- Source path: [`TauLib/BookI/Holomorphy/SpectralCoefficients.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/SpectralCoefficients.lean#L37-L41)
- Source range: L37-L41
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D65` — Spectral Coefficients

## Immediate Comment / Docstring

```lean
/-- [I.D65] Spectral coefficients of a StageFun at input n, stage k.
    The B-sector coefficient is the B-output; the C-sector coefficient
    is the C-output. Together they determine the function value at (n, k). -/
```

## Source Excerpt

```lean
structure SpectralCoeff where
  -- B-sector coefficient
  b_coeff : TauIdx
  -- C-sector coefficient
  c_coeff : TauIdx
```
