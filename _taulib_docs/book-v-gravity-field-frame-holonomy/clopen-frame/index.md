---
{
  "projection_kind": "taulib_declaration",
  "title": "ClopenFrame",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/clopen-frame/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.FrameHolonomy`.",
  "declaration_id": "TauLib.BookV.GravityField.FrameHolonomy::ClopenFrame",
  "declaration_slug": "clopen-frame",
  "kind": "structure",
  "name": "ClopenFrame",
  "module_name": "TauLib.BookV.GravityField.FrameHolonomy",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/",
  "source_line_start": 71,
  "source_line_end": 82,
  "registry_ids": [
    "V.D41"
  ],
  "related_registry_items": [
    {
      "id": "V.D41",
      "title": "Clopen frame",
      "url": "/registry/object/V.D41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L71-L82",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.FrameHolonomy",
        "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L71-L82",
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

- Module: [TauLib.BookV.GravityField.FrameHolonomy](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/)
- Source path: [`TauLib/BookV/GravityField/FrameHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L71-L82)
- Source range: L71-L82
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D41` — Clopen frame

## Immediate Comment / Docstring

```lean
/-- [V.D41] Clopen frame: gravitational reference frame at depth n.

    A clopen frame is a subset of the refinement tower that is both
    closed and open in the τ-topology. This means:
    - Every carrier is decidably inside or outside the frame
    - The frame boundary is a well-defined orbit-index predicate
    - Frame transition maps are holomorphic (boundary-character maps) -/
```

## Source Excerpt

```lean
structure ClopenFrame where
  /-- Refinement depth at which the frame is defined. -/
  depth : Nat
  /-- Depth must be positive (frames require at least one refinement step). -/
  depth_pos : depth > 0
  /-- Number of carriers in the frame at this depth. -/
  carrier_count : Nat
  /-- At least one carrier in any frame. -/
  carrier_pos : carrier_count > 0
  /-- The frame is clopen (decidable membership). -/
  is_clopen : Bool := true
  deriving Repr
```
