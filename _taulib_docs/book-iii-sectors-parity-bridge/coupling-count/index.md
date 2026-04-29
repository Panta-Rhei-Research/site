---
{
  "projection_kind": "taulib_declaration",
  "title": "coupling_count",
  "permalink": "/verify/taulib/docs/book-iii-sectors-parity-bridge/coupling-count/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Sectors.ParityBridge`.",
  "declaration_id": "TauLib.BookIII.Sectors.ParityBridge::coupling_count",
  "declaration_slug": "coupling-count",
  "kind": "theorem",
  "name": "coupling_count",
  "module_name": "TauLib.BookIII.Sectors.ParityBridge",
  "module_url": "/verify/taulib/docs/book-iii-sectors-parity-bridge/",
  "source_line_start": 181,
  "source_line_end": 183,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/ParityBridge.lean#L181-L183",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Sectors.ParityBridge",
        "url": "/verify/taulib/docs/book-iii-sectors-parity-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/ParityBridge.lean#L181-L183",
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

- Module: [TauLib.BookIII.Sectors.ParityBridge](/verify/taulib/docs/book-iii-sectors-parity-bridge/)
- Source path: [`TauLib/BookIII/Sectors/ParityBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/ParityBridge.lean#L181-L183)
- Source range: L181-L183
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D18` — Coupling Ledger

## Immediate Comment / Docstring

```lean
/-- [III.D18] Structural: the coupling ledger has exactly 10 entries
    for 4 sectors (upper triangle of 4×4 matrix). -/
```

## Source Excerpt

```lean
theorem coupling_count : 4 * (4 + 1) / 2 = 10 := by decide

end Tau.BookIII.Sectors
```
