---
{
  "projection_kind": "taulib_declaration",
  "title": "NeurodegenerationHayflickCrossing",
  "permalink": "/verify/taulib/docs/book-vi-consumer-neural/neurodegeneration-hayflick-crossing/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Consumer.Neural`.",
  "declaration_id": "TauLib.BookVI.Consumer.Neural::NeurodegenerationHayflickCrossing",
  "declaration_slug": "neurodegeneration-hayflick-crossing",
  "kind": "structure",
  "name": "NeurodegenerationHayflickCrossing",
  "module_name": "TauLib.BookVI.Consumer.Neural",
  "module_url": "/verify/taulib/docs/book-vi-consumer-neural/",
  "source_line_start": 408,
  "source_line_end": 421,
  "registry_ids": [
    "VI.T54"
  ],
  "related_registry_items": [
    {
      "id": "VI.T54",
      "title": "Neurodegeneration = Hayflick Crossing",
      "url": "/registry/object/VI.T54/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L408-L421",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L408-L421",
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
- Source path: [`TauLib/BookVI/Consumer/Neural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L408-L421)
- Source range: L408-L421
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T54` — Neurodegeneration = Hayflick Crossing

## Immediate Comment / Docstring

```lean
/-- [VI.T54] Neurodegeneration = Hayflick Crossing.
    A neurodegenerative disease occurs when a specific level's
    Hayflick bound H_i is exhausted before the organismal Hayflick
    limit: the repair budget at Level i is depleted, defects
    accumulate past the cascade threshold, and cognitive function
    degrades irreversibly.
    Alzheimer's: H₁ exhausted first (molecular repair depleted).
    Parkinson's: H₃ exhausted first (circuit repair depleted).
    Normal aging: all H_i > organismal limit (no level crosses first).
    The neural Hayflick bound is a sector-specific instance of the
    universal defect exhaustion (V.T62/VI.P16), with (1−ι_τ)^n
    governing the baseline.
    Scope: τ-effective. -/
```

## Source Excerpt

```lean
structure NeurodegenerationHayflickCrossing where
  /-- Disease = specific level Hayflick bound exhausted. -/
  disease_is_level_crossing : Bool := true
  /-- Alzheimer's = H₁ first. -/
  alzheimers_h1 : Bool := true
  /-- Parkinson's = H₃ first. -/
  parkinsons_h3 : Bool := true
  /-- Normal aging: no H_i crossed before organismal limit. -/
  normal_aging_safe : Bool := true
  /-- Sector-specific instance of V.T62/VI.P16. -/
  specializes_universal : Bool := true
  /-- Scope: τ-effective. -/
  scope : String := "tau-effective"
  deriving Repr
```
