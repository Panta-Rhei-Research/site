---
{
  "projection_kind": "taulib_declaration",
  "title": "ConsumerMixerUniqueness",
  "permalink": "/verify/taulib/docs/book-vi-sectors-life-loop/consumer-mixer-uniqueness/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Sectors.LifeLoop`.",
  "declaration_id": "TauLib.BookVI.Sectors.LifeLoop::ConsumerMixerUniqueness",
  "declaration_slug": "consumer-mixer-uniqueness",
  "kind": "structure",
  "name": "ConsumerMixerUniqueness",
  "module_name": "TauLib.BookVI.Sectors.LifeLoop",
  "module_url": "/verify/taulib/docs/book-vi-sectors-life-loop/",
  "source_line_start": 85,
  "source_line_end": 89,
  "registry_ids": [
    "VI.T06"
  ],
  "related_registry_items": [
    {
      "id": "VI.T06",
      "title": "Consumer Mixer Uniqueness",
      "url": "/registry/object/VI.T06/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/LifeLoop.lean#L85-L89",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Sectors.LifeLoop",
        "url": "/verify/taulib/docs/book-vi-sectors-life-loop/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/LifeLoop.lean#L85-L89",
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

- Module: [TauLib.BookVI.Sectors.LifeLoop](/verify/taulib/docs/book-vi-sectors-life-loop/)
- Source path: [`TauLib/BookVI/Sectors/LifeLoop.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/LifeLoop.lean#L85-L89)
- Source range: L85-L89
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T06` — Consumer Mixer Uniqueness

## Immediate Comment / Docstring

```lean
/-- [VI.T06] Consumer Mixer Uniqueness: exactly 1 admissible mixer on fiber pair. -/
```

## Source Excerpt

```lean
structure ConsumerMixerUniqueness where
  mixer_count : Nat
  unique : mixer_count = 1
  fiber_pair : Bool := true
  deriving Repr
```
