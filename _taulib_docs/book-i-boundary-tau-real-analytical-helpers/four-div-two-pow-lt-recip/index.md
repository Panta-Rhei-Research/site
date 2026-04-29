---
{
  "projection_kind": "taulib_declaration",
  "title": "Rat.four_div_two_pow_lt_recip",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-analytical-helpers/four-div-two-pow-lt-recip/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealAnalyticalHelpers`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealAnalyticalHelpers::Rat.four_div_two_pow_lt_recip",
  "declaration_slug": "four-div-two-pow-lt-recip",
  "kind": "theorem",
  "name": "Rat.four_div_two_pow_lt_recip",
  "module_name": "TauLib.BookI.Boundary.TauRealAnalyticalHelpers",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-analytical-helpers/",
  "source_line_start": 139,
  "source_line_end": 155,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAnalyticalHelpers.lean#L139-L155",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealAnalyticalHelpers",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-analytical-helpers/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAnalyticalHelpers.lean#L139-L155",
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

- Module: [TauLib.BookI.Boundary.TauRealAnalyticalHelpers](/verify/taulib/docs/book-i-boundary-tau-real-analytical-helpers/)
- Source path: [`TauLib/BookI/Boundary/TauRealAnalyticalHelpers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAnalyticalHelpers.lean#L139-L155)
- Source range: L139-L155
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The central inequality: for `k + 3 ≤ n`, `4/2^n < 1/(k+1)` over `Rat`.

    Proof chain:
    • `k + 3 ≤ n` gives `2^(k+3) ≤ 2^n` via `pow_le_pow_right₀`.
    • `2^(k+3) = 4 · 2^(k+1)` by ring.
    • `(k + 1 : Rat) < 2^(k+1)` by `Rat.two_pow_succ_gt_linear`.
    • Combine: `4(k+1) < 4 · 2^(k+1) = 2^(k+3) ≤ 2^n`.
    • Reciprocal: `4/2^n < 1/(k+1)` via `div_lt_div_iff₀`. -/
```

## Source Excerpt

```lean
theorem Rat.four_div_two_pow_lt_recip (k n : Nat) (hn : k + 3 ≤ n) :
    (4 : Rat) / (2 : Rat) ^ n < 1 / ((k : Rat) + 1) := by
  have h_exp : (2 : Rat) ^ (k + 3) ≤ (2 : Rat) ^ n :=
    pow_le_pow_right₀ (by norm_num : (1 : Rat) ≤ 2) (by omega : k + 3 ≤ n)
  have h_exp_pos : (0 : Rat) < 2 ^ n := by positivity
  have h_lin := Rat.two_pow_succ_gt_linear k
  have h_k3 : (2 : Rat) ^ (k + 3) = 4 * (2 : Rat) ^ (k + 1) := by ring
  have h_pos_k1 : (0 : Rat) < (k : Rat) + 1 := by
    have : (0 : Rat) ≤ (k : Rat) := by exact_mod_cast Nat.zero_le k
    linarith
  have h_key : 4 * ((k : Rat) + 1) < (2 : Rat) ^ n := by
    have h1 : 4 * ((k : Rat) + 1) < 4 * (2 : Rat) ^ (k + 1) := by linarith
    linarith [h_exp, h_k3]
  rw [div_lt_div_iff₀ h_exp_pos h_pos_k1]
  linarith

end Tau.Boundary
```
