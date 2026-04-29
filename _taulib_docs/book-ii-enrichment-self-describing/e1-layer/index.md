---
{
  "projection_kind": "taulib_declaration",
  "title": "E1Layer",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-self-describing/e1-layer/",
  "summary_short": "`structure` declaration in `TauLib.BookII.Enrichment.SelfDescribing`.",
  "declaration_id": "TauLib.BookII.Enrichment.SelfDescribing::E1Layer",
  "declaration_slug": "e1-layer",
  "kind": "structure",
  "name": "E1Layer",
  "module_name": "TauLib.BookII.Enrichment.SelfDescribing",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-self-describing/",
  "source_line_start": 47,
  "source_line_end": 52,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L47-L52",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L47-L52",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookII.Enrichment.SelfDescribing](/verify/taulib/docs/book-ii-enrichment-self-describing/)
- Source path: [`TauLib/BookII/Enrichment/SelfDescribing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L47-L52)
- Source range: L47-L52
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `II.D57` — E1 Enrichment Layer

## Immediate Comment / Docstring

```lean
/-- [II.D57] The E1 enrichment layer bundles four boolean witnesses:
    self-enrichment, Yoneda faithfulness, 2-category structure,
    and Code/Decode bijection. All four must hold simultaneously
    for the layer to be active. -/
```

## Source Excerpt

```lean
structure E1Layer where
  has_self_enrichment : Bool
  has_yoneda : Bool
  has_2cat : Bool
  has_code_decode : Bool
  deriving Repr, DecidableEq
```
