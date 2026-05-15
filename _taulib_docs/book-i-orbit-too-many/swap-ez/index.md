---
{
  "projection_kind": "taulib_declaration",
  "title": "swap_ez",
  "permalink": "/corpus/taulib/docs/book-i-orbit-too-many/swap-ez/",
  "summary_short": "`def` declaration in `TauLib.BookI.Orbit.TooMany`.",
  "declaration_id": "TauLib.BookI.Orbit.TooMany::swap_ez",
  "declaration_slug": "swap-ez",
  "kind": "def",
  "name": "swap_ez",
  "module_name": "TauLib.BookI.Orbit.TooMany",
  "module_url": "/corpus/taulib/docs/book-i-orbit-too-many/",
  "source_line_start": 99,
  "source_line_end": 102,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/TooMany.lean#L99-L102",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/TooMany.lean#L99-L102",
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

- Module: [TauLib.BookI.Orbit.TooMany](/corpus/taulib/docs/book-i-orbit-too-many/)
- Source path: [`TauLib/BookI/Orbit/TooMany.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/TooMany.lean#L99-L102)
- Source range: L99-L102
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Swap η and ζ, fix everything else. -/
```

## Source Excerpt

```lean
def swap_ez : Gen6 → Gen6
  | eta   => zeta
  | zeta  => eta
  | g     => g
```
