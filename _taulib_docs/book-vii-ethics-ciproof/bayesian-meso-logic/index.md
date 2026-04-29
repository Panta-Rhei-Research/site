---
{
  "projection_kind": "taulib_declaration",
  "title": "BayesianMesoLogic",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/bayesian-meso-logic/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::BayesianMesoLogic",
  "declaration_slug": "bayesian-meso-logic",
  "kind": "structure",
  "name": "BayesianMesoLogic",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 620,
  "source_line_end": 627,
  "registry_ids": [
    "VII.D58"
  ],
  "related_registry_items": [
    {
      "id": "VII.D58",
      "title": "Bayesian Meso-Logic",
      "url": "/registry/object/VII.D58/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L620-L627",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Ethics.CIProof",
        "url": "/verify/taulib/docs/book-vii-ethics-ciproof/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L620-L627",
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

- Module: [TauLib.BookVII.Ethics.CIProof](/verify/taulib/docs/book-vii-ethics-ciproof/)
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L620-L627)
- Source range: L620-L627
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D58` — Bayesian Meso-Logic

## Immediate Comment / Docstring

```lean
/-- [VII.D58] Bayesian Meso-Logic (ch39). Multi-address probabilistic
    logic: across multiple NF-addresses, propositions carry probability
    weights. Bayesian updating as the coherence criterion. -/
```

## Source Excerpt

```lean
structure BayesianMesoLogic where
  /-- Multi-address scope. -/
  multi_address : Bool := true
  /-- Probabilistic truth values. -/
  probabilistic : Bool := true
  /-- Bayesian updating. -/
  bayesian_update : Bool := true
  deriving Repr
```
