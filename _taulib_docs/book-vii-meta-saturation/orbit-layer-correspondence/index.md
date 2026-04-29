---
{
  "projection_kind": "taulib_declaration",
  "title": "orbit_layer_correspondence",
  "permalink": "/verify/taulib/docs/book-vii-meta-saturation/orbit-layer-correspondence/",
  "summary_short": "`def` declaration in `TauLib.BookVII.Meta.Saturation`.",
  "declaration_id": "TauLib.BookVII.Meta.Saturation::orbit_layer_correspondence",
  "declaration_slug": "orbit-layer-correspondence",
  "kind": "def",
  "name": "orbit_layer_correspondence",
  "module_name": "TauLib.BookVII.Meta.Saturation",
  "module_url": "/verify/taulib/docs/book-vii-meta-saturation/",
  "source_line_start": 352,
  "source_line_end": 356,
  "registry_ids": [
    "VII.P03"
  ],
  "related_registry_items": [
    {
      "id": "VII.P03",
      "title": "Four-Orbit Implies Four-Layer",
      "url": "/registry/object/VII.P03/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L352-L356",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Saturation",
        "url": "/verify/taulib/docs/book-vii-meta-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L352-L356",
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

- Module: [TauLib.BookVII.Meta.Saturation](/verify/taulib/docs/book-vii-meta-saturation/)
- Source path: [`TauLib/BookVII/Meta/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L352-L356)
- Source range: L352-L356
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `VII.P03` — Four-Orbit Implies Four-Layer

## Immediate Comment / Docstring

```lean
/-- [VII.P03] Four-Orbit Implies Four-Layer: structural correspondence.
    - Identity orbit {α} ↔ E₀ (mathematics)
    - Lobe orbit {π,π′} ↔ E₁ (physics)
    - Crossing orbit {π″} ↔ E₂ (life)
    - Closure orbit {ω} ↔ E₃ (metaphysics)
    Orbit closure = enrichment saturation. -/
```

## Source Excerpt

```lean
def orbit_layer_correspondence : Orbit → EnrichLayer
  | .identity => .e0
  | .lobes    => .e1
  | .crossing => .e2
  | .closure  => .e3
```
