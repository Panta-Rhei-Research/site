---
{
  "projection_kind": "taulib_declaration",
  "title": "comparison_10_1",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-enriched-bi-square/comparison-10-1/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Arithmetic.EnrichedBiSquare`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.EnrichedBiSquare::comparison_10_1",
  "declaration_slug": "comparison-10-1",
  "kind": "theorem",
  "name": "comparison_10_1",
  "module_name": "TauLib.BookIII.Arithmetic.EnrichedBiSquare",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-enriched-bi-square/",
  "source_line_start": 171,
  "source_line_end": 174,
  "registry_ids": [
    "III.T39"
  ],
  "related_registry_items": [
    {
      "id": "III.T39",
      "title": "Enriched Bi-Square Comparison",
      "url": "/registry/object/III.T39/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean#L171-L174",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.EnrichedBiSquare",
        "url": "/verify/taulib/docs/book-iii-arithmetic-enriched-bi-square/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean#L171-L174",
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

- Module: [TauLib.BookIII.Arithmetic.EnrichedBiSquare](/verify/taulib/docs/book-iii-arithmetic-enriched-bi-square/)
- Source path: [`TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean#L171-L174)
- Source range: L171-L174
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T39` — Enriched Bi-Square Comparison

## Immediate Comment / Docstring

```lean
/-- [III.T39] Structural: comparison at depth 1. -/
```

## Source Excerpt

```lean
theorem comparison_10_1 :
    bisquare_comparison_check 10 1 = true := by native_decide

end Tau.BookIII.Arithmetic
```
