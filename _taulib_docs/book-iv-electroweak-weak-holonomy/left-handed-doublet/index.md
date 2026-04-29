---
{
  "projection_kind": "taulib_declaration",
  "title": "LeftHandedDoublet",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/left-handed-doublet/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.WeakHolonomy`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakHolonomy::LeftHandedDoublet",
  "declaration_slug": "left-handed-doublet",
  "kind": "structure",
  "name": "LeftHandedDoublet",
  "module_name": "TauLib.BookIV.Electroweak.WeakHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/",
  "source_line_start": 92,
  "source_line_end": 102,
  "registry_ids": [
    "IV.D117"
  ],
  "related_registry_items": [
    {
      "id": "IV.D117",
      "title": "Left-Handed Doublets",
      "url": "/registry/object/IV.D117/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L92-L102",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakHolonomy",
        "url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L92-L102",
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

- Module: [TauLib.BookIV.Electroweak.WeakHolonomy](/verify/taulib/docs/book-iv-electroweak-weak-holonomy/)
- Source path: [`TauLib/BookIV/Electroweak/WeakHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L92-L102)
- Source range: L92-L102
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D117` — Left-Handed Doublets

## Immediate Comment / Docstring

```lean
/-- [IV.D117] A left-handed doublet: the fundamental representation
    of SU(2)_L. Pairs an "up-type" and a "down-type" fermion,
    both left-handed. The weak interaction rotates within doublets. -/
```

## Source Excerpt

```lean
structure LeftHandedDoublet where
  /-- Generation number (1, 2, or 3). -/
  generation : Fin 3
  /-- Up-type particle name. -/
  up_type : String
  /-- Down-type particle name. -/
  down_type : String
  /-- Both components are left-handed. -/
  chirality : ChiralityType
  chirality_left : chirality = .Left
  deriving Repr
```
