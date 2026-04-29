---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.IsCauchy_mul",
  "permalink": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/is-cauchy-mul/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Bridge.TauRealCongruence`.",
  "declaration_id": "TauLib.BookI.Boundary.Bridge.TauRealCongruence::TauReal.IsCauchy_mul",
  "declaration_slug": "is-cauchy-mul",
  "kind": "theorem",
  "name": "TauReal.IsCauchy_mul",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauRealCongruence",
  "module_url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/",
  "source_line_start": 308,
  "source_line_end": 430,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean#L308-L430",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Bridge.TauRealCongruence",
        "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean#L308-L430",
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

- Module: [TauLib.BookI.Boundary.Bridge.TauRealCongruence](/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/)
- Source path: [`TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean#L308-L430)
- Source range: L308-L430
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Product of Cauchy is Cauchy.**

    For Cauchy `a, b`, we have `(a.mul b).IsCauchy`. Strategy:
    `|a.m * b.m - a.n * b.n|`
       `= |a.m * b.m - a.n * b.m + a.n * b.m - a.n * b.n|`
       `≤ |b.m| * |a.m - a.n| + |a.n| * |b.m - b.n|`
    Both `|b.m|` and `|a.n|` are bounded (by Cauchy). At level `k`,
    pull each input modulus at level `2*Mab*(k+1) - 1` where `Mab` is
    the max of the two bounds; the conclusion follows. -/
