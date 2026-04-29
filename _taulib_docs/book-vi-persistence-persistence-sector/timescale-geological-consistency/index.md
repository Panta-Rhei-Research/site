---
{
  "projection_kind": "taulib_declaration",
  "title": "TimescaleGeologicalConsistency",
  "permalink": "/verify/taulib/docs/book-vi-persistence-persistence-sector/timescale-geological-consistency/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Persistence.PersistenceSector`.",
  "declaration_id": "TauLib.BookVI.Persistence.PersistenceSector::TimescaleGeologicalConsistency",
  "declaration_slug": "timescale-geological-consistency",
  "kind": "structure",
  "name": "TimescaleGeologicalConsistency",
  "module_name": "TauLib.BookVI.Persistence.PersistenceSector",
  "module_url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/",
  "source_line_start": 407,
  "source_line_end": 416,
  "registry_ids": [
    "VI.R27"
  ],
  "related_registry_items": [
    {
      "id": "VI.R27",
      "title": "Geological Consistency",
      "url": "/registry/object/VI.R27/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L407-L416",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Persistence.PersistenceSector",
        "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L407-L416",
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

- Module: [TauLib.BookVI.Persistence.PersistenceSector](/verify/taulib/docs/book-vi-persistence-persistence-sector/)
- Source path: [`TauLib/BookVI/Persistence/PersistenceSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L407-L416)
- Source range: L407-L416
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.R27` — Geological Consistency

## Immediate Comment / Docstring

```lean
/-- [VI.R27] Timescale Geological Consistency: orbit-step → physical-time
    mapping gives ~500 Myr, consistent with geological evidence (3.8–4.1 Gya).
    The logarithmic bound (VI.T45) with characteristic step time ~10⁻¹³ s
    and ~10¹⁵–10²¹ correlated steps gives τ_origin ~ 10²–10⁸ years.
    Scope note: structural bound (τ-effective), physical mapping (remark). -/
```

## Source Excerpt

```lean
structure TimescaleGeologicalConsistency where
  /-- Geological window: ~100–300 Myr. -/
  geological_window_myr : String := "100-300"
  /-- Predicted bound: ~500 Myr. -/
  predicted_bound_myr : String := "500"
  /-- Consistent with observation. -/
  consistent : Bool := true
  /-- Scope: remark (supporting). -/
  scope : String := "tau_effective"
  deriving Repr
```
