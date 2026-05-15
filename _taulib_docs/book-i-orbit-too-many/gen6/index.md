---
{
  "projection_kind": "taulib_declaration",
  "title": "Gen6",
  "permalink": "/corpus/taulib/docs/book-i-orbit-too-many/gen6/",
  "summary_short": "`inductive` declaration in `TauLib.BookI.Orbit.TooMany`.",
  "declaration_id": "TauLib.BookI.Orbit.TooMany::Gen6",
  "declaration_slug": "gen6",
  "kind": "inductive",
  "name": "Gen6",
  "module_name": "TauLib.BookI.Orbit.TooMany",
  "module_url": "/corpus/taulib/docs/book-i-orbit-too-many/",
  "source_line_start": 37,
  "source_line_end": 46,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/TooMany.lean#L37-L46",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.TooMany",
        "url": "/corpus/taulib/docs/book-i-orbit-too-many/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/TooMany.lean#L37-L46",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookI.Orbit.TooMany](/corpus/taulib/docs/book-i-orbit-too-many/)
- Source path: [`TauLib/BookI/Orbit/TooMany.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/TooMany.lean#L37-L46)
- Source range: L37-L46
- Kind: `inductive`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A hypothetical 6-generator alphabet: α, π, γ, η, ζ, ω. -/
```

## Source Excerpt

```lean
inductive Gen6 : Type where
  | alpha : Gen6
  | pi    : Gen6
  | gamma : Gen6
  | eta   : Gen6
  | zeta  : Gen6   -- the extra generator
  | omega : Gen6
  deriving DecidableEq, Repr

open Gen6
```
