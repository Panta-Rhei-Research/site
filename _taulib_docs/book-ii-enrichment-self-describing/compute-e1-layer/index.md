---
{
  "projection_kind": "taulib_declaration",
  "title": "compute_e1_layer",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-self-describing/compute-e1-layer/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.SelfDescribing`.",
  "declaration_id": "TauLib.BookII.Enrichment.SelfDescribing::compute_e1_layer",
  "declaration_slug": "compute-e1-layer",
  "kind": "def",
  "name": "compute_e1_layer",
  "module_name": "TauLib.BookII.Enrichment.SelfDescribing",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-self-describing/",
  "source_line_start": 208,
  "source_line_end": 213,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L208-L213",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L208-L213",
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
- Source path: [`TauLib/BookII/Enrichment/SelfDescribing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L208-L213)
- Source range: L208-L213
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D57` — E1 Enrichment Layer

## Immediate Comment / Docstring

```lean
/-- [II.D57] Compute the E1 layer by evaluating all four witnesses. -/
```

## Source Excerpt

```lean
def compute_e1_layer (bound db k_max : TauIdx) : E1Layer :=
  { has_self_enrichment := e1_self_enrichment_witness bound db
  , has_yoneda := e1_yoneda_witness bound db
  , has_2cat := e1_2cat_witness bound db
  , has_code_decode := e1_code_decode_witness k_max
  }
```
