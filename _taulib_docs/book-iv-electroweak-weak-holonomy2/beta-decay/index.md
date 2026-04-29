---
{
  "projection_kind": "taulib_declaration",
  "title": "BetaDecay",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/beta-decay/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.WeakHolonomy2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakHolonomy2::BetaDecay",
  "declaration_slug": "beta-decay",
  "kind": "structure",
  "name": "BetaDecay",
  "module_name": "TauLib.BookIV.Electroweak.WeakHolonomy2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/",
  "source_line_start": 201,
  "source_line_end": 210,
  "registry_ids": [
    "IV.P63"
  ],
  "related_registry_items": [
    {
      "id": "IV.P63",
      "title": "Beta-Decay Rate from Tau-Units",
      "url": "/registry/object/IV.P63/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L201-L210",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakHolonomy2",
        "url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L201-L210",
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

- Module: [TauLib.BookIV.Electroweak.WeakHolonomy2](/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/)
- Source path: [`TauLib/BookIV/Electroweak/WeakHolonomy2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L201-L210)
- Source range: L201-L210
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P63` — Beta-Decay Rate from Tau-Units

## Immediate Comment / Docstring

```lean
/-- [IV.P63] Beta decay (n -> p + e + nu_e_bar) is mediated by
    virtual W exchange: d-quark emits W- which decays to e + nu_e_bar.
    Structural: the transition is a polarity-switching process in A. -/
```

## Source Excerpt

```lean
structure BetaDecay where
  /-- Initial particle. -/
  initial : String
  /-- Final particles. -/
  finals : List String
  /-- Mediator boson. -/
  mediator : String
  /-- The mediator is a W boson. -/
  mediator_is_w : mediator = "W-"
  deriving Repr
```
