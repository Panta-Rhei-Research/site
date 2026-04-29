---
{
  "projection_kind": "taulib_declaration",
  "title": "integral_const_one_3",
  "permalink": "/verify/taulib/docs/book-i-boundary-integration/integral-const-one-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Integration`.",
  "declaration_id": "TauLib.BookI.Boundary.Integration::integral_const_one_3",
  "declaration_slug": "integral-const-one-3",
  "kind": "theorem",
  "name": "integral_const_one_3",
  "module_name": "TauLib.BookI.Boundary.Integration",
  "module_url": "/verify/taulib/docs/book-i-boundary-integration/",
  "source_line_start": 111,
  "source_line_end": 112,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Integration.lean#L111-L112",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Integration.lean#L111-L112",
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

- Module: [TauLib.BookI.Boundary.Integration](/verify/taulib/docs/book-i-boundary-integration/)
- Source path: [`TauLib/BookI/Boundary/Integration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Integration.lean#L111-L112)
- Source range: L111-L112
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.D99` — τ-Integral

## Immediate Comment / Docstring

```lean
/-- [I.D99] Integral of constant 1 at stage 3: ∫_3 1 = 30/30 = 1. -/
```

## Source Excerpt

```lean
theorem integral_const_one_3 :
    (tau_integral const_one 3).numerator = 30 := by native_decide
```
