---
{
  "projection_kind": "taulib_declaration",
  "title": "EnrichmentBoundary",
  "permalink": "/verify/taulib/docs/book-v-prologue-export-contract/enrichment-boundary/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Prologue.ExportContract`.",
  "declaration_id": "TauLib.BookV.Prologue.ExportContract::EnrichmentBoundary",
  "declaration_slug": "enrichment-boundary",
  "kind": "structure",
  "name": "EnrichmentBoundary",
  "module_name": "TauLib.BookV.Prologue.ExportContract",
  "module_url": "/verify/taulib/docs/book-v-prologue-export-contract/",
  "source_line_start": 184,
  "source_line_end": 191,
  "registry_ids": [
    "V.R12"
  ],
  "related_registry_items": [
    {
      "id": "V.R12",
      "title": "The Book~V--Book~VI boundary",
      "url": "/registry/object/V.R12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/ExportContract.lean#L184-L191",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Prologue.ExportContract",
        "url": "/verify/taulib/docs/book-v-prologue-export-contract/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/ExportContract.lean#L184-L191",
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

- Module: [TauLib.BookV.Prologue.ExportContract](/verify/taulib/docs/book-v-prologue-export-contract/)
- Source path: [`TauLib/BookV/Prologue/ExportContract.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/ExportContract.lean#L184-L191)
- Source range: L184-L191
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.R12` — The Book~V--Book~VI boundary

## Immediate Comment / Docstring

```lean
/-- [V.R12] The enrichment boundary between Book V and Book VI.

    Book V operates at E₁ (physics enrichment):
    - 5 sectors, 5 couplings, 5 primary invariants
    - All structures are τ-effective at E₁

    Book VI begins E₂ (computation/biology enrichment):
    - Computation, Turing machines, life criteria
    - Requires the full E₁ export contract as input -/
```

## Source Excerpt

```lean
structure EnrichmentBoundary where
  /-- Source enrichment level. -/
  source_level : Nat
  /-- Target enrichment level. -/
  target_level : Nat
  /-- Target is one level above source. -/
  step : target_level = source_level + 1
  deriving Repr
```
