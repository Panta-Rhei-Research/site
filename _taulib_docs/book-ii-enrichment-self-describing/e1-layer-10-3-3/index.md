---
{
  "projection_kind": "taulib_declaration",
  "title": "e1_layer_10_3_3",
  "permalink": "/corpus/taulib/docs/book-ii-enrichment-self-describing/e1-layer-10-3-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Enrichment.SelfDescribing`.",
  "declaration_id": "TauLib.BookII.Enrichment.SelfDescribing::e1_layer_10_3_3",
  "declaration_slug": "e1-layer-10-3-3",
  "kind": "theorem",
  "name": "e1_layer_10_3_3",
  "module_name": "TauLib.BookII.Enrichment.SelfDescribing",
  "module_url": "/corpus/taulib/docs/book-ii-enrichment-self-describing/",
  "source_line_start": 311,
  "source_line_end": 312,
  "registry_ids": [
    "II.D57"
  ],
  "related_registry_items": [
    {
      "id": "II.D57",
      "title": "E1 Enrichment Layer",
      "url": "/registry/object/II.D57/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L311-L312",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.SelfDescribing",
        "url": "/corpus/taulib/docs/book-ii-enrichment-self-describing/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L311-L312",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookII.Enrichment.SelfDescribing](/corpus/taulib/docs/book-ii-enrichment-self-describing/)
- Source path: [`TauLib/BookII/Enrichment/SelfDescribing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L311-L312)
- Source range: L311-L312
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `II.D57` — E1 Enrichment Layer

## Immediate Comment / Docstring

```lean
-- Full E1 layer [II.D57]
```

## Source Excerpt

```lean
theorem e1_layer_10_3_3 :
    e1_layer_check 10 3 3 = true := by native_decide
```
