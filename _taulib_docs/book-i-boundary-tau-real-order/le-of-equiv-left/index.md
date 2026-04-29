---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.le_of_equiv_left",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-order/le-of-equiv-left/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealOrder`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealOrder::TauReal.le_of_equiv_left",
  "declaration_slug": "le-of-equiv-left",
  "kind": "theorem",
  "name": "TauReal.le_of_equiv_left",
  "module_name": "TauLib.BookI.Boundary.TauRealOrder",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-order/",
  "source_line_start": 286,
  "source_line_end": 310,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealOrder.lean#L286-L310",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealOrder.lean#L286-L310",
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
- Source path: [`TauLib/BookI/Boundary/TauRealOrder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealOrder.lean#L286-L310)
- Source range: L286-L310
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `le` is preserved by `equiv` on the left. -/
```

## Source Excerpt

```lean
theorem TauReal.le_of_equiv_left {a a' b : TauReal}
    (h_equiv : TauReal.equiv a a') (h_le : TauReal.le a b) : TauReal.le a' b := by
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
  have h_abs : ((a.approx n).toRat - (a'.approx n).toRat) < 1 / ((2 * k + 1 : Nat) + 1) ∧
               -((a.approx n).toRat - (a'.approx n).toRat) < 1 / ((2 * k + 1 : Nat) + 1) := by
    constructor
    · have := abs_lt.mp h_e
      linarith [this.2]
    · have := abs_lt.mp h_e
      linarith [this.1]
  have h_sum : (1 : Rat) / ((2 * k + 1 : Nat) + 1) + 1 / ((2 * k + 1 : Nat) + 1)
               = 1 / ((k : Rat) + 1) := by
    push_cast; field_simp; ring
  linarith
```
