---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L190",
  "permalink": "/corpus/taulib/docs/book-i-topos-functors/eval-l190/",
  "summary_short": "`eval` declaration in `TauLib.BookI.Topos.Functors`.",
  "declaration_id": "TauLib.BookI.Topos.Functors::#eval:190",
  "declaration_slug": "eval-l190",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookI.Topos.Functors",
  "module_url": "/corpus/taulib/docs/book-i-topos-functors/",
  "source_line_start": 190,
  "source_line_end": 190,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/Functors.lean#L190-L190",
  "formal_status": "computed",
  "declaration_role": "computed check",
  "formal_status_label": "computed check",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.Functors",
        "url": "/corpus/taulib/docs/book-i-topos-functors/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/Functors.lean#L190-L190",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "role": "computed check",
      "status": "computed check"
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

- Module: [TauLib.BookI.Topos.Functors](/corpus/taulib/docs/book-i-topos-functors/)
- Source path: [`TauLib/BookI/Topos/Functors.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/Functors.lean#L190-L190)
- Source range: L190-L190
- Kind: `eval`
- Public role: `computed check`
- Formal status hint: `computed check`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- ============================================================
-- SMOKE TESTS
-- ============================================================

-- Functor composition
```

## Source Excerpt

```lean
#eval (double_functor.comp succ_functor).obj_map 5   -- 12
```
