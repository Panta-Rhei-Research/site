---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.add_lt_add_left",
  "permalink": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/add-lt-add-left/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRatOrder`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRatOrder::TauRat.add_lt_add_left",
  "declaration_slug": "add-lt-add-left",
  "kind": "theorem",
  "name": "TauRat.add_lt_add_left",
  "module_name": "TauLib.BookI.Boundary.TauRatOrder",
  "module_url": "/corpus/taulib/docs/book-i-boundary-tau-rat-order/",
  "source_line_start": 179,
  "source_line_end": 209,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatOrder.lean#L179-L209",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatOrder.lean#L179-L209",
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
- Source path: [`TauLib/BookI/Boundary/TauRatOrder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatOrder.lean#L179-L209)
- Source range: L179-L209
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Adding the same value on the left preserves lt. -/
```

## Source Excerpt

```lean
theorem TauRat.add_lt_add_left (c : TauRat) {a b : TauRat} (h : TauRat.lt a b) :
    TauRat.lt (c.add a) (c.add b) := by
  unfold TauRat.lt at *
  rw [toRat_add, toRat_add]
  exact _root_.add_lt_add_right h c.toRat

-- ============================================================
-- PART 7: LEAN CORE LT / LE HIERARCHY ALIGNMENT
-- ============================================================

/-!
Wire `TauRat.lt` and `TauRat.le` into Lean core's `LT` / `LE` type-class
hierarchy so that the usual `a < b` and `a ≤ b` notation works on
`TauRat` values.  Lean's `LT` / `LE` classes are in `Init.Core` (not
Mathlib), so these instances pull in no content modules and respect
the tactics-only Mathlib policy.

The instances make `a < b` and `TauRat.lt a b` definitionally equal,
so existing proofs that quote `TauRat.lt ...` continue to work and
consumers can use either spelling freely.
-/

instance : LT TauRat := ⟨TauRat.lt⟩

instance : LE TauRat := ⟨TauRat.le⟩

/-- `a < b` on `TauRat` unfolds to `TauRat.lt a b` by definition. -/
@[simp] theorem TauRat.lt_iff (a b : TauRat) : a < b ↔ TauRat.lt a b := Iff.rfl

/-- `a ≤ b` on `TauRat` unfolds to `TauRat.le a b` by definition. -/
@[simp] theorem TauRat.le_iff (a b : TauRat) : a ≤ b ↔ TauRat.le a b := Iff.rfl
```
