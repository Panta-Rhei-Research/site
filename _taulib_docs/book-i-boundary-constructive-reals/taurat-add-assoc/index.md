---
{
  "projection_kind": "taulib_declaration",
  "title": "taurat_add_assoc",
  "permalink": "/verify/taulib/docs/book-i-boundary-constructive-reals/taurat-add-assoc/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.ConstructiveReals`.",
  "declaration_id": "TauLib.BookI.Boundary.ConstructiveReals::taurat_add_assoc",
  "declaration_slug": "taurat-add-assoc",
  "kind": "theorem",
  "name": "taurat_add_assoc",
  "module_name": "TauLib.BookI.Boundary.ConstructiveReals",
  "module_url": "/verify/taulib/docs/book-i-boundary-constructive-reals/",
  "source_line_start": 63,
  "source_line_end": 68,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L63-L68",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.ConstructiveReals",
        "url": "/verify/taulib/docs/book-i-boundary-constructive-reals/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L63-L68",
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

- Module: [TauLib.BookI.Boundary.ConstructiveReals](/verify/taulib/docs/book-i-boundary-constructive-reals/)
- Source path: [`TauLib/BookI/Boundary/ConstructiveReals.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L63-L68)
- Source range: L63-L68
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Addition is associative up to equiv. -/
```

## Source Excerpt

```lean
theorem taurat_add_assoc (a b c : TauRat) :
    TauRat.equiv ((a.add b).add c) (a.add (b.add c)) := by
  simp only [TauRat.equiv, TauRat.add]
  rw [equiv_iff_toInt_eq]
  simp only [toInt_mul, toInt_add, toInt_fromNat]
  push_cast; ring
```
