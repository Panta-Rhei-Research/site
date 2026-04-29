---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.pi_pair_term_le_telescope",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-pi/pi-pair-term-le-telescope/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealPi`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealPi::TauRat.pi_pair_term_le_telescope",
  "declaration_slug": "pi-pair-term-le-telescope",
  "kind": "theorem",
  "name": "TauRat.pi_pair_term_le_telescope",
  "module_name": "TauLib.BookI.Boundary.TauRealPi",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-pi/",
  "source_line_start": 107,
  "source_line_end": 144,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPi.lean#L107-L144",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPi.lean#L107-L144",
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
- Source path: [`TauLib/BookI/Boundary/TauRealPi.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPi.lean#L107-L144)
- Source range: L107-L144
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `pi_pair_term k ≤ (1/2) · (1/k − 1/(k+1))` for `k ≥ 1`, at Rat level. -/
```

## Source Excerpt

```lean
theorem TauRat.pi_pair_term_le_telescope (k : Nat) (hk : 1 ≤ k) :
    (TauRat.pi_pair_term k).toRat ≤ (1 / 2) * (1 / (k : Rat) - 1 / ((k : Rat) + 1)) := by
  rw [TauRat.pi_pair_term_toRat]
  have h_k_pos : (0 : Rat) < (k : Rat) := by
    have : (1 : Rat) ≤ (k : Rat) := by exact_mod_cast hk
    linarith
  have h_k1_pos : (0 : Rat) < (k : Rat) + 1 := by linarith
  have h_kne : (k : Rat) ≠ 0 := ne_of_gt h_k_pos
  have h_k1ne : ((k : Rat) + 1) ≠ 0 := ne_of_gt h_k1_pos
  -- Step 1: simplify (1/k - 1/(k+1)) = 1/(k(k+1))
  have h_diff : (1 : Rat) / (k : Rat) - 1 / ((k : Rat) + 1)
                  = 1 / ((k : Rat) * ((k : Rat) + 1)) := by
    rw [div_sub_div _ _ h_kne h_k1ne, mul_one, one_mul]
    congr 1; ring
  rw [h_diff]
  -- Goal:  8 / (((4k+1)(4k+3) : Nat) : Rat) ≤ (1/2) * (1 / (k * (k+1)))
  -- Step 2: simplify (1/2) * (1 / (k(k+1))) = 1 / (2·k·(k+1))
  have h_kk1_pos : (0 : Rat) < (k : Rat) * ((k : Rat) + 1) := mul_pos h_k_pos h_k1_pos
  have h_2kk1_pos : (0 : Rat) < 2 * ((k : Rat) * ((k : Rat) + 1)) := by linarith
  have h_rhs_simp : (1 / 2 : Rat) * (1 / ((k : Rat) * ((k : Rat) + 1)))
                       = 1 / (2 * ((k : Rat) * ((k : Rat) + 1))) := by
    rw [div_mul_div_comm]; norm_num
  rw [h_rhs_simp]
  -- Goal:  8 / (((4k+1)(4k+3) : Nat) : Rat) ≤ 1 / (2 * (k * (k+1)))
  have h_prod_pos : (0 : Rat) < (((4 * k + 1) * (4 * k + 3) : Nat) : Rat) := by
    have : 0 < (4 * k + 1) * (4 * k + 3) := by positivity
    exact_mod_cast this
  rw [div_le_div_iff₀ h_prod_pos h_2kk1_pos]
  -- Goal:  8 * (2 * (k * (k+1))) ≤ 1 * (((4k+1)(4k+3) : Nat) : Rat)
  rw [one_mul]
  -- Goal:  8 * (2 * (k * (k+1))) ≤ (((4k+1)(4k+3) : Nat) : Rat)
  -- Use the Nat-level bound  16·k·(k+1) ≤ (4k+1)(4k+3)
  have h_nat := Nat.four_k_plus_one_three_ge k
  have h_rat_cast : ((16 * k * (k + 1) : Nat) : Rat)
                      ≤ (((4 * k + 1) * (4 * k + 3) : Nat) : Rat) := by exact_mod_cast h_nat
  have h_lhs_eq : ((16 * k * (k + 1) : Nat) : Rat)
                    = 8 * (2 * ((k : Rat) * ((k : Rat) + 1))) := by push_cast; ring
  linarith
```
