---
{
  "projection_kind": "taulib_declaration",
  "title": "SleepLemniscate",
  "permalink": "/verify/taulib/docs/book-vi-consumer-neural/sleep-lemniscate/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Consumer.Neural`.",
  "declaration_id": "TauLib.BookVI.Consumer.Neural::SleepLemniscate",
  "declaration_slug": "sleep-lemniscate",
  "kind": "structure",
  "name": "SleepLemniscate",
  "module_name": "TauLib.BookVI.Consumer.Neural",
  "module_url": "/verify/taulib/docs/book-vi-consumer-neural/",
  "source_line_start": 80,
  "source_line_end": 91,
  "registry_ids": [
    "VI.P19"
  ],
  "related_registry_items": [
    {
      "id": "VI.P19",
      "title": "Sleep as Temporal Lemniscate Second Lobe",
      "url": "/registry/object/VI.P19/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L80-L91",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Consumer.Neural",
        "url": "/verify/taulib/docs/book-vi-consumer-neural/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L80-L91",
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

- Module: [TauLib.BookVI.Consumer.Neural](/verify/taulib/docs/book-vi-consumer-neural/)
- Source path: [`TauLib/BookVI/Consumer/Neural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L80-L91)
- Source range: L80-L91
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.P19` — Sleep as Temporal Lemniscate Second Lobe

## Immediate Comment / Docstring

```lean
/-- [VI.P19] Sleep as Temporal Lemniscate Second Lobe.
    The temporal lemniscate L_T = S¹ ∨ S¹ (Book VI, Part 2)
    has two lobes: wakefulness (active processing) and sleep
    (consolidation/pruning). Circadian rhythm is the orbit
    traversing both lobes. -/
```

## Source Excerpt

```lean
structure SleepLemniscate where
  /-- Number of lemniscate lobes. -/
  lobe_count : Nat
  /-- Exactly 2 lobes. -/
  count_eq : lobe_count = 2
  /-- Lobe 1: wakefulness. -/
  wake_lobe : Bool := true
  /-- Lobe 2: sleep. -/
  sleep_lobe : Bool := true
  /-- Linked to circadian rhythm (Part 2). -/
  circadian_link : Bool := true
  deriving Repr
```
