---
{
  "projection_kind": "taulib_declaration",
  "title": "HomochiralityUniversality",
  "permalink": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/homochirality-universality/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Persistence.TemporalLemniscate`.",
  "declaration_id": "TauLib.BookVI.Persistence.TemporalLemniscate::HomochiralityUniversality",
  "declaration_slug": "homochirality-universality",
  "kind": "structure",
  "name": "HomochiralityUniversality",
  "module_name": "TauLib.BookVI.Persistence.TemporalLemniscate",
  "module_url": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/",
  "source_line_start": 238,
  "source_line_end": 247,
  "registry_ids": [
    "VI.T43"
  ],
  "related_registry_items": [
    {
      "id": "VI.T43",
      "title": "Homochirality Universality",
      "url": "/registry/object/VI.T43/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L238-L247",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Persistence.TemporalLemniscate",
        "url": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L238-L247",
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

- Module: [TauLib.BookVI.Persistence.TemporalLemniscate](/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/)
- Source path: [`TauLib/BookVI/Persistence/TemporalLemniscate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L238-L247)
- Source range: L238-L247
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T43` — Homochirality Universality

## Immediate Comment / Docstring

```lean
/-- [VI.T43] Homochirality Universality: all persistence-sector entries
    inherit the same chirality from the unique polarity propagation path.
    Since the Parity Bridge (VI.T01) is the unique factorization and the
    chirality seed (VI.D72) has definite sign, every carrier satisfying
    Distinction + SelfDesc must exhibit the same enantiomeric preference. -/
```

## Source Excerpt

```lean
structure HomochiralityUniversality where
  /-- All persistence-sector entries share same chirality. -/
  universal_chirality : Bool := true
  /-- Derived from unique propagation path (VI.L14). -/
  from_unique_path : Bool := true
  /-- Applies to all carriers satisfying Distinction + SelfDesc. -/
  applies_to_all_carriers : Bool := true
  /-- Scope: τ-effective (derived from Parity Bridge chain). -/
  scope : String := "tau_effective"
  deriving Repr
```
