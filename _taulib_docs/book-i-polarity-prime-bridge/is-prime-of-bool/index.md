---
{
  "projection_kind": "taulib_declaration",
  "title": "is_prime_of_bool",
  "permalink": "/verify/taulib/docs/book-i-polarity-prime-bridge/is-prime-of-bool/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.PrimeBridge`.",
  "declaration_id": "TauLib.BookI.Polarity.PrimeBridge::is_prime_of_bool",
  "declaration_slug": "is-prime-of-bool",
  "kind": "theorem",
  "name": "is_prime_of_bool",
  "module_name": "TauLib.BookI.Polarity.PrimeBridge",
  "module_url": "/verify/taulib/docs/book-i-polarity-prime-bridge/",
  "source_line_start": 115,
  "source_line_end": 159,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimeBridge.lean#L115-L159",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.PrimeBridge",
        "url": "/verify/taulib/docs/book-i-polarity-prime-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimeBridge.lean#L115-L159",
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

- Module: [TauLib.BookI.Polarity.PrimeBridge](/verify/taulib/docs/book-i-polarity-prime-bridge/)
- Source path: [`TauLib/BookI/Polarity/PrimeBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimeBridge.lean#L115-L159)
- Source range: L115-L159
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Forward: is_prime_bool p = true → idx_prime p. -/
```

## Source Excerpt

```lean
theorem is_prime_of_bool (p : TauIdx) (h : is_prime_bool p = true) : idx_prime p := by
  unfold is_prime_bool at h
  have hp2 : p ≥ 2 := by
    simp only [Bool.and_eq_true, decide_eq_true_eq] at h; exact h.1
  have hnfb : no_factor_below p 2 = true := by
    simp only [Bool.and_eq_true, decide_eq_true_eq] at h; exact h.2
  constructor
  · exact hp2
  · intro d hd
    by_cases hd1 : d = 1
    · exact Or.inl hd1
    · by_cases hdp : d = p
      · exact Or.inr hdp
      · exfalso
        have hd0 : d ≠ 0 := by
          intro heq; subst heq; obtain ⟨k, hk⟩ := hd
          simp only [Nat.zero_mul] at hk; simp only [TauIdx] at hp2; omega
        have hd2 : d ≥ 2 := by
          rcases d with _ | _ | d
          · exact absurd rfl hd0
          · exact absurd rfl hd1
          · exact Nat.le_add_left 2 d
        have hddvd : d ∣ p := hd
        obtain ⟨q, hq⟩ := hd
        have hq2 : q ≥ 2 := by
          rcases q with _ | _ | q
          · simp only [TauIdx] at *; omega
          · simp only [TauIdx] at *; omega
          · exact Nat.le_add_left 2 q
        have hno := no_factor_below_true_imp p 2 hp2 (Nat.le_refl 2) hnfb
        by_cases hdq : d ≤ q
        · -- d*d ≤ d*q = p
          have hsq : d * d ≤ p := by rw [hq]; exact Nat.mul_le_mul_left d hdq
          have hmod : p % d = 0 := by
            obtain ⟨k, hk⟩ := hddvd; rw [hk, Nat.mul_mod_right]
          exact hno d hd2 hsq hmod
        · -- q < d, so q*q ≤ q*d ≤ d*q = p
          have hqd : q ≤ d := by simp only [TauIdx] at *; omega
          have hsq : q * q ≤ p := by
            calc q * q ≤ q * d := Nat.mul_le_mul_left q hqd
              _ = d * q := Nat.mul_comm q d
              _ = p := hq.symm
          have hmod : p % q = 0 := by
            rw [hq, Nat.mul_comm d q, Nat.mul_mod_right]
          exact hno q hq2 hsq hmod
```
