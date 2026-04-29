---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.abs_sub_abs_le_abs_sub_toRat",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-abs/abs-sub-abs-le-abs-sub-to-rat/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealAbs`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealAbs::TauRat.abs_sub_abs_le_abs_sub_toRat",
  "declaration_slug": "abs-sub-abs-le-abs-sub-to-rat",
  "kind": "theorem",
  "name": "TauRat.abs_sub_abs_le_abs_sub_toRat",
  "module_name": "TauLib.BookI.Boundary.TauRealAbs",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-abs/",
  "source_line_start": 96,
  "source_line_end": 99,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAbs.lean#L96-L99",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealAbs",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-abs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAbs.lean#L96-L99",
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

- Module: [TauLib.BookI.Boundary.TauRealAbs](/verify/taulib/docs/book-i-boundary-tau-real-abs/)
- Source path: [`TauLib/BookI/Boundary/TauRealAbs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAbs.lean#L96-L99)
- Source range: L96-L99
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Reverse triangle inequality at the TauRat toRat level:
    `||a.toRat| - |b.toRat|| ≤ |a.toRat - b.toRat|`. -/
```

## Source Excerpt

```lean
private theorem TauRat.abs_sub_abs_le_abs_sub_toRat (a b : TauRat) :
    |a.abs.toRat - b.abs.toRat| ≤ |a.toRat - b.toRat| := by
  rw [TauRat.toRat_abs, TauRat.toRat_abs]
  exact abs_abs_sub_abs_le_abs_sub (a.toRat) (b.toRat)
```
