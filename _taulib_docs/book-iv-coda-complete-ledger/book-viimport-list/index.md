---
{
  "projection_kind": "taulib_declaration",
  "title": "BookVIImportList",
  "permalink": "/verify/taulib/docs/book-iv-coda-complete-ledger/book-viimport-list/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Coda.CompleteLedger`.",
  "declaration_id": "TauLib.BookIV.Coda.CompleteLedger::BookVIImportList",
  "declaration_slug": "book-viimport-list",
  "kind": "structure",
  "name": "BookVIImportList",
  "module_name": "TauLib.BookIV.Coda.CompleteLedger",
  "module_url": "/verify/taulib/docs/book-iv-coda-complete-ledger/",
  "source_line_start": 239,
  "source_line_end": 248,
  "registry_ids": [
    "IV.D244"
  ],
  "related_registry_items": [
    {
      "id": "IV.D244",
      "title": "Book VI import list",
      "url": "/registry/object/IV.D244/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L239-L248",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L239-L248",
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
- Source path: [`TauLib/BookIV/Coda/CompleteLedger.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L239-L248)
- Source range: L239-L248
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D244` — Book VI import list

## Immediate Comment / Docstring

```lean
/-- [IV.D244] Book VI Import List: what Book IV exports to Book VI.

    Book VI (Categorical Life) receives:
    - The 4-component defect tuple as substrate for biological dynamics
    - The 8+1 fluid regimes as environmental classification
    - Phase transition taxonomy (for biological phase transitions)
    - Thermodynamic structure (entropy splitting, arrow of time)
    - UV finiteness (life cannot exploit UV divergences) -/
```

## Source Excerpt

```lean
structure BookVIImportList where
  /-- Defect tuple as biological substrate. -/
  defect_tuple : Bool := true
  /-- Regimes as environment. -/
  regimes : Nat := 9
  /-- Thermodynamic structure. -/
  thermodynamics : Bool := true
  /-- Arrow of time. -/
  arrow_of_time : Bool := true
  deriving Repr
```
