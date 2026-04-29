---
{
  "projection_kind": "taulib_declaration",
  "title": "TauIntegral",
  "permalink": "/verify/taulib/docs/book-i-boundary-integration/tau-integral/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Boundary.Integration`.",
  "declaration_id": "TauLib.BookI.Boundary.Integration::TauIntegral",
  "declaration_slug": "tau-integral",
  "kind": "structure",
  "name": "TauIntegral",
  "module_name": "TauLib.BookI.Boundary.Integration",
  "module_url": "/verify/taulib/docs/book-i-boundary-integration/",
  "source_line_start": 49,
  "source_line_end": 52,
  "registry_ids": [
    "I.D99"
  ],
  "related_registry_items": [
    {
      "id": "I.D99",
      "title": "τ-Integral",
      "url": "/registry/object/I.D99/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Integration.lean#L49-L52",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Integration",
        "url": "/verify/taulib/docs/book-i-boundary-integration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Integration.lean#L49-L52",
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

- Module: [TauLib.BookI.Boundary.Integration](/verify/taulib/docs/book-i-boundary-integration/)
- Source path: [`TauLib/BookI/Boundary/Integration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Integration.lean#L49-L52)
- Source range: L49-L52
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D99` — τ-Integral

## Immediate Comment / Docstring

```lean
/-- [I.D99] The τ-integral as a rational pair:
    ∫_k f = (Σ f(x), M_k). -/
```

## Source Excerpt

```lean
structure TauIntegral where
  numerator : Int
  denominator : Nat
  deriving Repr
```
