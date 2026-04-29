---
{
  "projection_kind": "taulib_declaration",
  "title": "language_as_self_enrichment",
  "permalink": "/verify/taulib/docs/book-vii-meta-saturation/language-as-self-enrichment/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Meta.Saturation`.",
  "declaration_id": "TauLib.BookVII.Meta.Saturation::language_as_self_enrichment",
  "declaration_slug": "language-as-self-enrichment",
  "kind": "theorem",
  "name": "language_as_self_enrichment",
  "module_name": "TauLib.BookVII.Meta.Saturation",
  "module_url": "/verify/taulib/docs/book-vii-meta-saturation/",
  "source_line_start": 675,
  "source_line_end": 679,
  "registry_ids": [
    "VII.T20"
  ],
  "related_registry_items": [
    {
      "id": "VII.T20",
      "title": "Language as Self-Enrichment",
      "url": "/registry/object/VII.T20/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L675-L679",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Saturation",
        "url": "/verify/taulib/docs/book-vii-meta-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L675-L679",
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

- Module: [TauLib.BookVII.Meta.Saturation](/verify/taulib/docs/book-vii-meta-saturation/)
- Source path: [`TauLib/BookVII/Meta/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L675-L679)
- Source range: L675-L679
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T20` — Language as Self-Enrichment

## Immediate Comment / Docstring

```lean
/-- [VII.T20] Language as Self-Enrichment (ch62). Language enriches the
    enricher: an E₃ system with language can describe its own enrichment
    chain. This is a second-order self-description: the system models
    the fact that it models itself. Language is the vehicle for SelfDesc². -/
```

## Source Excerpt

```lean
theorem language_as_self_enrichment :
    language_temporal.temporal_markers = true ∧
    language_temporal.temporal_indexing = true ∧
    subsymbolic.pre_symbolic = true :=
  ⟨rfl, rfl, rfl⟩
```
