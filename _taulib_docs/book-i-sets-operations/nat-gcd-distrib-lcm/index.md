---
{
  "projection_kind": "taulib_declaration",
  "title": "nat_gcd_distrib_lcm",
  "permalink": "/verify/taulib/docs/book-i-sets-operations/nat-gcd-distrib-lcm/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.Operations`.",
  "declaration_id": "TauLib.BookI.Sets.Operations::nat_gcd_distrib_lcm",
  "declaration_slug": "nat-gcd-distrib-lcm",
  "kind": "theorem",
  "name": "nat_gcd_distrib_lcm",
  "module_name": "TauLib.BookI.Sets.Operations",
  "module_url": "/verify/taulib/docs/book-i-sets-operations/",
  "source_line_start": 245,
  "source_line_end": 281,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Operations.lean#L245-L281",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Operations.lean#L245-L281",
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
- Source path: [`TauLib/BookI/Sets/Operations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Operations.lean#L245-L281)
- Source range: L245-L281
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- gcd distributes over lcm for Nat (the core identity).
    gcd(a, lcm(b,c)) = lcm(gcd(a,b), gcd(a,c)). -/
```

## Source Excerpt

```lean
private theorem nat_gcd_distrib_lcm (a b c : Nat) :
    Nat.gcd a (Nat.lcm b c) = Nat.lcm (Nat.gcd a b) (Nat.gcd a c) := by
  -- Handle a = 0 case directly (everything collapses)
  by_cases ha : a = 0
  · subst ha; simp [Nat.gcd_zero_left]
  -- Factor out G = gcd(a, gcd(b,c))
  set G := Nat.gcd a (Nat.gcd b c) with hG_def
  have hG_pos : G > 0 := by
    apply Nat.pos_of_ne_zero; intro hG0
    rw [Nat.gcd_eq_zero_iff] at hG0; exact ha hG0.1
  have hGa : G ∣ a := Nat.gcd_dvd_left a _
  have hGb : G ∣ b := Nat.dvd_trans (Nat.gcd_dvd_right a _) (Nat.gcd_dvd_left b c)
  have hGc : G ∣ c := Nat.dvd_trans (Nat.gcd_dvd_right a _) (Nat.gcd_dvd_right b c)
  obtain ⟨a', ha'⟩ := hGa
  obtain ⟨b', hb'⟩ := hGb
  obtain ⟨c', hc'⟩ := hGc
  have h_lhs : Nat.gcd a (Nat.lcm b c) = G * Nat.gcd a' (Nat.lcm b' c') := by
    rw [ha', hb', hc', Nat.lcm_mul_left, Nat.gcd_mul_left]
  have h_rhs : Nat.lcm (Nat.gcd a b) (Nat.gcd a c) =
      G * Nat.lcm (Nat.gcd a' b') (Nat.gcd a' c') := by
    rw [ha', hb', hc', Nat.gcd_mul_left, Nat.gcd_mul_left, Nat.lcm_mul_left]
  rw [h_lhs, h_rhs]; congr 1
  -- Coprime case: gcd(a', gcd(b',c')) = 1
  have h_coprime : Nat.Coprime a' (Nat.gcd b' c') := by
    show Nat.gcd a' (Nat.gcd b' c') = 1
    have h_eq : G * Nat.gcd a' (Nat.gcd b' c') = G * 1 := by
      rw [Nat.mul_one, ← Nat.gcd_mul_left, ← Nat.gcd_mul_left, ← ha', ← hb', ← hc']
    exact nat_mul_cancel hG_pos h_eq
  have ha'_pos : a' > 0 := Nat.pos_of_ne_zero (fun h => by
    rw [h, Nat.mul_zero] at ha'; exact ha ha')
  have h_dist := distrib_coprime a' b' c' ha'_pos h_coprime
  have hcop_parts : Nat.Coprime (Nat.gcd a' b') (Nat.gcd a' c') := by
    show Nat.gcd (Nat.gcd a' b') (Nat.gcd a' c') = 1; rw [gcd_gcd_eq]; exact h_coprime
  have h_lcm_prod : Nat.lcm (Nat.gcd a' b') (Nat.gcd a' c') = Nat.gcd a' b' * Nat.gcd a' c' := by
    have := (Nat.gcd_mul_lcm (Nat.gcd a' b') (Nat.gcd a' c')).symm
    rw [hcop_parts, Nat.one_mul] at this; exact this.symm
  rw [h_lcm_prod, ← h_dist]
```
