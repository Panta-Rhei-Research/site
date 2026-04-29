---
{
  "projection_kind": "taulib_declaration",
  "title": "product_meet_10_1",
  "permalink": "/verify/taulib/docs/book-iii-computation-comp-bi-square/product-meet-10-1/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Computation.CompBiSquare`.",
  "declaration_id": "TauLib.BookIII.Computation.CompBiSquare::product_meet_10_1",
  "declaration_slug": "product-meet-10-1",
  "kind": "theorem",
  "name": "product_meet_10_1",
  "module_name": "TauLib.BookIII.Computation.CompBiSquare",
  "module_url": "/verify/taulib/docs/book-iii-computation-comp-bi-square/",
  "source_line_start": 185,
  "source_line_end": 186,
  "registry_ids": [
    "III.T32"
  ],
  "related_registry_items": [
    {
      "id": "III.T32",
      "title": "Product-Meet Collapse",
      "url": "/registry/object/III.T32/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/CompBiSquare.lean#L185-L186",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.CompBiSquare",
        "url": "/verify/taulib/docs/book-iii-computation-comp-bi-square/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/CompBiSquare.lean#L185-L186",
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

- Module: [TauLib.BookIII.Computation.CompBiSquare](/verify/taulib/docs/book-iii-computation-comp-bi-square/)
- Source path: [`TauLib/BookIII/Computation/CompBiSquare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/CompBiSquare.lean#L185-L186)
- Source range: L185-L186
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T32` — Product-Meet Collapse

## Immediate Comment / Docstring

```lean
/-- [III.T32] Structural: product-meet at depth 1. -/
```

## Source Excerpt

```lean
theorem product_meet_10_1 :
    product_meet_collapse_check 10 1 = true := by native_decide
```
