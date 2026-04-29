---
{
  "projection_kind": "taulib_declaration",
  "title": "exists_prime_divisor",
  "permalink": "/verify/taulib/docs/book-i-coordinates-primes/exists-prime-divisor/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.Primes`.",
  "declaration_id": "TauLib.BookI.Coordinates.Primes::exists_prime_divisor",
  "declaration_slug": "exists-prime-divisor",
  "kind": "theorem",
  "name": "exists_prime_divisor",
  "module_name": "TauLib.BookI.Coordinates.Primes",
  "module_url": "/verify/taulib/docs/book-i-coordinates-primes/",
  "source_line_start": 106,
  "source_line_end": 135,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L106-L135",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.Primes",
        "url": "/verify/taulib/docs/book-i-coordinates-primes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L106-L135",
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

- Module: [TauLib.BookI.Coordinates.Primes](/verify/taulib/docs/book-i-coordinates-primes/)
- Source path: [`TauLib/BookI/Coordinates/Primes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean#L106-L135)
- Source range: L106-L135
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Every n ≥ 2 has a prime divisor. Proved by strong induction. -/
```

## Source Excerpt

```lean
theorem exists_prime_divisor (n : TauIdx) (hn : n ≥ 2) :
    ∃ p, idx_prime p ∧ p ∣ n := by
  induction n using Nat.strongRecOn with
  | _ n ih =>
    rcases Classical.em (∀ d : TauIdx, d ∣ n → d = 1 ∨ d = n) with h | h
    · exact ⟨n, ⟨hn, h⟩, nat_dvd_refl n⟩
    · -- n is composite
      have ⟨d, hd_dvd, hd_ne⟩ : ∃ d, d ∣ n ∧ ¬(d = 1 ∨ d = n) :=
        Classical.byContradiction fun hall =>
          h fun d hd => Classical.byContradiction fun hbad => hall ⟨d, hd, hbad⟩
      have hd1 : d ≠ 1 := fun heq => hd_ne (Or.inl heq)
      have hdn : d ≠ n := fun heq => hd_ne (Or.inr heq)
      have hd0 : d ≠ 0 := by
        intro heq; subst heq
        obtain ⟨k, hk⟩ := hd_dvd
        simp only [Nat.zero_mul] at hk
        simp only [TauIdx] at hn; omega
      have hd_ge2 : d ≥ 2 := by
        rcases d with _ | _ | d
        · exact absurd rfl hd0
        · exact absurd rfl hd1
        · exact Nat.le_add_left 2 d
      have hd_lt : d < n := by
        have hpos : n > 0 := by simp only [TauIdx] at hn ⊢; omega
        have hle := Nat.le_of_dvd hpos hd_dvd
        rcases Nat.eq_or_lt_of_le hle with heq | hlt
        · exact absurd heq hdn
        · exact hlt
      obtain ⟨p, hp, hpd⟩ := ih d hd_lt hd_ge2
      exact ⟨p, hp, nat_dvd_trans hpd hd_dvd⟩
```
