---
{
  "projection_kind": "taulib_declaration",
  "title": "GTauFromShape",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/gtau-from-shape/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.FrameHolonomy`.",
  "declaration_id": "TauLib.BookV.GravityField.FrameHolonomy::GTauFromShape",
  "declaration_slug": "gtau-from-shape",
  "kind": "structure",
  "name": "GTauFromShape",
  "module_name": "TauLib.BookV.GravityField.FrameHolonomy",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/",
  "source_line_start": 188,
  "source_line_end": 198,
  "registry_ids": [
    "V.D45"
  ],
  "related_registry_items": [
    {
      "id": "V.D45",
      "title": "Gravitational constant --- V.D02",
      "url": "/registry/object/V.D45/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L188-L198",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L188-L198",
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
- Source path: [`TauLib/BookV/GravityField/FrameHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L188-L198)
- Source range: L188-L198
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D45` — Gravitational constant --- V.D02

## Immediate Comment / Docstring

```lean
/-- [V.D45] G_τ from shape ratio: the gravitational constant derived
    from the torus vacuum shape ratio r/R = ι_τ.

    In orthodox units: G = (c³/ℏ) · ι_τ²

    The ι_τ² factor is the structural core.
    Numerator = iota² = 341304² = 116594274681
    Denominator = iotaD² = 10¹² -/
```

## Source Excerpt

```lean
structure GTauFromShape where
  /-- ι_τ² numerator. -/
  iota_sq_num : Nat
  /-- ι_τ² denominator. -/
  iota_sq_den : Nat
  /-- Denominator positive. -/
  denom_pos : iota_sq_den > 0
  /-- The value equals iota². -/
  is_iota_squared : iota_sq_num = iota * iota ∧
                    iota_sq_den = iotaD * iotaD
  deriving Repr
```
