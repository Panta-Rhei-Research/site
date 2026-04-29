---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.sumFromTo_pi_pair_term_bound",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-pi/sum-from-to-pi-pair-term-bound/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealPi`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealPi::TauReal.sumFromTo_pi_pair_term_bound",
  "declaration_slug": "sum-from-to-pi-pair-term-bound",
  "kind": "theorem",
  "name": "TauReal.sumFromTo_pi_pair_term_bound",
  "module_name": "TauLib.BookI.Boundary.TauRealPi",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-pi/",
  "source_line_start": 152,
  "source_line_end": 199,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPi.lean#L152-L199",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealPi",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-pi/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPi.lean#L152-L199",
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

- Module: [TauLib.BookI.Boundary.TauRealPi](/verify/taulib/docs/book-i-boundary-tau-real-pi/)
- Source path: [`TauLib/BookI/Boundary/TauRealPi.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPi.lean#L152-L199)
- Source range: L152-L199
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Strengthened telescoping bound on the ranged sum:
    `sumFromTo pi_pair_term n m ≤ 1/(2n) − 1/(2m)` for `1 ≤ n ≤ m`. -/
```

## Source Excerpt

```lean
theorem TauReal.sumFromTo_pi_pair_term_bound (n : Nat) (hn : 1 ≤ n) :
    ∀ m, n ≤ m →
    (TauRat.sumFromTo TauRat.pi_pair_term n m).toRat
      ≤ 1 / (2 * (n : Rat)) - 1 / (2 * (m : Rat)) := by
  intro m hnm
  induction m with
  | zero => omega
  | succ m ih =>
    by_cases h_eq : n = m + 1
    · subst h_eq
      rw [TauRat.sumFromTo_self, toRat_zero]
      have h_pos : (0 : Rat) < (m : Rat) + 1 := by
        have : (0 : Rat) ≤ (m : Rat) := by exact_mod_cast Nat.zero_le m
        linarith
      have h_2pos : (0 : Rat) < 2 * ((m : Rat) + 1) := by linarith
      have h_recip_le : (1 : Rat) / (2 * ((m : Rat) + 1)) ≤ 1 / (2 * ((m : Rat) + 1)) :=
        _root_.le_refl _
      -- Goal: 0 ≤ 1/(2(m+1)) − 1/(2(m+1))
      have : (1 : Rat) / (2 * ((m : Rat) + 1)) - 1 / (2 * ((m : Rat) + 1)) = 0 := by ring
      have h_cast : ((m + 1 : Nat) : Rat) = (m : Rat) + 1 := by push_cast; ring
      rw [h_cast]
      linarith
    · have hnm' : n ≤ m := by omega
      have h_m_ge_one : 1 ≤ m := by omega
      have ih' := ih hnm'
      have h_rec : TauRat.sumFromTo TauRat.pi_pair_term n (m + 1) =
                   (TauRat.sumFromTo TauRat.pi_pair_term n m).add (TauRat.pi_pair_term m) := by
        show (if n ≤ m then _ else _) = _; rw [if_pos hnm']
      rw [h_rec, toRat_add]
      have h_term_bound : (TauRat.pi_pair_term m).toRat ≤
            (1 / 2) * (1 / (m : Rat) - 1 / ((m : Rat) + 1)) :=
        TauRat.pi_pair_term_le_telescope m h_m_ge_one
      -- Goal: SFT.toRat + pi_pair_term m .toRat ≤ 1/(2n) − 1/(2(m+1))
      -- IH:   SFT.toRat ≤ 1/(2n) − 1/(2m)
      -- Term: pi_pair_term m .toRat ≤ (1/2)(1/m − 1/(m+1)) = 1/(2m) − 1/(2(m+1))
      -- Sum:  SFT + term ≤ (1/(2n) − 1/(2m)) + (1/(2m) − 1/(2(m+1))) = 1/(2n) − 1/(2(m+1))  ✓
      -- Prepare cast equality for m + 1
      have h_cast_succ : ((m + 1 : Nat) : Rat) = (m : Rat) + 1 := by push_cast; ring
      rw [h_cast_succ]
      -- Bridge for linarith: (1/2)(1/m − 1/(m+1)) = 1/(2m) − 1/(2(m+1))
      have h_term_rewrite :
          (1 / 2) * (1 / (m : Rat) - 1 / ((m : Rat) + 1))
            = 1 / (2 * (m : Rat)) - 1 / (2 * ((m : Rat) + 1)) := by
        have h_m_pos : (0 : Rat) < (m : Rat) := by exact_mod_cast h_m_ge_one
        have h_m1_pos : (0 : Rat) < (m : Rat) + 1 := by linarith
        field_simp
      rw [h_term_rewrite] at h_term_bound
      linarith [ih']
```
