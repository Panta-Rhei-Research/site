---
{
  "projection_kind": "taulib_declaration",
  "title": "spine_check",
  "permalink": "/verify/taulib/docs/book-i-coordinates-normal-form/spine-check/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.NormalForm`.",
  "declaration_id": "TauLib.BookI.Coordinates.NormalForm::spine_check",
  "declaration_slug": "spine-check",
  "kind": "def",
  "name": "spine_check",
  "module_name": "TauLib.BookI.Coordinates.NormalForm",
  "module_url": "/verify/taulib/docs/book-i-coordinates-normal-form/",
  "source_line_start": 95,
  "source_line_end": 95,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NormalForm.lean#L95-L95",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.NormalForm",
        "url": "/verify/taulib/docs/book-i-coordinates-normal-form/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NormalForm.lean#L95-L95",
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

- Module: [TauLib.BookI.Coordinates.NormalForm](/verify/taulib/docs/book-i-coordinates-normal-form/)
- Source path: [`TauLib/BookI/Coordinates/NormalForm.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NormalForm.lean#L95-L95)
- Source range: L95-L95
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Check that spine(x) reconstructs to x. Computable boolean test. -/
```

## Source Excerpt

```lean
def spine_check (x : TauIdx) : Bool := list_tower_prod (spine x) == x
```
