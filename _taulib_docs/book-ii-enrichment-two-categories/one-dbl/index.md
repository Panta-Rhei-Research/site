---
{
  "projection_kind": "taulib_declaration",
  "title": "one_dbl",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-two-categories/one-dbl/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.TwoCategories`.",
  "declaration_id": "TauLib.BookII.Enrichment.TwoCategories::one_dbl",
  "declaration_slug": "one-dbl",
  "kind": "def",
  "name": "one_dbl",
  "module_name": "TauLib.BookII.Enrichment.TwoCategories",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-two-categories/",
  "source_line_start": 101,
  "source_line_end": 101,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L101-L101",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.TwoCategories",
        "url": "/verify/taulib/docs/book-ii-enrichment-two-categories/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L101-L101",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookII.Enrichment.TwoCategories](/verify/taulib/docs/book-ii-enrichment-two-categories/)
- Source path: [`TauLib/BookII/Enrichment/TwoCategories.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L101-L101)
- Source range: L101-L101
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Sample 1-cell: doubling endomorphism. -/
```

## Source Excerpt

```lean
def one_dbl : OneCell := fun n k => reduce (2 * n) k
```
