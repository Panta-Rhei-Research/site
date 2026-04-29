---
{
  "projection_kind": "taulib_declaration",
  "title": "ladder_has_7_levels",
  "permalink": "/verify/taulib/docs/book-vi-cosmic-life-galaxy-basin/ladder-has-7-levels/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.CosmicLife.GalaxyBasin`.",
  "declaration_id": "TauLib.BookVI.CosmicLife.GalaxyBasin::ladder_has_7_levels",
  "declaration_slug": "ladder-has-7-levels",
  "kind": "theorem",
  "name": "ladder_has_7_levels",
  "module_name": "TauLib.BookVI.CosmicLife.GalaxyBasin",
  "module_url": "/verify/taulib/docs/book-vi-cosmic-life-galaxy-basin/",
  "source_line_start": 68,
  "source_line_end": 71,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L68-L71",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.CosmicLife.GalaxyBasin",
        "url": "/verify/taulib/docs/book-vi-cosmic-life-galaxy-basin/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L68-L71",
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

- Module: [TauLib.BookVI.CosmicLife.GalaxyBasin](/verify/taulib/docs/book-vi-cosmic-life-galaxy-basin/)
- Source path: [`TauLib/BookVI/CosmicLife/GalaxyBasin.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/GalaxyBasin.lean#L68-L71)
- Source range: L68-L71
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
theorem ladder_has_7_levels :
    carrier_ladder.level_count = 7 ∧
    ladder_level_names.length = 7 :=
  ⟨rfl, by native_decide⟩
```
