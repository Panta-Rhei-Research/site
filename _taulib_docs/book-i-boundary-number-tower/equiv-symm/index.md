---
{
  "projection_kind": "taulib_declaration",
  "title": "TauInt.equiv_symm",
  "permalink": "/corpus/taulib/docs/book-i-boundary-number-tower/equiv-symm/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.NumberTower`.",
  "declaration_id": "TauLib.BookI.Boundary.NumberTower::TauInt.equiv_symm",
  "declaration_slug": "equiv-symm",
  "kind": "theorem",
  "name": "TauInt.equiv_symm",
  "module_name": "TauLib.BookI.Boundary.NumberTower",
  "module_url": "/corpus/taulib/docs/book-i-boundary-number-tower/",
  "source_line_start": 94,
  "source_line_end": 98,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumberTower.lean#L94-L98",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.NumberTower",
        "url": "/corpus/taulib/docs/book-i-boundary-number-tower/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumberTower.lean#L94-L98",
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

- Module: [TauLib.BookI.Boundary.NumberTower](/corpus/taulib/docs/book-i-boundary-number-tower/)
- Source path: [`TauLib/BookI/Boundary/NumberTower.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumberTower.lean#L94-L98)
- Source range: L94-L98
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- TauInt equivalence is symmetric. -/
```

## Source Excerpt

```lean
theorem TauInt.equiv_symm {a b : TauInt} (h : TauInt.equiv a b) :
    TauInt.equiv b a := by
  show b.pos + a.neg = a.pos + b.neg
  have h' : a.pos + b.neg = b.pos + a.neg := h
  simp only [TauIdx] at *; omega
```
