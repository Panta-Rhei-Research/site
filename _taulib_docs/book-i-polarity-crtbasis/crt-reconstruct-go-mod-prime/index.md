---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_reconstruct_go_mod_prime",
  "permalink": "/verify/taulib/docs/book-i-polarity-crtbasis/crt-reconstruct-go-mod-prime/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.CRTBasis`.",
  "declaration_id": "TauLib.BookI.Polarity.CRTBasis::crt_reconstruct_go_mod_prime",
  "declaration_slug": "crt-reconstruct-go-mod-prime",
  "kind": "theorem",
  "name": "crt_reconstruct_go_mod_prime",
  "module_name": "TauLib.BookI.Polarity.CRTBasis",
  "module_url": "/verify/taulib/docs/book-i-polarity-crtbasis/",
  "source_line_start": 364,
  "source_line_end": 428,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L364-L428",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L364-L428",
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
- Source path: [`TauLib/BookI/Polarity/CRTBasis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L364-L428)
- Source range: L364-L428
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Accumulator invariant: crt_reconstruct_go modulo p_{l+1} picks up exactly
    the l-th residue (all other contributions vanish by basis orthogonality). -/
```

## Source Excerpt

```lean
private theorem crt_reconstruct_go_mod_prime
    {k l : TauIdx} (residues : List TauIdx) (hl : l < k) (hyp : CRTHyp k) :
    ∀ (i fuel : Nat) (acc : TauIdx), i ≤ k → fuel ≥ k - i →
    crt_reconstruct_go residues k i fuel acc % nth_prime (l + 1) =
    (acc + if l ≥ i then residues.getD l 0 else 0) % nth_prime (l + 1) := by
  intro i fuel
  induction fuel generalizing i with
  | zero =>
    intro acc hi hfuel
    have hik : i = k := by omega
    unfold crt_reconstruct_go; simp
    rw [hik]
    have hlk : ¬(l ≥ k) := by simp only [TauIdx] at *; omega
    simp [hlk]
  | succ n ih =>
    intro acc hi hfuel
    unfold crt_reconstruct_go
    simp only [Nat.succ_ne_zero, ↓reduceIte]
    split
    · -- i ≥ k: returns acc
      rename_i hige
      have hlti : ¬(l ≥ i) := by simp only [TauIdx] at *; omega
      simp [hlti]
    · -- i < k: take one step
      rename_i hige
      have hilt : i < k := by simp only [TauIdx] at *; omega
      -- Simplify fuel: n + 1 - 1 = n (clear afterward to not confuse omega)
      have hfuel_simp : n + 1 - 1 = n := by omega
      rw [hfuel_simp]; clear hfuel_simp
      -- Apply IH at i+1
      rw [ih (i + 1) _ (by omega) (by omega)]
      -- Clear hfuel (Nat subtraction confuses omega)
      clear hfuel
      -- Goal: (acc' + if l ≥ i+1 ...) % p = (acc + if l ≥ i ...) % p
      -- where acc' = (acc + r_i * e_i) % M_k
      by_cases hli : l = i
      · -- Diagonal: l = i (subst eliminates i, keeps l)
        subst hli
        rw [if_neg (show ¬(l ≥ l + 1) from by simp only [TauIdx] at *; omega), Nat.add_zero,
          if_pos (Nat.le_refl l)]
        -- Goal: ((acc + rl * el) % Mk) % p = (acc + rl) % p
        rw [mod_mod_of_dvd _ _ _
          (nth_prime_dvd_primorial (show l + 1 ≤ k by simp only [TauIdx] at *; omega))]
        exact add_mul_basis_diag hilt hyp
      · by_cases hlti : l < i
        · -- l < i: both ifs are false
          rw [if_neg (show ¬(l ≥ i + 1) from by simp only [TauIdx] at *; omega),
            if_neg (show ¬(l ≥ i) from by simp only [TauIdx] at *; omega),
            Nat.add_zero, Nat.add_zero]
          rw [mod_mod_of_dvd _ _ _
            (nth_prime_dvd_primorial (show l + 1 ≤ k by simp only [TauIdx] at *; omega))]
          exact add_mul_basis_off_diag hilt hl
            (by simp only [TauIdx] at *; omega) hyp
        · -- l > i: both ifs are true, same residue
          have hlgei1 : l ≥ i + 1 := by simp only [TauIdx] at *; omega
          have hlgei : l ≥ i := by simp only [TauIdx] at *; omega
          have hne_il : i ≠ l := by simp only [TauIdx] at *; omega
          rw [if_pos hlgei1, if_pos hlgei]
          -- Goal: ((acc + ri*ei) % Mk + rl) % p = (acc + rl) % p
          rw [add_mod_primorial hl]
          -- Rearrange: acc + ri*ei + rl = (acc + rl) + ri*ei
          rw [Nat.add_assoc,
            Nat.add_comm (residues.getD i 0 * crt_basis k i) (residues.getD l 0),
            ← Nat.add_assoc]
          exact add_mul_basis_off_diag hilt hl hne_il hyp
```
