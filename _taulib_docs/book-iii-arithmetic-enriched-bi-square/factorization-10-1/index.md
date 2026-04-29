---
{
  "projection_kind": "taulib_declaration",
  "title": "factorization_10_1",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-enriched-bi-square/factorization-10-1/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Arithmetic.EnrichedBiSquare`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.EnrichedBiSquare::factorization_10_1",
  "declaration_slug": "factorization-10-1",
  "kind": "theorem",
  "name": "factorization_10_1",
  "module_name": "TauLib.BookIII.Arithmetic.EnrichedBiSquare",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-enriched-bi-square/",
  "source_line_start": 167,
  "source_line_end": 168,
  "registry_ids": [
    "III.T38"
  ],
  "related_registry_items": [
    {
      "id": "III.T38",
      "title": "Finite Factorization Pasting",
      "url": "/registry/object/III.T38/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean#L167-L168",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean#L167-L168",
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
- Source path: [`TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean#L167-L168)
- Source range: L167-L168
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T38` — Finite Factorization Pasting

## Immediate Comment / Docstring

```lean
/-- [III.T38] Structural: factorization at depth 1. -/
```

## Source Excerpt

```lean
theorem factorization_10_1 :
    finite_factorization_check 10 1 = true := by native_decide
```
