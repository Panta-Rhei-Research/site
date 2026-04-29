---
{
  "projection_kind": "taulib_declaration",
  "title": "topo_obstruction_4",
  "permalink": "/verify/taulib/docs/book-iii-bridge-translation-obstruction/topo-obstruction-4/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Bridge.TranslationObstruction`.",
  "declaration_id": "TauLib.BookIII.Bridge.TranslationObstruction::topo_obstruction_4",
  "declaration_slug": "topo-obstruction-4",
  "kind": "theorem",
  "name": "topo_obstruction_4",
  "module_name": "TauLib.BookIII.Bridge.TranslationObstruction",
  "module_url": "/verify/taulib/docs/book-iii-bridge-translation-obstruction/",
  "source_line_start": 246,
  "source_line_end": 247,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L246-L247",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L246-L247",
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

- Module: [TauLib.BookIII.Bridge.TranslationObstruction](/verify/taulib/docs/book-iii-bridge-translation-obstruction/)
- Source path: [`TauLib/BookIII/Bridge/TranslationObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L246-L247)
- Source range: L246-L247
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D92` — Forbidden Move Obstruction Classes

## Immediate Comment / Docstring

```lean
/-- [III.D92] Topology has 4 obstruction classes. -/
```

## Source Excerpt

```lean
theorem topo_obstruction_4 :
    topo_obstruction_count = 4 := by native_decide
```
