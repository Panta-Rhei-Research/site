---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L264",
  "permalink": "/verify/taulib/docs/book-iv-many-body-condensed-matter/eval-l264/",
  "summary_short": "`eval` declaration in `TauLib.BookIV.ManyBody.CondensedMatter`.",
  "declaration_id": "TauLib.BookIV.ManyBody.CondensedMatter::#eval:264",
  "declaration_slug": "eval-l264",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookIV.ManyBody.CondensedMatter",
  "module_url": "/verify/taulib/docs/book-iv-many-body-condensed-matter/",
  "source_line_start": 264,
  "source_line_end": 266,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/CondensedMatter.lean#L264-L266",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.CondensedMatter",
        "url": "/verify/taulib/docs/book-iv-many-body-condensed-matter/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/CondensedMatter.lean#L264-L266",
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

- Module: [TauLib.BookIV.ManyBody.CondensedMatter](/verify/taulib/docs/book-iv-many-body-condensed-matter/)
- Source path: [`TauLib/BookIV/ManyBody/CondensedMatter.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/CondensedMatter.lean#L264-L266)
- Source range: L264-L266
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
#eval match regime_summary_table with | h :: _ => h.name | [] => ""  -- "Crystal"

end Tau.BookIV.ManyBody
```
