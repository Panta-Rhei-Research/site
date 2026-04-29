---
{
  "projection_kind": "taulib_declaration",
  "title": "syntax_semantics_collapse",
  "permalink": "/verify/taulib/docs/book-vii-meta-saturation/syntax-semantics-collapse/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Meta.Saturation`.",
  "declaration_id": "TauLib.BookVII.Meta.Saturation::syntax_semantics_collapse",
  "declaration_slug": "syntax-semantics-collapse",
  "kind": "theorem",
  "name": "syntax_semantics_collapse",
  "module_name": "TauLib.BookVII.Meta.Saturation",
  "module_url": "/verify/taulib/docs/book-vii-meta-saturation/",
  "source_line_start": 689,
  "source_line_end": 693,
  "registry_ids": [
    "VII.T21"
  ],
  "related_registry_items": [
    {
      "id": "VII.T21",
      "title": "Syntax-Semantics Collapse",
      "url": "/registry/object/VII.T21/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L689-L693",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L689-L693",
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
- Source path: [`TauLib/BookVII/Meta/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L689-L693)
- Source range: L689-L693
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T21` — Syntax-Semantics Collapse

## Immediate Comment / Docstring

```lean
/-- [VII.T21] Syntax-Semantics Collapse (ch63). At S_L (logos sector):
    form = content. The distinction between syntactic form and semantic
    content collapses because the D-C coincidence means the proof
    structure IS the meaning. -/
```

## Source Excerpt

```lean
theorem syntax_semantics_collapse :
    -- Links to logos sector D-C coincidence
    sector_logos.dc_coincidence = true ∧
    language_temporal.temporal_markers = true :=
  ⟨rfl, rfl⟩
```
