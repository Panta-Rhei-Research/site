---
{
  "projection_kind": "taulib_declaration",
  "title": "yoneda_10_3",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-self-describing/yoneda-10-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Enrichment.SelfDescribing`.",
  "declaration_id": "TauLib.BookII.Enrichment.SelfDescribing::yoneda_10_3",
  "declaration_slug": "yoneda-10-3",
  "kind": "theorem",
  "name": "yoneda_10_3",
  "module_name": "TauLib.BookII.Enrichment.SelfDescribing",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-self-describing/",
  "source_line_start": 299,
  "source_line_end": 300,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L299-L300",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.SelfDescribing",
        "url": "/verify/taulib/docs/book-ii-enrichment-self-describing/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L299-L300",
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

- Module: [TauLib.BookII.Enrichment.SelfDescribing](/verify/taulib/docs/book-ii-enrichment-self-describing/)
- Source path: [`TauLib/BookII/Enrichment/SelfDescribing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L299-L300)
- Source range: L299-L300
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- Yoneda faithfulness [II.D57, clause 2]
```

## Source Excerpt

```lean
theorem yoneda_10_3 :
    e1_yoneda_witness 10 3 = true := by native_decide
```
