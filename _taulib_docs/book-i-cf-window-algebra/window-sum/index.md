---
{
  "projection_kind": "taulib_declaration",
  "title": "windowSum",
  "permalink": "/verify/taulib/docs/book-i-cf-window-algebra/window-sum/",
  "summary_short": "`def` declaration in `TauLib.BookI.CF.WindowAlgebra`.",
  "declaration_id": "TauLib.BookI.CF.WindowAlgebra::windowSum",
  "declaration_slug": "window-sum",
  "kind": "def",
  "name": "windowSum",
  "module_name": "TauLib.BookI.CF.WindowAlgebra",
  "module_url": "/verify/taulib/docs/book-i-cf-window-algebra/",
  "source_line_start": 57,
  "source_line_end": 59,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/CF/WindowAlgebra.lean#L57-L59",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.CF.WindowAlgebra",
        "url": "/verify/taulib/docs/book-i-cf-window-algebra/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/CF/WindowAlgebra.lean#L57-L59",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookI.CF.WindowAlgebra](/verify/taulib/docs/book-i-cf-window-algebra/)
- Source path: [`TauLib/BookI/CF/WindowAlgebra.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/CF/WindowAlgebra.lean#L57-L59)
- Source range: L57-L59
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Window sum W_k(j): sum of `width` consecutive CF terms starting at position `start`.
    Returns 0 if any index is out of bounds. -/
```

## Source Excerpt

```lean
def windowSum (cf : List Nat) (width start : Nat) : Nat :=
  (List.range width).foldl (fun acc i =>
    acc + (cf.getD (start + i) 0)) 0
```
