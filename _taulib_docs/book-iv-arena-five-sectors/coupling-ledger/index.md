---
{
  "projection_kind": "taulib_declaration",
  "title": "CouplingLedger",
  "permalink": "/verify/taulib/docs/book-iv-arena-five-sectors/coupling-ledger/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Arena.FiveSectors`.",
  "declaration_id": "TauLib.BookIV.Arena.FiveSectors::CouplingLedger",
  "declaration_slug": "coupling-ledger",
  "kind": "structure",
  "name": "CouplingLedger",
  "module_name": "TauLib.BookIV.Arena.FiveSectors",
  "module_url": "/verify/taulib/docs/book-iv-arena-five-sectors/",
  "source_line_start": 73,
  "source_line_end": 79,
  "registry_ids": [
    "IV.D265"
  ],
  "related_registry_items": [
    {
      "id": "IV.D265",
      "title": "Coupling Ledger",
      "url": "/registry/object/IV.D265/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L73-L79",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.FiveSectors",
        "url": "/verify/taulib/docs/book-iv-arena-five-sectors/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L73-L79",
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

- Module: [TauLib.BookIV.Arena.FiveSectors](/verify/taulib/docs/book-iv-arena-five-sectors/)
- Source path: [`TauLib/BookIV/Arena/FiveSectors.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L73-L79)
- Source range: L73-L79
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D265` — Coupling Ledger

## Immediate Comment / Docstring

```lean
/-- [IV.D265] The complete coupling ledger: 5 self + 10 cross = 15 entries.
    All determined by ι_τ alone (No Knobs, III.T08). -/
```

## Source Excerpt

```lean
structure CouplingLedger where
  /-- Self-coupling entries (5). -/
  self_entries : List CouplingEntry
  self_count : self_entries.length = 5
  /-- Cross-coupling entries (10). -/
  cross_entries : List CouplingEntry
  cross_count : cross_entries.length = 10
```
