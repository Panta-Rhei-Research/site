---
{
  "projection_kind": "taulib_declaration",
  "title": "RegimeSelector",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-coupling/regime-selector/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongCoupling`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongCoupling::RegimeSelector",
  "declaration_slug": "regime-selector",
  "kind": "structure",
  "name": "RegimeSelector",
  "module_name": "TauLib.BookIV.Strong.StrongCoupling",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-coupling/",
  "source_line_start": 234,
  "source_line_end": 243,
  "registry_ids": [
    "IV.D185"
  ],
  "related_registry_items": [
    {
      "id": "IV.D185",
      "title": "Regime selector",
      "url": "/registry/object/IV.D185/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L234-L243",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.StrongCoupling",
        "url": "/verify/taulib/docs/book-iv-strong-strong-coupling/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L234-L243",
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

- Module: [TauLib.BookIV.Strong.StrongCoupling](/verify/taulib/docs/book-iv-strong-strong-coupling/)
- Source path: [`TauLib/BookIV/Strong/StrongCoupling.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L234-L243)
- Source range: L234-L243
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D185` — Regime selector

## Immediate Comment / Docstring

```lean
/-- [IV.D185] A regime selector: finite datum specifying truncation
    depth, operational chart, sector carrier, and calibration bridge. -/
```

## Source Excerpt

```lean
structure RegimeSelector where
  /-- Truncation depth n_0. -/
  truncation_depth : Nat
  /-- Operational chart (coordinate choice). -/
  chart : String
  /-- Sector carrier. -/
  carrier : Sector
  /-- Calibration bridge from tau-units to SI. -/
  calibration : String
  deriving Repr
```
