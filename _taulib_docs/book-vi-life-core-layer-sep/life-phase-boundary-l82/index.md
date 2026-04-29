---
{
  "projection_kind": "taulib_declaration",
  "title": "life_phase_boundary",
  "permalink": "/verify/taulib/docs/book-vi-life-core-layer-sep/life-phase-boundary-l82/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.LifeCore.LayerSep`.",
  "declaration_id": "TauLib.BookVI.LifeCore.LayerSep::life_phase_boundary",
  "declaration_slug": "life-phase-boundary-l82",
  "kind": "theorem",
  "name": "life_phase_boundary",
  "module_name": "TauLib.BookVI.LifeCore.LayerSep",
  "module_url": "/verify/taulib/docs/book-vi-life-core-layer-sep/",
  "source_line_start": 82,
  "source_line_end": 87,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/LayerSep.lean#L82-L87",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/LayerSep.lean#L82-L87",
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
- Source path: [`TauLib/BookVI/LifeCore/LayerSep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/LayerSep.lean#L82-L87)
- Source range: L82-L87
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
theorem life_phase_boundary :
    phase_boundary.is_sharp = true ∧
    phase_boundary.topology_change = true :=
  ⟨rfl, rfl⟩

end Tau.BookVI.LayerSep
```
