---
{
  "projection_kind": "taulib_declaration",
  "title": "AttractorExistence",
  "permalink": "/verify/taulib/docs/book-vi-persistence-persistence-sector/attractor-existence/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Persistence.PersistenceSector`.",
  "declaration_id": "TauLib.BookVI.Persistence.PersistenceSector::AttractorExistence",
  "declaration_slug": "attractor-existence",
  "kind": "structure",
  "name": "AttractorExistence",
  "module_name": "TauLib.BookVI.Persistence.PersistenceSector",
  "module_url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/",
  "source_line_start": 296,
  "source_line_end": 311,
  "registry_ids": [
    "VI.T44"
  ],
  "related_registry_items": [
    {
      "id": "VI.T44",
      "title": "Attractor Existence",
      "url": "/registry/object/VI.T44/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L296-L311",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L296-L311",
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
- Source path: [`TauLib/BookVI/Persistence/PersistenceSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L296-L311)
- Source range: L296-L311
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T44` — Attractor Existence

## Immediate Comment / Docstring

```lean
/-- [VI.T44] Attractor Existence Theorem: under 3 conditions,
    Distinction+SelfDesc basin entry is forced.
    C1: finite defect budget (V.T60)
    C2: polarity seed (VI.T01)
    C3: temporal stability (VI.D25)
    Proof: C(n) increases monotonically (VI.L15), threshold is finite (VI.D76),
    so ∃ n₀: C(n₀) ≥ threshold; SelfDesc closure (VI.T03) makes basin absorbing. -/
```

## Source Excerpt

```lean
structure AttractorExistence where
  /-- Number of structural conditions. -/
  condition_count : Nat
  /-- Exactly 3 conditions. -/
  conditions_eq : condition_count = 3
  /-- C1: Finite defect budget (V.T60). -/
  finite_budget : Bool := true
  /-- C2: Polarity seed exists (VI.T01). -/
  polarity_seed : Bool := true
  /-- C3: Temporal stability predicate satisfiable (VI.D25). -/
  temporal_stability : Bool := true
  /-- Basin entry is forced (threshold crossing guaranteed). -/
  entry_forced : Bool := true
  /-- Scope: τ-effective. -/
  scope : String := "tau_effective"
  deriving Repr
```
