---
{
  "projection_kind": "taulib_declaration",
  "title": "one_anchor_not_zero",
  "permalink": "/verify/taulib/docs/book-v-coda-constants-ledger/one-anchor-not-zero/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Coda.ConstantsLedger`.",
  "declaration_id": "TauLib.BookV.Coda.ConstantsLedger::one_anchor_not_zero",
  "declaration_slug": "one-anchor-not-zero",
  "kind": "theorem",
  "name": "one_anchor_not_zero",
  "module_name": "TauLib.BookV.Coda.ConstantsLedger",
  "module_url": "/verify/taulib/docs/book-v-coda-constants-ledger/",
  "source_line_start": 265,
  "source_line_end": 267,
  "registry_ids": [
    "V.R305"
  ],
  "related_registry_items": [
    {
      "id": "V.R305",
      "title": "One anchor, not zero",
      "url": "/registry/object/V.R305/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L265-L267",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L265-L267",
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
- Source path: [`TauLib/BookV/Coda/ConstantsLedger.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L265-L267)
- Source range: L265-L267
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R305` — One anchor, not zero

## Immediate Comment / Docstring

```lean
/-- [V.R305] One anchor, not zero: zero free parameters means no
    dimensionless ratio is fitted. One experimental input (m_n)
    sets the scale. iota_tau determines every ratio. -/
```

## Source Excerpt

```lean
theorem one_anchor_not_zero :
    "0 free parameters, 1 anchor (m_n); iota_tau determines all ratios" =
    "0 free parameters, 1 anchor (m_n); iota_tau determines all ratios" := rfl
```
