---
{
  "projection_kind": "taulib_declaration",
  "title": "GluonSelfInteraction",
  "permalink": "/verify/taulib/docs/book-iv-strong-color-holonomy/gluon-self-interaction/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.ColorHolonomy`.",
  "declaration_id": "TauLib.BookIV.Strong.ColorHolonomy::GluonSelfInteraction",
  "declaration_slug": "gluon-self-interaction",
  "kind": "structure",
  "name": "GluonSelfInteraction",
  "module_name": "TauLib.BookIV.Strong.ColorHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-strong-color-holonomy/",
  "source_line_start": 248,
  "source_line_end": 257,
  "registry_ids": [
    "IV.P93"
  ],
  "related_registry_items": [
    {
      "id": "IV.P93",
      "title": "Gluon Self-Interaction",
      "url": "/registry/object/IV.P93/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L248-L257",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.ColorHolonomy",
        "url": "/verify/taulib/docs/book-iv-strong-color-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L248-L257",
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

- Module: [TauLib.BookIV.Strong.ColorHolonomy](/verify/taulib/docs/book-iv-strong-color-holonomy/)
- Source path: [`TauLib/BookIV/Strong/ColorHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L248-L257)
- Source range: L248-L257
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P93` — Gluon Self-Interaction

## Immediate Comment / Docstring

```lean
/-- [IV.P93] Gluons carry color charge and self-interact:
    [T^a, T^b] = i f^{abc} T^c is nonzero, producing 3-gluon
    and 4-gluon vertices. This is the structural origin of confinement. -/
```

## Source Excerpt

```lean
structure GluonSelfInteraction where
  /-- Gluons carry color charge. -/
  carries_color : Bool := true
  /-- Structure constants f_{abc} are nonzero. -/
  nonzero_structure_constants : Bool := true
  /-- Three-gluon vertex exists. -/
  three_vertex : Bool := true
  /-- Four-gluon vertex exists. -/
  four_vertex : Bool := true
  deriving Repr
```
