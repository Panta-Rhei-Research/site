---
{
  "projection_kind": "taulib_declaration",
  "title": "topo_obstruction_count",
  "permalink": "/verify/taulib/docs/book-iii-bridge-translation-obstruction/topo-obstruction-count/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.TranslationObstruction`.",
  "declaration_id": "TauLib.BookIII.Bridge.TranslationObstruction::topo_obstruction_count",
  "declaration_slug": "topo-obstruction-count",
  "kind": "def",
  "name": "topo_obstruction_count",
  "module_name": "TauLib.BookIII.Bridge.TranslationObstruction",
  "module_url": "/verify/taulib/docs/book-iii-bridge-translation-obstruction/",
  "source_line_start": 153,
  "source_line_end": 157,
  "registry_ids": [
    "III.D92"
  ],
  "related_registry_items": [
    {
      "id": "III.D92",
      "title": "Forbidden Move Obstruction Classes",
      "url": "/registry/object/III.D92/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L153-L157",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.TranslationObstruction",
        "url": "/verify/taulib/docs/book-iii-bridge-translation-obstruction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L153-L157",
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

- Module: [TauLib.BookIII.Bridge.TranslationObstruction](/verify/taulib/docs/book-iii-bridge-translation-obstruction/)
- Source path: [`TauLib/BookIII/Bridge/TranslationObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L153-L157)
- Source range: L153-L157
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D92` — Forbidden Move Obstruction Classes

## Immediate Comment / Docstring

```lean
/-- [III.D92] Count how many obstructions affect topology. -/
```

## Source Excerpt

```lean
def topo_obstruction_count : Nat :=
  let obs := [TranslationObstruction.unbounded_fanout,
              .global_equality, .succinct_circuits,
              .exponential_quantification, .nonlocal_disguise]
  obs.foldl (fun acc o => acc + if move_obstructs_topo o then 1 else 0) 0
```
