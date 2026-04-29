---
{
  "projection_kind": "taulib_declaration",
  "title": "bool_of_is_prime",
  "permalink": "/verify/taulib/docs/book-i-polarity-prime-bridge/bool-of-is-prime/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.PrimeBridge`.",
  "declaration_id": "TauLib.BookI.Polarity.PrimeBridge::bool_of_is_prime",
  "declaration_slug": "bool-of-is-prime",
  "kind": "theorem",
  "name": "bool_of_is_prime",
  "module_name": "TauLib.BookI.Polarity.PrimeBridge",
  "module_url": "/verify/taulib/docs/book-i-polarity-prime-bridge/",
  "source_line_start": 166,
  "source_line_end": 179,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimeBridge.lean#L166-L179",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimeBridge.lean#L166-L179",
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
- Source path: [`TauLib/BookI/Polarity/PrimeBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimeBridge.lean#L166-L179)
- Source range: L166-L179
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Backward: idx_prime p → is_prime_bool p = true. -/
```

## Source Excerpt

```lean
theorem bool_of_is_prime (p : TauIdx) (h : idx_prime p) : is_prime_bool p = true := by
  unfold is_prime_bool
  simp only [Bool.and_eq_true, decide_eq_true_eq]
  refine ⟨h.1, no_factor_below_of_spec p 2 h.1 (Nat.le_refl 2) fun k hk2 hkk hmod => ?_⟩
  have hkdvd : k ∣ p := Nat.dvd_of_mod_eq_zero hmod
  rcases h.2 k hkdvd with hk1 | hkp
  · -- k = 1 contradicts k ≥ 2
    simp only [TauIdx] at *; omega
  · -- k = p: k*k ≤ p with k = p contradicts p ≥ 2
    rw [hkp] at hkk
    have hp0 : p > 0 := by simp only [TauIdx] at *; omega
    have hkk' : p * p ≤ p * 1 := by rwa [Nat.mul_one]
    have := Nat.le_of_mul_le_mul_left hkk' hp0
    simp only [TauIdx] at *; omega
```
