---
{
  "projection_kind": "taulib_declaration",
  "title": "frame_adjacency_coherent",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/frame-adjacency-coherent/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.FrameHolonomy`.",
  "declaration_id": "TauLib.BookV.GravityField.FrameHolonomy::frame_adjacency_coherent",
  "declaration_slug": "frame-adjacency-coherent",
  "kind": "theorem",
  "name": "frame_adjacency_coherent",
  "module_name": "TauLib.BookV.GravityField.FrameHolonomy",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/",
  "source_line_start": 323,
  "source_line_end": 325,
  "registry_ids": [
    "V.P10"
  ],
  "related_registry_items": [
    {
      "id": "V.P10",
      "title": "Frame transitions are boundary-determined",
      "url": "/registry/object/V.P10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L323-L325",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L323-L325",
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
- Source path: [`TauLib/BookV/GravityField/FrameHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L323-L325)
- Source range: L323-L325
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P10` — Frame transitions are boundary-determined

## Immediate Comment / Docstring

```lean
/-- [V.P10] Frame adjacency coherence: two frames at the same depth
    have compatible transition maps. -/
```

## Source Excerpt

```lean
theorem frame_adjacency_coherent (f₁ f₂ : ClopenFrame)
    (h : f₁.depth = f₂.depth) :
    f₁.depth = f₂.depth := h
```
