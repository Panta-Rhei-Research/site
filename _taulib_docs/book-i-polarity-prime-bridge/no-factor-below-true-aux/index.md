---
{
  "projection_kind": "taulib_declaration",
  "title": "no_factor_below_true_aux",
  "permalink": "/verify/taulib/docs/book-i-polarity-prime-bridge/no-factor-below-true-aux/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.PrimeBridge`.",
  "declaration_id": "TauLib.BookI.Polarity.PrimeBridge::no_factor_below_true_aux",
  "declaration_slug": "no-factor-below-true-aux",
  "kind": "theorem",
  "name": "no_factor_below_true_aux",
  "module_name": "TauLib.BookI.Polarity.PrimeBridge",
  "module_url": "/verify/taulib/docs/book-i-polarity-prime-bridge/",
  "source_line_start": 27,
  "source_line_end": 64,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimeBridge.lean#L27-L64",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimeBridge.lean#L27-L64",
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
- Source path: [`TauLib/BookI/Polarity/PrimeBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimeBridge.lean#L27-L64)
- Source range: L27-L64
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- ============================================================
-- NO_FACTOR_BELOW: FORWARD DIRECTION
-- ============================================================
```

## Source Excerpt

```lean
private theorem no_factor_below_true_aux (n : TauIdx) (hn : n ≥ 2) :
    ∀ fuel : Nat, ∀ d : TauIdx, fuel = n - d → d ≥ 2 →
    no_factor_below n d = true →
    ∀ k : TauIdx, k ≥ d → k * k ≤ n → n % k ≠ 0 := by
  intro fuel
  induction fuel using Nat.strongRecOn with
  | _ fuel ih =>
  intro d hfuel hd h k hkd hkk
  unfold no_factor_below at h
  split at h
  · -- d ≥ n: k ≥ d ≥ n, so k*k ≥ n*n > n (since n ≥ 2)
    rename_i hdn
    have hkn : k ≥ n := Nat.le_trans hdn hkd
    have : n * n ≤ k * k := Nat.mul_le_mul hkn hkn
    -- n * n ≤ k * k ≤ n, but n * n > n for n ≥ 2
    have hnn : n * n ≤ n := Nat.le_trans this hkk
    have hnn1 : n * n ≤ n * 1 := by rwa [Nat.mul_one]
    have : n ≤ 1 := Nat.le_of_mul_le_mul_left hnn1 (by simp only [TauIdx] at *; omega)
    simp only [TauIdx] at *; omega
  · split at h
    · -- d * d > n: k ≥ d, so k*k ≥ d*d > n, contradiction
      rename_i hdn hdd
      have : d * d ≤ k * k := Nat.mul_le_mul hkd hkd
      simp only [TauIdx] at *; omega
    · split at h
      · -- n % d = 0: returns false, contradicts h
        exact absurd h Bool.false_ne_true
      · -- Recursive case: ¬(n % d = 0), h : no_factor_below n (d+1) = true
        rename_i hdn hdd hmod
        -- hmod : ¬(n % d = 0)
        rcases Nat.eq_or_lt_of_le hkd with rfl | hlt
        · -- k = d: n % d ≠ 0
          exact hmod
        · -- k > d, so k ≥ d + 1: recurse
          have hfuel_lt : n - (d + 1) < fuel := by
            rw [hfuel]; simp only [TauIdx] at *; omega
          exact ih (n - (d + 1)) hfuel_lt (d + 1) rfl
              (by simp only [TauIdx] at *; omega) h k hlt hkk
```
