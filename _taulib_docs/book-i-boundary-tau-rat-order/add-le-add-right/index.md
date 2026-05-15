---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.add_le_add_right",
  "permalink": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/add-le-add-right/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRatOrder`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRatOrder::TauRat.add_le_add_right",
  "declaration_slug": "add-le-add-right",
  "kind": "theorem",
  "name": "TauRat.add_le_add_right",
  "module_name": "TauLib.BookI.Boundary.TauRatOrder",
  "module_url": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/",
  "source_line_start": 172,
  "source_line_end": 176,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatOrder.lean#L172-L176",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRatOrder",
        "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatOrder.lean#L172-L176",
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

- Module: [TauLib.BookI.Boundary.TauRatOrder](/corpus/taulib/docs/book-i-boundary-tau-rat-order/)
- Source path: [`TauLib/BookI/Boundary/TauRatOrder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatOrder.lean#L172-L176)
- Source range: L172-L176
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Adding the same value preserves le. -/
```

## Source Excerpt

```lean
theorem TauRat.add_le_add_right {a b : TauRat} (h : TauRat.le a b) (c : TauRat) :
    TauRat.le (a.add c) (b.add c) := by
  unfold TauRat.le at *
  rw [toRat_add, toRat_add]
  exact _root_.add_le_add_left h c.toRat
```
