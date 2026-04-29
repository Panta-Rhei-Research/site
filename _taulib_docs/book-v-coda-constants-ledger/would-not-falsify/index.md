---
{
  "projection_kind": "taulib_declaration",
  "title": "would_not_falsify",
  "permalink": "/verify/taulib/docs/book-v-coda-constants-ledger/would-not-falsify/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Coda.ConstantsLedger`.",
  "declaration_id": "TauLib.BookV.Coda.ConstantsLedger::would_not_falsify",
  "declaration_slug": "would-not-falsify",
  "kind": "theorem",
  "name": "would_not_falsify",
  "module_name": "TauLib.BookV.Coda.ConstantsLedger",
  "module_url": "/verify/taulib/docs/book-v-coda-constants-ledger/",
  "source_line_start": 258,
  "source_line_end": 260,
  "registry_ids": [
    "V.R303"
  ],
  "related_registry_items": [
    {
      "id": "V.R303",
      "title": "What would NOT falsify tau",
      "url": "/registry/object/V.R303/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L258-L260",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Coda.ConstantsLedger",
        "url": "/verify/taulib/docs/book-v-coda-constants-ledger/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L258-L260",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookV.Coda.ConstantsLedger](/verify/taulib/docs/book-v-coda-constants-ledger/)
- Source path: [`TauLib/BookV/Coda/ConstantsLedger.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L258-L260)
- Source range: L258-L260
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R303` — What would NOT falsify tau

## Immediate Comment / Docstring

```lean
/-- [V.R303] What would NOT falsify tau: failure to compute QCD
    confinement from tau does not falsify the framework. It means
    the computation is hard, not the structure wrong. Falsification
    requires a structural prediction (Lambda = 0, no dark matter,
    no singularities) to fail, not a computational deadline. -/
```

## Source Excerpt

```lean
theorem would_not_falsify :
    "Missing computation does not falsify; structural prediction failure does" =
    "Missing computation does not falsify; structural prediction failure does" := rfl
```
