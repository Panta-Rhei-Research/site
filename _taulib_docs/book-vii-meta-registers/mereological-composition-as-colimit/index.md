---
{
  "projection_kind": "taulib_declaration",
  "title": "MereologicalCompositionAsColimit",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/mereological-composition-as-colimit/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::MereologicalCompositionAsColimit",
  "declaration_slug": "mereological-composition-as-colimit",
  "kind": "structure",
  "name": "MereologicalCompositionAsColimit",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 851,
  "source_line_end": 856,
  "registry_ids": [
    "VII.D35"
  ],
  "related_registry_items": [
    {
      "id": "VII.D35",
      "title": "Mereological Composition as Colimit",
      "url": "/registry/object/VII.D35/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L851-L856",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Registers",
        "url": "/verify/taulib/docs/book-vii-meta-registers/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L851-L856",
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

- Module: [TauLib.BookVII.Meta.Registers](/verify/taulib/docs/book-vii-meta-registers/)
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L851-L856)
- Source range: L851-L856
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D35` — Mereological Composition as Colimit

## Immediate Comment / Docstring

```lean
/-- [VII.D35] Mereological Composition as Colimit (ch27). Parts and
    wholes via categorical colimits: composition of parts = colimit
    of a diagram of parts. Universal property gives canonical whole. -/
```

## Source Excerpt

```lean
structure MereologicalCompositionAsColimit where
  /-- Composition = colimit. -/
  composition_as_colimit : Bool := true
  /-- Universal property. -/
  universal_property : Bool := true
  deriving Repr
```
