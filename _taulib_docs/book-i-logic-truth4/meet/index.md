---
{
  "projection_kind": "taulib_declaration",
  "title": "Truth4.meet",
  "permalink": "/verify/taulib/docs/book-i-logic-truth4/meet/",
  "summary_short": "`def` declaration in `TauLib.BookI.Logic.Truth4`.",
  "declaration_id": "TauLib.BookI.Logic.Truth4::Truth4.meet",
  "declaration_slug": "meet",
  "kind": "def",
  "name": "Truth4.meet",
  "module_name": "TauLib.BookI.Logic.Truth4",
  "module_url": "/verify/taulib/docs/book-i-logic-truth4/",
  "source_line_start": 68,
  "source_line_end": 76,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/Truth4.lean#L68-L76",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Logic.Truth4",
        "url": "/verify/taulib/docs/book-i-logic-truth4/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/Truth4.lean#L68-L76",
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

- Module: [TauLib.BookI.Logic.Truth4](/verify/taulib/docs/book-i-logic-truth4/)
- Source path: [`TauLib/BookI/Logic/Truth4.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/Truth4.lean#L68-L76)
- Source range: L68-L76
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Meet (conjunction): greatest lower bound in the diamond lattice. -/
```

## Source Excerpt

```lean
def Truth4.meet : Truth4 -> Truth4 -> Truth4
  | T, b => b
  | a, T => a
  | F, _ => F
  | _, F => F
  | B, B => B
  | N, N => N
  | B, N => F
  | N, B => F
```
