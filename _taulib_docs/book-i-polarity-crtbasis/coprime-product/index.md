---
{
  "projection_kind": "taulib_declaration",
  "title": "coprime_product",
  "permalink": "/verify/taulib/docs/book-i-polarity-crtbasis/coprime-product/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.CRTBasis`.",
  "declaration_id": "TauLib.BookI.Polarity.CRTBasis::coprime_product",
  "declaration_slug": "coprime-product",
  "kind": "theorem",
  "name": "coprime_product",
  "module_name": "TauLib.BookI.Polarity.CRTBasis",
  "module_url": "/verify/taulib/docs/book-i-polarity-crtbasis/",
  "source_line_start": 31,
  "source_line_end": 59,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L31-L59",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L31-L59",
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
- Source path: [`TauLib/BookI/Polarity/CRTBasis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L31-L59)
- Source range: L31-L59
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- coprime(a,c) ∧ coprime(b,c) → coprime(a*b,c).
    Proof by prime factor contradiction using euclid_lemma. -/
```

## Source Excerpt

```lean
theorem coprime_product {a b c : Nat}
    (hac : Nat.Coprime a c) (hbc : Nat.Coprime b c) :
    Nat.Coprime (a * b) c := by
  by_contra hne
  -- gcd(a*b, c) ≥ 2
  have hne0 : Nat.gcd (a * b) c ≠ 0 := by
    intro h0
    apply hne
    -- gcd = 0 → c = 0
    have hc0 : c = 0 := by
      rcases Nat.gcd_dvd_right (a * b) c with ⟨k, hk⟩
      rw [h0, Nat.zero_mul] at hk; exact hk
    subst hc0
    -- hac : Coprime a 0, hbc : Coprime b 0 — unwrap to gcd form
    have ha : Nat.gcd a 0 = 1 := hac
    have hb : Nat.gcd b 0 = 1 := hbc
    rw [Nat.gcd_zero_right] at ha hb
    show Nat.gcd (a * b) 0 = 1
    rw [Nat.gcd_zero_right, ha, hb]
  have hge2 : Nat.gcd (a * b) c ≥ 2 := by omega
  obtain ⟨p, hp, hpdvd⟩ := exists_prime_divisor _ hge2
  have hpab : p ∣ a * b := dvd_trans hpdvd (Nat.gcd_dvd_left _ _)
  have hpc : p ∣ c := dvd_trans hpdvd (Nat.gcd_dvd_right _ _)
  rcases euclid_lemma hp hpab with hpa | hpb
  · -- p | a and p | c → p | gcd(a,c) = 1, but p ≥ 2
    have h1 := Nat.le_of_dvd (by omega) (Nat.dvd_gcd hpa hpc)
    rw [hac] at h1; have := hp.1; simp only [TauIdx] at *; omega
  · have h1 := Nat.le_of_dvd (by omega) (Nat.dvd_gcd hpb hpc)
    rw [hbc] at h1; have := hp.1; simp only [TauIdx] at *; omega
```
