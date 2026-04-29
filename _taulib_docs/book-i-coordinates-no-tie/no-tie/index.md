---
{
  "projection_kind": "taulib_declaration",
  "title": "no_tie",
  "permalink": "/verify/taulib/docs/book-i-coordinates-no-tie/no-tie/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.NoTie`.",
  "declaration_id": "TauLib.BookI.Coordinates.NoTie::no_tie",
  "declaration_slug": "no-tie",
  "kind": "theorem",
  "name": "no_tie",
  "module_name": "TauLib.BookI.Coordinates.NoTie",
  "module_url": "/verify/taulib/docs/book-i-coordinates-no-tie/",
  "source_line_start": 94,
  "source_line_end": 132,
  "registry_ids": [
    "I.L03"
  ],
  "related_registry_items": [
    {
      "id": "I.L03",
      "title": "No-Tie Determinism",
      "url": "/registry/object/I.L03/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NoTie.lean#L94-L132",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.NoTie",
        "url": "/verify/taulib/docs/book-i-coordinates-no-tie/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NoTie.lean#L94-L132",
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

- Module: [TauLib.BookI.Coordinates.NoTie](/verify/taulib/docs/book-i-coordinates-no-tie/)
- Source path: [`TauLib/BookI/Coordinates/NoTie.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NoTie.lean#L94-L132)
- Source range: L94-L132
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.L03` — No-Tie Determinism

## Immediate Comment / Docstring

```lean
/-- [I.L03] No-Tie Lemma: If b₁ · A↑↑(c₁-1) = b₂ · A↑↑(c₂-1) (=: v),
    and both c₁, c₂ are maximal (¬(A↑↑cᵢ ∣ v)), then c₁ = c₂ and b₁ = b₂.

    Proof: Suppose c₁ < c₂. Then A↑↑c₁ ∣ A↑↑(c₂-1) (since both are
    powers of A and c₁ ≤ c₂-1). Hence A↑↑c₁ ∣ v = b₂ · A↑↑(c₂-1).
    But ¬(A↑↑c₁ ∣ v), contradiction. So c₁ = c₂, then b₁ = b₂. -/
```

## Source Excerpt

```lean
theorem no_tie (a b1 c1 b2 c2 : Nat)
    (ha : a ≥ 2)
    (_hb1 : b1 ≥ 1) (hc1 : c1 ≥ 1) (_hb2 : b2 ≥ 1) (hc2 : c2 ≥ 1)
    (heq : b1 * tetration a (c1 - 1) = b2 * tetration a (c2 - 1))
    (hmax1 : ¬(tetration a c1 ∣ b1 * tetration a (c1 - 1)))
    (hmax2 : ¬(tetration a c2 ∣ b2 * tetration a (c2 - 1))) :
    c1 = c2 ∧ b1 = b2 := by
  -- Step 1: Show c1 = c2
  have hc_eq : c1 = c2 := by
    -- By trichotomy: c1 < c2, c1 = c2, or c1 > c2
    rcases Nat.lt_or_ge c1 c2 with h | h
    · -- Case c1 < c2: contradiction with hmax1
      exfalso; apply hmax1
      -- A↑↑c1 | A↑↑(c2-1) (both powers of A, with exponent mono)
      have hdvd_tet : tetration a c1 ∣ tetration a (c2 - 1) :=
        tetration_dvd_of_le a ha hc1 (by omega : c2 - 1 ≥ 1) (Nat.le_sub_one_of_lt h)
      -- A↑↑(c2-1) | b2 * A↑↑(c2-1)
      have hdvd_mul : tetration a (c2 - 1) ∣ b2 * tetration a (c2 - 1) :=
        dvd_mul_left' _ _
      -- A↑↑c1 | v (by transitivity)
      rw [heq]
      exact dvd_trans' hdvd_tet hdvd_mul
    · -- Case c1 ≥ c2: show c2 ≥ c1 → c1 = c2
      rcases Nat.lt_or_ge c2 c1 with h' | h'
      · -- Case c2 < c1: contradiction with hmax2
        exfalso; apply hmax2
        have hdvd_tet : tetration a c2 ∣ tetration a (c1 - 1) :=
          tetration_dvd_of_le a ha hc2 (by omega : c1 - 1 ≥ 1) (Nat.le_sub_one_of_lt h')
        have hdvd_mul : tetration a (c1 - 1) ∣ b1 * tetration a (c1 - 1) :=
          dvd_mul_left' _ _
        rw [← heq]
        exact dvd_trans' hdvd_tet hdvd_mul
      · -- c1 ≤ c2 and c2 ≤ c1, so c1 = c2
        exact Nat.le_antisymm h' h
  -- Step 2: Show b1 = b2 (cancel A↑↑(c1-1))
  constructor
  · exact hc_eq
  · rw [hc_eq] at heq
    exact nat_mul_cancel_right heq (tetration_pos a (by omega : a ≥ 1) (c2 - 1))
```
