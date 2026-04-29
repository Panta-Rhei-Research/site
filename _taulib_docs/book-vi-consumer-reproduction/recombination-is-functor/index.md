---
{
  "projection_kind": "taulib_declaration",
  "title": "recombination_is_functor",
  "permalink": "/verify/taulib/docs/book-vi-consumer-reproduction/recombination-is-functor/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.Consumer.Reproduction`.",
  "declaration_id": "TauLib.BookVI.Consumer.Reproduction::recombination_is_functor",
  "declaration_slug": "recombination-is-functor",
  "kind": "theorem",
  "name": "recombination_is_functor",
  "module_name": "TauLib.BookVI.Consumer.Reproduction",
  "module_url": "/verify/taulib/docs/book-vi-consumer-reproduction/",
  "source_line_start": 55,
  "source_line_end": 60,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Reproduction.lean#L55-L60",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Reproduction.lean#L55-L60",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookVI/Consumer/Reproduction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Reproduction.lean#L55-L60)
- Source range: L55-L60
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem recombination_is_functor :
    recomb.input_arity = 2 ∧
    recomb.haploid_fusion = true ∧
    recomb.stochastic = true ∧
    recomb.channels = 2 :=
  ⟨rfl, rfl, rfl, rfl⟩
```
