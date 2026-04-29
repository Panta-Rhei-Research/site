---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.mul_respects_equiv_right_of_bound",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-mul-congr/mul-respects-equiv-right-of-bound/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealMulCongr`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealMulCongr::TauReal.mul_respects_equiv_right_of_bound",
  "declaration_slug": "mul-respects-equiv-right-of-bound",
  "kind": "theorem",
  "name": "TauReal.mul_respects_equiv_right_of_bound",
  "module_name": "TauLib.BookI.Boundary.TauRealMulCongr",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-mul-congr/",
  "source_line_start": 73,
  "source_line_end": 179,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealMulCongr.lean#L73-L179",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealMulCongr",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-mul-congr/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealMulCongr.lean#L73-L179",
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

- Module: [TauLib.BookI.Boundary.TauRealMulCongr](/verify/taulib/docs/book-i-boundary-tau-real-mul-congr/)
- Source path: [`TauLib/BookI/Boundary/TauRealMulCongr.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealMulCongr.lean#L73-L179)
- Source range: L73-L179
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Multiplication respects Cauchy equivalence (with explicit bound).**

    If `a ≡ b` at the Cauchy level (`TauReal.equiv`) and the
    `toRat`-absolute-value of every approximation of `c` is bounded
    above by a positive natural number `M`, then `a · c ≡ b · c`.

    Strategy: for target tolerance `1/(k+1)` on the conclusion, pull
    the equivalence at the finer tolerance level `M·(k+1) − 1` (so
    `|a − b| < 1 / (M·(k+1))` past that modulus).  Then
    `|c| · |a − b| ≤ M · 1/(M·(k+1)) = 1/(k+1)`, as required. -/
```

## Source Excerpt

```lean
theorem TauReal.mul_respects_equiv_right_of_bound
    (a b c : TauReal) (M : Nat) (hM : 1 ≤ M)
    (h_bound : ∀ n, (c.approx n).abs.toRat ≤ M)
    (h_equiv : TauReal.equiv a b) :
    TauReal.equiv (a.mul c) (b.mul c) := by
  obtain ⟨μ, h_mod⟩ := h_equiv
  -- The refined modulus uses level `M · (k + 1) - 1` on h_mod:
  -- at that level, |a - b| < 1 / (M·(k+1)), and `M · |a − b| < 1/(k+1)`.
  refine ⟨fun k => μ (M * (k + 1) - 1), fun k n hn => ?_⟩
  have h_base := h_mod (M * (k + 1) - 1) n hn
  unfold TauRat.lt at h_base ⊢
  rw [TauRat.toRat_abs, toRat_sub] at h_base
  rw [TauRat.toRat_abs, toRat_sub]
  rw [TauRat.ofNatRecip_toRat] at h_base ⊢
  -- h_base: |a.approx n .toRat - b.approx n .toRat|
  --           < 1 / ((M * (k + 1) - 1 : Nat) + 1)
  -- Goal:  |(a.mul c).approx n .toRat - (b.mul c).approx n .toRat|
  --           < 1 / ((k : Rat) + 1)
  -- Step 1: rewrite (a.mul c).approx n  as  a.approx n  *  c.approx n
  --         (and same for b), reducing the difference to
  --         (a - b)(n) · c(n) and applying abs_mul.
  have h_lhs_eq :
      ((a.mul c).approx n).toRat
        = (a.approx n).toRat * (c.approx n).toRat := by
    show ((a.approx n).mul (c.approx n)).toRat = _
    rw [toRat_mul]
  have h_rhs_eq :
      ((b.mul c).approx n).toRat
        = (b.approx n).toRat * (c.approx n).toRat := by
    show ((b.approx n).mul (c.approx n)).toRat = _
    rw [toRat_mul]
  rw [h_lhs_eq, h_rhs_eq]
  -- Goal: |a(n)·c(n) − b(n)·c(n)| < 1/(k+1)
  -- Factor:  = |c(n)| · |a(n) − b(n)|
  have h_factor :
      (a.approx n).toRat * (c.approx n).toRat
        - (b.approx n).toRat * (c.approx n).toRat
        = ((a.approx n).toRat - (b.approx n).toRat) * (c.approx n).toRat := by ring
  rw [h_factor]
  -- Goal: |(a(n) - b(n)) · c(n)| < 1/(k+1)
  -- Hand-rolled abs_mul (the mathlib lemma exists but isn't reachable
  -- via the tactics-only imports we have).  Case-analysis on signs.
  have h_abs_mul_local : |((a.approx n).toRat - (b.approx n).toRat) * (c.approx n).toRat|
                          = |(a.approx n).toRat - (b.approx n).toRat| * |(c.approx n).toRat| := by
    set x := (a.approx n).toRat - (b.approx n).toRat
    set y := (c.approx n).toRat
    by_cases hx : 0 ≤ x
    · by_cases hy : 0 ≤ y
      · have hxy : 0 ≤ x * y := mul_nonneg hx hy
        rw [abs_of_nonneg hxy, abs_of_nonneg hx, abs_of_nonneg hy]
      · push_neg at hy
        have hxy : x * y ≤ 0 := by nlinarith
        rw [abs_of_nonpos hxy, abs_of_nonneg hx, abs_of_neg hy]; ring
    · push_neg at hx
      by_cases hy : 0 ≤ y
      · have hxy : x * y ≤ 0 := by nlinarith
        rw [abs_of_nonpos hxy, abs_of_neg hx, abs_of_nonneg hy]; ring
      · push_neg at hy
        have hxy : 0 ≤ x * y := by nlinarith
        rw [abs_of_nonneg hxy, abs_of_neg hx, abs_of_neg hy]; ring
  rw [h_abs_mul_local]
  -- Goal: |a(n) - b(n)| · |c(n)| < 1/(k+1)
  have h_c_bound : |(c.approx n).toRat| ≤ (M : Rat) := by
    have h_abs_form : (c.approx n).abs.toRat = |(c.approx n).toRat| :=
      TauRat.toRat_abs _
    have := h_bound n
    rw [h_abs_form] at this
    exact this
  have h_diff_pos :
      0 ≤ |(a.approx n).toRat - (b.approx n).toRat| := _root_.abs_nonneg _
  -- Numeric setup
  have h_M_pos : (0 : Rat) < M := by exact_mod_cast hM
  have h_k1_pos : (0 : Rat) < (k : Rat) + 1 := by
    have : (0 : Rat) ≤ (k : Rat) := by exact_mod_cast Nat.zero_le k
    linarith
  have h_Mk1_pos : (0 : Rat) < (M : Rat) * ((k : Rat) + 1) := by positivity
  -- The refined-tolerance Rat conversion
  have h_refined_eq :
      (1 : Rat) / ((M * (k + 1) - 1 : Nat) + 1) = 1 / ((M : Rat) * ((k : Rat) + 1)) := by
    have h_Mk1_nat_pos : 1 ≤ M * (k + 1) := by
      have : 1 ≤ k + 1 := by omega
      have := Nat.mul_le_mul hM this
      omega
    have h_cast : ((M * (k + 1) - 1 : Nat) + 1 : Rat) = (M : Rat) * ((k : Rat) + 1) := by
      have h_nat_eq : (M * (k + 1) - 1) + 1 = M * (k + 1) := by omega
      rw [show ((M * (k + 1) - 1 : Nat) + 1 : Rat) = ((M * (k + 1) - 1 + 1 : Nat) : Rat) by push_cast; ring]
      rw [h_nat_eq]
      push_cast; ring
    rw [h_cast]
  rw [h_refined_eq] at h_base
  -- Now: |a - b| < 1 / (M · (k+1))  and  |c| ≤ M
  -- Combine: |a - b| · |c| ≤ |a - b| · M < (1 / (M·(k+1))) · M = 1/(k+1)
  have h_step1 :
      |(a.approx n).toRat - (b.approx n).toRat| * |(c.approx n).toRat|
        ≤ |(a.approx n).toRat - (b.approx n).toRat| * M := by
    apply mul_le_mul_of_nonneg_left h_c_bound h_diff_pos
  have h_step2 :
      |(a.approx n).toRat - (b.approx n).toRat| * (M : Rat)
        < (1 / ((M : Rat) * ((k : Rat) + 1))) * (M : Rat) :=
    mul_lt_mul_of_pos_right h_base h_M_pos
  have h_step3 :
      (1 / ((M : Rat) * ((k : Rat) + 1))) * (M : Rat)
        = 1 / ((k : Rat) + 1) := by
    field_simp
  linarith

end Tau.Boundary
```
