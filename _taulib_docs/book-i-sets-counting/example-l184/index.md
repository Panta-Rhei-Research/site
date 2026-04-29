---
{
  "projection_kind": "taulib_declaration",
  "title": "example at L184",
  "permalink": "/verify/taulib/docs/book-i-sets-counting/example-l184/",
  "summary_short": "`example` declaration in `TauLib.BookI.Sets.Counting`.",
  "declaration_id": "TauLib.BookI.Sets.Counting::#eval:184",
  "declaration_slug": "example-l184",
  "kind": "example",
  "name": null,
  "module_name": "TauLib.BookI.Sets.Counting",
  "module_url": "/verify/taulib/docs/book-i-sets-counting/",
  "source_line_start": 184,
  "source_line_end": 184,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Counting.lean#L184-L184",
  "formal_status": "example",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Counting.lean#L184-L184",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "example",
      "status": "example"
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
- Source path: [`TauLib/BookI/Sets/Counting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Counting.lean#L184-L184)
- Source range: L184-L184
- Kind: `example`
- Formal status hint: `example`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- Expected: { seed := pi, depth := 3 }

-- Encoding injectivity check
```

## Source Excerpt

```lean
example : tauObj_encode ⟨alpha, 0⟩ ≠ tauObj_encode ⟨alpha, 1⟩ := by decide
```
