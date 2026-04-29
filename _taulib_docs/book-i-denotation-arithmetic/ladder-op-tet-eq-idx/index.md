---
{
  "projection_kind": "taulib_declaration",
  "title": "ladderOp_tet_eq_idx",
  "permalink": "/verify/taulib/docs/book-i-denotation-arithmetic/ladder-op-tet-eq-idx/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.Arithmetic`.",
  "declaration_id": "TauLib.BookI.Denotation.Arithmetic::ladderOp_tet_eq_idx",
  "declaration_slug": "ladder-op-tet-eq-idx",
  "kind": "theorem",
  "name": "ladderOp_tet_eq_idx",
  "module_name": "TauLib.BookI.Denotation.Arithmetic",
  "module_url": "/verify/taulib/docs/book-i-denotation-arithmetic/",
  "source_line_start": 128,
  "source_line_end": 130,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Arithmetic.lean#L128-L130",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.Arithmetic",
        "url": "/verify/taulib/docs/book-i-denotation-arithmetic/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Arithmetic.lean#L128-L130",
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

- Module: [TauLib.BookI.Denotation.Arithmetic](/verify/taulib/docs/book-i-denotation-arithmetic/)
- Source path: [`TauLib/BookI/Denotation/Arithmetic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Arithmetic.lean#L128-L130)
- Source range: L128-L130
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- ladderOp at tet_level coincides with earned idx_tetration. -/
```

## Source Excerpt

```lean
theorem ladderOp_tet_eq_idx (n m : TauIdx) :
    ladderOp .tet_level n m = idx_tetration n m := by
  simp [ladderOp, idx_tetration_eq]
```
