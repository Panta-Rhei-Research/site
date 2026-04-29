---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.pi_partial_cauchy_bound",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-pi/pi-partial-cauchy-bound/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealPi`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealPi::TauReal.pi_partial_cauchy_bound",
  "declaration_slug": "pi-partial-cauchy-bound",
  "kind": "theorem",
  "name": "TauReal.pi_partial_cauchy_bound",
  "module_name": "TauLib.BookI.Boundary.TauRealPi",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-pi/",
  "source_line_start": 205,
  "source_line_end": 243,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPi.lean#L205-L243",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealPi",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-pi/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPi.lean#L205-L243",
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

- Module: [TauLib.BookI.Boundary.TauRealPi](/verify/taulib/docs/book-i-boundary-tau-real-pi/)
- Source path: [`TauLib/BookI/Boundary/TauRealPi.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPi.lean#L205-L243)
- Source range: L205-L243
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- ============================================================
-- PART 4: MAIN Cauchy BOUND  |pi_partial m − pi_partial n| ≤ 1/(2n)
-- ============================================================
```

## Source Excerpt

```lean
theorem TauReal.pi_partial_cauchy_bound (m n : Nat) (hn : 1 ≤ n) (hnm : n ≤ m) :
    |((TauRat.pi_partial m).toRat - (TauRat.pi_partial n).toRat)|
      ≤ 1 / (2 * (n : Rat)) := by
  unfold TauRat.pi_partial
  rw [TauRat.sum_sub_toRat_eq_sumFromTo TauRat.pi_pair_term n m hnm]
  have h_tri := TauRat.sumFromTo_abs_le TauRat.pi_pair_term n m
  have h_strong := TauReal.sumFromTo_pi_pair_term_bound n hn m hnm
  -- |pi_pair_term k| = pi_pair_term k at toRat (positive)
  have h_abs_eq : (TauRat.sumFromTo (fun k => (TauRat.pi_pair_term k).abs) n m).toRat
                    = (TauRat.sumFromTo TauRat.pi_pair_term n m).toRat := by
    clear h_tri h_strong hnm hn
    induction m with
    | zero => simp [TauRat.sumFromTo_zero, toRat_zero]
    | succ m ih =>
      by_cases h : n ≤ m
      · have h_abs_rec :
            TauRat.sumFromTo (fun k => (TauRat.pi_pair_term k).abs) n (m + 1) =
              (TauRat.sumFromTo (fun k => (TauRat.pi_pair_term k).abs) n m).add
                ((TauRat.pi_pair_term m).abs) := by
          show (if n ≤ m then _ else _) = _; rw [if_pos h]
        have h_f_rec : TauRat.sumFromTo TauRat.pi_pair_term n (m + 1) =
              (TauRat.sumFromTo TauRat.pi_pair_term n m).add (TauRat.pi_pair_term m) := by
          show (if n ≤ m then _ else _) = _; rw [if_pos h]
        rw [h_abs_rec, h_f_rec, toRat_add, toRat_add, ih, TauRat.abs_pi_pair_term_toRat]
      · have h_abs_rec :
            TauRat.sumFromTo (fun k => (TauRat.pi_pair_term k).abs) n (m + 1) = TauRat.zero := by
          show (if n ≤ m then _ else _) = _; rw [if_neg h]
        have h_f_rec : TauRat.sumFromTo TauRat.pi_pair_term n (m + 1) = TauRat.zero := by
          show (if n ≤ m then _ else _) = _; rw [if_neg h]
        rw [h_abs_rec, h_f_rec]
  have h_pos_2m : (0 : Rat) < 2 * (m : Rat) := by
    have h_m_ge : 1 ≤ m := by omega
    have : (0 : Rat) < (m : Rat) := by exact_mod_cast h_m_ge
    linarith
  have h_recip_2m_nn : (0 : Rat) ≤ 1 / (2 * (m : Rat)) := by
    have h1 : (0 : Rat) ≤ 1 := by norm_num
    exact div_nonneg h1 (_root_.le_of_lt h_pos_2m)
  rw [h_abs_eq] at h_tri
  linarith
```
