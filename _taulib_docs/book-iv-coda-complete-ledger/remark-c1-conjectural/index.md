---
{
  "projection_kind": "taulib_declaration",
  "title": "remark_c1_conjectural",
  "permalink": "/verify/taulib/docs/book-iv-coda-complete-ledger/remark-c1-conjectural/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Coda.CompleteLedger`.",
  "declaration_id": "TauLib.BookIV.Coda.CompleteLedger::remark_c1_conjectural",
  "declaration_slug": "remark-c1-conjectural",
  "kind": "def",
  "name": "remark_c1_conjectural",
  "module_name": "TauLib.BookIV.Coda.CompleteLedger",
  "module_url": "/verify/taulib/docs/book-iv-coda-complete-ledger/",
  "source_line_start": 59,
  "source_line_end": 61,
  "registry_ids": [
    "IV.R184"
  ],
  "related_registry_items": [
    {
      "id": "IV.R184",
      "title": "Why C1 is conjectural",
      "url": "/registry/object/IV.R184/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L59-L61",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L59-L61",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookIV/Coda/CompleteLedger.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L59-L61)
- Source range: L59-L61
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.R184` — Why C1 is conjectural

## Immediate Comment / Docstring

```lean
/-- [IV.R184] (Conjectural) The electron mass prediction
    m_e = 0.510998937 MeV (0.025 ppm) remains conjectural despite its
    precision: the mass ratio formula R is tau-effective as an internal
    structural identity, but the numerical calibration against SI units
    requires the neutron mass anchor, which is an empirical input.

    The prediction is as precise as CODATA but not a derivation from
    axioms alone (which would require establishing m_n from K0-K6). -/
```

## Source Excerpt

```lean
def remark_c1_conjectural : String :=
  "[conjectural] m_e = 0.510998937 MeV (0.025 ppm): R formula is " ++
  "tau-effective, but SI calibration needs empirical m_n anchor"
```
