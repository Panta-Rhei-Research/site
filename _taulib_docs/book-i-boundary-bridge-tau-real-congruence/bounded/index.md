---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.IsCauchy.bounded",
  "permalink": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/bounded/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Bridge.TauRealCongruence`.",
  "declaration_id": "TauLib.BookI.Boundary.Bridge.TauRealCongruence::TauReal.IsCauchy.bounded",
  "declaration_slug": "bounded",
  "kind": "theorem",
  "name": "TauReal.IsCauchy.bounded",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauRealCongruence",
  "module_url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/",
  "source_line_start": 212,
  "source_line_end": 257,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean#L212-L257",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean#L212-L257",
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
- Source path: [`TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean#L212-L257)
- Source range: L212-L257
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Every Cauchy sequence is uniformly bounded** (constructive form).

    Given `IsCauchy a`, returns a natural-number bound `M` such that
    `|a.approx n|.toRat ≤ M` for all `n`.

    Strategy: past `μ 0`, all `a.approx n` are within `1` of `a.approx (μ 0)`
    (the Cauchy property at `k=0` says `|a.m - a.n| < 1/(0+1) = 1`). Below
    `μ 0`, finitely many indices give a max via `Finset.sup'`. Combined
    `Rat` bound is then dominated by some `Nat` via `exists_nat_ge`. -/
```

## Source Excerpt

```lean
theorem TauReal.IsCauchy.bounded {a : TauReal} (ha : a.IsCauchy) :
    ∃ M : Nat, 1 ≤ M ∧ ∀ n, (a.approx n).abs.toRat ≤ M := by
  obtain ⟨μ, hμ⟩ := ha
  set N0 := μ 0 with hN0_def
  -- Head bound: max of |a.0|, ..., |a.N0| at the Rat level
  set head_R : Rat := (Finset.range (N0 + 1)).sup'
    ⟨0, Finset.mem_range.mpr (Nat.succ_pos N0)⟩
    (fun i => (a.approx i).abs.toRat) with head_R_def
  -- Tail bound: |a.N0| + 1 dominates |a.n| for n > N0
  set tail_R : Rat := (a.approx N0).abs.toRat + 1 with tail_R_def
  set R : Rat := max head_R tail_R with R_def
  -- Convert to a Nat bound via Archimedean
  obtain ⟨M', hM'⟩ := exists_nat_ge R
  refine ⟨max M' 1, le_max_right _ _, ?_⟩
  intro n
  have h_M : (R : Rat) ≤ ((max M' 1 : Nat) : Rat) := by
    have : (M' : Rat) ≤ ((max M' 1 : Nat) : Rat) := by exact_mod_cast (le_max_left M' 1)
    linarith
  by_cases hn : n ≤ N0
  · -- Head case
    have h_in : n ∈ Finset.range (N0 + 1) := Finset.mem_range.mpr (by omega)
    have h_head : (a.approx n).abs.toRat ≤ head_R :=
      Finset.le_sup' (fun i => (a.approx i).abs.toRat) h_in
    have h_R : head_R ≤ R := le_max_left _ _
    linarith
  · -- Tail case: n > N0
    push_neg at hn
    have hN0_le_n : N0 ≤ n := Nat.le_of_lt hn
    have h_close := hμ 0 n N0 hN0_le_n (Nat.le_refl _)
    unfold TauRat.lt at h_close
    rw [TauRat.toRat_abs, toRat_sub, TauRat.ofNatRecip_toRat] at h_close
    have h_diff : |(a.approx n).toRat - (a.approx N0).toRat| < 1 := by simpa using h_close
    -- Triangle: |a.n| = |a.N0 + (a.n - a.N0)| ≤ |a.N0| + |a.n - a.N0|
    have h_eq_pre :
        (a.approx N0).toRat + ((a.approx n).toRat - (a.approx N0).toRat) =
          (a.approx n).toRat := by ring
    have h_pre_tri := abs_add_le (a.approx N0).toRat
                                  ((a.approx n).toRat - (a.approx N0).toRat)
    rw [h_eq_pre] at h_pre_tri
    have h_aN0 : |(a.approx N0).toRat| = (a.approx N0).abs.toRat := by
      rw [TauRat.toRat_abs]
    rw [TauRat.toRat_abs]
    have h_to_tail : |(a.approx n).toRat| ≤ tail_R := by
      rw [tail_R_def, ← h_aN0]; linarith
    have h_R : tail_R ≤ R := le_max_right _ _
    linarith
```
