---
{
  "projection_kind": "taulib_declaration",
  "title": "mod_inv_exists",
  "permalink": "/verify/taulib/docs/book-i-polarity-ext-gcd/mod-inv-exists/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.ExtGCD`.",
  "declaration_id": "TauLib.BookI.Polarity.ExtGCD::mod_inv_exists",
  "declaration_slug": "mod-inv-exists",
  "kind": "theorem",
  "name": "mod_inv_exists",
  "module_name": "TauLib.BookI.Polarity.ExtGCD",
  "module_url": "/verify/taulib/docs/book-i-polarity-ext-gcd/",
  "source_line_start": 91,
  "source_line_end": 130,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ExtGCD.lean#L91-L130",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.ExtGCD",
        "url": "/verify/taulib/docs/book-i-polarity-ext-gcd/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ExtGCD.lean#L91-L130",
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

- Module: [TauLib.BookI.Polarity.ExtGCD](/verify/taulib/docs/book-i-polarity-ext-gcd/)
- Source path: [`TauLib/BookI/Polarity/ExtGCD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ExtGCD.lean#L91-L130)
- Source range: L91-L130
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- If gcd(a, m) = 1 and m > 1, there exists x < m with (a*x) % m = 1. -/
```

## Source Excerpt

```lean
theorem mod_inv_exists (a m : Nat) (hcop : Nat.Coprime a m) (hm : m > 1) :
    ∃ x : Nat, x < m ∧ (a * x) % m = 1 := by
  -- Get Bézout: ↑a * s + ↑m * t = ↑(gcd a m) = 1
  have hbez := ext_gcd_spec a m
  rw [hcop] at hbez
  -- hbez : ↑a * s + ↑m * t = 1
  set s := (ext_gcd a m).2.1
  set t := (ext_gcd a m).2.2
  -- (↑a * s) mod ↑m = 1
  have hm0 : (↑m : Int) ≠ 0 := by omega
  have hm_pos : (↑m : Int) > 0 := by omega
  have has_mod : ((↑a : Int) * s) % (↑m : Int) = 1 := by
    -- (↑a * s + ↑m * t) % ↑m = (↑a * s) % ↑m
    have h1 := Int.add_mul_emod_self_left ((↑a : Int) * s) (↑m : Int) t
    -- h1 : (↑a * s + ↑m * t) % ↑m = (↑a * s) % ↑m
    rw [hbez] at h1
    -- h1 : (1 : Int) % ↑m = (↑a * s) % ↑m
    rw [Int.emod_eq_of_lt (by omega) (by omega)] at h1
    -- h1 : 1 = (↑a * s) % ↑m
    exact h1.symm
  -- Positive representative: x = ((s % m) + m) % m
  let x_int := (s % (↑m : Int) + ↑m) % (↑m : Int)
  have hx_nonneg : x_int ≥ 0 := Int.emod_nonneg _ hm0
  have hx_lt : x_int < (↑m : Int) := Int.emod_lt_of_pos _ hm_pos
  -- x_int = s % ↑m (and hence x_int ≡ s mod m)
  have hx_eq : x_int = s % (↑m : Int) := by
    show (s % (↑m : Int) + ↑m) % (↑m : Int) = s % (↑m : Int)
    have h1 := Int.add_mul_emod_self_left (s % (↑m : Int)) (↑m : Int) 1
    simp only [Int.mul_one] at h1
    rw [h1]; exact Int.emod_emod_of_dvd s ⟨1, by ring⟩
  have hx_mod : ((↑a : Int) * x_int) % (↑m : Int) = 1 := by
    rw [hx_eq, Int.mul_emod (↑a : Int) (s % (↑m : Int)) (↑m : Int),
        Int.emod_emod_of_dvd s ⟨1, by ring⟩, ← Int.mul_emod, has_mod]
  -- Convert to Nat
  use x_int.toNat
  refine ⟨?_, ?_⟩
  · exact (Int.toNat_lt hx_nonneg).mpr hx_lt
  · have : (↑(a * x_int.toNat) : Int) % (↑m : Int) = 1 := by
      rw [Nat.cast_mul, Int.toNat_of_nonneg hx_nonneg]; exact hx_mod
    exact_mod_cast this
```
