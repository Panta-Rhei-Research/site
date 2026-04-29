---
{
  "projection_kind": "taulib_declaration",
  "title": "FMOCoherence",
  "permalink": "/verify/taulib/docs/book-vi-source-source-sector/fmocoherence/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Source.SourceSector`.",
  "declaration_id": "TauLib.BookVI.Source.SourceSector::FMOCoherence",
  "declaration_slug": "fmocoherence",
  "kind": "structure",
  "name": "FMOCoherence",
  "module_name": "TauLib.BookVI.Source.SourceSector",
  "module_url": "/verify/taulib/docs/book-vi-source-source-sector/",
  "source_line_start": 154,
  "source_line_end": 163,
  "registry_ids": [
    "VI.P13"
  ],
  "related_registry_items": [
    {
      "id": "VI.P13",
      "title": "Quantum Coherence in FMO Complex",
      "url": "/registry/object/VI.P13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/SourceSector.lean#L154-L163",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Source.SourceSector",
        "url": "/verify/taulib/docs/book-vi-source-source-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/SourceSector.lean#L154-L163",
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

- Module: [TauLib.BookVI.Source.SourceSector](/verify/taulib/docs/book-vi-source-source-sector/)
- Source path: [`TauLib/BookVI/Source/SourceSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/SourceSector.lean#L154-L163)
- Source range: L154-L163
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.P13` — Quantum Coherence in FMO Complex

## Immediate Comment / Docstring

```lean
/-- [VI.P13] Quantum Coherence in FMO Complex (conjectural).
    The Fenna-Matthews-Olson complex exploits quantum coherence for
    near-unity energy transfer efficiency. Interpreted as
    P vs NP force at E₂ (Book III, Part I): the complex solves
    an NP-hard optimization (exciton routing) in polynomial time
    by exploiting quantum superposition. -/
```

## Source Excerpt

```lean
structure FMOCoherence where
  /-- Transfer efficiency (percent). -/
  efficiency_percent : Nat
  /-- Near-unity: ≥ 95%. -/
  high_efficiency : efficiency_percent ≥ 95
  /-- Connected to P vs NP force (Book III, Part I). -/
  p_vs_np_connection : Bool := true
  /-- Scope: conjectural. -/
  scope : String := "conjectural"
  deriving Repr
```
