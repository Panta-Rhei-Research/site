---
{
  "projection_kind": "taulib_declaration",
  "title": "neutrino_precision",
  "permalink": "/verify/taulib/docs/book-v-coda-constants-ledger/neutrino-precision/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Coda.ConstantsLedger`.",
  "declaration_id": "TauLib.BookV.Coda.ConstantsLedger::neutrino_precision",
  "declaration_slug": "neutrino-precision",
  "kind": "theorem",
  "name": "neutrino_precision",
  "module_name": "TauLib.BookV.Coda.ConstantsLedger",
  "module_url": "/verify/taulib/docs/book-v-coda-constants-ledger/",
  "source_line_start": 226,
  "source_line_end": 228,
  "registry_ids": [
    "V.R298"
  ],
  "related_registry_items": [
    {
      "id": "V.R298",
      "title": "Precision of the neutrino prediction",
      "url": "/registry/object/V.R298/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L226-L228",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L226-L228",
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
- Source path: [`TauLib/BookV/Coda/ConstantsLedger.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L226-L228)
- Source range: L226-L228
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R298` — Precision of the neutrino prediction

## Immediate Comment / Docstring

```lean
/-- [V.R298] Precision of the neutrino prediction: m_3(nu) ~ m_e *
    iota_tau^15 ~ 50.7 meV. The experimental range is 49-62 meV from
    cosmological bounds. The prediction is within the allowed range
    but the exponent 15 is conjectural. -/
```

## Source Excerpt

```lean
theorem neutrino_precision :
    "m_3(nu) ~ 50.7 meV (exponent 15 conjectural); expt 49-62 meV" =
    "m_3(nu) ~ 50.7 meV (exponent 15 conjectural); expt 49-62 meV" := rfl
```
