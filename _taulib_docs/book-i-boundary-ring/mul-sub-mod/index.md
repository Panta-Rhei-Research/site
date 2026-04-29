---
{
  "projection_kind": "taulib_declaration",
  "title": "mul_sub_mod",
  "permalink": "/verify/taulib/docs/book-i-boundary-ring/mul-sub-mod/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Ring`.",
  "declaration_id": "TauLib.BookI.Boundary.Ring::mul_sub_mod",
  "declaration_slug": "mul-sub-mod",
  "kind": "theorem",
  "name": "mul_sub_mod",
  "module_name": "TauLib.BookI.Boundary.Ring",
  "module_url": "/verify/taulib/docs/book-i-boundary-ring/",
  "source_line_start": 58,
  "source_line_end": 98,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L58-L98",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Ring",
        "url": "/verify/taulib/docs/book-i-boundary-ring/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L58-L98",
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

- Module: [TauLib.BookI.Boundary.Ring](/verify/taulib/docs/book-i-boundary-ring/)
- Source path: [`TauLib/BookI/Boundary/Ring.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L58-L98)
- Source range: L58-L98
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Helper: (m * c - a) % m = (m - a % m) % m when a ≤ m * c and m > 0.
    Proof by induction on c. -/
```

## Source Excerpt

```lean
private theorem mul_sub_mod (m : Nat) (hm : m > 0) :
    ∀ (c a : Nat), a ≤ m * c → (m * c - a) % m = (m - a % m) % m := by
  intro c
  induction c with
  | zero =>
    intro a ha
    simp only [Nat.mul_zero, Nat.le_zero] at ha
    subst ha; simp
  | succ c' ih =>
    intro a ha
    by_cases ham : a ≤ m * c'
    · -- a ≤ m * c': strip one copy of m
      have h1 : m * (c' + 1) - a = m * c' - a + m := by
        have := mul_succ_eq m c'
        omega
      rw [h1, Nat.add_mod_right]
      exact ih a ham
    · -- a > m * c': a is in the last "block" [m*c', m*(c'+1)]
      push_neg at ham
      -- a - m*c' is in range (0, m]
      have h_diff_bound : a - m * c' ≤ m := by
        have := mul_succ_eq m c'; omega
      have h_diff_pos : a - m * c' > 0 := by omega
      -- m*(c'+1) - a = m - (a - m*c')
      have h_rhs : m * (c' + 1) - a = m - (a - m * c') := by
        have := mul_succ_eq m c'; omega
      rw [h_rhs]
      -- a % m = (a - m*c') % m because a = m*c' + (a - m*c')
      have hmod : a % m = (a - m * c') % m := by
        have ha_split : a = a - m * c' + m * c' := by omega
        conv_lhs => rw [ha_split]
        exact Nat.add_mul_mod_self_left (a - m * c') m c'
      rw [hmod]
      -- case split: a - m*c' = m or < m
      by_cases heq : a - m * c' = m
      · -- a - m*c' = m: both sides become 0
        rw [heq]
        -- Goal: (m - m) % m = (m - m % m) % m
        simp [Nat.mod_self]
      · have hlt : a - m * c' < m := by omega
        rw [Nat.mod_eq_of_lt hlt]
```
