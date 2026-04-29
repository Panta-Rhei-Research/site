---
{
  "projection_kind": "taulib_declaration",
  "title": "hol_assoc_thm",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-category-structure/hol-assoc-thm/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Hartogs.CategoryStructure`.",
  "declaration_id": "TauLib.BookII.Hartogs.CategoryStructure::hol_assoc_thm",
  "declaration_slug": "hol-assoc-thm",
  "kind": "theorem",
  "name": "hol_assoc_thm",
  "module_name": "TauLib.BookII.Hartogs.CategoryStructure",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-category-structure/",
  "source_line_start": 211,
  "source_line_end": 213,
  "registry_ids": [
    "II.T29"
  ],
  "related_registry_items": [
    {
      "id": "II.T29",
      "title": "Associativity of Holomorphic Composition",
      "url": "/registry/object/II.T29/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L211-L213",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.CategoryStructure",
        "url": "/verify/taulib/docs/book-ii-hartogs-category-structure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L211-L213",
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

- Module: [TauLib.BookII.Hartogs.CategoryStructure](/verify/taulib/docs/book-ii-hartogs-category-structure/)
- Source path: [`TauLib/BookII/Hartogs/CategoryStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L211-L213)
- Source range: L211-L213
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T29` — Associativity of Holomorphic Composition

## Immediate Comment / Docstring

```lean
/-- [II.T29] Associativity theorem (formal):
    Holomorphic composition is associative by definition.
    hol_comp f (hol_comp g h) n k = hol_comp (hol_comp f g) h n k

    This is an immediate consequence of the definition:
    both sides expand to f(g(h(n, k), k), k). -/
```

## Source Excerpt

```lean
theorem hol_assoc_thm (f g h : TauIdx -> TauIdx -> TauIdx) (n k : TauIdx) :
    hol_comp f (hol_comp g h) n k = hol_comp (hol_comp f g) h n k := by
  rfl
```
