---
{
  "projection_kind": "taulib_declaration",
  "title": "AbstractObjectAsStructuralPosition",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/abstract-object-as-structural-position/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::AbstractObjectAsStructuralPosition",
  "declaration_slug": "abstract-object-as-structural-position",
  "kind": "structure",
  "name": "AbstractObjectAsStructuralPosition",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 881,
  "source_line_end": 886,
  "registry_ids": [
    "VII.D36"
  ],
  "related_registry_items": [
    {
      "id": "VII.D36",
      "title": "Abstract Object as Structural Position",
      "url": "/registry/object/VII.D36/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L881-L886",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L881-L886",
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
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L881-L886)
- Source range: L881-L886
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D36` — Abstract Object as Structural Position

## Immediate Comment / Docstring

```lean
/-- [VII.D36] Abstract Object as Structural Position (ch28). Abstract
    objects = positions in structures (ante rem structuralism).
    Numbers, sets, categories: identified with their structural role
    via Yoneda. No Platonic realm needed. -/
```

## Source Excerpt

```lean
structure AbstractObjectAsStructuralPosition where
  /-- Position in structure. -/
  structural_position : Bool := true
  /-- Yoneda identification. -/
  yoneda_identified : Bool := true
  deriving Repr
```
