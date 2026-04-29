---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.e_partial_le_three",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-pi-plus-e/e-partial-le-three/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealPiPlusE`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealPiPlusE::TauRat.e_partial_le_three",
  "declaration_slug": "e-partial-le-three",
  "kind": "theorem",
  "name": "TauRat.e_partial_le_three",
  "module_name": "TauLib.BookI.Boundary.TauRealPiPlusE",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-pi-plus-e/",
  "source_line_start": 262,
  "source_line_end": 299,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPiPlusE.lean#L262-L299",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPiPlusE.lean#L262-L299",
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
- Source path: [`TauLib/BookI/Boundary/TauRealPiPlusE.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPiPlusE.lean#L262-L299)
- Source range: L262-L299
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Upper bound on `e_partial`**: for every `n`,
    `e_partial n .toRat ≤ 3`.  Proof: for `n = 0`, value is 0; for
    `n ≥ 1`, telescope via `sum_sub_toRat_eq_sumFromTo` and apply
    `sumFromTo_e_term_bound` with starting index `1`:

      `e_partial n .toRat = e_partial 1 .toRat + sumFromTo e_term 1 n .toRat`
                         `≤ 1 + (2 - 4/2^n) ≤ 3`.

    The bound `3 > e ≈ 2.718` is loose; tight enough for the
    `(π + e) ≤ 7` combination. -/
```

## Source Excerpt

```lean
theorem TauRat.e_partial_le_three (n : Nat) :
    (TauRat.e_partial n).toRat ≤ 3 := by
  by_cases hn : 1 ≤ n
  · -- Case n ≥ 1
    have h_tele := TauRat.sum_sub_toRat_eq_sumFromTo TauRat.e_term 1 n hn
    have h_sum_bound :
        (TauRat.sumFromTo TauRat.e_term 1 n).toRat
          ≤ 4 / (2 ^ (1 : Nat) : Rat) - 4 / (2 ^ n : Rat) :=
      TauReal.sumFromTo_e_term_bound 1 (by norm_num) n hn
    have h_e1 : (TauRat.e_partial 1).toRat = 1 :=
      TauRat.e_partial_one_toRat
    have h_pow_pos : (0 : Rat) < 2 ^ n := by positivity
    have h_recip_nonneg : (0 : Rat) ≤ 4 / (2 ^ n : Rat) := by
      have h_4_nn : (0 : Rat) ≤ 4 := by norm_num
      exact div_nonneg h_4_nn h_pow_pos.le
    -- Bound the ranged sum by 2 directly via calc, avoiding reliance
    -- on linarith's ability to normalise `4 / 2^1 = 2`.
    have h_sum_le_2 : (TauRat.sumFromTo TauRat.e_term 1 n).toRat ≤ 2 := by
      have h_base : (4 : Rat) / (2 ^ (1 : Nat) : Rat) = 2 := by norm_num
      have h_step :
          (4 : Rat) / (2 ^ (1 : Nat) : Rat) - 4 / (2 ^ n : Rat) ≤ 2 := by
        rw [h_base]; linarith
      linarith [h_sum_bound]
    have h_e_eq :
        (TauRat.e_partial n).toRat =
          (TauRat.e_partial 1).toRat + (TauRat.sumFromTo TauRat.e_term 1 n).toRat := by
      show (TauRat.sum TauRat.e_term n).toRat =
           (TauRat.sum TauRat.e_term 1).toRat + _
      linarith [h_tele]
    rw [h_e_eq, h_e1]
    linarith
  · -- Case n = 0: value is 0 ≤ 3 trivially
    push_neg at hn
    have hn0 : n = 0 := by omega
    subst hn0
    show (TauRat.sum TauRat.e_term 0).toRat ≤ 3
    rw [TauRat.sum_zero, toRat_zero]
    norm_num
```
