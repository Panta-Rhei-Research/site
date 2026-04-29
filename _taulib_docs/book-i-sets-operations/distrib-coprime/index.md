---
{
  "projection_kind": "taulib_declaration",
  "title": "distrib_coprime",
  "permalink": "/verify/taulib/docs/book-i-sets-operations/distrib-coprime/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.Operations`.",
  "declaration_id": "TauLib.BookI.Sets.Operations::distrib_coprime",
  "declaration_slug": "distrib-coprime",
  "kind": "theorem",
  "name": "distrib_coprime",
  "module_name": "TauLib.BookI.Sets.Operations",
  "module_url": "/verify/taulib/docs/book-i-sets-operations/",
  "source_line_start": 182,
  "source_line_end": 241,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Operations.lean#L182-L241",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.Operations",
        "url": "/verify/taulib/docs/book-i-sets-operations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Operations.lean#L182-L241",
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

- Module: [TauLib.BookI.Sets.Operations](/verify/taulib/docs/book-i-sets-operations/)
- Source path: [`TauLib/BookI/Sets/Operations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Operations.lean#L182-L241)
- Source range: L182-L241
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The coprime-case proof for distributivity. When a > 0 and gcd(a, gcd(b,c)) = 1,
    we show gcd(a, lcm(b,c)) = gcd(a,b) * gcd(a,c).

    Requires a > 0 to guarantee P = gcd(a,b)*gcd(a,c) > 0, avoiding
    degenerate cases. The a = 0 case is handled separately in nat_gcd_distrib_lcm. -/
```

## Source Excerpt

```lean
private theorem distrib_coprime (a b c : Nat) (ha : a > 0)
    (h_coprime : Nat.Coprime a (Nat.gcd b c)) :
    Nat.gcd a (Nat.lcm b c) = Nat.gcd a b * Nat.gcd a c := by
  have hcop_parts : Nat.Coprime (Nat.gcd a b) (Nat.gcd a c) := by
    show Nat.gcd (Nat.gcd a b) (Nat.gcd a c) = 1; rw [gcd_gcd_eq]; exact h_coprime
  -- P = gcd(a,b) * gcd(a,c) > 0 since a > 0 implies gcd(a,b) ≥ 1 and gcd(a,c) ≥ 1
  set P := Nat.gcd a b * Nat.gcd a c with hP_def
  have hgab_pos : Nat.gcd a b > 0 := Nat.pos_of_ne_zero (fun h => by
    have := Nat.gcd_eq_zero_iff.mp h; omega)
  have hgac_pos : Nat.gcd a c > 0 := Nat.pos_of_ne_zero (fun h => by
    have := Nat.gcd_eq_zero_iff.mp h; omega)
  have hPpos : P > 0 := Nat.mul_pos hgab_pos hgac_pos
  have hPa : P ∣ a := hcop_parts.mul_dvd_of_dvd_of_dvd (Nat.gcd_dvd_left a b) (Nat.gcd_dvd_left a c)
  have hPl : P ∣ Nat.lcm b c := hcop_parts.mul_dvd_of_dvd_of_dvd
    (Nat.dvd_trans (Nat.gcd_dvd_right a b) (Nat.dvd_lcm_left b c))
    (Nat.dvd_trans (Nat.gcd_dvd_right a c) (Nat.dvd_lcm_right b c))
  obtain ⟨m, hm⟩ := hPa
  obtain ⟨n, hn⟩ := hPl
  have h_gcd : Nat.gcd a (Nat.lcm b c) = P * Nat.gcd m n := by rw [hm, hn, Nat.gcd_mul_left]
  rw [h_gcd]; suffices Nat.gcd m n = 1 by rw [this, Nat.mul_one]
  obtain ⟨b', hb'⟩ := Nat.gcd_dvd_right a b
  obtain ⟨c', hc'⟩ := Nat.gcd_dvd_right a c
  -- coprime(gcd(a,c)*m, b'): factor through gcd(a, b) = gcd(a,b) * gcd(gcd(a,c)*m, b')
  have h_cop1 : Nat.Coprime (Nat.gcd a c * m) b' := by
    have hm_expand : a = Nat.gcd a b * (Nat.gcd a c * m) := by
      rw [← Nat.mul_assoc]; exact hm
    have h_factor : Nat.gcd a b * Nat.gcd (Nat.gcd a c * m) b' = Nat.gcd a b := by
      rw [← Nat.gcd_mul_left, ← hm_expand, ← hb']
    have : Nat.gcd a b * 1 = Nat.gcd a b * Nat.gcd (Nat.gcd a c * m) b' := by
      rw [Nat.mul_one]; exact h_factor.symm
    exact (nat_mul_cancel hgab_pos this).symm
  -- coprime(gcd(a,b)*m, c'): symmetric argument
  have h_cop2 : Nat.Coprime (Nat.gcd a b * m) c' := by
    have hm_expand : a = Nat.gcd a c * (Nat.gcd a b * m) := by
      have : a = P * m := hm; rw [hP_def] at this
      calc a = Nat.gcd a b * Nat.gcd a c * m := this
        _ = Nat.gcd a c * Nat.gcd a b * m := by ring
        _ = Nat.gcd a c * (Nat.gcd a b * m) := by ring
    have h_factor : Nat.gcd a c * Nat.gcd (Nat.gcd a b * m) c' = Nat.gcd a c := by
      rw [← Nat.gcd_mul_left, ← hm_expand, ← hc']
    have : Nat.gcd a c * 1 = Nat.gcd a c * Nat.gcd (Nat.gcd a b * m) c' := by
      rw [Nat.mul_one]; exact h_factor.symm
    exact (nat_mul_cancel hgac_pos this).symm
  have h_m_b' : Nat.Coprime m b' := h_cop1.coprime_dvd_left (Nat.dvd_mul_left m _)
  have h_m_c' : Nat.Coprime m c' := h_cop2.coprime_dvd_left (Nat.dvd_mul_left m _)
  have h_m_prod : Nat.Coprime m (b' * c') := h_m_b'.mul_right h_m_c'
  have h_n_dvd : n ∣ b' * c' := by
    apply nat_mul_dvd_cancel hPpos
    show P * n ∣ P * (b' * c')
    have hn' : P * n = Nat.lcm b c := hn.symm
    rw [hn']
    calc Nat.lcm b c ∣ b * c := by
            rw [show b * c = Nat.gcd b c * Nat.lcm b c from (Nat.gcd_mul_lcm b c).symm]
            exact Nat.dvd_mul_left _ _
      _ = Nat.gcd a b * b' * (Nat.gcd a c * c') := by rw [← hb', ← hc']
      _ = P * (b' * c') := by rw [hP_def]; ring
  have : Nat.gcd m n ∣ Nat.gcd m (b' * c') :=
    Nat.dvd_gcd (Nat.gcd_dvd_left m n) (Nat.dvd_trans (Nat.gcd_dvd_right m n) h_n_dvd)
  rw [h_m_prod] at this
  exact Nat.eq_one_of_dvd_one this
```
