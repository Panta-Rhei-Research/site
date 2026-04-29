---
{
  "projection_kind": "taulib_declaration",
  "title": "NFStep.ofPeel",
  "permalink": "/verify/taulib/docs/book-i-coordinates-normal-form/of-peel/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.NormalForm`.",
  "declaration_id": "TauLib.BookI.Coordinates.NormalForm::NFStep.ofPeel",
  "declaration_slug": "of-peel",
  "kind": "def",
  "name": "NFStep.ofPeel",
  "module_name": "TauLib.BookI.Coordinates.NormalForm",
  "module_url": "/verify/taulib/docs/book-i-coordinates-normal-form/",
  "source_line_start": 44,
  "source_line_end": 46,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NormalForm.lean#L44-L46",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NormalForm.lean#L44-L46",
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
- Source path: [`TauLib/BookI/Coordinates/NormalForm.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NormalForm.lean#L44-L46)
- Source range: L44-L46
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Convert greedy_peel output to NFStep. -/
```

## Source Excerpt

```lean
def NFStep.ofPeel (x : TauIdx) : NFStep :=
  let (a, b, c, d) := greedy_peel x
  { A := a, B := b, C := c, D := d }
```
