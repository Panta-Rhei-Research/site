---
{
  "projection_kind": "taulib_declaration",
  "title": "FormalizationFrontier",
  "permalink": "/verify/taulib/docs/book-iv-coda-complete-ledger/formalization-frontier/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Coda.CompleteLedger`.",
  "declaration_id": "TauLib.BookIV.Coda.CompleteLedger::FormalizationFrontier",
  "declaration_slug": "formalization-frontier",
  "kind": "structure",
  "name": "FormalizationFrontier",
  "module_name": "TauLib.BookIV.Coda.CompleteLedger",
  "module_url": "/verify/taulib/docs/book-iv-coda-complete-ledger/",
  "source_line_start": 105,
  "source_line_end": 114,
  "registry_ids": [
    "IV.R186"
  ],
  "related_registry_items": [
    {
      "id": "IV.R186",
      "title": "The formalization frontier",
      "url": "/registry/object/IV.R186/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L105-L114",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L105-L114",
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
- Source path: [`TauLib/BookIV/Coda/CompleteLedger.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L105-L114)
- Source range: L105-L114
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R186` — The formalization frontier

## Immediate Comment / Docstring

```lean
/-- [IV.R186] Fifteen of twenty-five tau-effective results await Lean
    formalization. This reflects LaTeX exposition outpacing formal
    verification; no tau-effective result contradicts existing Lean proofs. -/
```

## Source Excerpt

```lean
structure FormalizationFrontier where
  /-- Tau-effective awaiting formalization. -/
  awaiting : Nat := 15
  /-- Total tau-effective. -/
  total_te : Nat := 25
  /-- Formalized tau-effective. -/
  formalized : Nat := 10
  /-- No contradictions found. -/
  no_contradictions : Bool := true
  deriving Repr
```
