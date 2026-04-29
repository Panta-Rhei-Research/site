---
{
  "projection_kind": "taulib_declaration",
  "title": "LayerSeparation",
  "permalink": "/verify/taulib/docs/book-vi-life-core-layer-sep/layer-separation/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.LifeCore.LayerSep`.",
  "declaration_id": "TauLib.BookVI.LifeCore.LayerSep::LayerSeparation",
  "declaration_slug": "layer-separation",
  "kind": "structure",
  "name": "LayerSeparation",
  "module_name": "TauLib.BookVI.LifeCore.LayerSep",
  "module_url": "/verify/taulib/docs/book-vi-life-core-layer-sep/",
  "source_line_start": 42,
  "source_line_end": 47,
  "registry_ids": [
    "VI.T04"
  ],
  "related_registry_items": [
    {
      "id": "VI.T04",
      "title": "Layer Separation Lemma",
      "url": "/registry/object/VI.T04/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/LayerSep.lean#L42-L47",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.LifeCore.LayerSep",
        "url": "/verify/taulib/docs/book-vi-life-core-layer-sep/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/LayerSep.lean#L42-L47",
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

- Module: [TauLib.BookVI.LifeCore.LayerSep](/verify/taulib/docs/book-vi-life-core-layer-sep/)
- Source path: [`TauLib/BookVI/LifeCore/LayerSep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/LayerSep.lean#L42-L47)
- Source range: L42-L47
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T04` — Layer Separation Lemma

## Immediate Comment / Docstring

```lean
/-- [VI.T04] Layer Separation Lemma: E₂ is non-reducible to E₁.
    Witness: NS-TOV system. -/
```

## Source Excerpt

```lean
structure LayerSeparation where
  e1_has_distinction : Bool := true
  e1_lacks_selfdesc : Bool := true
  non_reducible : Bool := true
  has_witness : Bool := true
  deriving Repr
```
