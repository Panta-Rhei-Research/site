---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L302",
  "permalink": "/verify/taulib/docs/book-i-topos-h6-earned-categorical-machine/eval-l302/",
  "summary_short": "`eval` declaration in `TauLib.BookI.Topos.H6EarnedCategoricalMachine`.",
  "declaration_id": "TauLib.BookI.Topos.H6EarnedCategoricalMachine::#eval:302",
  "declaration_slug": "eval-l302",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookI.Topos.H6EarnedCategoricalMachine",
  "module_url": "/verify/taulib/docs/book-i-topos-h6-earned-categorical-machine/",
  "source_line_start": 302,
  "source_line_end": 302,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H6EarnedCategoricalMachine.lean#L302-L302",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.H6EarnedCategoricalMachine",
        "url": "/verify/taulib/docs/book-i-topos-h6-earned-categorical-machine/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H6EarnedCategoricalMachine.lean#L302-L302",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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

- Module: [TauLib.BookI.Topos.H6EarnedCategoricalMachine](/verify/taulib/docs/book-i-topos-h6-earned-categorical-machine/)
- Source path: [`TauLib/BookI/Topos/H6EarnedCategoricalMachine.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H6EarnedCategoricalMachine.lean#L302-L302)
- Source range: L302-L302
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- Associativity at concrete inputs
```

## Source Excerpt

```lean
#eval (StageFun.comp (StageFun.comp chi_plus_stage chi_minus_stage) id_stage).b_fun 42 5
```
