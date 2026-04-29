---
{
  "projection_kind": "taulib_declaration",
  "title": "ExtendedLemniscate",
  "permalink": "/verify/taulib/docs/book-vi-mind-bridge/extended-lemniscate/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Mind.Bridge`.",
  "declaration_id": "TauLib.BookVI.Mind.Bridge::ExtendedLemniscate",
  "declaration_slug": "extended-lemniscate",
  "kind": "structure",
  "name": "ExtendedLemniscate",
  "module_name": "TauLib.BookVI.Mind.Bridge",
  "module_url": "/verify/taulib/docs/book-vi-mind-bridge/",
  "source_line_start": 70,
  "source_line_end": 79,
  "registry_ids": [
    "VI.D70"
  ],
  "related_registry_items": [
    {
      "id": "VI.D70",
      "title": "Extended Lemniscate",
      "url": "/registry/object/VI.D70/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Bridge.lean#L70-L79",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Bridge.lean#L70-L79",
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
- Source path: [`TauLib/BookVI/Mind/Bridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Bridge.lean#L70-L79)
- Source range: L70-L79
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D70` — Extended Lemniscate

## Immediate Comment / Docstring

```lean
/-- [VI.D70] Extended Lemniscate: multi-agent lemniscate.
    When two or more conscious agents share a signal channel,
    the lemniscate extends: each agent contributes a lobe,
    and the shared code traverses lobes bidirectionally.
    π₁(𝕃) = ℤ * ℤ (Book II, Part III) generalizes to multi-agent. -/
```

## Source Excerpt

```lean
structure ExtendedLemniscate where
  /-- Number of agents sharing the lemniscate. -/
  agent_count : Nat
  /-- At least 2 agents. -/
  multi_agent : agent_count ≥ 2
  /-- Signal channel exists between agents. -/
  signal_channel : Bool := true
  /-- Communication is bidirectional. -/
  bidirectional : Bool := true
  deriving Repr
```
