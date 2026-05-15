---
{
  "projection_kind": "taulib_declaration",
  "title": "getD_eq_getElem",
  "permalink": "/corpus/taulib/docs/book-i-boundary-ring/get-d-eq-get-elem/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Ring`.",
  "declaration_id": "TauLib.BookI.Boundary.Ring::getD_eq_getElem",
  "declaration_slug": "get-d-eq-get-elem",
  "kind": "theorem",
  "name": "getD_eq_getElem",
  "module_name": "TauLib.BookI.Boundary.Ring",
  "module_url": "/corpus/taulib/docs/book-i-boundary-ring/",
  "source_line_start": 44,
  "source_line_end": 46,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L44-L46",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Ring",
        "url": "/corpus/taulib/docs/book-i-boundary-ring/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L44-L46",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Boundary.Ring](/corpus/taulib/docs/book-i-boundary-ring/)
- Source path: [`TauLib/BookI/Boundary/Ring.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L44-L46)
- Source range: L44-L46
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- ============================================================
-- UTILITY
-- ============================================================
```

## Source Excerpt

```lean
private theorem getD_eq_getElem (l : List TauIdx) (i : Nat) (d : TauIdx) (h : i < l.length) :
    l.getD i d = l[i] := by
  simp [List.getD, h]
```
