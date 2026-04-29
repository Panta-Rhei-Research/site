---
{
  "projection_kind": "taulib_declaration",
  "title": "layer_separation_lemma",
  "permalink": "/verify/taulib/docs/book-vi-life-core-layer-sep/layer-separation-lemma/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.LifeCore.LayerSep`.",
  "declaration_id": "TauLib.BookVI.LifeCore.LayerSep::layer_separation_lemma",
  "declaration_slug": "layer-separation-lemma",
  "kind": "theorem",
  "name": "layer_separation_lemma",
  "module_name": "TauLib.BookVI.LifeCore.LayerSep",
  "module_url": "/verify/taulib/docs/book-vi-life-core-layer-sep/",
  "source_line_start": 51,
  "source_line_end": 55,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/LayerSep.lean#L51-L55",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/LayerSep.lean#L51-L55",
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

- Module: [TauLib.BookVI.LifeCore.LayerSep](/verify/taulib/docs/book-vi-life-core-layer-sep/)
- Source path: [`TauLib/BookVI/LifeCore/LayerSep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/LayerSep.lean#L51-L55)
- Source range: L51-L55
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem layer_separation_lemma :
    layer_sep.e1_has_distinction = true ∧
    layer_sep.e1_lacks_selfdesc = true ∧
    layer_sep.non_reducible = true :=
  ⟨rfl, rfl, rfl⟩
```
