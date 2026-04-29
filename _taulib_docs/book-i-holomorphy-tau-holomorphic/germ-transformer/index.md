---
{
  "projection_kind": "taulib_declaration",
  "title": "GermTransformer",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/germ-transformer/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Holomorphy.TauHolomorphic`.",
  "declaration_id": "TauLib.BookI.Holomorphy.TauHolomorphic::GermTransformer",
  "declaration_slug": "germ-transformer",
  "kind": "structure",
  "name": "GermTransformer",
  "module_name": "TauLib.BookI.Holomorphy.TauHolomorphic",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/",
  "source_line_start": 92,
  "source_line_end": 100,
  "registry_ids": [
    "I.D45"
  ],
  "related_registry_items": [
    {
      "id": "I.D45",
      "title": "Omega-Germ Transformer",
      "url": "/registry/object/I.D45/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L92-L100",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.TauHolomorphic",
        "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L92-L100",
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

- Module: [TauLib.BookI.Holomorphy.TauHolomorphic](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/)
- Source path: [`TauLib/BookI/Holomorphy/TauHolomorphic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L92-L100)
- Source range: L92-L100
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D45` — Omega-Germ Transformer

## Immediate Comment / Docstring

```lean
/-- [I.D45] An ω-germ transformer maps omega-tails to sector-pair values.
    It carries BOTH:
    - A SectorFun giving the D-holomorphic structure (sector independence)
    - A StageFun giving the stagewise evaluation (for tower coherence)
    The SectorFun provides the algebraic structure; the StageFun provides
    the arithmetic evaluation that must be tower-coherent. -/
```

## Source Excerpt

```lean
structure GermTransformer where
  /-- The sector function (D-holomorphic structure). -/
  sector_fun : SectorFun
  /-- The stagewise evaluation (arithmetic structure). -/
  stage_fun : StageFun
  /-- Maximum depth as a τ-native primorial-tower index.
      Wave 38 type-discipline refactor: was `Nat`, elevated to `TauIdx`
      to reflect the τ-stage-index semantics (paper §H4 + Wave 16). -/
  depth : TauIdx
```
