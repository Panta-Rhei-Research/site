---
{
  "projection_kind": "taulib_declaration",
  "title": "DerivedGeometry",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/derived-geometry/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::DerivedGeometry",
  "declaration_slug": "derived-geometry",
  "kind": "structure",
  "name": "DerivedGeometry",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 688,
  "source_line_end": 693,
  "registry_ids": [
    "VII.D28"
  ],
  "related_registry_items": [
    {
      "id": "VII.D28",
      "title": "Derived Geometry",
      "url": "/registry/object/VII.D28/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L688-L693",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L688-L693",
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
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L688-L693)
- Source range: L688-L693
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D28` — Derived Geometry

## Immediate Comment / Docstring

```lean
/-- [VII.D28] Derived Geometry (ch20). Geometry is derived from
    categorical structure, not postulated. Spatial relations emerge
    from morphism structure in the kernel. -/
```

## Source Excerpt

```lean
structure DerivedGeometry where
  /-- Geometry derived, not postulated. -/
  derived : Bool := true
  /-- From morphism structure. -/
  from_morphisms : Bool := true
  deriving Repr
```
