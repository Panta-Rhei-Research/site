---
{
  "projection_kind": "taulib_declaration",
  "title": "coupling_ledger_check",
  "permalink": "/corpus/taulib/docs/book-iii-sectors-parity-bridge/coupling-ledger-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Sectors.ParityBridge`.",
  "declaration_id": "TauLib.BookIII.Sectors.ParityBridge::coupling_ledger_check",
  "declaration_slug": "coupling-ledger-check",
  "kind": "def",
  "name": "coupling_ledger_check",
  "module_name": "TauLib.BookIII.Sectors.ParityBridge",
  "module_url": "/corpus/taulib/docs/book-iii-sectors-parity-bridge/",
  "source_line_start": 110,
  "source_line_end": 111,
  "registry_ids": [
    "III.D18"
  ],
  "related_registry_items": [
    {
      "id": "III.D18",
      "title": "Coupling Ledger",
      "url": "/registry/object/III.D18/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/ParityBridge.lean#L110-L111",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Sectors.ParityBridge",
        "url": "/corpus/taulib/docs/book-iii-sectors-parity-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/ParityBridge.lean#L110-L111",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookIII.Sectors.ParityBridge](/corpus/taulib/docs/book-iii-sectors-parity-bridge/)
- Source path: [`TauLib/BookIII/Sectors/ParityBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/ParityBridge.lean#L110-L111)
- Source range: L110-L111
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `III.D18` — Coupling Ledger

## Immediate Comment / Docstring

```lean
/-- [III.D18] Coupling ledger completeness: exactly 10 entries. -/
```

## Source Excerpt

```lean
def coupling_ledger_check (bound : TauIdx) : Bool :=
  (coupling_ledger bound).length == 10
```
