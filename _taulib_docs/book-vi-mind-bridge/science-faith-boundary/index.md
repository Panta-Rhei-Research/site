---
{
  "projection_kind": "taulib_declaration",
  "title": "ScienceFaithBoundary",
  "permalink": "/verify/taulib/docs/book-vi-mind-bridge/science-faith-boundary/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Mind.Bridge`.",
  "declaration_id": "TauLib.BookVI.Mind.Bridge::ScienceFaithBoundary",
  "declaration_slug": "science-faith-boundary",
  "kind": "structure",
  "name": "ScienceFaithBoundary",
  "module_name": "TauLib.BookVI.Mind.Bridge",
  "module_url": "/verify/taulib/docs/book-vi-mind-bridge/",
  "source_line_start": 196,
  "source_line_end": 203,
  "registry_ids": [
    "VI.R25"
  ],
  "related_registry_items": [
    {
      "id": "VI.R25",
      "title": "Principled Science-Faith Boundary",
      "url": "/registry/object/VI.R25/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Bridge.lean#L196-L203",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Mind.Bridge",
        "url": "/verify/taulib/docs/book-vi-mind-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Bridge.lean#L196-L203",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookVI.Mind.Bridge](/verify/taulib/docs/book-vi-mind-bridge/)
- Source path: [`TauLib/BookVI/Mind/Bridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Bridge.lean#L196-L203)
- Source range: L196-L203
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.R25` — Principled Science-Faith Boundary

## Immediate Comment / Docstring

```lean
/-- [VI.R25] Principled Science-Faith Boundary.
    The boundary between science and faith is structurally located
    at the ω-germ: everything inside finite diagrams is science
    (structurally decidable), the ω-germ question is faith
    (non-diagrammatic). This is neither agnosticism (no position)
    nor fideism (faith overrides reason). -/
```

## Source Excerpt

```lean
structure ScienceFaithBoundary where
  /-- Boundary is structurally located. -/
  structurally_located : Bool := true
  /-- Not agnosticism. -/
  not_agnosticism : Bool := true
  /-- Not fideism. -/
  not_fideism : Bool := true
  deriving Repr
```
