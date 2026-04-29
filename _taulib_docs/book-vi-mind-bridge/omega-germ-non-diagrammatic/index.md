---
{
  "projection_kind": "taulib_declaration",
  "title": "OmegaGermNonDiagrammatic",
  "permalink": "/verify/taulib/docs/book-vi-mind-bridge/omega-germ-non-diagrammatic/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Mind.Bridge`.",
  "declaration_id": "TauLib.BookVI.Mind.Bridge::OmegaGermNonDiagrammatic",
  "declaration_slug": "omega-germ-non-diagrammatic",
  "kind": "structure",
  "name": "OmegaGermNonDiagrammatic",
  "module_name": "TauLib.BookVI.Mind.Bridge",
  "module_url": "/verify/taulib/docs/book-vi-mind-bridge/",
  "source_line_start": 172,
  "source_line_end": 177,
  "registry_ids": [
    "VI.L13"
  ],
  "related_registry_items": [
    {
      "id": "VI.L13",
      "title": "ω-Germ Cannot Be Resolved Diagrammatically",
      "url": "/registry/object/VI.L13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Bridge.lean#L172-L177",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Bridge.lean#L172-L177",
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
- Source path: [`TauLib/BookVI/Mind/Bridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Bridge.lean#L172-L177)
- Source range: L172-L177
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.L13` — ω-Germ Cannot Be Resolved Diagrammatically

## Immediate Comment / Docstring

```lean
/-- [VI.L13] ω-Germ Non-Diagrammatic.
    The ω-germ question ("What is the ultimate ground of structure?")
    is non-diagrammatic: it cannot be resolved within any finite
    diagram of Category τ. It concerns existence, not structure.
    Book I, Part I: K0–K6 axioms specify initial/terminal but
    the ω-germ as profinite limit transcends finite diagrams. -/
```

## Source Excerpt

```lean
structure OmegaGermNonDiagrammatic where
  /-- The question is non-diagrammatic. -/
  non_diagrammatic : Bool := true
  /-- Concerns existence, not structure. -/
  existence_not_structure : Bool := true
  deriving Repr
```
