---
{
  "projection_kind": "taulib_declaration",
  "title": "squarefree_dominance_thm",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-abcdeep/squarefree-dominance-thm/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Arithmetic.ABCDeep`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.ABCDeep::squarefree_dominance_thm",
  "declaration_slug": "squarefree-dominance-thm",
  "kind": "theorem",
  "name": "squarefree_dominance_thm",
  "module_name": "TauLib.BookIII.Arithmetic.ABCDeep",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-abcdeep/",
  "source_line_start": 208,
  "source_line_end": 209,
  "registry_ids": [
    "III.P47"
  ],
  "related_registry_items": [
    {
      "id": "III.P47",
      "title": "Squarefree Dominance Theorem",
      "url": "/registry/object/III.P47/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCDeep.lean#L208-L209",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.ABCDeep",
        "url": "/verify/taulib/docs/book-iii-arithmetic-abcdeep/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCDeep.lean#L208-L209",
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

- Module: [TauLib.BookIII.Arithmetic.ABCDeep](/verify/taulib/docs/book-iii-arithmetic-abcdeep/)
- Source path: [`TauLib/BookIII/Arithmetic/ABCDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCDeep.lean#L208-L209)
- Source range: L208-L209
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P47` — Squarefree Dominance Theorem

## Immediate Comment / Docstring

```lean
/-- [III.P47] Zero high-quality triples among squarefree coprimes ≤ 50. -/
```

## Source Excerpt

```lean
theorem squarefree_dominance_thm :
    squarefree_high_quality_count 50 = 0 := by native_decide
```
