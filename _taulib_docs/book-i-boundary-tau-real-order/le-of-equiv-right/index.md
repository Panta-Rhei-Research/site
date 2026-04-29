---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.le_of_equiv_right",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-order/le-of-equiv-right/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealOrder`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealOrder::TauReal.le_of_equiv_right",
  "declaration_slug": "le-of-equiv-right",
  "kind": "theorem",
  "name": "TauReal.le_of_equiv_right",
  "module_name": "TauLib.BookI.Boundary.TauRealOrder",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-order/",
  "source_line_start": 313,
  "source_line_end": 359,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealOrder.lean#L313-L359",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealOrder",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-order/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealOrder.lean#L313-L359",
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

- Module: [TauLib.BookI.Boundary.TauRealOrder](/verify/taulib/docs/book-i-boundary-tau-real-order/)
- Source path: [`TauLib/BookI/Boundary/TauRealOrder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealOrder.lean#L313-L359)
- Source range: L313-L359
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `le` is preserved by `equiv` on the right. -/
```

## Source Excerpt

```lean
theorem TauReal.le_of_equiv_right {a b b' : TauReal}
    (h_equiv : TauReal.equiv b b') (h_le : TauReal.le a b) : TauReal.le a b' := by
  intro k
  obtain ⟨μ, h_mod⟩ := h_equiv
  obtain ⟨N, h_le_inst⟩ := h_le (2 * k + 1)
  refine ⟨max N (μ (2 * k + 1)), fun n hn => ?_⟩
  have hn_N : N ≤ n := le_of_max_le_left hn
  have hn_μ : μ (2 * k + 1) ≤ n := le_of_max_le_right hn
  have h_L := h_le_inst n hn_N
  have h_e := h_mod (2 * k + 1) n hn_μ
  unfold TauRat.lt at h_L h_e ⊢
  rw [toRat_add, TauRat.ofNatRecip_toRat] at h_L
  rw [TauRat.toRat_abs, toRat_sub, TauRat.ofNatRecip_toRat] at h_e
  rw [toRat_add, TauRat.ofNatRecip_toRat]
  have h_abs : ((b.approx n).toRat - (b'.approx n).toRat) < 1 / ((2 * k + 1 : Nat) + 1) ∧
               -((b.approx n).toRat - (b'.approx n).toRat) < 1 / ((2 * k + 1 : Nat) + 1) := by
    constructor
    · have := abs_lt.mp h_e
      linarith [this.2]
    · have := abs_lt.mp h_e
      linarith [this.1]
  have h_sum : (1 : Rat) / ((2 * k + 1 : Nat) + 1) + 1 / ((2 * k + 1 : Nat) + 1)
               = 1 / ((k : Rat) + 1) := by
    push_cast; field_simp; ring
  linarith

-- ============================================================
-- PART 7: LEAN CORE LT / LE HIERARCHY ALIGNMENT
-- ============================================================

/-!
Wire `TauReal.lt` and `TauReal.le` into Lean core's `LT` / `LE` type-class
hierarchy, matching the Wave 1b alignment for `TauRat`.  Downstream
consumers can use `a < b` and `a ≤ b` on `TauReal` values.
-/

instance : LT TauReal := ⟨TauReal.lt⟩

instance : LE TauReal := ⟨TauReal.le⟩

/-- `a < b` on `TauReal` unfolds to `TauReal.lt a b` by definition. -/
@[simp] theorem TauReal.lt_iff (a b : TauReal) : a < b ↔ TauReal.lt a b := Iff.rfl

/-- `a ≤ b` on `TauReal` unfolds to `TauReal.le a b` by definition. -/
@[simp] theorem TauReal.le_iff (a b : TauReal) : a ≤ b ↔ TauReal.le a b := Iff.rfl

end Tau.Boundary
```
