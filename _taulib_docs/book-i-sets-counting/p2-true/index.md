---
{
  "projection_kind": "taulib_declaration",
  "title": "p2_true",
  "permalink": "/verify/taulib/docs/book-i-sets-counting/p2-true/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.Counting`.",
  "declaration_id": "TauLib.BookI.Sets.Counting::p2_true",
  "declaration_slug": "p2-true",
  "kind": "theorem",
  "name": "p2_true",
  "module_name": "TauLib.BookI.Sets.Counting",
  "module_url": "/verify/taulib/docs/book-i-sets-counting/",
  "source_line_start": 168,
  "source_line_end": 169,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Counting.lean#L168-L169",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.Counting",
        "url": "/verify/taulib/docs/book-i-sets-counting/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Counting.lean#L168-L169",
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

- Module: [TauLib.BookI.Sets.Counting](/verify/taulib/docs/book-i-sets-counting/)
- Source path: [`TauLib/BookI/Sets/Counting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Counting.lean#L168-L169)
- Source range: L168-L169
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- P2 is provably true: no Russell set exists. -/
```

## Source Excerpt

```lean
theorem p2_true : ¬ exists (R : TauIdx), forall (a : TauIdx), tau_mem a R <-> ¬ tau_mem a R :=
  no_russell_set
```
