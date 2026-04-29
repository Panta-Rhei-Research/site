---
{
  "projection_kind": "taulib_declaration",
  "title": "AutoimmunityFailure",
  "permalink": "/verify/taulib/docs/book-vi-consumer-immune/autoimmunity-failure/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Consumer.Immune`.",
  "declaration_id": "TauLib.BookVI.Consumer.Immune::AutoimmunityFailure",
  "declaration_slug": "autoimmunity-failure",
  "kind": "structure",
  "name": "AutoimmunityFailure",
  "module_name": "TauLib.BookVI.Consumer.Immune",
  "module_url": "/verify/taulib/docs/book-vi-consumer-immune/",
  "source_line_start": 61,
  "source_line_end": 76,
  "registry_ids": [
    "VI.T28"
  ],
  "related_registry_items": [
    {
      "id": "VI.T28",
      "title": "Autoimmunity as Distinction Failure",
      "url": "/registry/object/VI.T28/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Immune.lean#L61-L76",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Consumer.Immune",
        "url": "/verify/taulib/docs/book-vi-consumer-immune/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Immune.lean#L61-L76",
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

- Module: [TauLib.BookVI.Consumer.Immune](/verify/taulib/docs/book-vi-consumer-immune/)
- Source path: [`TauLib/BookVI/Consumer/Immune.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Immune.lean#L61-L76)
- Source range: L61-L76
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T28` — Autoimmunity as Distinction Failure

## Immediate Comment / Docstring

```lean
/-- [VI.T28] Autoimmunity as Distinction Failure.
    Five failure modes, one for each condition of VI.D04:
    (1) Clopen violation — boundary leakage
    (2) Refinement violation — tolerance breakdown
    (3) Stability violation — stochastic misfire
    (4) Law violation — regulatory T-cell deficiency
    (5) Equivariance violation — molecular mimicry
    Each autoimmune disease maps to one or more failure modes. -/
```

## Source Excerpt

```lean
structure AutoimmunityFailure where
  /-- Total failure modes. -/
  failure_modes : Nat
  /-- Exactly 5 (one per Distinction condition). -/
  modes_eq : failure_modes = 5
  /-- (1) Clopen boundary leakage. -/
  clopen_violation : Bool := true
  /-- (2) Refinement/tolerance breakdown. -/
  refinement_violation : Bool := true
  /-- (3) Stability/stochastic misfire. -/
  stability_violation : Bool := true
  /-- (4) Law/regulatory T-cell deficiency. -/
  law_violation : Bool := true
  /-- (5) Equivariance/molecular mimicry. -/
  equivariance_violation : Bool := true
  deriving Repr
```
