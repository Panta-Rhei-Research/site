---
{
  "projection_kind": "taulib_declaration",
  "title": "tower_complete_check",
  "permalink": "/verify/taulib/docs/book-iii-mirror-saturation/tower-complete-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Mirror.Saturation`.",
  "declaration_id": "TauLib.BookIII.Mirror.Saturation::tower_complete_check",
  "declaration_slug": "tower-complete-check",
  "kind": "def",
  "name": "tower_complete_check",
  "module_name": "TauLib.BookIII.Mirror.Saturation",
  "module_url": "/verify/taulib/docs/book-iii-mirror-saturation/",
  "source_line_start": 149,
  "source_line_end": 169,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/Saturation.lean#L149-L169",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Mirror.Saturation",
        "url": "/verify/taulib/docs/book-iii-mirror-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/Saturation.lean#L149-L169",
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

- Module: [TauLib.BookIII.Mirror.Saturation](/verify/taulib/docs/book-iii-mirror-saturation/)
- Source path: [`TauLib/BookIII/Mirror/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/Saturation.lean#L149-L169)
- Source range: L149-L169
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Tower completeness: the full enrichment tower E0 < E1 < E2 < E3
    is a total order on exactly 4 elements. -/
```

## Source Excerpt

```lean
def tower_complete_check : Bool :=
  -- Strict ordering: E0 < E1 < E2 < E3
  let strict :=
    EnrLevel.lt .E0 .E1 &&
    EnrLevel.lt .E1 .E2 &&
    EnrLevel.lt .E2 .E3
  -- Irreflexivity: no level exceeds itself
  let irrefl :=
    !EnrLevel.lt .E0 .E0 &&
    !EnrLevel.lt .E1 .E1 &&
    !EnrLevel.lt .E2 .E2 &&
    !EnrLevel.lt .E3 .E3
  -- Totality: for every pair, one is <= the other
  let total :=
    EnrLevel.le .E0 .E1 &&
    EnrLevel.le .E1 .E2 &&
    EnrLevel.le .E2 .E3 &&
    EnrLevel.le .E0 .E3
  -- Exactly 4 levels
  let count := [EnrLevel.E0, .E1, .E2, .E3].length == 4
  strict && irrefl && total && count
```
