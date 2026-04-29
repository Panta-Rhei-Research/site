---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.sumFromTo_e_term_bound",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-e/sum-from-to-e-term-bound/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealE`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealE::TauReal.sumFromTo_e_term_bound",
  "declaration_slug": "sum-from-to-e-term-bound",
  "kind": "theorem",
  "name": "TauReal.sumFromTo_e_term_bound",
  "module_name": "TauLib.BookI.Boundary.TauRealE",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-e/",
  "source_line_start": 99,
  "source_line_end": 129,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealE.lean#L99-L129",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealE.lean#L99-L129",
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
- Source path: [`TauLib/BookI/Boundary/TauRealE.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealE.lean#L99-L129)
- Source range: L99-L129
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Strengthened bound with telescoping tail: the `−4/2^m` term is what
    lets the induction close. -/
```

## Source Excerpt

```lean
theorem TauReal.sumFromTo_e_term_bound (n : Nat) (hn : 1 ≤ n) :
    ∀ m, n ≤ m →
    (TauRat.sumFromTo TauRat.e_term n m).toRat
      ≤ 4 / (2 ^ n : Rat) - 4 / (2 ^ m : Rat) := by
  intro m hnm
  induction m with
  | zero => omega
  | succ m ih =>
    by_cases h_eq : n = m + 1
    · subst h_eq
      rw [TauRat.sumFromTo_self, toRat_zero]
      linarith
    · have hnm' : n ≤ m := by omega
      have h_m_ge_one : 1 ≤ m := by omega
      have ih' := ih hnm'
      have h_rec : TauRat.sumFromTo TauRat.e_term n (m + 1) =
                   (TauRat.sumFromTo TauRat.e_term n m).add (TauRat.e_term m) := by
        show (if n ≤ m then _ else _) = _; rw [if_pos hnm']
      rw [h_rec, toRat_add]
      have h_term_bound : (TauRat.e_term m).toRat ≤ 1 / (2 ^ (m - 1) : Rat) :=
        TauRat.e_term_le_geom m h_m_ge_one
      have h_rewrite_term : (1 : Rat) / 2 ^ (m - 1) = 2 / 2 ^ m :=
        Rat.one_div_two_pow_pred_eq_two_div_two_pow m h_m_ge_one
      have h_rewrite_goal : (4 : Rat) / 2 ^ (m + 1) = 2 / 2 ^ m :=
        Rat.four_div_two_pow_succ_eq_two_div_two_pow m
      rw [h_rewrite_term] at h_term_bound
      rw [h_rewrite_goal]
      -- Tell linarith that `4/2^m = 2 * (2/2^m)` so it can chain ih' through.
      have h_BC : (4 : Rat) / 2 ^ m = 2 * (2 / 2 ^ m) := by ring
      rw [h_BC] at ih'
      linarith [ih', h_term_bound]
```
