---
{
  "projection_kind": "taulib_declaration",
  "title": "TranslationObstruction",
  "permalink": "/verify/taulib/docs/book-iii-bridge-translation-obstruction/translation-obstruction/",
  "summary_short": "`inductive` declaration in `TauLib.BookIII.Bridge.TranslationObstruction`.",
  "declaration_id": "TauLib.BookIII.Bridge.TranslationObstruction::TranslationObstruction",
  "declaration_slug": "translation-obstruction",
  "kind": "inductive",
  "name": "TranslationObstruction",
  "module_name": "TauLib.BookIII.Bridge.TranslationObstruction",
  "module_url": "/verify/taulib/docs/book-iii-bridge-translation-obstruction/",
  "source_line_start": 59,
  "source_line_end": 65,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L59-L65",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L59-L65",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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
- Source path: [`TauLib/BookIII/Bridge/TranslationObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L59-L65)
- Source range: L59-L65
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Forbidden move type (mirrors ForbiddenMoves.lean). -/
```

## Source Excerpt

```lean
inductive TranslationObstruction where
  | unbounded_fanout : TranslationObstruction
  | global_equality : TranslationObstruction
  | succinct_circuits : TranslationObstruction
  | exponential_quantification : TranslationObstruction
  | nonlocal_disguise : TranslationObstruction
  deriving Repr, DecidableEq, BEq
```
