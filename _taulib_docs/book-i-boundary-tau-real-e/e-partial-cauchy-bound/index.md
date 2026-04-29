---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.e_partial_cauchy_bound",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-e/e-partial-cauchy-bound/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealE`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealE::TauReal.e_partial_cauchy_bound",
  "declaration_slug": "e-partial-cauchy-bound",
  "kind": "theorem",
  "name": "TauReal.e_partial_cauchy_bound",
  "module_name": "TauLib.BookI.Boundary.TauRealE",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-e/",
  "source_line_start": 135,
  "source_line_end": 171,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealE.lean#L135-L171",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealE",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-e/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealE.lean#L135-L171",
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

- Module: [TauLib.BookI.Boundary.TauRealE](/verify/taulib/docs/book-i-boundary-tau-real-e/)
- Source path: [`TauLib/BookI/Boundary/TauRealE.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealE.lean#L135-L171)
- Source range: L135-L171
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- ============================================================
-- PART 4: MAIN Cauchy BOUND  |e_partial m − e_partial n| ≤ 4/2^n
-- ============================================================
```

## Source Excerpt

```lean
theorem TauReal.e_partial_cauchy_bound (m n : Nat) (hn : 1 ≤ n) (hnm : n ≤ m) :
    |((TauRat.e_partial m).toRat - (TauRat.e_partial n).toRat)|
      ≤ 4 / (2 ^ n : Rat) := by
  unfold TauRat.e_partial
  rw [TauRat.sum_sub_toRat_eq_sumFromTo TauRat.e_term n m hnm]
  have h_tri := TauRat.sumFromTo_abs_le TauRat.e_term n m
  have h_strong := TauReal.sumFromTo_e_term_bound n hn m hnm
  -- |e_term k| = e_term k at toRat, so sumFromTo |e_term| n m = sumFromTo e_term n m.
  have h_abs_eq : (TauRat.sumFromTo (fun k => (TauRat.e_term k).abs) n m).toRat
                    = (TauRat.sumFromTo TauRat.e_term n m).toRat := by
    clear h_tri h_strong hnm hn
    induction m with
    | zero => simp [TauRat.sumFromTo_zero, toRat_zero]
    | succ m ih =>
      by_cases h : n ≤ m
      · have h_abs_rec :
            TauRat.sumFromTo (fun k => (TauRat.e_term k).abs) n (m + 1) =
              (TauRat.sumFromTo (fun k => (TauRat.e_term k).abs) n m).add
                ((TauRat.e_term m).abs) := by
          show (if n ≤ m then _ else _) = _; rw [if_pos h]
        have h_f_rec : TauRat.sumFromTo TauRat.e_term n (m + 1) =
              (TauRat.sumFromTo TauRat.e_term n m).add (TauRat.e_term m) := by
          show (if n ≤ m then _ else _) = _; rw [if_pos h]
        rw [h_abs_rec, h_f_rec, toRat_add, toRat_add, ih, TauRat.abs_e_term_toRat]
      · have h_abs_rec :
            TauRat.sumFromTo (fun k => (TauRat.e_term k).abs) n (m + 1) = TauRat.zero := by
          show (if n ≤ m then _ else _) = _; rw [if_neg h]
        have h_f_rec : TauRat.sumFromTo TauRat.e_term n (m + 1) = TauRat.zero := by
          show (if n ≤ m then _ else _) = _; rw [if_neg h]
        rw [h_abs_rec, h_f_rec]
  have h_pos_m : (0 : Rat) < 2 ^ m := by positivity
  have h_pos_4_2m : (0 : Rat) ≤ 4 / 2 ^ m := by
    have h_pos : (0 : Rat) < 2 ^ m := by positivity
    have h4 : (0 : Rat) ≤ 4 := by norm_num
    exact div_nonneg h4 (_root_.le_of_lt h_pos)
  rw [h_abs_eq] at h_tri
  linarith
```
