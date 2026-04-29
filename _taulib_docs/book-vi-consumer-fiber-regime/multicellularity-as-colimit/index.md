---
{
  "projection_kind": "taulib_declaration",
  "title": "multicellularity_as_colimit",
  "permalink": "/verify/taulib/docs/book-vi-consumer-fiber-regime/multicellularity-as-colimit/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.Consumer.FiberRegime`.",
  "declaration_id": "TauLib.BookVI.Consumer.FiberRegime::multicellularity_as_colimit",
  "declaration_slug": "multicellularity-as-colimit",
  "kind": "theorem",
  "name": "multicellularity_as_colimit",
  "module_name": "TauLib.BookVI.Consumer.FiberRegime",
  "module_url": "/verify/taulib/docs/book-vi-consumer-fiber-regime/",
  "source_line_start": 108,
  "source_line_end": 112,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/FiberRegime.lean#L108-L112",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Consumer.FiberRegime",
        "url": "/verify/taulib/docs/book-vi-consumer-fiber-regime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/FiberRegime.lean#L108-L112",
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

- Module: [TauLib.BookVI.Consumer.FiberRegime](/verify/taulib/docs/book-vi-consumer-fiber-regime/)
- Source path: [`TauLib/BookVI/Consumer/FiberRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/FiberRegime.lean#L108-L112)
- Source range: L108-L112
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
theorem multicellularity_as_colimit :
    multicellular.cell_count ≥ 2 ∧
    multicellular.cooperative = true ∧
    multicellular.colimit_construction = true :=
  ⟨multicellular.multi, rfl, rfl⟩
```
