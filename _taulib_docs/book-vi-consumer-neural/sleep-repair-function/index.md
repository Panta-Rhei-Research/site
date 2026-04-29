---
{
  "projection_kind": "taulib_declaration",
  "title": "SleepRepairFunction",
  "permalink": "/verify/taulib/docs/book-vi-consumer-neural/sleep-repair-function/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Consumer.Neural`.",
  "declaration_id": "TauLib.BookVI.Consumer.Neural::SleepRepairFunction",
  "declaration_slug": "sleep-repair-function",
  "kind": "structure",
  "name": "SleepRepairFunction",
  "module_name": "TauLib.BookVI.Consumer.Neural",
  "module_url": "/verify/taulib/docs/book-vi-consumer-neural/",
  "source_line_start": 271,
  "source_line_end": 284,
  "registry_ids": [
    "VI.D90"
  ],
  "related_registry_items": [
    {
      "id": "VI.D90",
      "title": "Sleep Repair Function",
      "url": "/registry/object/VI.D90/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L271-L284",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L271-L284",
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
- Source path: [`TauLib/BookVI/Consumer/Neural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L271-L284)
- Source range: L271-L284
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D90` — Sleep Repair Function

## Immediate Comment / Docstring

```lean
/-- [VI.D90] Sleep Repair Function: dual-lobe repair at specific
    NeuralDefectTower levels, using the sleep lemniscate (VI.P19).
    NREM/SWS (S¹_sleep Lobe 1): Level 1 repair — glymphatic clearance
      removes molecular debris (amyloid-β, metabolic waste).
    REM (S¹_sleep Lobe 2): Level 2 repair — synaptic homeostasis,
      memory consolidation, pruning of weak connections.
    Levels 3–4 are NOT repaired by sleep: circuit and network
    degradation are irreversible once established (repair budget
    does not cover these levels at the rate they accumulate).
    Scope: τ-effective. -/
```

## Source Excerpt

```lean
structure SleepRepairFunction where
  /-- NREM repairs Level 1 (molecular/glymphatic). -/
  nrem_repairs_molecular : Bool := true
  /-- REM repairs Level 2 (synaptic homeostasis). -/
  rem_repairs_synaptic : Bool := true
  /-- Level 3 not repaired by sleep. -/
  no_circuit_repair : Bool := true
  /-- Level 4 not repaired by sleep. -/
  no_network_repair : Bool := true
  /-- Each sleep cycle consumes repair budget (VI.D45). -/
  consumes_repair_budget : Bool := true
  /-- Scope: τ-effective. -/
  scope : String := "tau-effective"
  deriving Repr
```
