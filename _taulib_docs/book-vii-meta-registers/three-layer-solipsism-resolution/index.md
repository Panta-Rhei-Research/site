---
{
  "projection_kind": "taulib_declaration",
  "title": "ThreeLayerSolipsismResolution",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/three-layer-solipsism-resolution/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::ThreeLayerSolipsismResolution",
  "declaration_slug": "three-layer-solipsism-resolution",
  "kind": "structure",
  "name": "ThreeLayerSolipsismResolution",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 924,
  "source_line_end": 933,
  "registry_ids": [
    "VII.D39"
  ],
  "related_registry_items": [
    {
      "id": "VII.D39",
      "title": "Three-Layer Solipsism Resolution",
      "url": "/registry/object/VII.D39/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L924-L933",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Registers",
        "url": "/verify/taulib/docs/book-vii-meta-registers/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L924-L933",
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

- Module: [TauLib.BookVII.Meta.Registers](/verify/taulib/docs/book-vii-meta-registers/)
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L924-L933)
- Source range: L924-L933
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D39` — Three-Layer Solipsism Resolution

## Immediate Comment / Docstring

```lean
/-- [VII.D39] Three-Layer Solipsism Resolution (ch31). Solipsism
    dissolved via three layers:
    (1) Ontic: other minds have NF-addresses (exist structurally)
    (2) Epistemic: register independence gives independent evidence
    (3) Bayesian: solipsism has vanishing posterior under any prior -/
```

## Source Excerpt

```lean
structure ThreeLayerSolipsismResolution where
  /-- (1) Ontic layer: NF-addresses for other minds. -/
  ontic_layer : Bool := true
  /-- (2) Epistemic layer: register independence. -/
  epistemic_layer : Bool := true
  /-- (3) Bayesian layer: vanishing posterior. -/
  bayesian_layer : Bool := true
  /-- Three layers. -/
  layer_count : Nat := 3
  deriving Repr
```
