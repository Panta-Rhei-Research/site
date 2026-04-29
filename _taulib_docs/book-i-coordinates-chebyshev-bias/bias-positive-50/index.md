---
{
  "projection_kind": "taulib_declaration",
  "title": "bias_positive_50",
  "permalink": "/verify/taulib/docs/book-i-coordinates-chebyshev-bias/bias-positive-50/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.ChebyshevBias`.",
  "declaration_id": "TauLib.BookI.Coordinates.ChebyshevBias::bias_positive_50",
  "declaration_slug": "bias-positive-50",
  "kind": "theorem",
  "name": "bias_positive_50",
  "module_name": "TauLib.BookI.Coordinates.ChebyshevBias",
  "module_url": "/verify/taulib/docs/book-i-coordinates-chebyshev-bias/",
  "source_line_start": 168,
  "source_line_end": 169,
  "registry_ids": [
    "I.D98"
  ],
  "related_registry_items": [
    {
      "id": "I.D98",
      "title": "Galois Group of Primorial Stage",
      "url": "/registry/object/I.D98/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ChebyshevBias.lean#L168-L169",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.ChebyshevBias",
        "url": "/verify/taulib/docs/book-i-coordinates-chebyshev-bias/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ChebyshevBias.lean#L168-L169",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookI.Coordinates.ChebyshevBias](/verify/taulib/docs/book-i-coordinates-chebyshev-bias/)
- Source path: [`TauLib/BookI/Coordinates/ChebyshevBias.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ChebyshevBias.lean#L168-L169)
- Source range: L168-L169
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.D98` — Galois Group of Primorial Stage

## Immediate Comment / Docstring

```lean
/-- [I.D98] Chebyshev bias (q=4, 3 vs 1) is positive up to 50. -/
```

## Source Excerpt

```lean
theorem bias_positive_50 :
    bias_quantification_check 50 = true := by native_decide
```
