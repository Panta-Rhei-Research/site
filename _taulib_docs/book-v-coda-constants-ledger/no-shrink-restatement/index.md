---
{
  "projection_kind": "taulib_declaration",
  "title": "no_shrink_restatement",
  "permalink": "/verify/taulib/docs/book-v-coda-constants-ledger/no-shrink-restatement/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Coda.ConstantsLedger`.",
  "declaration_id": "TauLib.BookV.Coda.ConstantsLedger::no_shrink_restatement",
  "declaration_slug": "no-shrink-restatement",
  "kind": "theorem",
  "name": "no_shrink_restatement",
  "module_name": "TauLib.BookV.Coda.ConstantsLedger",
  "module_url": "/verify/taulib/docs/book-v-coda-constants-ledger/",
  "source_line_start": 161,
  "source_line_end": 163,
  "registry_ids": [
    "V.T141"
  ],
  "related_registry_items": [
    {
      "id": "V.T141",
      "title": "No Shrink---restatement",
      "url": "/registry/object/V.T141/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L161-L163",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L161-L163",
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
- Source path: [`TauLib/BookV/Coda/ConstantsLedger.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L161-L163)
- Source range: L161-L163
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T141` — No Shrink---restatement

## Immediate Comment / Docstring

```lean
/-- [V.T141] No Shrink restatement: black holes do not evaporate.

    The total boundary-character amplitude of a BH region is
    non-decreasing under profinite flow. Bekenstein-Hawking
    entropy is real (topological, not thermal).

    Hawking radiation in the orthodox readout is a chart artifact:
    the readout functor produces a thermal spectrum from the
    boundary algebra's non-thermal character evolution. -/
```

## Source Excerpt

```lean
theorem no_shrink_restatement :
    "BH boundary-character amplitude non-decreasing; no evaporation" =
    "BH boundary-character amplitude non-decreasing; no evaporation" := rfl
```
