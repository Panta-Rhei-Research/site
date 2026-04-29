---
{
  "projection_kind": "taulib_declaration",
  "title": "SleepConsolidatesLevels12",
  "permalink": "/verify/taulib/docs/book-vi-consumer-neural/sleep-consolidates-levels12/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Consumer.Neural`.",
  "declaration_id": "TauLib.BookVI.Consumer.Neural::SleepConsolidatesLevels12",
  "declaration_slug": "sleep-consolidates-levels12",
  "kind": "structure",
  "name": "SleepConsolidatesLevels12",
  "module_name": "TauLib.BookVI.Consumer.Neural",
  "module_url": "/verify/taulib/docs/book-vi-consumer-neural/",
  "source_line_start": 305,
  "source_line_end": 314,
  "registry_ids": [
    "VI.T53"
  ],
  "related_registry_items": [
    {
      "id": "VI.T53",
      "title": "Sleep Consolidates Levels 1-2",
      "url": "/registry/object/VI.T53/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L305-L314",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L305-L314",
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
- Source path: [`TauLib/BookVI/Consumer/Neural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L305-L314)
- Source range: L305-L314
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T53` — Sleep Consolidates Levels 1-2

## Immediate Comment / Docstring

```lean
/-- [VI.T53] Sleep Consolidates Levels 1–2 Defects.
    The sleep lobe of the neural temporal lemniscate (VI.P19)
    implements defect consolidation specifically at Levels 1 and 2
    of the NeuralDefectTower (VI.D88).
    Proof: (1) NREM/SWS activates glymphatic clearance, which
    removes Level 1 molecular debris (amyloid-β, tau oligomers,
    metabolic waste). (2) REM activates synaptic homeostasis
    (Tononi–Cirelli downscaling), which maintains Level 2 synaptic
    integrity by pruning overfit connections. (3) Levels 3–4 operate
    on timescales (years–decades) that individual sleep cycles
    cannot address: circuit and network degradation accumulate
    irreversibly under the repair budget constraint (VI.D45).
    Scope: τ-effective. -/
```

## Source Excerpt

```lean
structure SleepConsolidatesLevels12 where
  /-- NREM → Level 1 glymphatic repair. -/
  nrem_level_1 : Bool := true
  /-- REM → Level 2 synaptic homeostasis. -/
  rem_level_2 : Bool := true
  /-- Levels 3–4 not addressed by sleep. -/
  levels_3_4_excluded : Bool := true
  /-- Scope: τ-effective. -/
  scope : String := "tau-effective"
  deriving Repr
```
