---
{
  "projection_kind": "taulib_declaration",
  "title": "TimescaleFromHalfLife",
  "permalink": "/verify/taulib/docs/book-vi-persistence-persistence-sector/timescale-from-half-life/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Persistence.PersistenceSector`.",
  "declaration_id": "TauLib.BookVI.Persistence.PersistenceSector::TimescaleFromHalfLife",
  "declaration_slug": "timescale-from-half-life",
  "kind": "structure",
  "name": "TimescaleFromHalfLife",
  "module_name": "TauLib.BookVI.Persistence.PersistenceSector",
  "module_url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/",
  "source_line_start": 381,
  "source_line_end": 390,
  "registry_ids": [
    "VI.T45"
  ],
  "related_registry_items": [
    {
      "id": "VI.T45",
      "title": "Timescale From Half-Life",
      "url": "/registry/object/VI.T45/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L381-L390",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L381-L390",
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
- Source path: [`TauLib/BookVI/Persistence/PersistenceSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L381-L390)
- Source range: L381-L390
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T45` — Timescale From Half-Life

## Immediate Comment / Docstring

```lean
/-- [VI.T45] Timescale From Half-Life Theorem:
    T_abio ≤ n₁/₂ · ⌈ln(N/threshold)⌉.
    Proof: geometric decay rate (1−ι_τ)^n with half-life n₁/₂ gives
    |D_n| = N·(1−ι_τ)^n. Threshold crossing at C(n₀) = N − |D_{n₀}| ≥ 8
    requires |D_{n₀}| ≤ N − 8, giving n₀ ≤ n₁/₂ · ⌈log₂(N/8)⌉. -/
```

## Source Excerpt

```lean
structure TimescaleFromHalfLife where
  /-- Decay factor per orbit step. -/
  decay_factor : String := "1 - iota_tau"
  /-- Half-life n₁/₂ ≈ 1.66 orbit steps (V.D90). -/
  half_life : String := "1.66"
  /-- Upper bound is logarithmic in initial defect count. -/
  logarithmic_bound : Bool := true
  /-- Scope: τ-effective. -/
  scope : String := "tau_effective"
  deriving Repr
```
