---
{
  "projection_kind": "taulib_declaration",
  "title": "coercion_preserves_order",
  "permalink": "/verify/taulib/docs/book-iii-enrichment-layer-template/coercion-preserves-order/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Enrichment.LayerTemplate`.",
  "declaration_id": "TauLib.BookIII.Enrichment.LayerTemplate::coercion_preserves_order",
  "declaration_slug": "coercion-preserves-order",
  "kind": "theorem",
  "name": "coercion_preserves_order",
  "module_name": "TauLib.BookIII.Enrichment.LayerTemplate",
  "module_url": "/verify/taulib/docs/book-iii-enrichment-layer-template/",
  "source_line_start": 375,
  "source_line_end": 377,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/LayerTemplate.lean#L375-L377",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/LayerTemplate.lean#L375-L377",
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
- Source path: [`TauLib/BookIII/Enrichment/LayerTemplate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/LayerTemplate.lean#L375-L377)
- Source range: L375-L377
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Coercion preserves order: if E0 < E1 in Book II, then ofBookII preserves this. -/
```

## Source Excerpt

```lean
theorem coercion_preserves_order :
    EnrLevel.lt (EnrLevel.ofBookII .E0) (EnrLevel.ofBookII .E1) = true := by
  rfl
```
