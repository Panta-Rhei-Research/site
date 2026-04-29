---
{
  "projection_kind": "taulib_declaration",
  "title": "SleepDeprivationAccelerates",
  "permalink": "/verify/taulib/docs/book-vi-consumer-neural/sleep-deprivation-accelerates/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Consumer.Neural`.",
  "declaration_id": "TauLib.BookVI.Consumer.Neural::SleepDeprivationAccelerates",
  "declaration_slug": "sleep-deprivation-accelerates",
  "kind": "structure",
  "name": "SleepDeprivationAccelerates",
  "module_name": "TauLib.BookVI.Consumer.Neural",
  "module_url": "/verify/taulib/docs/book-vi-consumer-neural/",
  "source_line_start": 337,
  "source_line_end": 348,
  "registry_ids": [
    "VI.P24"
  ],
  "related_registry_items": [
    {
      "id": "VI.P24",
      "title": "Sleep Deprivation Accelerates Defect Crossing",
      "url": "/registry/object/VI.P24/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L337-L348",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L337-L348",
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
- Source path: [`TauLib/BookVI/Consumer/Neural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L337-L348)
- Source range: L337-L348
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.P24` — Sleep Deprivation Accelerates Defect Crossing

## Immediate Comment / Docstring

```lean
/-- [VI.P24] Sleep Deprivation Accelerates Defect Threshold Crossing.
    Chronic sleep deprivation skips Level 1–2 repair cycles (VI.D90),
    accelerating repair budget exhaustion (VI.D45) at these levels.
    Consequence: the Level 1 defect trajectory crosses the cascade
    threshold earlier, triggering accelerated Level 2 degradation
    via inter-level cascade (VI.T52), consistent with epidemiological
    evidence linking sleep deprivation to increased Alzheimer's risk.
    Scope: τ-effective (structural budget argument; quantitative
    prediction would require empirical rates). -/
```

## Source Excerpt

```lean
structure SleepDeprivationAccelerates where
  /-- Skipped repair cycles → faster budget exhaustion. -/
  budget_exhaustion_accelerated : Bool := true
  /-- Level 1 threshold crossed earlier. -/
  level_1_earlier : Bool := true
  /-- Cascade to Level 2 triggered earlier. -/
  cascade_earlier : Bool := true
  /-- Consistent with Alzheimer's epidemiology. -/
  alzheimers_consistent : Bool := true
  /-- Scope: τ-effective. -/
  scope : String := "tau-effective"
  deriving Repr
```
