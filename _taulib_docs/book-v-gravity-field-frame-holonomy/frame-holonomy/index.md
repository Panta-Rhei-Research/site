---
{
  "projection_kind": "taulib_declaration",
  "title": "FrameHolonomy",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/frame-holonomy/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.FrameHolonomy`.",
  "declaration_id": "TauLib.BookV.GravityField.FrameHolonomy::FrameHolonomy",
  "declaration_slug": "frame-holonomy",
  "kind": "structure",
  "name": "FrameHolonomy",
  "module_name": "TauLib.BookV.GravityField.FrameHolonomy",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/",
  "source_line_start": 101,
  "source_line_end": 114,
  "registry_ids": [
    "V.D42"
  ],
  "related_registry_items": [
    {
      "id": "V.D42",
      "title": "Frame holonomy on tau^1",
      "url": "/registry/object/V.D42/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L101-L114",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L101-L114",
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
- Source path: [`TauLib/BookV/GravityField/FrameHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L101-L114)
- Source range: L101-L114
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D42` — Frame holonomy on tau^1

## Immediate Comment / Docstring

```lean
/-- [V.D42] Frame holonomy: phase accumulated by parallel transport
    around a D-sector loop on τ¹.

    The holonomy is the D-sector boundary character evaluated on a
    closed loop. At depth n, the holonomy group is a finite cyclic
    group whose order grows with n.

    The holonomy gap is the smallest non-trivial element:
    gap_n = 1/order_n in normalized holonomy units. -/
```

## Source Excerpt

```lean
structure FrameHolonomy where
  /-- The frame around which transport occurs. -/
  frame : ClopenFrame
  /-- Holonomy group order at this depth. -/
  group_order : Nat
  /-- Group order is positive. -/
  order_pos : group_order > 0
  /-- Holonomy gap numerator (= 1 in normalized units). -/
  gap_numer : Nat := 1
  /-- Holonomy gap denominator (= group_order). -/
  gap_denom : Nat := group_order
  /-- Gap is minimal (1/order). -/
  gap_minimal : gap_numer = 1 ∧ gap_denom = group_order
  deriving Repr
```
