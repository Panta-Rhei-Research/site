---
{
  "projection_kind": "taulib_declaration",
  "title": "CosmicStackAPI",
  "permalink": "/verify/taulib/docs/book-v-temporal-cosmic-api/cosmic-stack-api-l126/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Temporal.CosmicAPI`.",
  "declaration_id": "TauLib.BookV.Temporal.CosmicAPI::CosmicStackAPI",
  "declaration_slug": "cosmic-stack-api-l126",
  "kind": "structure",
  "name": "CosmicStackAPI",
  "module_name": "TauLib.BookV.Temporal.CosmicAPI",
  "module_url": "/verify/taulib/docs/book-v-temporal-cosmic-api/",
  "source_line_start": 126,
  "source_line_end": 135,
  "registry_ids": [
    "V.D40"
  ],
  "related_registry_items": [
    {
      "id": "V.D40",
      "title": "Cosmic Stack API",
      "url": "/registry/object/V.D40/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/CosmicAPI.lean#L126-L135",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.CosmicAPI",
        "url": "/verify/taulib/docs/book-v-temporal-cosmic-api/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/CosmicAPI.lean#L126-L135",
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

- Module: [TauLib.BookV.Temporal.CosmicAPI](/verify/taulib/docs/book-v-temporal-cosmic-api/)
- Source path: [`TauLib/BookV/Temporal/CosmicAPI.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/CosmicAPI.lean#L126-L135)
- Source range: L126-L135
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D40` — Cosmic Stack API

## Immediate Comment / Docstring

```lean
/-- [V.D40] Cosmic Stack API summary: counts of total items,
    τ-effective items, and conjectural items. -/
```

## Source Excerpt

```lean
structure CosmicStackAPI where
  /-- Total number of API items. -/
  total_count : Nat
  /-- Number of τ-effective items. -/
  tau_effective_count : Nat
  /-- Number of conjectural items. -/
  conjectural_count : Nat
  /-- Scope partition: τ-effective + conjectural = total. -/
  scope_partition : tau_effective_count + conjectural_count = total_count
  deriving Repr
```
