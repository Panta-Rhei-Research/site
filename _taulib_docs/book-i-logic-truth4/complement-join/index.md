---
{
  "projection_kind": "taulib_declaration",
  "title": "Truth4.complement_join",
  "permalink": "/verify/taulib/docs/book-i-logic-truth4/complement-join/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Logic.Truth4`.",
  "declaration_id": "TauLib.BookI.Logic.Truth4::Truth4.complement_join",
  "declaration_slug": "complement-join",
  "kind": "theorem",
  "name": "Truth4.complement_join",
  "module_name": "TauLib.BookI.Logic.Truth4",
  "module_url": "/verify/taulib/docs/book-i-logic-truth4/",
  "source_line_start": 226,
  "source_line_end": 227,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/Truth4.lean#L226-L227",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/Truth4.lean#L226-L227",
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

- Module: [TauLib.BookI.Logic.Truth4](/verify/taulib/docs/book-i-logic-truth4/)
- Source path: [`TauLib/BookI/Logic/Truth4.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/Truth4.lean#L226-L227)
- Source range: L226-L227
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Complement law: join a (neg a) = T for all a. -/
```

## Source Excerpt

```lean
theorem Truth4.complement_join (a : Truth4) : Truth4.join a (Truth4.neg a) = T := by
  cases a <;> rfl
```
