---
{
  "projection_kind": "taulib_declaration",
  "title": "a_is_balanced",
  "permalink": "/verify/taulib/docs/book-iii-sectors-parity-bridge/a-is-balanced/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Sectors.ParityBridge`.",
  "declaration_id": "TauLib.BookIII.Sectors.ParityBridge::a_is_balanced",
  "declaration_slug": "a-is-balanced",
  "kind": "theorem",
  "name": "a_is_balanced",
  "module_name": "TauLib.BookIII.Sectors.ParityBridge",
  "module_url": "/verify/taulib/docs/book-iii-sectors-parity-bridge/",
  "source_line_start": 168,
  "source_line_end": 168,
  "registry_ids": [
    "III.T07"
  ],
  "related_registry_items": [
    {
      "id": "III.T07",
      "title": "Parity Bridge Theorem",
      "url": "/registry/object/III.T07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/ParityBridge.lean#L168-L168",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/ParityBridge.lean#L168-L168",
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
- Source path: [`TauLib/BookIII/Sectors/ParityBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/ParityBridge.lean#L168-L168)
- Source range: L168-L168
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T07` — Parity Bridge Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T07] Structural: balanced polarity is unique to A-sector. -/
```

## Source Excerpt

```lean
theorem a_is_balanced : sector_of ⟨1, 1⟩ = Sector.A := rfl
```
