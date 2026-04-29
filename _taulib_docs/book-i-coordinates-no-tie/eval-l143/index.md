---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L143",
  "permalink": "/verify/taulib/docs/book-i-coordinates-no-tie/eval-l143/",
  "summary_short": "`eval` declaration in `TauLib.BookI.Coordinates.NoTie`.",
  "declaration_id": "TauLib.BookI.Coordinates.NoTie::#eval:143",
  "declaration_slug": "eval-l143",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookI.Coordinates.NoTie",
  "module_url": "/verify/taulib/docs/book-i-coordinates-no-tie/",
  "source_line_start": 143,
  "source_line_end": 143,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NoTie.lean#L143-L143",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.NoTie",
        "url": "/verify/taulib/docs/book-i-coordinates-no-tie/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NoTie.lean#L143-L143",
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

- Module: [TauLib.BookI.Coordinates.NoTie](/verify/taulib/docs/book-i-coordinates-no-tie/)
- Source path: [`TauLib/BookI/Coordinates/NoTie.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NoTie.lean#L143-L143)
- Source range: L143-L143
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- (1, 2, 4, 16)

-- Verify divisibility chain
```

## Source Excerpt

```lean
#eval (16 % 4, 16 % 2, 4 % 2)  -- (0, 0, 0): 2 | 4 | 16
```
