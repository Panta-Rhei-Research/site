---
{
  "projection_kind": "taulib_declaration",
  "title": "one_id",
  "permalink": "/corpus/taulib/docs/book-ii-enrichment-two-categories/one-id/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.TwoCategories`.",
  "declaration_id": "TauLib.BookII.Enrichment.TwoCategories::one_id",
  "declaration_slug": "one-id",
  "kind": "def",
  "name": "one_id",
  "module_name": "TauLib.BookII.Enrichment.TwoCategories",
  "module_url": "/corpus/taulib/docs/book-ii-enrichment-two-categories/",
  "source_line_start": 95,
  "source_line_end": 95,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L95-L95",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.TwoCategories",
        "url": "/corpus/taulib/docs/book-ii-enrichment-two-categories/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L95-L95",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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

- Module: [TauLib.BookII.Enrichment.TwoCategories](/corpus/taulib/docs/book-ii-enrichment-two-categories/)
- Source path: [`TauLib/BookII/Enrichment/TwoCategories.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L95-L95)
- Source range: L95-L95
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Sample 1-cell: identity endomorphism. -/
```

## Source Excerpt

```lean
def one_id : OneCell := fun n k => reduce n k
```
