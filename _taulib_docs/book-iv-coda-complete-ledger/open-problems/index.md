---
{
  "projection_kind": "taulib_declaration",
  "title": "OpenProblems",
  "permalink": "/verify/taulib/docs/book-iv-coda-complete-ledger/open-problems/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Coda.CompleteLedger`.",
  "declaration_id": "TauLib.BookIV.Coda.CompleteLedger::OpenProblems",
  "declaration_slug": "open-problems",
  "kind": "structure",
  "name": "OpenProblems",
  "module_name": "TauLib.BookIV.Coda.CompleteLedger",
  "module_url": "/verify/taulib/docs/book-iv-coda-complete-ledger/",
  "source_line_start": 128,
  "source_line_end": 143,
  "registry_ids": [
    "IV.R187"
  ],
  "related_registry_items": [
    {
      "id": "IV.R187",
      "title": "Open vs wrong problems",
      "url": "/registry/object/IV.R187/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L128-L143",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L128-L143",
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
- Source path: [`TauLib/BookIV/Coda/CompleteLedger.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L128-L143)
- Source range: L128-L143
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R187` — Open vs wrong problems

## Immediate Comment / Docstring

```lean
/-- [IV.R187] Five open problems are explicitly distinguished from
    wrong claims. Open problems have well-defined resolution criteria;
    wrong claims have been refuted or are inconsistent. -/
```

## Source Excerpt

```lean
structure OpenProblems where
  /-- Number of open problems. -/
  num_open : Nat := 5
  /-- Problem list. -/
  problems : List String := [
    "Sphaleron: base-fiber transition",
    "Readout functor: explicit construction",
    "Dark matter: defect-based candidate",
    "Cosmological constant: base tau^1 value",
    "Closing identity correction: c_1 = 3/pi proof"
  ]
  /-- All have well-defined resolution criteria. -/
  resolution_criteria : Bool := true
  /-- None are wrong claims. -/
  not_wrong : Bool := true
  deriving Repr
```
