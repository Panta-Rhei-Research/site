---
{
  "projection_kind": "taulib_declaration",
  "title": "d_self_coupling_1",
  "permalink": "/verify/taulib/docs/book-iii-sectors-parity-bridge/d-self-coupling-1/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Sectors.ParityBridge`.",
  "declaration_id": "TauLib.BookIII.Sectors.ParityBridge::d_self_coupling_1",
  "declaration_slug": "d-self-coupling-1",
  "kind": "theorem",
  "name": "d_self_coupling_1",
  "module_name": "TauLib.BookIII.Sectors.ParityBridge",
  "module_url": "/verify/taulib/docs/book-iii-sectors-parity-bridge/",
  "source_line_start": 176,
  "source_line_end": 177,
  "registry_ids": [
    "III.T08"
  ],
  "related_registry_items": [
    {
      "id": "III.T08",
      "title": "No Knobs Principle",
      "url": "/registry/object/III.T08/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/ParityBridge.lean#L176-L177",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/ParityBridge.lean#L176-L177",
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
- Source path: [`TauLib/BookIII/Sectors/ParityBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/ParityBridge.lean#L176-L177)
- Source range: L176-L177
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T08` — No Knobs Principle

## Immediate Comment / Docstring

```lean
/-- [III.T08] Structural: D-sector self-coupling is always 1
    (only the trivial character maps to D). -/
```

## Source Excerpt

```lean
theorem d_self_coupling_1 :
    sector_coupling .D .D 5 = 1 := by native_decide
```
