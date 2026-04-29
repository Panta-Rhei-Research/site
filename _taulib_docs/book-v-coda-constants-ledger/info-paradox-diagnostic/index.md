---
{
  "projection_kind": "taulib_declaration",
  "title": "info_paradox_diagnostic",
  "permalink": "/verify/taulib/docs/book-v-coda-constants-ledger/info-paradox-diagnostic/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Coda.ConstantsLedger`.",
  "declaration_id": "TauLib.BookV.Coda.ConstantsLedger::info_paradox_diagnostic",
  "declaration_slug": "info-paradox-diagnostic",
  "kind": "theorem",
  "name": "info_paradox_diagnostic",
  "module_name": "TauLib.BookV.Coda.ConstantsLedger",
  "module_url": "/verify/taulib/docs/book-v-coda-constants-ledger/",
  "source_line_start": 242,
  "source_line_end": 244,
  "registry_ids": [
    "V.R301"
  ],
  "related_registry_items": [
    {
      "id": "V.R301",
      "title": "The information paradox as diagnostic",
      "url": "/registry/object/V.R301/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L242-L244",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L242-L244",
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
- Source path: [`TauLib/BookV/Coda/ConstantsLedger.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L242-L244)
- Source range: L242-L244
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R301` — The information paradox as diagnostic

## Immediate Comment / Docstring

```lean
/-- [V.R301] The information paradox as diagnostic: the information
    paradox (Hawking 1976) arises from treating BH evaporation as
    physical. In tau, BHs do not evaporate (No Shrink) and the
    paradox does not arise. Information is preserved on L. -/
```

## Source Excerpt

```lean
theorem info_paradox_diagnostic :
    "No evaporation (No Shrink) -> no information paradox" =
    "No evaporation (No Shrink) -> no information paradox" := rfl
```
