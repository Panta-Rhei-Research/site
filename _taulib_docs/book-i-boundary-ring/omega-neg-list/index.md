---
{
  "projection_kind": "taulib_declaration",
  "title": "omega_neg_list",
  "permalink": "/verify/taulib/docs/book-i-boundary-ring/omega-neg-list/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Ring`.",
  "declaration_id": "TauLib.BookI.Boundary.Ring::omega_neg_list",
  "declaration_slug": "omega-neg-list",
  "kind": "def",
  "name": "omega_neg_list",
  "module_name": "TauLib.BookI.Boundary.Ring",
  "module_url": "/verify/taulib/docs/book-i-boundary-ring/",
  "source_line_start": 120,
  "source_line_end": 122,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L120-L122",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Ring",
        "url": "/verify/taulib/docs/book-i-boundary-ring/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L120-L122",
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

- Module: [TauLib.BookI.Boundary.Ring](/verify/taulib/docs/book-i-boundary-ring/)
- Source path: [`TauLib/BookI/Boundary/Ring.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L120-L122)
- Source range: L120-L122
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- ============================================================
-- COMPONENTWISE NEGATION
-- ============================================================
```

## Source Excerpt

```lean
private def omega_neg_list (n : Nat) : Nat -> List TauIdx
  | 0 => []
  | d + 1 => omega_neg_list n d ++ [(primorial (d + 1) - reduce n (d + 1)) % primorial (d + 1)]
```
