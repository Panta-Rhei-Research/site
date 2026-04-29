---
{
  "projection_kind": "taulib_declaration",
  "title": "holfun_comp_rf",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/holfun-comp-rf/",
  "summary_short": "`def` declaration in `TauLib.BookI.Holomorphy.DiagonalProtection`.",
  "declaration_id": "TauLib.BookI.Holomorphy.DiagonalProtection::holfun_comp_rf",
  "declaration_slug": "holfun-comp-rf",
  "kind": "def",
  "name": "holfun_comp_rf",
  "module_name": "TauLib.BookI.Holomorphy.DiagonalProtection",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/",
  "source_line_start": 163,
  "source_line_end": 168,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L163-L168",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.DiagonalProtection",
        "url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L163-L168",
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

- Module: [TauLib.BookI.Holomorphy.DiagonalProtection](/verify/taulib/docs/book-i-holomorphy-diagonal-protection/)
- Source path: [`TauLib/BookI/Holomorphy/DiagonalProtection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L163-L168)
- Source range: L163-L168
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- HolFun composition for reduce-form functions with reduce-compatible maps. -/
```

## Source Excerpt

```lean
def holfun_comp_rf (hf₁ hf₂ : HolFun)
    (rf₁ : ReduceForm hf₁.transformer.stage_fun)
    (rf₂ : ReduceForm hf₂.transformer.stage_fun)
    (hrc_b : ReduceCompat rf₁.b_map) (hrc_c : ReduceCompat rf₁.c_map) : HolFun :=
  ⟨hf₁.transformer.comp hf₂.transformer,
   comp_reduce_coherent _ _ rf₁ rf₂ hf₁.coherent hf₂.coherent hrc_b hrc_c⟩
```
