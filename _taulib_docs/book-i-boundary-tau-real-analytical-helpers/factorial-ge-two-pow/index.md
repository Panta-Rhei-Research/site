---
{
  "projection_kind": "taulib_declaration",
  "title": "Nat.factorial_ge_two_pow",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-analytical-helpers/factorial-ge-two-pow/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealAnalyticalHelpers`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealAnalyticalHelpers::Nat.factorial_ge_two_pow",
  "declaration_slug": "factorial-ge-two-pow",
  "kind": "theorem",
  "name": "Nat.factorial_ge_two_pow",
  "module_name": "TauLib.BookI.Boundary.TauRealAnalyticalHelpers",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-analytical-helpers/",
  "source_line_start": 51,
  "source_line_end": 73,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAnalyticalHelpers.lean#L51-L73",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAnalyticalHelpers.lean#L51-L73",
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
- Source path: [`TauLib/BookI/Boundary/TauRealAnalyticalHelpers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAnalyticalHelpers.lean#L51-L73)
- Source range: L51-L73
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `2^(n−1) ≤ n!` for `n ≥ 1`, pure-Nat form. -/
```

## Source Excerpt

```lean
theorem Nat.factorial_ge_two_pow (n : Nat) (hn : 1 ≤ n) :
    2 ^ (n - 1) ≤ Nat.factorial n := by
  induction n with
  | zero => omega
  | succ n ih =>
    rcases Nat.lt_or_ge 1 (n + 1) with h | h
    · have hn' : 1 ≤ n := by omega
      have ih' := ih hn'
      have h_lhs : 2 ^ ((n + 1) - 1) = 2 * 2 ^ (n - 1) := by
        have h_sub : (n + 1) - 1 = n := by omega
        have h_n : n = (n - 1) + 1 := by omega
        rw [h_sub]; conv_lhs => rw [h_n]
        rw [pow_succ]; ring
      rw [h_lhs, Nat.factorial_succ]
      have h2 : 2 ≤ n + 1 := by omega
      have hfn : 0 < Nat.factorial n := Nat.factorial_pos n
      calc 2 * 2 ^ (n - 1)
          ≤ 2 * Nat.factorial n := by
            have := ih'; have := hfn; nlinarith
        _ ≤ (n + 1) * Nat.factorial n :=
            Nat.mul_le_mul_right _ h2
    · have hn0 : n = 0 := by omega
      subst hn0; simp [Nat.factorial]
```
