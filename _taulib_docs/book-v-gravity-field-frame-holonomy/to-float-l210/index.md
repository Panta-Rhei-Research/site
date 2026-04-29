---
{
  "projection_kind": "taulib_declaration",
  "title": "GTauFromShape.toFloat",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/to-float-l210/",
  "summary_short": "`def` declaration in `TauLib.BookV.GravityField.FrameHolonomy`.",
  "declaration_id": "TauLib.BookV.GravityField.FrameHolonomy::GTauFromShape.toFloat",
  "declaration_slug": "to-float-l210",
  "kind": "def",
  "name": "GTauFromShape.toFloat",
  "module_name": "TauLib.BookV.GravityField.FrameHolonomy",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/",
  "source_line_start": 210,
  "source_line_end": 211,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L210-L211",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L210-L211",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookV/GravityField/FrameHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L210-L211)
- Source range: L210-L211
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- G_τ shape factor as Float (≈ 0.116594, i.e., ι_τ²). -/
```

## Source Excerpt

```lean
def GTauFromShape.toFloat (g : GTauFromShape) : Float :=
  Float.ofNat g.iota_sq_num / Float.ofNat g.iota_sq_den
```
