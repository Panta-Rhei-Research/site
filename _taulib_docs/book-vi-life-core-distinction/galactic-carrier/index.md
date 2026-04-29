---
{
  "projection_kind": "taulib_declaration",
  "title": "GalacticCarrier",
  "permalink": "/verify/taulib/docs/book-vi-life-core-distinction/galactic-carrier/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.LifeCore.Distinction`.",
  "declaration_id": "TauLib.BookVI.LifeCore.Distinction::GalacticCarrier",
  "declaration_slug": "galactic-carrier",
  "kind": "structure",
  "name": "GalacticCarrier",
  "module_name": "TauLib.BookVI.LifeCore.Distinction",
  "module_url": "/verify/taulib/docs/book-vi-life-core-distinction/",
  "source_line_start": 58,
  "source_line_end": 62,
  "registry_ids": [
    "VI.D07"
  ],
  "related_registry_items": [
    {
      "id": "VI.D07",
      "title": "Galactic Carrier",
      "url": "/registry/object/VI.D07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/Distinction.lean#L58-L62",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.LifeCore.Distinction",
        "url": "/verify/taulib/docs/book-vi-life-core-distinction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/Distinction.lean#L58-L62",
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

- Module: [TauLib.BookVI.LifeCore.Distinction](/verify/taulib/docs/book-vi-life-core-distinction/)
- Source path: [`TauLib/BookVI/LifeCore/Distinction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/Distinction.lean#L58-L62)
- Source range: L58-L62
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D07` — Galactic Carrier

## Immediate Comment / Docstring

```lean
/-- [VI.D07] Galactic carrier: galaxy carrier with halo boundary, SMBH-anchored. -/
```

## Source Excerpt

```lean
structure GalacticCarrier where
  has_halo_boundary : Bool := true
  smbh_anchored : Bool := true
  carrier_type : String := "galactic"
  deriving Repr
```
