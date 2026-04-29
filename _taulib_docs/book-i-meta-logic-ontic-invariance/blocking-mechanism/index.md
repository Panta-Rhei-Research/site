---
{
  "projection_kind": "taulib_declaration",
  "title": "BlockingMechanism",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-ontic-invariance/blocking-mechanism/",
  "summary_short": "`inductive` declaration in `TauLib.BookI.MetaLogic.OnticInvariance`.",
  "declaration_id": "TauLib.BookI.MetaLogic.OnticInvariance::BlockingMechanism",
  "declaration_slug": "blocking-mechanism",
  "kind": "inductive",
  "name": "BlockingMechanism",
  "module_name": "TauLib.BookI.MetaLogic.OnticInvariance",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-ontic-invariance/",
  "source_line_start": 30,
  "source_line_end": 34,
  "registry_ids": [
    "I.T46"
  ],
  "related_registry_items": [
    {
      "id": "I.T46",
      "title": "Ontic Identity Invariance",
      "url": "/registry/object/I.T46/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/OnticInvariance.lean#L30-L34",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.MetaLogic.OnticInvariance",
        "url": "/verify/taulib/docs/book-i-meta-logic-ontic-invariance/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/OnticInvariance.lean#L30-L34",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookI.MetaLogic.OnticInvariance](/verify/taulib/docs/book-i-meta-logic-ontic-invariance/)
- Source path: [`TauLib/BookI/MetaLogic/OnticInvariance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/OnticInvariance.lean#L30-L34)
- Source range: L30-L34
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `I.T46` — Ontic Identity Invariance

## Immediate Comment / Docstring

```lean
/-- [I.T46] The three mechanisms that block diagonal resonance in τ. -/
```

## Source Excerpt

```lean
inductive BlockingMechanism where
  | k5_diagonal_discipline    -- Blocks (L): no free contraction at ontic level
  | nf_confluence             -- Blocks (E): unique normal forms, decidable identity
  | star_autonomous_structure -- Blocks (P): no free self-products/diagonals
  deriving DecidableEq, Repr
```
