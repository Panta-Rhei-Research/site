---
{
  "projection_kind": "taulib_declaration",
  "title": "PPASFitness",
  "permalink": "/verify/taulib/docs/book-vi-consumer-evolution/ppasfitness/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Consumer.Evolution`.",
  "declaration_id": "TauLib.BookVI.Consumer.Evolution::PPASFitness",
  "declaration_slug": "ppasfitness",
  "kind": "structure",
  "name": "PPASFitness",
  "module_name": "TauLib.BookVI.Consumer.Evolution",
  "module_url": "/verify/taulib/docs/book-vi-consumer-evolution/",
  "source_line_start": 35,
  "source_line_end": 44,
  "registry_ids": [
    "VI.D50"
  ],
  "related_registry_items": [
    {
      "id": "VI.D50",
      "title": "PPAS Algorithm on Fitness Landscapes",
      "url": "/registry/object/VI.D50/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Evolution.lean#L35-L44",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Consumer.Evolution",
        "url": "/verify/taulib/docs/book-vi-consumer-evolution/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Evolution.lean#L35-L44",
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

- Module: [TauLib.BookVI.Consumer.Evolution](/verify/taulib/docs/book-vi-consumer-evolution/)
- Source path: [`TauLib/BookVI/Consumer/Evolution.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Evolution.lean#L35-L44)
- Source range: L35-L44
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D50` — PPAS Algorithm on Fitness Landscapes

## Immediate Comment / Docstring

```lean
/-- [VI.D50] PPAS Algorithm on Fitness Landscapes.
    Population = Prover, Selection = Verifier (Book III, Part IX).
    The NP-hard fitness landscape optimization (Book III, Part I)
    is solved in polynomial generations by the PPAS protocol:
    mutation proposes, selection verifies, population converges. -/
```

## Source Excerpt

```lean
structure PPASFitness where
  /-- Fitness landscape is NP-hard. -/
  landscape_np_hard : Bool := true
  /-- Population acts as prover. -/
  prover : String := "population"
  /-- Selection acts as verifier. -/
  verifier : String := "selection"
  /-- PPAS achieves polynomial convergence. -/
  polynomial_converge : Bool := true
  deriving Repr
```
