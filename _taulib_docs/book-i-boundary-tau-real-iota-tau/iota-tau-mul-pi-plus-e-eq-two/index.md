---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.iota_tau_mul_pi_plus_e_eq_two",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-iota-tau/iota-tau-mul-pi-plus-e-eq-two/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealIotaTau`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealIotaTau::TauReal.iota_tau_mul_pi_plus_e_eq_two",
  "declaration_slug": "iota-tau-mul-pi-plus-e-eq-two",
  "kind": "theorem",
  "name": "TauReal.iota_tau_mul_pi_plus_e_eq_two",
  "module_name": "TauLib.BookI.Boundary.TauRealIotaTau",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-iota-tau/",
  "source_line_start": 118,
  "source_line_end": 167,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealIotaTau.lean#L118-L167",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealIotaTau",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-iota-tau/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealIotaTau.lean#L118-L167",
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

- Module: [TauLib.BookI.Boundary.TauRealIotaTau](/verify/taulib/docs/book-i-boundary-tau-real-iota-tau/)
- Source path: [`TauLib/BookI/Boundary/TauRealIotaTau.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealIotaTau.lean#L118-L167)
- Source range: L118-L167
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The defining identity of `iota_tau`: `iota_tau · (π + e) ≡ 2` in
    the Cauchy completion.

    Proof outline:
      iota_tau · (π + e)
    = (2 · (π + e)⁻¹) · (π + e)   [by definition of iota_tau and div]
    ≡ 2 · ((π + e)⁻¹ · (π + e))    [associativity]
    ≡ 2 · 1                         [inv_mul_cancel, using BoundedAwayFromZero]
    ≡ 2                             [mul_one]

    The three equivalences are chained via `equiv_trans` and the
    multiplicative congruence lemma `taureal_mul_comm` / ring-axiom
    wrappers. -/
```

## Source Excerpt

```lean
theorem TauReal.iota_tau_mul_pi_plus_e_eq_two :
    TauReal.equiv
      (TauReal.iota_tau.mul (TauReal.pi.add TauReal.e))
      TauReal.two := by
  -- Strategy: past the BoundedAwayFromZero modulus N₀, every (π+e).approx n
  -- is nonzero, so the pointwise product (2 · (π+e)⁻¹ · (π+e)) evaluates to
  -- exactly 2 at toRat level — the Cauchy equivalence with TauReal.two has
  -- zero pointwise difference past N₀ and the constant modulus N₀ works.
  obtain ⟨k₀, N₀, hN₀⟩ := TauReal.pi_plus_e_boundedAwayFromZero
  refine ⟨fun _ => N₀, fun k n hn => ?_⟩
  -- hn : N₀ ≤ n, so (pi + e).approx n is nonzero
  have h_nz : ((TauReal.pi.add TauReal.e).approx n).is_nonzero :=
    TauReal.is_nonzero_of_bounded_away hN₀ n hn
  -- Compute (iota_tau · (pi+e)).approx n at toRat level: equals 2 exactly.
  have h_lhs_toRat :
      ((TauReal.iota_tau.mul (TauReal.pi.add TauReal.e)).approx n).toRat = 2 := by
    -- Unfold the TauReal-level definitions at index n
    show (((TauReal.iota_tau.approx n).mul ((TauReal.pi.add TauReal.e).approx n))).toRat = 2
    -- iota_tau.approx n = (two · (pi+e).inv).approx n = (two.approx n).mul ((pi+e).inv.approx n)
    have h_iota_approx :
        TauReal.iota_tau.approx n
          = (TauReal.two.approx n).mul ((TauReal.pi.add TauReal.e).inv.approx n) := rfl
    rw [h_iota_approx]
    -- (pi+e).inv.approx n, under h_nz, takes the TauRat.inv branch
    have h_inv_approx :
        (TauReal.pi.add TauReal.e).inv.approx n
          = TauRat.inv ((TauReal.pi.add TauReal.e).approx n) h_nz := by
      show (if h : ((TauReal.pi.add TauReal.e).approx n).is_nonzero
            then TauRat.inv ((TauReal.pi.add TauReal.e).approx n) h
            else TauRat.one) = _
      rw [dif_pos h_nz]
    rw [h_inv_approx]
    -- Now compute the toRat
    rw [toRat_mul, toRat_mul, TauReal.two_approx_toRat, toRat_inv]
    have h_pe_ne : ((TauReal.pi.add TauReal.e).approx n).toRat ≠ 0 :=
      (TauRat.is_nonzero_iff_toRat_ne_zero _).mp h_nz
    field_simp
  -- Now the Cauchy bound: |LHS − 2| = |2 − 2| = 0 < 1/(k+1)
  unfold TauRat.lt
  rw [TauRat.toRat_abs, toRat_sub, TauRat.ofNatRecip_toRat]
  rw [h_lhs_toRat, TauReal.two_approx_toRat]
  -- Goal: |2 − 2| < 1 / (k + 1)
  have h_zero : |(2 : Rat) - 2| = 0 := by norm_num
  have h_pos_k1 : (0 : Rat) < 1 / ((k : Rat) + 1) := by
    have : (0 : Rat) ≤ (k : Rat) := by exact_mod_cast Nat.zero_le k
    have : (0 : Rat) < (k : Rat) + 1 := by linarith
    exact div_pos (by norm_num) this
  linarith

end Tau.Boundary
```
