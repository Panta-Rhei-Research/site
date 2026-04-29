---
{
  "projection_kind": "taulib_declaration",
  "title": "TemporalLemniscate",
  "permalink": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/temporal-lemniscate/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Persistence.TemporalLemniscate`.",
  "declaration_id": "TauLib.BookVI.Persistence.TemporalLemniscate::TemporalLemniscate",
  "declaration_slug": "temporal-lemniscate",
  "kind": "structure",
  "name": "TemporalLemniscate",
  "module_name": "TauLib.BookVI.Persistence.TemporalLemniscate",
  "module_url": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/",
  "source_line_start": 38,
  "source_line_end": 49,
  "registry_ids": [
    "VI.D27"
  ],
  "related_registry_items": [
    {
      "id": "VI.D27",
      "title": "Temporal Lemniscate",
      "url": "/registry/object/VI.D27/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L38-L49",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Persistence.TemporalLemniscate",
        "url": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L38-L49",
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

- Module: [TauLib.BookVI.Persistence.TemporalLemniscate](/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/)
- Source path: [`TauLib/BookVI/Persistence/TemporalLemniscate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L38-L49)
- Source range: L38-L49
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D27` — Temporal Lemniscate

## Immediate Comment / Docstring

```lean
/-- [VI.D27] Temporal Lemniscate L_T = S¹_act ∨ S¹_rest.
    The persistence Life loop projected onto τ¹ traces a figure-eight:
    active phase (S¹_act) and rest phase (S¹_rest).
    Inherits lemniscate topology from L = S¹ ∨ S¹ (Book II, Part III). -/
```

## Source Excerpt

```lean
structure TemporalLemniscate where
  /-- Number of lobes. -/
  lobe_count : Nat
  /-- Exactly 2 lobes. -/
  lobes_eq : lobe_count = 2
  /-- Active-phase lobe. -/
  active_lobe : String := "S1_active"
  /-- Rest-phase lobe. -/
  rest_lobe : String := "S1_rest"
  /-- Winding number on τ¹. -/
  winding_number : Nat := 1
  deriving Repr
```
