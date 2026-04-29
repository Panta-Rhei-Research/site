---
{
  "projection_kind": "taulib_declaration",
  "title": "NeurodegenerativeMapping",
  "permalink": "/verify/taulib/docs/book-vi-consumer-neural/neurodegenerative-mapping/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Consumer.Neural`.",
  "declaration_id": "TauLib.BookVI.Consumer.Neural::NeurodegenerativeMapping",
  "declaration_slug": "neurodegenerative-mapping",
  "kind": "structure",
  "name": "NeurodegenerativeMapping",
  "module_name": "TauLib.BookVI.Consumer.Neural",
  "module_url": "/verify/taulib/docs/book-vi-consumer-neural/",
  "source_line_start": 172,
  "source_line_end": 183,
  "registry_ids": [
    "VI.D89"
  ],
  "related_registry_items": [
    {
      "id": "VI.D89",
      "title": "Neurodegenerative Disease Mapping",
      "url": "/registry/object/VI.D89/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L172-L183",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L172-L183",
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
- Source path: [`TauLib/BookVI/Consumer/Neural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L172-L183)
- Source range: L172-L183
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D89` — Neurodegenerative Disease Mapping

## Immediate Comment / Docstring

```lean
/-- [VI.D89] Neurodegenerative Disease Mapping: each major
    neurodegenerative disease is characterized by a dominant
    defect level at which repair budget exhaustion occurs first.
    Alzheimer's: Level 1 dominant (amyloid/tau aggregation).
    Parkinson's: Level 3 dominant (dopaminergic circuit loss).
    ALS: Level 3 dominant (motor neuron circuit failure).
    Huntington's: Level 1 dominant (polyQ aggregation).
    Normal aging: all levels degrade but none crosses threshold
    before organismal Hayflick limit.
    Scope: τ-effective (structural classification; protein names
    appear in documentation only, not in formal conditions). -/
```

## Source Excerpt

```lean
structure NeurodegenerativeMapping where
  /-- Alzheimer's: molecular level dominant. -/
  alzheimers_level : NeuralDefectLevel := .molecular
  /-- Parkinson's: circuit level dominant. -/
  parkinsons_level : NeuralDefectLevel := .circuit
  /-- ALS: circuit level dominant. -/
  als_level : NeuralDefectLevel := .circuit
  /-- Huntington's: molecular level dominant. -/
  huntingtons_level : NeuralDefectLevel := .molecular
  /-- Scope: τ-effective. -/
  scope : String := "tau-effective"
  deriving Repr
```
