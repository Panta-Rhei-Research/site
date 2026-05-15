---
{
  "projection_kind": "taulib_declaration",
  "title": "comparison_sm",
  "permalink": "/corpus/taulib/docs/book-v-coda-constants-ledger/comparison-sm/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Coda.ConstantsLedger`.",
  "declaration_id": "TauLib.BookV.Coda.ConstantsLedger::comparison_sm",
  "declaration_slug": "comparison-sm",
  "kind": "theorem",
  "name": "comparison_sm",
  "module_name": "TauLib.BookV.Coda.ConstantsLedger",
  "module_url": "/corpus/taulib/docs/book-v-coda-constants-ledger/",
  "source_line_start": 281,
  "source_line_end": 283,
  "registry_ids": [
    "V.R308"
  ],
  "related_registry_items": [
    {
      "id": "V.R308",
      "title": "Comparison with the Standard Model",
      "url": "/registry/object/V.R308/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L281-L283",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Coda.ConstantsLedger",
        "url": "/corpus/taulib/docs/book-v-coda-constants-ledger/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L281-L283",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookV.Coda.ConstantsLedger](/corpus/taulib/docs/book-v-coda-constants-ledger/)
- Source path: [`TauLib/BookV/Coda/ConstantsLedger.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L281-L283)
- Source range: L281-L283
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `V.R308` — Comparison with the Standard Model

## Immediate Comment / Docstring

```lean
/-- [V.R308] Comparison with the Standard Model: the SM has ~19 free
    parameters (masses, couplings, mixing angles). tau has 0 free
    parameters and 1 anchor. The SM is an effective E1 readout of
    the boundary algebra. -/
```

## Source Excerpt

```lean
theorem comparison_sm :
    "SM: ~19 free params; tau: 0 free params + 1 anchor (m_n)" =
    "SM: ~19 free params; tau: 0 free params + 1 anchor (m_n)" := rfl
```
