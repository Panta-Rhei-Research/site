---
{
  "projection_kind": "taulib_declaration",
  "title": "nth_prime_dvd_primorial",
  "permalink": "/verify/taulib/docs/book-i-polarity-nth-prime/nth-prime-dvd-primorial/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.NthPrime`.",
  "declaration_id": "TauLib.BookI.Polarity.NthPrime::nth_prime_dvd_primorial",
  "declaration_slug": "nth-prime-dvd-primorial",
  "kind": "theorem",
  "name": "nth_prime_dvd_primorial",
  "module_name": "TauLib.BookI.Polarity.NthPrime",
  "module_url": "/verify/taulib/docs/book-i-polarity-nth-prime/",
  "source_line_start": 153,
  "source_line_end": 170,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/NthPrime.lean#L153-L170",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.NthPrime",
        "url": "/verify/taulib/docs/book-i-polarity-nth-prime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/NthPrime.lean#L153-L170",
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

- Module: [TauLib.BookI.Polarity.NthPrime](/verify/taulib/docs/book-i-polarity-nth-prime/)
- Source path: [`TauLib/BookI/Polarity/NthPrime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/NthPrime.lean#L153-L170)
- Source range: L153-L170
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- nth_prime(i+1) divides primorial(k) for i + 1 ≤ k. Structural induction. -/
```

## Source Excerpt

```lean
theorem nth_prime_dvd_primorial {i k : TauIdx} (h : i + 1 ≤ k) :
    nth_prime (i + 1) ∣ primorial k := by
  induction k with
  | zero => exact absurd h (Nat.not_succ_le_zero i)
  | succ k' ih =>
    simp only [primorial]
    rcases Nat.eq_or_lt_of_le h with heq | hlt
    · -- i + 1 = k' + 1, so i = k'
      have hik : i = k' := by simp only [TauIdx] at *; omega
      rw [hik]
      exact ⟨primorial k', rfl⟩
    · -- i + 1 < k' + 1, so i + 1 ≤ k'
      have hle : i + 1 ≤ k' := by simp only [TauIdx] at *; omega
      obtain ⟨c, hc⟩ := ih hle
      exact ⟨nth_prime (k' + 1) * c, by
        rw [hc, ← Nat.mul_assoc,
          Nat.mul_comm (nth_prime (k' + 1)) (nth_prime (i + 1)),
          Nat.mul_assoc]⟩
```
