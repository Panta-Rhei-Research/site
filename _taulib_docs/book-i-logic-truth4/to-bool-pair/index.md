---
{
  "projection_kind": "taulib_declaration",
  "title": "Truth4.toBoolPair",
  "permalink": "/corpus/taulib/docs/book-i-logic-truth4/to-bool-pair/",
  "summary_short": "`def` declaration in `TauLib.BookI.Logic.Truth4`.",
  "declaration_id": "TauLib.BookI.Logic.Truth4::Truth4.toBoolPair",
  "declaration_slug": "to-bool-pair",
  "kind": "def",
  "name": "Truth4.toBoolPair",
  "module_name": "TauLib.BookI.Logic.Truth4",
  "module_url": "/corpus/taulib/docs/book-i-logic-truth4/",
  "source_line_start": 118,
  "source_line_end": 122,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/Truth4.lean#L118-L122",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Logic.Truth4",
        "url": "/corpus/taulib/docs/book-i-logic-truth4/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/Truth4.lean#L118-L122",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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

- Module: [TauLib.BookI.Logic.Truth4](/corpus/taulib/docs/book-i-logic-truth4/)
- Source path: [`TauLib/BookI/Logic/Truth4.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/Truth4.lean#L118-L122)
- Source range: L118-L122
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Encode Truth4 as a pair of Booleans (B-sector, C-sector). -/
```

## Source Excerpt

```lean
def Truth4.toBoolPair : Truth4 -> Bool × Bool
  | T => (true, true)
  | F => (false, false)
  | B => (true, false)
  | N => (false, true)
```
