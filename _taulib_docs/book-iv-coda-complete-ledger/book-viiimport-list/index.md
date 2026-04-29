---
{
  "projection_kind": "taulib_declaration",
  "title": "BookVIIImportList",
  "permalink": "/verify/taulib/docs/book-iv-coda-complete-ledger/book-viiimport-list/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Coda.CompleteLedger`.",
  "declaration_id": "TauLib.BookIV.Coda.CompleteLedger::BookVIIImportList",
  "declaration_slug": "book-viiimport-list",
  "kind": "structure",
  "name": "BookVIIImportList",
  "module_name": "TauLib.BookIV.Coda.CompleteLedger",
  "module_url": "/verify/taulib/docs/book-iv-coda-complete-ledger/",
  "source_line_start": 264,
  "source_line_end": 275,
  "registry_ids": [
    "IV.D245"
  ],
  "related_registry_items": [
    {
      "id": "IV.D245",
      "title": "Book VII import list",
      "url": "/registry/object/IV.D245/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L264-L275",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Coda.CompleteLedger",
        "url": "/verify/taulib/docs/book-iv-coda-complete-ledger/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L264-L275",
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

- Module: [TauLib.BookIV.Coda.CompleteLedger](/verify/taulib/docs/book-iv-coda-complete-ledger/)
- Source path: [`TauLib/BookIV/Coda/CompleteLedger.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L264-L275)
- Source range: L264-L275
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D245` — Book VII import list

## Immediate Comment / Docstring

```lean
/-- [IV.D245] Book VII Import List: what Book IV exports to Book VII.

    Book VII (Categorical Metaphysics) receives:
    - The ontic/non-ontic ontological framework
    - The self-enrichment claim (tau^3 enriched over itself)
    - The deterministic arrow of time (S_ref monotonicity)
    - UV finiteness as metaphysical claim (no infinities in nature)
    - The "laws as structure" thesis -/
```

## Source Excerpt

```lean
structure BookVIIImportList where
  /-- Ontic/non-ontic framework. -/
  ontological_framework : Bool := true
  /-- Self-enrichment claim. -/
  self_enrichment : Bool := true
  /-- Deterministic arrow of time. -/
  arrow_of_time : Bool := true
  /-- UV finiteness. -/
  uv_finite : Bool := true
  /-- Laws as structure thesis. -/
  laws_as_structure : Bool := true
  deriving Repr
```