```

## Source Excerpt

```lean
theorem TauReal.IsCauchy_mul (a b : TauReal)
    (ha : a.IsCauchy) (hb : b.IsCauchy) :
    (a.mul b).IsCauchy := by
  obtain ⟨Ma, hMa_pos, hMa⟩ := ha.bounded
  obtain ⟨Mb, hMb_pos, hMb⟩ := hb.bounded
  obtain ⟨μa, hμa⟩ := ha
  obtain ⟨μb, hμb⟩ := hb
  let M := max Ma Mb
  have hM_pos : 1 ≤ M := le_max_of_le_left hMa_pos
  -- Tighter modulus: at level `2*M*(k+1) - 1` we get `|a.m - a.n| < 1/(2M(k+1))`
  -- Then `|b.m| * |a.m - a.n| ≤ M * 1/(2M(k+1)) = 1/(2(k+1))`. Sum ≤ 1/(k+1).
  refine ⟨fun k => max (μa (2*M*(k+1) - 1)) (μb (2*M*(k+1) - 1)),
          fun k m n hm hn => ?_⟩
  have hμa_m : μa (2*M*(k+1) - 1) ≤ m := le_of_max_le_left hm
  have hμa_n : μa (2*M*(k+1) - 1) ≤ n := le_of_max_le_left hn
  have hμb_m : μb (2*M*(k+1) - 1) ≤ m := le_of_max_le_right hm
  have hμb_n : μb (2*M*(k+1) - 1) ≤ n := le_of_max_le_right hn
  have ha_step := hμa (2*M*(k+1) - 1) m n hμa_m hμa_n
  have hb_step := hμb (2*M*(k+1) - 1) m n hμb_m hμb_n
  unfold TauRat.lt at ha_step hb_step ⊢
  rw [TauRat.toRat_abs, toRat_sub] at ha_step hb_step
  rw [TauRat.toRat_abs, toRat_sub]
  rw [TauRat.ofNatRecip_toRat] at ha_step hb_step ⊢
  have h_lhs_eq :
      ((a.mul b).approx m).toRat - ((a.mul b).approx n).toRat
        = (b.approx m).toRat * ((a.approx m).toRat - (a.approx n).toRat) +
          (a.approx n).toRat * ((b.approx m).toRat - (b.approx n).toRat) := by
    show ((a.approx m).mul (b.approx m)).toRat -
           ((a.approx n).mul (b.approx n)).toRat = _
    rw [toRat_mul, toRat_mul]; ring
  rw [h_lhs_eq]
  -- Triangle: |x + y| ≤ |x| + |y|
  have h_tri := abs_add_le
      ((b.approx m).toRat * ((a.approx m).toRat - (a.approx n).toRat))
      ((a.approx n).toRat * ((b.approx m).toRat - (b.approx n).toRat))
  -- |b.m * (a.m - a.n)| = |b.m| * |a.m - a.n|
  have h_factor1 : |(b.approx m).toRat * ((a.approx m).toRat - (a.approx n).toRat)|
                 = |(b.approx m).toRat| * |(a.approx m).toRat - (a.approx n).toRat| :=
    abs_mul _ _
  have h_factor2 : |(a.approx n).toRat * ((b.approx m).toRat - (b.approx n).toRat)|
                 = |(a.approx n).toRat| * |(b.approx m).toRat - (b.approx n).toRat| :=
    abs_mul _ _
  -- |b.m| ≤ Mb, |a.n| ≤ Ma; both ≤ M
  have hbm_le : |(b.approx m).toRat| ≤ (M : Rat) := by
    have h1 : |(b.approx m).toRat| ≤ (Mb : Rat) := by
      have := hMb m; rw [TauRat.toRat_abs] at this; exact this
    have h2 : (Mb : Rat) ≤ (M : Rat) := by exact_mod_cast (le_max_right Ma Mb)
    linarith
  have han_le : |(a.approx n).toRat| ≤ (M : Rat) := by
    have h1 : |(a.approx n).toRat| ≤ (Ma : Rat) := by
      have := hMa n; rw [TauRat.toRat_abs] at this; exact this
    have h2 : (Ma : Rat) ≤ (M : Rat) := by exact_mod_cast (le_max_left Ma Mb)
    linarith
  -- |a.m - a.n| < 1/((2M(k+1) - 1) + 1) = 1/(2M(k+1))
  -- |b.m - b.n| < 1/(2M(k+1))
  have hM_pos' : (1 : Nat) ≤ 2 * M * (k+1) := by
    have h_2M : 1 ≤ 2 * M := by omega
    have h_kp1 : 1 ≤ k+1 := by omega
    calc 1 = 1 * 1 := by ring
      _ ≤ (2 * M) * (k+1) := Nat.mul_le_mul h_2M h_kp1
  have h_nat_eq : (2*M*(k+1) - 1 : Nat) + 1 = 2 * M * (k+1) :=
    Nat.sub_add_cancel hM_pos'
  have h_rat_eq : ((2*M*(k+1) - 1 : Nat) : Rat) + 1 = ((2 * M * (k+1) : Nat) : Rat) := by
    exact_mod_cast h_nat_eq
  have h_recip_eq :
      (1 : Rat) / ((2*M*(k+1) - 1 : Nat) + 1) = 1 / (2 * M * (k+1) : Nat) := by
    rw [h_rat_eq]
  rw [h_recip_eq] at ha_step hb_step
  have h_abs_a_nonneg : 0 ≤ |(a.approx m).toRat - (a.approx n).toRat| :=
    _root_.abs_nonneg _
  have h_abs_b_nonneg : 0 ≤ |(b.approx m).toRat - (b.approx n).toRat| :=
    _root_.abs_nonneg _
  have h_M_pos_rat : (0 : Rat) < M := by exact_mod_cast hM_pos
  have h_two_M_kp1_pos : (0 : Rat) < 2 * M * (k+1 : Nat) := by
    have hk : (0 : Rat) < (k + 1 : Nat) := by
      push_cast; linarith [show (0 : Rat) ≤ k by exact_mod_cast Nat.zero_le k]
    have : (0 : Rat) < 2 * M := by linarith
    have : (0 : Rat) < 2 * M * (k + 1 : Nat) := by positivity
    exact this
  -- Bound first term STRICTLY: |b.m| * |a.m - a.n| < M * 1/(2M(k+1)) = 1/(2(k+1))
  -- Two-step: |b.m| * |a.m - a.n| ≤ M * |a.m - a.n| (from hbm_le)
  --        < M * 1/(2M(k+1))                       (from ha_step strict, M > 0)
  have h_term1_lt :
      |(b.approx m).toRat| * |(a.approx m).toRat - (a.approx n).toRat| <
      (M : Rat) * (1 / (2 * M * (k+1) : Nat)) := by
    have h1 :
        |(b.approx m).toRat| * |(a.approx m).toRat - (a.approx n).toRat| ≤
        (M : Rat) * |(a.approx m).toRat - (a.approx n).toRat| :=
      mul_le_mul_of_nonneg_right hbm_le h_abs_a_nonneg
    have h2 : (M : Rat) * |(a.approx m).toRat - (a.approx n).toRat| <
              (M : Rat) * (1 / (2 * M * (k+1) : Nat)) :=
      mul_lt_mul_of_pos_left ha_step h_M_pos_rat
    linarith
  have h_term2_lt :
      |(a.approx n).toRat| * |(b.approx m).toRat - (b.approx n).toRat| <
      (M : Rat) * (1 / (2 * M * (k+1) : Nat)) := by
    have h1 :
        |(a.approx n).toRat| * |(b.approx m).toRat - (b.approx n).toRat| ≤
        (M : Rat) * |(b.approx m).toRat - (b.approx n).toRat| :=
      mul_le_mul_of_nonneg_right han_le h_abs_b_nonneg
    have h2 : (M : Rat) * |(b.approx m).toRat - (b.approx n).toRat| <
              (M : Rat) * (1 / (2 * M * (k+1) : Nat)) :=
      mul_lt_mul_of_pos_left hb_step h_M_pos_rat
    linarith
  have h_simplify : (M : Rat) * (1 / (2 * M * (k+1) : Nat)) = 1 / (2 * (k+1) : Nat) := by
    have h_M_ne : (M : Rat) ≠ 0 := ne_of_gt h_M_pos_rat
    have h_kp1_ne : ((k+1 : Nat) : Rat) ≠ 0 := by
      push_cast; linarith [show (0 : Rat) ≤ k by exact_mod_cast Nat.zero_le k]
    push_cast
    field_simp
  rw [h_simplify] at h_term1_lt h_term2_lt
  -- Sum: 1/(2(k+1)) + 1/(2(k+1)) = 1/(k+1)
  have h_sum : (1 : Rat) / (2 * (k+1) : Nat) + 1 / (2 * (k+1) : Nat)
             = 1 / ((k : Rat) + 1) := by
    have h_kp1_ne : ((k+1 : Nat) : Rat) ≠ 0 := by
      push_cast; linarith [show (0 : Rat) ≤ k by exact_mod_cast Nat.zero_le k]
    push_cast
    field_simp
    ring
  rw [h_factor1, h_factor2] at h_tri
  linarith

end Tau.Boundary
```
