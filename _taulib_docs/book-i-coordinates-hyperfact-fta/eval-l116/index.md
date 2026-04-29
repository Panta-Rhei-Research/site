---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L116",
  "permalink": "/verify/taulib/docs/book-i-coordinates-hyperfact-fta/eval-l116/",
  "summary_short": "`eval` declaration in `TauLib.BookI.Coordinates.HyperfactFTA`.",
  "declaration_id": "TauLib.BookI.Coordinates.HyperfactFTA::#eval:116",
  "declaration_slug": "eval-l116",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookI.Coordinates.HyperfactFTA",
  "module_url": "/verify/taulib/docs/book-i-coordinates-hyperfact-fta/",
  "source_line_start": 116,
  "source_line_end": 116,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactFTA.lean#L116-L116",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.HyperfactFTA",
        "url": "/verify/taulib/docs/book-i-coordinates-hyperfact-fta/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactFTA.lean#L116-L116",
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

- Module: [TauLib.BookI.Coordinates.HyperfactFTA](/verify/taulib/docs/book-i-coordinates-hyperfact-fta/)
- Source path: [`TauLib/BookI/Coordinates/HyperfactFTA.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactFTA.lean#L116-L116)
- Source range: L116-L116
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- `12 = 3^1 · 4` is the height-1 ABCD chart of 12 (with A=3 the
-- largest prime divisor).
```

## Source Excerpt

```lean
#eval (3 ^ 1 * 4 = 12 : Bool)  -- true
```
