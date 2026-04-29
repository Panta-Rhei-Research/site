---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.add_respects_equiv",
  "permalink": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/add-respects-equiv/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Bridge.TauRealCongruence`.",
  "declaration_id": "TauLib.BookI.Boundary.Bridge.TauRealCongruence::TauReal.add_respects_equiv",
  "declaration_slug": "add-respects-equiv",
  "kind": "theorem",
  "name": "TauReal.add_respects_equiv",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauRealCongruence",
  "module_url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/",
  "source_line_start": 78,
  "source_line_end": 117,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean#L78-L117",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Bridge.TauRealCongruence",
        "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean#L78-L117",
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

- Module: [TauLib.BookI.Boundary.Bridge.TauRealCongruence](/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/)
- Source path: [`TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean#L78-L117)
- Source range: L78-L117
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Addition respects Cauchy equivalence.**

    If `a₁ ≡ a₂` and `b₁ ≡ b₂` (Cauchy-equiv), then `a₁ + b₁ ≡ a₂ + b₂`.
    The triangle inequality `|x+y| ≤ |x|+|y|` reduces this to splitting
    the target tolerance `1/(k+1)` into `1/(2k+2) + 1/(2k+2)` and pulling
    each input equiv at refined level `2k+1`. -/
```

## Source Excerpt

```lean
theorem TauReal.add_respects_equiv
    (a₁ a₂ b₁ b₂ : TauReal)
    (ha : TauReal.equiv a₁ a₂) (hb : TauReal.equiv b₁ b₂) :
    TauReal.equiv (a₁.add b₁) (a₂.add b₂) := by
  obtain ⟨μa, hma⟩ := ha
  obtain ⟨μb, hmb⟩ := hb
  refine ⟨fun k => max (μa (2*k + 1)) (μb (2*k + 1)), fun k n hn => ?_⟩
  have hna : μa (2*k + 1) ≤ n := le_of_max_le_left hn
  have hnb : μb (2*k + 1) ≤ n := le_of_max_le_right hn
  have ha_step := hma (2*k + 1) n hna
  have hb_step := hmb (2*k + 1) n hnb
  unfold TauRat.lt at ha_step hb_step ⊢
  rw [TauRat.toRat_abs, toRat_sub] at ha_step hb_step
  rw [TauRat.toRat_abs, toRat_sub]
  rw [TauRat.ofNatRecip_toRat] at ha_step hb_step ⊢
  have h_lhs_eq :
      ((a₁.add b₁).approx n).toRat - ((a₂.add b₂).approx n).toRat
        = ((a₁.approx n).toRat - (a₂.approx n).toRat) +
          ((b₁.approx n).toRat - (b₂.approx n).toRat) := by
    show ((a₁.approx n).add (b₁.approx n)).toRat -
           ((a₂.approx n).add (b₂.approx n)).toRat = _
    rw [toRat_add, toRat_add]; ring
  rw [h_lhs_eq]
  -- Goal: |x + y| < 1/(k+1), with |x| < 1/(2k+2), |y| < 1/(2k+2)
  have h_tri := abs_add_le
      ((a₁.approx n).toRat - (a₂.approx n).toRat)
      ((b₁.approx n).toRat - (b₂.approx n).toRat)
  have hk_pos : (0 : Rat) < (2*k + 1 : Nat) + 1 := by
    have : (0 : Rat) ≤ (2*k + 1 : Nat) := by exact_mod_cast Nat.zero_le _
    linarith
  have hkk_pos : (0 : Rat) < (k : Rat) + 1 := by
    have : (0 : Rat) ≤ (k : Rat) := by exact_mod_cast Nat.zero_le k
    linarith
  -- 1/((2k+1)+1) = 1/(2(k+1)) so 1/(2k+2) + 1/(2k+2) = 1/(k+1)
  have h_split : (1 : Rat) / ((2*k + 1 : Nat) + 1) +
                 1 / ((2*k + 1 : Nat) + 1) = 1 / ((k : Rat) + 1) := by
    push_cast
    field_simp
    ring
  linarith
```
