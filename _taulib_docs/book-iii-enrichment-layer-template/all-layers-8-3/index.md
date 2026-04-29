---
{
  "projection_kind": "taulib_declaration",
  "title": "all_layers_8_3",
  "permalink": "/verify/taulib/docs/book-iii-enrichment-layer-template/all-layers-8-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Enrichment.LayerTemplate`.",
  "declaration_id": "TauLib.BookIII.Enrichment.LayerTemplate::all_layers_8_3",
  "declaration_slug": "all-layers-8-3",
  "kind": "theorem",
  "name": "all_layers_8_3",
  "module_name": "TauLib.BookIII.Enrichment.LayerTemplate",
  "module_url": "/verify/taulib/docs/book-iii-enrichment-layer-template/",
  "source_line_start": 354,
  "source_line_end": 355,
  "registry_ids": [
    "III.D05"
  ],
  "related_registry_items": [
    {
      "id": "III.D05",
      "title": "Layer Template",
      "url": "/registry/object/III.D05/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/LayerTemplate.lean#L354-L355",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Enrichment.LayerTemplate",
        "url": "/verify/taulib/docs/book-iii-enrichment-layer-template/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/LayerTemplate.lean#L354-L355",
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

- Module: [TauLib.BookIII.Enrichment.LayerTemplate](/verify/taulib/docs/book-iii-enrichment-layer-template/)
- Source path: [`TauLib/BookIII/Enrichment/LayerTemplate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/LayerTemplate.lean#L354-L355)
- Source range: L354-L355
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D05` — Layer Template

## Immediate Comment / Docstring

```lean
-- All four layers valid [III.D05]
```

## Source Excerpt

```lean
theorem all_layers_8_3 :
    all_layers_valid 8 3 = true := by native_decide
```
