---
{
  "projection_kind": "taulib_declaration",
  "title": "QGApproach",
  "permalink": "/verify/taulib/docs/book-v-orthodox-other-approaches/qgapproach/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.Orthodox.OtherApproaches`.",
  "declaration_id": "TauLib.BookV.Orthodox.OtherApproaches::QGApproach",
  "declaration_slug": "qgapproach",
  "kind": "inductive",
  "name": "QGApproach",
  "module_name": "TauLib.BookV.Orthodox.OtherApproaches",
  "module_url": "/verify/taulib/docs/book-v-orthodox-other-approaches/",
  "source_line_start": 71,
  "source_line_end": 86,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L71-L86",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.OtherApproaches",
        "url": "/verify/taulib/docs/book-v-orthodox-other-approaches/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L71-L86",
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

- Module: [TauLib.BookV.Orthodox.OtherApproaches](/verify/taulib/docs/book-v-orthodox-other-approaches/)
- Source path: [`TauLib/BookV/Orthodox/OtherApproaches.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L71-L86)
- Source range: L71-L86
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Classification of a quantum gravity approach. -/
```

## Source Excerpt

```lean
inductive QGApproach where
  /-- String theory / M-theory. -/
  | StringTheory
  /-- Loop quantum gravity. -/
  | LQG
  /-- Causal dynamical triangulations. -/
  | CDT
  /-- Causal set theory. -/
  | CausalSets
  /-- Twistor theory. -/
  | Twistors
  /-- Non-commutative geometry (Connes). -/
  | NCG
  /-- Category tau. -/
  | Tau
  deriving Repr, DecidableEq, BEq
```
