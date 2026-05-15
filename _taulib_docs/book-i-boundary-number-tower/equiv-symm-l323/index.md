---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.equiv_symm",
  "permalink": "/corpus/taulib/docs/book-i-boundary-number-tower/equiv-symm-l323/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.NumberTower`.",
  "declaration_id": "TauLib.BookI.Boundary.NumberTower::TauRat.equiv_symm",
  "declaration_slug": "equiv-symm-l323",
  "kind": "theorem",
  "name": "TauRat.equiv_symm",
  "module_name": "TauLib.BookI.Boundary.NumberTower",
  "module_url": "/corpus/taulib/docs/book-i-boundary-number-tower/",
  "source_line_start": 323,
  "source_line_end": 326,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumberTower.lean#L323-L326",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumberTower.lean#L323-L326",
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
- Source path: [`TauLib/BookI/Boundary/NumberTower.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumberTower.lean#L323-L326)
- Source range: L323-L326
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- TauRat equivalence is symmetric. -/
```

## Source Excerpt

```lean
theorem TauRat.equiv_symm {a b : TauRat} (h : TauRat.equiv a b) :
    TauRat.equiv b a := by
  simp only [TauRat.equiv] at *
  exact TauInt.equiv_symm h
```
