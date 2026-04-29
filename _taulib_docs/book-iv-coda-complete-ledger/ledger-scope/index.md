---
{
  "projection_kind": "taulib_declaration",
  "title": "LedgerScope",
  "permalink": "/verify/taulib/docs/book-iv-coda-complete-ledger/ledger-scope/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.Coda.CompleteLedger`.",
  "declaration_id": "TauLib.BookIV.Coda.CompleteLedger::LedgerScope",
  "declaration_slug": "ledger-scope",
  "kind": "inductive",
  "name": "LedgerScope",
  "module_name": "TauLib.BookIV.Coda.CompleteLedger",
  "module_url": "/verify/taulib/docs/book-iv-coda-complete-ledger/",
  "source_line_start": 290,
  "source_line_end": 295,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L290-L295",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L290-L295",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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
- Source path: [`TauLib/BookIV/Coda/CompleteLedger.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L290-L295)
- Source range: L290-L295
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Scope label for a ledger entry. -/
```

## Source Excerpt

```lean
inductive LedgerScope where
  | Established
  | TauEffective
  | Conjectural
  | Metaphorical
  deriving Repr, DecidableEq, BEq
```
