---
{
  "projection_kind": "taulib_declaration",
  "title": "echo_search_catalog",
  "permalink": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-search-catalog/",
  "summary_short": "`def` declaration in `TauLib.BookV.Gravity.BHTopoModes`.",
  "declaration_id": "TauLib.BookV.Gravity.BHTopoModes::echo_search_catalog",
  "declaration_slug": "echo-search-catalog",
  "kind": "def",
  "name": "echo_search_catalog",
  "module_name": "TauLib.BookV.Gravity.BHTopoModes",
  "module_url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/",
  "source_line_start": 641,
  "source_line_end": 652,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L641-L652",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.BHTopoModes",
        "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L641-L652",
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

- Module: [TauLib.BookV.Gravity.BHTopoModes](/verify/taulib/docs/book-v-gravity-bhtopo-modes/)
- Source path: [`TauLib/BookV/Gravity/BHTopoModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L641-L652)
- Source range: L641-L652
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- 10-event echo search catalog -/
```

## Source Excerpt

```lean
def echo_search_catalog : List EchoSearchEvent := [
  ⟨"GW150914",  631, 240, 104, 3643, 424⟩,
  ⟨"GW151226",  205, 130,  56, 1184, 138⟩,
  ⟨"GW170104",  489, 130,  56, 2824, 329⟩,
  ⟨"GW170608",  178, 150,  65, 1028, 120⟩,
  ⟨"GW170729",  795, 100,  43, 4590, 535⟩,
  ⟨"GW170814",  532, 180,  78, 3072, 358⟩,
  ⟨"GW190521", 1500, 140,  60, 8661, 1009⟩,
  ⟨"GW190814",  250, 250, 108, 1444, 168⟩,
  ⟨"GW200115",   61, 120,  52,  352,  41⟩,
  ⟨"GW191109", 1070, 110,  48, 6178, 720⟩
]
```
