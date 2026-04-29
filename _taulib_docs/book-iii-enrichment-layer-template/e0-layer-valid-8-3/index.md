---
{
  "projection_kind": "taulib_declaration",
  "title": "e0_layer_valid_8_3",
  "permalink": "/verify/taulib/docs/book-iii-enrichment-layer-template/e0-layer-valid-8-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Enrichment.LayerTemplate`.",
  "declaration_id": "TauLib.BookIII.Enrichment.LayerTemplate::e0_layer_valid_8_3",
  "declaration_slug": "e0-layer-valid-8-3",
  "kind": "theorem",
  "name": "e0_layer_valid_8_3",
  "module_name": "TauLib.BookIII.Enrichment.LayerTemplate",
  "module_url": "/verify/taulib/docs/book-iii-enrichment-layer-template/",
  "source_line_start": 338,
  "source_line_end": 339,
  "registry_ids": [
    "III.D06"
  ],
  "related_registry_items": [
    {
      "id": "III.D06",
      "title": "E₀ Layer (Mathematics)",
      "url": "/registry/object/III.D06/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/LayerTemplate.lean#L338-L339",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/LayerTemplate.lean#L338-L339",
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
- Source path: [`TauLib/BookIII/Enrichment/LayerTemplate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/LayerTemplate.lean#L338-L339)
- Source range: L338-L339
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D06` — E₀ Layer (Mathematics)

## Immediate Comment / Docstring

```lean
-- ============================================================
-- FORMAL VERIFICATION (native_decide)
-- ============================================================

-- E₀ layer valid [III.D06]
```

## Source Excerpt

```lean
theorem e0_layer_valid_8_3 :
    layer_valid_at .E0 8 3 = true := by native_decide
```
