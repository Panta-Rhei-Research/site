---
{
  "projection_kind": "taulib_declaration",
  "title": "MacroTorusCarrier",
  "permalink": "/verify/taulib/docs/book-vi-life-core-distinction/macro-torus-carrier/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.LifeCore.Distinction`.",
  "declaration_id": "TauLib.BookVI.LifeCore.Distinction::MacroTorusCarrier",
  "declaration_slug": "macro-torus-carrier",
  "kind": "structure",
  "name": "MacroTorusCarrier",
  "module_name": "TauLib.BookVI.LifeCore.Distinction",
  "module_url": "/verify/taulib/docs/book-vi-life-core-distinction/",
  "source_line_start": 51,
  "source_line_end": 55,
  "registry_ids": [
    "VI.D06"
  ],
  "related_registry_items": [
    {
      "id": "VI.D06",
      "title": "Macro-Torus Carrier",
      "url": "/registry/object/VI.D06/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/Distinction.lean#L51-L55",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/Distinction.lean#L51-L55",
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
- Source path: [`TauLib/BookVI/LifeCore/Distinction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/Distinction.lean#L51-L55)
- Source range: L51-L55
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D06` — Macro-Torus Carrier

## Immediate Comment / Docstring

```lean
/-- [VI.D06] Macro-torus carrier: BH carrier with T² boundary, immortal. -/
```

## Source Excerpt

```lean
structure MacroTorusCarrier where
  has_t2_boundary : Bool := true
  is_immortal : Bool := true
  carrier_type : String := "macro-torus"
  deriving Repr
```
