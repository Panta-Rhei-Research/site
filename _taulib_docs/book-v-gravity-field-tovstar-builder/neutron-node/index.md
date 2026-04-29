---
{
  "projection_kind": "taulib_declaration",
  "title": "NeutronNode",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/neutron-node/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.TOVStarBuilder`.",
  "declaration_id": "TauLib.BookV.GravityField.TOVStarBuilder::NeutronNode",
  "declaration_slug": "neutron-node",
  "kind": "structure",
  "name": "NeutronNode",
  "module_name": "TauLib.BookV.GravityField.TOVStarBuilder",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/",
  "source_line_start": 193,
  "source_line_end": 200,
  "registry_ids": [
    "V.D71"
  ],
  "related_registry_items": [
    {
      "id": "V.D71",
      "title": "Neutron node",
      "url": "/registry/object/V.D71/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L193-L200",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TOVStarBuilder",
        "url": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L193-L200",
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

- Module: [TauLib.BookV.GravityField.TOVStarBuilder](/verify/taulib/docs/book-v-gravity-field-tovstar-builder/)
- Source path: [`TauLib/BookV/GravityField/TOVStarBuilder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L193-L200)
- Source range: L193-L200
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D71` — Neutron node

## Immediate Comment / Docstring

```lean
/-- [V.D71] Neutron node: the basic building block of a neutron star.
    Each node carries one neutron mass unit. -/
```

## Source Excerpt

```lean
structure NeutronNode where
  /-- Node index (position in star). -/
  index : Nat
  /-- Whether the node is in the star interior. -/
  is_interior : Bool
  /-- Whether the node is EW-stable (electroweak stability). -/
  is_ew_stable : Bool
  deriving Repr
```
