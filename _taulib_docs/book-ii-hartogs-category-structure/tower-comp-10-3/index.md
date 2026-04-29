---
{
  "projection_kind": "taulib_declaration",
  "title": "tower_comp_10_3",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-category-structure/tower-comp-10-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Hartogs.CategoryStructure`.",
  "declaration_id": "TauLib.BookII.Hartogs.CategoryStructure::tower_comp_10_3",
  "declaration_slug": "tower-comp-10-3",
  "kind": "theorem",
  "name": "tower_comp_10_3",
  "module_name": "TauLib.BookII.Hartogs.CategoryStructure",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-category-structure/",
  "source_line_start": 461,
  "source_line_end": 462,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L461-L462",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L461-L462",
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
- Source path: [`TauLib/BookII/Hartogs/CategoryStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L461-L462)
- Source range: L461-L462
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- Tower coherence under composition
```

## Source Excerpt

```lean
theorem tower_comp_10_3 :
    tower_coherent_comp_check 10 3 = true := by native_decide
```
