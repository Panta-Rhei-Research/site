---
{
  "projection_kind": "taulib_declaration",
  "title": "RecombinationFunctor",
  "permalink": "/verify/taulib/docs/book-vi-consumer-reproduction/recombination-functor/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Consumer.Reproduction`.",
  "declaration_id": "TauLib.BookVI.Consumer.Reproduction::RecombinationFunctor",
  "declaration_slug": "recombination-functor",
  "kind": "structure",
  "name": "RecombinationFunctor",
  "module_name": "TauLib.BookVI.Consumer.Reproduction",
  "module_url": "/verify/taulib/docs/book-vi-consumer-reproduction/",
  "source_line_start": 34,
  "source_line_end": 47,
  "registry_ids": [
    "VI.D49"
  ],
  "related_registry_items": [
    {
      "id": "VI.D49",
      "title": "Recombination Functor",
      "url": "/registry/object/VI.D49/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Reproduction.lean#L34-L47",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Consumer.Reproduction",
        "url": "/verify/taulib/docs/book-vi-consumer-reproduction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Reproduction.lean#L34-L47",
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

- Module: [TauLib.BookVI.Consumer.Reproduction](/verify/taulib/docs/book-vi-consumer-reproduction/)
- Source path: [`TauLib/BookVI/Consumer/Reproduction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Reproduction.lean#L34-L47)
- Source range: L34-L47
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D49` — Recombination Functor

## Immediate Comment / Docstring

```lean
/-- [VI.D49] Recombination Functor: binary input, stochastic output.
    Gamete fusion: two haploid inputs → one diploid output.
    The two lemniscate lobes (Book II, Part III) provide
    two independent channels for gamete production. -/
```

## Source Excerpt

```lean
structure RecombinationFunctor where
  /-- Number of inputs (gametes). -/
  input_arity : Nat
  /-- Binary: exactly 2 inputs. -/
  arity_eq : input_arity = 2
  /-- Haploid fusion produces diploid. -/
  haploid_fusion : Bool := true
  /-- Crossover is stochastic. -/
  stochastic : Bool := true
  /-- Number of gamete channels (= lemniscate lobes). -/
  channels : Nat
  /-- Exactly 2 channels. -/
  channels_eq : channels = 2
  deriving Repr
```
