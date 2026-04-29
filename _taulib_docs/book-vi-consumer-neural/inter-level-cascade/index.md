---
{
  "projection_kind": "taulib_declaration",
  "title": "InterLevelCascade",
  "permalink": "/verify/taulib/docs/book-vi-consumer-neural/inter-level-cascade/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Consumer.Neural`.",
  "declaration_id": "TauLib.BookVI.Consumer.Neural::InterLevelCascade",
  "declaration_slug": "inter-level-cascade",
  "kind": "structure",
  "name": "InterLevelCascade",
  "module_name": "TauLib.BookVI.Consumer.Neural",
  "module_url": "/verify/taulib/docs/book-vi-consumer-neural/",
  "source_line_start": 203,
  "source_line_end": 214,
  "registry_ids": [
    "VI.T52"
  ],
  "related_registry_items": [
    {
      "id": "VI.T52",
      "title": "Inter-Level Cascade",
      "url": "/registry/object/VI.T52/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L203-L214",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L203-L214",
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
- Source path: [`TauLib/BookVI/Consumer/Neural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L203-L214)
- Source range: L203-L214
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T52` — Inter-Level Cascade

## Immediate Comment / Docstring

```lean
/-- [VI.T52] Inter-Level Cascade Theorem.
    Level i defect accumulation beyond threshold triggers accelerated
    defect accumulation at Level i+1 (upward cascade). Proof:
    (1) Molecular aggregates (Level 1) impair synaptic transmission
    (Level 2) by disrupting vesicle trafficking and receptor function.
    (2) Synaptic loss (Level 2) degrades circuit integrity (Level 3)
    by removing edges from the τ³-computer subgraph.
    (3) Circuit degradation (Level 3) fragments the global network
    (Level 4) by disconnecting integrative pathways.
    Each transition is monotone: more Level i defect → more Level i+1
    defect. The cascade is unidirectional (upward only).
    Scope: τ-effective. -/
```

## Source Excerpt

```lean
structure InterLevelCascade where
  /-- Level 1 → Level 2 cascade. -/
  molecular_to_synaptic : Bool := true
  /-- Level 2 → Level 3 cascade. -/
  synaptic_to_circuit : Bool := true
  /-- Level 3 → Level 4 cascade. -/
  circuit_to_network : Bool := true
  /-- Cascade is unidirectional (upward). -/
  upward_only : Bool := true
  /-- Scope: τ-effective. -/
  scope : String := "tau-effective"
  deriving Repr
```
