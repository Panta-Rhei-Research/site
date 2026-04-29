---
{
  "projection_kind": "taulib_declaration",
  "title": "FarFromEquilibriumRegime",
  "permalink": "/verify/taulib/docs/book-vi-persistence-persistence-sector/far-from-equilibrium-regime/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Persistence.PersistenceSector`.",
  "declaration_id": "TauLib.BookVI.Persistence.PersistenceSector::FarFromEquilibriumRegime",
  "declaration_slug": "far-from-equilibrium-regime",
  "kind": "structure",
  "name": "FarFromEquilibriumRegime",
  "module_name": "TauLib.BookVI.Persistence.PersistenceSector",
  "module_url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/",
  "source_line_start": 193,
  "source_line_end": 202,
  "registry_ids": [
    "VI.D74"
  ],
  "related_registry_items": [
    {
      "id": "VI.D74",
      "title": "Far-From-Equilibrium Regime",
      "url": "/registry/object/VI.D74/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L193-L202",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L193-L202",
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
- Source path: [`TauLib/BookVI/Persistence/PersistenceSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L193-L202)
- Source range: L193-L202
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D74` — Far-From-Equilibrium Regime

## Immediate Comment / Docstring

```lean
/-- [VI.D74] Far-From-Equilibrium Regime: pre-E₂ state where |D_n| >> 0.
    A system in active defect decay, before coherence horizon (V.D89),
    with sustained dissipative energy throughput.
    Cross-ref: V.T62 (geometric decay), V.D89 (coherence horizon). -/
```

## Source Excerpt

```lean
structure FarFromEquilibriumRegime where
  /-- Defect count significantly above zero. -/
  defect_above_zero : Bool := true
  /-- System is dissipative (sustained energy throughput). -/
  dissipative : Bool := true
  /-- Pre-coherence-horizon: defect decay still active. -/
  pre_coherence_horizon : Bool := true
  /-- Scope: τ-effective. -/
  scope : String := "tau_effective"
  deriving Repr
```
