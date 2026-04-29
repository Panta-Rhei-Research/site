---
{
  "projection_kind": "taulib_declaration",
  "title": "move_obstructs_arith",
  "permalink": "/verify/taulib/docs/book-iii-bridge-translation-obstruction/move-obstructs-arith/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.TranslationObstruction`.",
  "declaration_id": "TauLib.BookIII.Bridge.TranslationObstruction::move_obstructs_arith",
  "declaration_slug": "move-obstructs-arith",
  "kind": "def",
  "name": "move_obstructs_arith",
  "module_name": "TauLib.BookIII.Bridge.TranslationObstruction",
  "module_url": "/verify/taulib/docs/book-iii-bridge-translation-obstruction/",
  "source_line_start": 128,
  "source_line_end": 134,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L128-L134",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L128-L134",
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
- Source path: [`TauLib/BookIII/Bridge/TranslationObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L128-L134)
- Source range: L128-L134
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D92` — Forbidden Move Obstruction Classes

## Immediate Comment / Docstring

```lean
/-- [III.D92] Does this move obstruct arithmetic translation? -/
```

## Source Excerpt

```lean
def move_obstructs_arith (obs : TranslationObstruction) : Bool :=
  match obs with
  | .unbounded_fanout => true          -- CRT decomposition unbounded
  | .global_equality => false          -- arithmetic uses local equality
  | .succinct_circuits => true         -- blocks polynomial evaluation
  | .exponential_quantification => true -- blocks bounded arithmetic
  | .nonlocal_disguise => false        -- arithmetic uses canonical form
```
