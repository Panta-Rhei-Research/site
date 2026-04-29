---
{
  "projection_kind": "taulib_declaration",
  "title": "LayerTemplate",
  "permalink": "/verify/taulib/docs/book-iii-enrichment-layer-template/layer-template/",
  "summary_short": "`structure` declaration in `TauLib.BookIII.Enrichment.LayerTemplate`.",
  "declaration_id": "TauLib.BookIII.Enrichment.LayerTemplate::LayerTemplate",
  "declaration_slug": "layer-template",
  "kind": "structure",
  "name": "LayerTemplate",
  "module_name": "TauLib.BookIII.Enrichment.LayerTemplate",
  "module_url": "/verify/taulib/docs/book-iii-enrichment-layer-template/",
  "source_line_start": 98,
  "source_line_end": 106,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/LayerTemplate.lean#L98-L106",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/LayerTemplate.lean#L98-L106",
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

- Module: [TauLib.BookIII.Enrichment.LayerTemplate](/verify/taulib/docs/book-iii-enrichment-layer-template/)
- Source path: [`TauLib/BookIII/Enrichment/LayerTemplate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/LayerTemplate.lean#L98-L106)
- Source range: L98-L106
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `III.D05` — Layer Template

## Immediate Comment / Docstring

```lean
/-- [III.D05] The uniform four-component layer template.
    Each enrichment layer E_k instantiates this with specific
    carrier, predicate, decoder, and invariant functions.

    The template captures the structural pattern:
    - Carrier: the objects that live at this level
    - Predicate: the admissibility condition for carrier elements
    - Decoder: the projection/extraction map (one level down)
    - Invariant: the structure preserved at this level

    Template flow: E_k.invariant → E_{k+1}.carrier -/
```

## Source Excerpt

```lean
structure LayerTemplate where
  /-- Carrier check: is x a valid carrier element at stage k? -/
  carrier_check : TauIdx → TauIdx → Bool
  /-- Predicate check: does x satisfy the admissibility predicate? -/
  predicate_check : TauIdx → TauIdx → Bool
  /-- Decoder: project x from this layer to the previous. -/
  decoder : TauIdx → TauIdx → TauIdx
  /-- Invariant check: is the layer invariant satisfied? -/
  invariant_check : TauIdx → TauIdx → Bool
```
