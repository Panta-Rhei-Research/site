---
{
  "projection_kind": "taulib_declaration",
  "title": "cofactor_coprime",
  "permalink": "/verify/taulib/docs/book-i-polarity-crtbasis/cofactor-coprime/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.CRTBasis`.",
  "declaration_id": "TauLib.BookI.Polarity.CRTBasis::cofactor_coprime",
  "declaration_slug": "cofactor-coprime",
  "kind": "theorem",
  "name": "cofactor_coprime",
  "module_name": "TauLib.BookI.Polarity.CRTBasis",
  "module_url": "/verify/taulib/docs/book-i-polarity-crtbasis/",
  "source_line_start": 107,
  "source_line_end": 134,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L107-L134",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.CRTBasis",
        "url": "/verify/taulib/docs/book-i-polarity-crtbasis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L107-L134",
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

- Module: [TauLib.BookI.Polarity.CRTBasis](/verify/taulib/docs/book-i-polarity-crtbasis/)
- Source path: [`TauLib/BookI/Polarity/CRTBasis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L107-L134)
- Source range: L107-L134
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Key induction: the primorial cofactor M_k/p_{i+1} is coprime to p_{i+1}. -/
```

## Source Excerpt

```lean
theorem cofactor_coprime : ∀ {k i : TauIdx}, i < k → CRTHyp k →
    Nat.Coprime (primorial k / nth_prime (i + 1)) (nth_prime (i + 1)) := by
  intro k
  induction k with
  | zero => intro i hi; exact absurd hi (Nat.not_succ_le_zero i)
  | succ n ih =>
    intro i hi hyp
    simp only [primorial]
    rcases Nat.eq_or_lt_of_le (Nat.lt_succ_iff.mp hi) with heq | hlt
    · -- i = n: cofactor = (p_{n+1} * M_n) / p_{n+1} = M_n
      rw [heq, Nat.mul_div_cancel_left _ (by
        have := nth_prime_pos (show n + 1 ≥ 1 by omega)
        simp only [TauIdx] at *; omega)]
      exact (prime_coprime_primorial hyp).symm
    · -- i < n: cofactor = p_{n+1} * (M_n / p_{i+1})
      have hi_n : i + 1 ≤ n := by simp only [TauIdx] at *; omega
      rw [Nat.mul_div_assoc _ (nth_prime_dvd_primorial hi_n)]
      apply coprime_product
      · -- Coprime p_{n+1} p_{i+1}
        exact hyp.pairwise_coprime n i
          (by simp only [TauIdx] at *; omega)
          (by simp only [TauIdx] at *; omega)
          (by simp only [TauIdx] at *; omega)
      · -- Coprime (M_n/p_{i+1}) p_{i+1}: IH
        exact ih (by simp only [TauIdx] at *; omega)
          ⟨fun j hj => hyp.all_prime j (by simp only [TauIdx] at *; omega),
           fun j l hj hl hjl => hyp.pairwise_coprime j l
             (by simp only [TauIdx] at *; omega) (by simp only [TauIdx] at *; omega) hjl⟩
```
