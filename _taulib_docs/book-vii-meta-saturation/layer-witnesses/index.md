---
{
  "projection_kind": "taulib_declaration",
  "title": "layer_witnesses",
  "permalink": "/verify/taulib/docs/book-vii-meta-saturation/layer-witnesses/",
  "summary_short": "`def` declaration in `TauLib.BookVII.Meta.Saturation`.",
  "declaration_id": "TauLib.BookVII.Meta.Saturation::layer_witnesses",
  "declaration_slug": "layer-witnesses",
  "kind": "def",
  "name": "layer_witnesses",
  "module_name": "TauLib.BookVII.Meta.Saturation",
  "module_url": "/verify/taulib/docs/book-vii-meta-saturation/",
  "source_line_start": 59,
  "source_line_end": 63,
  "registry_ids": [
    "VII.L03"
  ],
  "related_registry_items": [
    {
      "id": "VII.L03",
      "title": "Non-Emptiness at Each Layer",
      "url": "/registry/object/VII.L03/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L59-L63",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L59-L63",
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
- Source path: [`TauLib/BookVII/Meta/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L59-L63)
- Source range: L59-L63
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `VII.L03` — Non-Emptiness at Each Layer

## Immediate Comment / Docstring

```lean
/-- [VII.L03] Non-emptiness at each layer: constructive witnesses.
    - E₀: Kernel K_τ (NF-addressable objects)
    - E₁: Four holonomy sectors of boundary algebra
    - E₂: Life predicate (Distinction + SelfDesc)
    - E₃: BH basin law-code (SelfDesc²) -/
```

## Source Excerpt

```lean
def layer_witnesses : List LayerWitness :=
  [ ⟨.e0, "kernel", true⟩
  , ⟨.e1, "holonomy_sectors", true⟩
  , ⟨.e2, "life_predicate", true⟩
  , ⟨.e3, "bh_basin_law_code", true⟩ ]
```
