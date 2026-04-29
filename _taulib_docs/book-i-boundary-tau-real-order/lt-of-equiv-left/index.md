---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.lt_of_equiv_left",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-order/lt-of-equiv-left/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealOrder`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealOrder::TauReal.lt_of_equiv_left",
  "declaration_slug": "lt-of-equiv-left",
  "kind": "theorem",
  "name": "TauReal.lt_of_equiv_left",
  "module_name": "TauLib.BookI.Boundary.TauRealOrder",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-order/",
  "source_line_start": 224,
  "source_line_end": 257,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealOrder.lean#L224-L257",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealOrder.lean#L224-L257",
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
- Source path: [`TauLib/BookI/Boundary/TauRealOrder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealOrder.lean#L224-L257)
- Source range: L224-L257
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `lt` is preserved by `equiv` on the left. -/
```

## Source Excerpt

```lean
theorem TauReal.lt_of_equiv_left {a a' b : TauReal}
    (h_equiv : TauReal.equiv a a') (h_lt : TauReal.lt a b) : TauReal.lt a' b := by
  obtain ⟨k, N, h_gap⟩ := h_lt
  obtain ⟨μ, h_mod⟩ := h_equiv
  -- Pick a half-tolerance at level `2k+1` on the equiv side, so the
  -- difference |a - a'| is below `1/(2k+2)`.  Combined with the `1/(k+1)`
  -- gap  a + 1/(k+1) < b, we keep a strictly positive gap from `a'`
  -- at a refined tolerance.
  refine ⟨2 * k + 1, max N (μ (2 * k + 1)), fun n hn => ?_⟩
  have hn_N : N ≤ n := le_of_max_le_left hn
  have hn_μ : μ (2 * k + 1) ≤ n := le_of_max_le_right hn
  have h_g := h_gap n hn_N
  have h_e := h_mod (2 * k + 1) n hn_μ
  unfold TauRat.lt at h_g h_e ⊢
  rw [toRat_add, TauRat.ofNatRecip_toRat] at h_g
  rw [TauRat.toRat_abs, toRat_sub, TauRat.ofNatRecip_toRat] at h_e
  rw [toRat_add, TauRat.ofNatRecip_toRat]
  -- h_g : a.toRat + 1/(k+1) < b.toRat
  -- h_e : |a.toRat - a'.toRat| < 1/(2k+2)
  -- Goal: a'.toRat + 1/(2k+2) < b.toRat
  -- From h_e:  a.toRat - 1/(2k+2) < a'.toRat < a.toRat + 1/(2k+2)
  --   ⇒  a'.toRat - 1/(2k+2) < a.toRat, so a'.toRat < a.toRat + 1/(2k+2)
  -- Then a'.toRat + 1/(2k+2) < a.toRat + 2/(2k+2) = a.toRat + 1/(k+1) < b.toRat
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
