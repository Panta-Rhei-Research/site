---
{
  "projection_kind": "taulib_declaration",
  "title": "bias_primorial_3",
  "permalink": "/verify/taulib/docs/book-i-coordinates-chebyshev-bias/bias-primorial-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.ChebyshevBias`.",
  "declaration_id": "TauLib.BookI.Coordinates.ChebyshevBias::bias_primorial_3",
  "declaration_slug": "bias-primorial-3",
  "kind": "theorem",
  "name": "bias_primorial_3",
  "module_name": "TauLib.BookI.Coordinates.ChebyshevBias",
  "module_url": "/verify/taulib/docs/book-i-coordinates-chebyshev-bias/",
  "source_line_start": 176,
  "source_line_end": 177,
  "registry_ids": [
    "I.T50"
  ],
  "related_registry_items": [
    {
      "id": "I.T50",
      "title": "Fundamental Theorem of Internal Galois Theory",
      "url": "/registry/object/I.T50/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ChebyshevBias.lean#L176-L177",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ChebyshevBias.lean#L176-L177",
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
- Source path: [`TauLib/BookI/Coordinates/ChebyshevBias.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ChebyshevBias.lean#L176-L177)
- Source range: L176-L177
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.T50` — Fundamental Theorem of Internal Galois Theory

## Immediate Comment / Docstring

```lean
/-- [I.T50] Bias at primorial levels up to depth 3. -/
```

## Source Excerpt

```lean
theorem bias_primorial_3 :
    bias_primorial_check 3 = true := by native_decide
```
