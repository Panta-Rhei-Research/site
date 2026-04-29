---
{
  "projection_kind": "taulib_declaration",
  "title": "e1_layer_check",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-self-describing/e1-layer-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.SelfDescribing`.",
  "declaration_id": "TauLib.BookII.Enrichment.SelfDescribing::e1_layer_check",
  "declaration_slug": "e1-layer-check",
  "kind": "def",
  "name": "e1_layer_check",
  "module_name": "TauLib.BookII.Enrichment.SelfDescribing",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-self-describing/",
  "source_line_start": 216,
  "source_line_end": 219,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L216-L219",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L216-L219",
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

- Module: [TauLib.BookII.Enrichment.SelfDescribing](/verify/taulib/docs/book-ii-enrichment-self-describing/)
- Source path: [`TauLib/BookII/Enrichment/SelfDescribing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L216-L219)
- Source range: L216-L219
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D57` — E1 Enrichment Layer

## Immediate Comment / Docstring

```lean
/-- [II.D57] Check that all four E1 components are present. -/
```

## Source Excerpt

```lean
def e1_layer_check (bound db k_max : TauIdx) : Bool :=
  let layer := compute_e1_layer bound db k_max
  layer.has_self_enrichment && layer.has_yoneda &&
  layer.has_2cat && layer.has_code_decode
```
