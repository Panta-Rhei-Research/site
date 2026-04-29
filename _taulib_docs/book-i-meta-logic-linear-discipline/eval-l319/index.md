---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L319",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l319/",
  "summary_short": "`eval` declaration in `TauLib.BookI.MetaLogic.LinearDiscipline`.",
  "declaration_id": "TauLib.BookI.MetaLogic.LinearDiscipline::#eval:319",
  "declaration_slug": "eval-l319",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookI.MetaLogic.LinearDiscipline",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/",
  "source_line_start": 319,
  "source_line_end": 321,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L319-L321",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.MetaLogic.LinearDiscipline",
        "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L319-L321",
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

- Module: [TauLib.BookI.MetaLogic.LinearDiscipline](/verify/taulib/docs/book-i-meta-logic-linear-discipline/)
- Source path: [`TauLib/BookI/MetaLogic/LinearDiscipline.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L319-L321)
- Source range: L319-L321
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- Cut-elimination additivity
```

## Source Excerpt

```lean
#eval Tau.Denotation.countRho [.rho_inst, .sigma_inst .alpha .pi, .rho_inst]  -- 2

end Tau.MetaLogic
```
