---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.lt_of_equiv_left",
  "permalink": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/lt-of-equiv-left/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRatOrder`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRatOrder::TauRat.lt_of_equiv_left",
  "declaration_slug": "lt-of-equiv-left",
  "kind": "theorem",
  "name": "TauRat.lt_of_equiv_left",
  "module_name": "TauLib.BookI.Boundary.TauRatOrder",
  "module_url": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/",
  "source_line_start": 131,
  "source_line_end": 135,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatOrder.lean#L131-L135",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatOrder.lean#L131-L135",
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
- Source path: [`TauLib/BookI/Boundary/TauRatOrder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatOrder.lean#L131-L135)
- Source range: L131-L135
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- lt is preserved by equiv on the left. -/
```

## Source Excerpt

```lean
theorem TauRat.lt_of_equiv_left {a a' b : TauRat}
    (h_equiv : TauRat.equiv a a') (h_lt : TauRat.lt a b) : TauRat.lt a' b := by
  unfold TauRat.lt at *
  rw [← (equiv_iff_toRat_eq a a').mp h_equiv]
  exact h_lt
```
