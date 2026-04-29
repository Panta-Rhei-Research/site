---
{
  "projection_kind": "taulib_declaration",
  "title": "swap6_rho_comm",
  "permalink": "/verify/taulib/docs/book-i-orbit-too-many/swap6-rho-comm/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.TooMany`.",
  "declaration_id": "TauLib.BookI.Orbit.TooMany::swap6_rho_comm",
  "declaration_slug": "swap6-rho-comm",
  "kind": "theorem",
  "name": "swap6_rho_comm",
  "module_name": "TauLib.BookI.Orbit.TooMany",
  "module_url": "/verify/taulib/docs/book-i-orbit-too-many/",
  "source_line_start": 117,
  "source_line_end": 119,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/TooMany.lean#L117-L119",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.TooMany",
        "url": "/verify/taulib/docs/book-i-orbit-too-many/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/TooMany.lean#L117-L119",
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

- Module: [TauLib.BookI.Orbit.TooMany](/verify/taulib/docs/book-i-orbit-too-many/)
- Source path: [`TauLib/BookI/Orbit/TooMany.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/TooMany.lean#L117-L119)
- Source range: L117-L119
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- swap6 commutes with ρ₆. -/
```

## Source Excerpt

```lean
theorem swap6_rho_comm (x : Obj6) : swap6 (rho6 x) = rho6 (swap6 x) := by
  cases x with | mk s d =>
  cases s <;> rfl
```
