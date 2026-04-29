---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.lt_iff_le_and_not_equiv",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-rat-order/lt-iff-le-and-not-equiv/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRatOrder`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRatOrder::TauRat.lt_iff_le_and_not_equiv",
  "declaration_slug": "lt-iff-le-and-not-equiv",
  "kind": "theorem",
  "name": "TauRat.lt_iff_le_and_not_equiv",
  "module_name": "TauLib.BookI.Boundary.TauRatOrder",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-rat-order/",
  "source_line_start": 100,
  "source_line_end": 112,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatOrder.lean#L100-L112",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRatOrder",
        "url": "/verify/taulib/docs/book-i-boundary-tau-rat-order/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatOrder.lean#L100-L112",
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

- Module: [TauLib.BookI.Boundary.TauRatOrder](/verify/taulib/docs/book-i-boundary-tau-rat-order/)
- Source path: [`TauLib/BookI/Boundary/TauRatOrder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatOrder.lean#L100-L112)
- Source range: L100-L112
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- lt iff le and not equiv. -/
```

## Source Excerpt

```lean
theorem TauRat.lt_iff_le_and_not_equiv (a b : TauRat) :
    TauRat.lt a b ↔ TauRat.le a b ∧ ¬ TauRat.equiv a b := by
  constructor
  · intro h
    refine ⟨_root_.le_of_lt h, ?_⟩
    intro h_eq
    rw [equiv_iff_toRat_eq] at h_eq
    -- Now h_eq : a.toRat = b.toRat; h : TauRat.lt a b ↔ a.toRat < b.toRat
    unfold TauRat.lt at h
    exact _root_.lt_irrefl _ (h_eq ▸ h)
  · intro ⟨hle, hne⟩
    rw [equiv_iff_toRat_eq] at hne
    exact lt_of_le_of_ne hle hne
```
