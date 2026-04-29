---
{
  "projection_kind": "taulib_declaration",
  "title": "HolFun",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/hol-fun/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Holomorphy.TauHolomorphic`.",
  "declaration_id": "TauLib.BookI.Holomorphy.TauHolomorphic::HolFun",
  "declaration_slug": "hol-fun",
  "kind": "structure",
  "name": "HolFun",
  "module_name": "TauLib.BookI.Holomorphy.TauHolomorphic",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/",
  "source_line_start": 117,
  "source_line_end": 121,
  "registry_ids": [
    "I.D47"
  ],
  "related_registry_items": [
    {
      "id": "I.D47",
      "title": "Tau-Holomorphic Function",
      "url": "/registry/object/I.D47/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L117-L121",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L117-L121",
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
- Source path: [`TauLib/BookI/Holomorphy/TauHolomorphic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L117-L121)
- Source range: L117-L121
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D47` — Tau-Holomorphic Function

## Immediate Comment / Docstring

```lean
/-- [I.D47] A τ-holomorphic function (HolFun) is a germ transformer that is:
    1. D-holomorphic (sector-independent — given by the SectorFun structure)
    2. Tower-coherent (compatible with primorial reduction maps)

    The D-holomorphic condition is structural: the SectorFun ensures sector
    independence by construction. The tower coherence condition is the
    additional constraint that makes τ-holomorphy rigid. -/
```

## Source Excerpt

```lean
structure HolFun where
  /-- The underlying germ transformer. -/
  transformer : GermTransformer
  /-- Proof of tower coherence. -/
  coherent : TowerCoherent transformer.stage_fun
```
