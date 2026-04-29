---
{
  "projection_kind": "taulib_declaration",
  "title": "bridge_ledger_complete",
  "permalink": "/verify/taulib/docs/book-iii-doors-bridge-tightening/bridge-ledger-complete/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Doors.BridgeTightening`.",
  "declaration_id": "TauLib.BookIII.Doors.BridgeTightening::bridge_ledger_complete",
  "declaration_slug": "bridge-ledger-complete",
  "kind": "theorem",
  "name": "bridge_ledger_complete",
  "module_name": "TauLib.BookIII.Doors.BridgeTightening",
  "module_url": "/verify/taulib/docs/book-iii-doors-bridge-tightening/",
  "source_line_start": 276,
  "source_line_end": 277,
  "registry_ids": [
    "III.P39"
  ],
  "related_registry_items": [
    {
      "id": "III.P39",
      "title": "Bridge Ledger Completeness",
      "url": "/registry/object/III.P39/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L276-L277",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.BridgeTightening",
        "url": "/verify/taulib/docs/book-iii-doors-bridge-tightening/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L276-L277",
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

- Module: [TauLib.BookIII.Doors.BridgeTightening](/verify/taulib/docs/book-iii-doors-bridge-tightening/)
- Source path: [`TauLib/BookIII/Doors/BridgeTightening.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L276-L277)
- Source range: L276-L277
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P39` — Bridge Ledger Completeness

## Immediate Comment / Docstring

```lean
/-- [III.P39] Bridge ledger is complete. -/
```

## Source Excerpt

```lean
theorem bridge_ledger_complete :
    bridge_ledger_complete_check = true := by native_decide
```
