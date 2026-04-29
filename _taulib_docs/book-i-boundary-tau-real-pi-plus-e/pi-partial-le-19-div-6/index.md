---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.pi_partial_le_19_div_6",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-pi-plus-e/pi-partial-le-19-div-6/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealPiPlusE`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealPiPlusE::TauRat.pi_partial_le_19_div_6",
  "declaration_slug": "pi-partial-le-19-div-6",
  "kind": "theorem",
  "name": "TauRat.pi_partial_le_19_div_6",
  "module_name": "TauLib.BookI.Boundary.TauRealPiPlusE",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-pi-plus-e/",
  "source_line_start": 211,
  "source_line_end": 250,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPiPlusE.lean#L211-L250",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealPiPlusE",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-pi-plus-e/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPiPlusE.lean#L211-L250",
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

- Module: [TauLib.BookI.Boundary.TauRealPiPlusE](/verify/taulib/docs/book-i-boundary-tau-real-pi-plus-e/)
- Source path: [`TauLib/BookI/Boundary/TauRealPiPlusE.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPiPlusE.lean#L211-L250)
- Source range: L211-L250
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Upper bound on `pi_partial`**: for every `n`,
    `pi_partial n .toRat ≤ 19/6`.  Proof: for `n = 0`, value is 0;
    for `n ≥ 1`, telescope via `sum_sub_toRat_eq_sumFromTo` and apply
    `sumFromTo_pi_pair_term_bound` with starting index `1`:

      `pi_partial n .toRat = pi_partial 1 .toRat + sumFromTo pi_pair_term 1 n .toRat`
                          `≤ 8/3 + (1/2 - 1/(2n)) ≤ 8/3 + 1/2 = 19/6 < 4`.

    The bound `19/6 ≈ 3.17 < π ≈ 3.14159...` is loose by design; we just
    need *some* integer bound below 7 for the `(π + e)` combination. -/
```

## Source Excerpt

```lean
theorem TauRat.pi_partial_le_19_div_6 (n : Nat) :
    (TauRat.pi_partial n).toRat ≤ 19 / 6 := by
  by_cases hn : 1 ≤ n
  · -- Case n ≥ 1: telescope via sum_sub_toRat_eq_sumFromTo
    have h_tele := TauRat.sum_sub_toRat_eq_sumFromTo TauRat.pi_pair_term 1 n hn
    have h_sum_bound :
        (TauRat.sumFromTo TauRat.pi_pair_term 1 n).toRat
          ≤ 1 / (2 * (1 : Rat)) - 1 / (2 * (n : Rat)) :=
      TauReal.sumFromTo_pi_pair_term_bound 1 (by norm_num) n hn
    have h_pi1 : (TauRat.pi_partial 1).toRat = 8 / 3 :=
      TauRat.pi_partial_one_toRat
    have h_n_pos : (0 : Rat) < (n : Rat) := by exact_mod_cast hn
    have h_2n_pos : (0 : Rat) < 2 * (n : Rat) := by linarith
    have h_recip_nonneg : (0 : Rat) ≤ 1 / (2 * (n : Rat)) := by
      have h_one_nn : (0 : Rat) ≤ 1 := by norm_num
      exact div_nonneg h_one_nn h_2n_pos.le
    -- Bound the ranged sum by `1/2` directly via calc, avoiding
    -- reliance on linarith's ability to normalise `1 / (2 * 1) = 1/2`.
    have h_sum_le_half :
        (TauRat.sumFromTo TauRat.pi_pair_term 1 n).toRat ≤ 1 / 2 := by
      have h_21 : (1 : Rat) / (2 * (1 : Rat)) = 1 / 2 := by norm_num
      have h_step :
          (1 : Rat) / (2 * (1 : Rat)) - 1 / (2 * (n : Rat)) ≤ 1 / 2 := by
        rw [h_21]; linarith
      linarith [h_sum_bound]
    have h_pi_eq :
        (TauRat.pi_partial n).toRat =
          (TauRat.pi_partial 1).toRat + (TauRat.sumFromTo TauRat.pi_pair_term 1 n).toRat := by
      show (TauRat.sum TauRat.pi_pair_term n).toRat =
           (TauRat.sum TauRat.pi_pair_term 1).toRat + _
      linarith [h_tele]
    rw [h_pi_eq, h_pi1]
    linarith
  · -- Case n = 0: value is 0 ≤ 19/6 trivially
    push_neg at hn
    have hn0 : n = 0 := by omega
    subst hn0
    show (TauRat.sum TauRat.pi_pair_term 0).toRat ≤ 19 / 6
    rw [TauRat.sum_zero, toRat_zero]
    norm_num
```
