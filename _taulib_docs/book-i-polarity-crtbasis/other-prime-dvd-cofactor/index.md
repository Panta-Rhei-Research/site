---
{
  "projection_kind": "taulib_declaration",
  "title": "other_prime_dvd_cofactor",
  "permalink": "/verify/taulib/docs/book-i-polarity-crtbasis/other-prime-dvd-cofactor/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.CRTBasis`.",
  "declaration_id": "TauLib.BookI.Polarity.CRTBasis::other_prime_dvd_cofactor",
  "declaration_slug": "other-prime-dvd-cofactor",
  "kind": "theorem",
  "name": "other_prime_dvd_cofactor",
  "module_name": "TauLib.BookI.Polarity.CRTBasis",
  "module_url": "/verify/taulib/docs/book-i-polarity-crtbasis/",
  "source_line_start": 141,
  "source_line_end": 157,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L141-L157",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L141-L157",
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
- Source path: [`TauLib/BookI/Polarity/CRTBasis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L141-L157)
- Source range: L141-L157
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- p_{j+1} divides the cofactor M_k/p_{i+1} when j ≠ i (both < k). -/
```

## Source Excerpt

```lean
theorem other_prime_dvd_cofactor {k i j : TauIdx}
    (hi : i < k) (hj : j < k) (hne : i ≠ j) (hyp : CRTHyp k) :
    nth_prime (j + 1) ∣ primorial k / nth_prime (i + 1) := by
  have hjdvd := nth_prime_dvd_primorial (show j + 1 ≤ k by simp only [TauIdx] at *; omega)
  rw [← cofactor_exact (show i + 1 ≤ k by simp only [TauIdx] at *; omega)] at hjdvd
  have hp_j := hyp.all_prime j hj
  rcases euclid_lemma hp_j hjdvd with h | h
  · exact h
  · -- p_{j+1} | p_{i+1}: contradiction
    exfalso
    have hcop := hyp.pairwise_coprime j i hj hi (Ne.symm hne)
    -- p_{j+1} | p_{i+1} and gcd(p_{j+1}, p_{i+1}) = 1, but p_{j+1} ≥ 2
    have hle := Nat.le_of_dvd
      (by have := (hyp.all_prime i hi).1; simp only [TauIdx] at *; omega)
      (Nat.dvd_gcd ⟨1, (Nat.mul_one _).symm⟩ h)
    rw [hcop] at hle
    have := hp_j.1; simp only [TauIdx] at *; omega
```
