---
{
  "projection_kind": "taulib_declaration",
  "title": "shape_ratio_is_iota",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/shape-ratio-is-iota/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.FrameHolonomy`.",
  "declaration_id": "TauLib.BookV.GravityField.FrameHolonomy::shape_ratio_is_iota",
  "declaration_slug": "shape-ratio-is-iota",
  "kind": "theorem",
  "name": "shape_ratio_is_iota",
  "module_name": "TauLib.BookV.GravityField.FrameHolonomy",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/",
  "source_line_start": 289,
  "source_line_end": 292,
  "registry_ids": [
    "V.T21"
  ],
  "related_registry_items": [
    {
      "id": "V.T21",
      "title": "Vacuum shape ratio --- V.T01",
      "url": "/registry/object/V.T21/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L289-L292",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L289-L292",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookV/GravityField/FrameHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L289-L292)
- Source range: L289-L292
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T21` — Vacuum shape ratio --- V.T01

## Immediate Comment / Docstring

```lean
/-- [V.T21] The torus vacuum shape ratio r/R = ι_τ.
    Restated from V.T01 in the gravitational field context. -/
```

## Source Excerpt

```lean
theorem shape_ratio_is_iota :
    g_tau_from_shape.iota_sq_num = iota * iota ∧
    g_tau_from_shape.iota_sq_den = iotaD * iotaD :=
  g_tau_from_shape.is_iota_squared
```
