---
{
  "projection_kind": "taulib_declaration",
  "title": "toRat_inv",
  "permalink": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/to-rat-inv/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Bridge.TauRatQuotient`.",
  "declaration_id": "TauLib.BookI.Boundary.Bridge.TauRatQuotient::toRat_inv",
  "declaration_slug": "to-rat-inv",
  "kind": "theorem",
  "name": "toRat_inv",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauRatQuotient",
  "module_url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/",
  "source_line_start": 186,
  "source_line_end": 236,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L186-L236",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Bridge.TauRatQuotient",
        "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L186-L236",
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

- Module: [TauLib.BookI.Boundary.Bridge.TauRatQuotient](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/)
- Source path: [`TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L186-L236)
- Source range: L186-L236
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- toRat of inv: `(q.inv).toRat = (q.toRat)⁻¹`. -/
```

## Source Excerpt

```lean
theorem toRat_inv (q : TauRat) : q.inv.toRat = q.toRat⁻¹ := by
  unfold TauRat.inv
  by_cases hgt : q.num.pos > q.num.neg
  · -- positive case: q > 0
    simp only [hgt, ↓reduceDIte]
    unfold TauRat.toRat TauInt.toInt
    have hle : q.num.neg ≤ q.num.pos := Nat.le_of_lt hgt
    have hsub_rat : ((q.num.pos - q.num.neg : Nat) : Rat)
                  = (q.num.pos : Rat) - (q.num.neg : Rat) := by
      have hsub_int : ((q.num.pos - q.num.neg : Nat) : Int)
                    = (q.num.pos : Int) - (q.num.neg : Int) := Int.ofNat_sub hle
      exact_mod_cast hsub_int
    have hden_pos : (q.den : Rat) > 0 := q.den_pos_rat
    have hnum_lt : (q.num.neg : Rat) < (q.num.pos : Rat) := by exact_mod_cast hgt
    have hnum_ne : ((q.num.pos : Rat) - (q.num.neg : Rat)) ≠ 0 := by linarith
    push_cast
    rw [hsub_rat]
    field_simp
    ring
  · simp only [hgt, ↓reduceDIte]
    by_cases hlt : q.num.neg > q.num.pos
    · -- negative case: q < 0
      simp only [hlt, ↓reduceDIte]
      unfold TauRat.toRat TauInt.toInt
      have hle : q.num.pos ≤ q.num.neg := Nat.le_of_lt hlt
      have hsub_rat : ((q.num.neg - q.num.pos : Nat) : Rat)
                    = (q.num.neg : Rat) - (q.num.pos : Rat) := by
        have hsub_int : ((q.num.neg - q.num.pos : Nat) : Int)
                      = (q.num.neg : Int) - (q.num.pos : Int) := Int.ofNat_sub hle
        exact_mod_cast hsub_int
      have hden_pos : (q.den : Rat) > 0 := q.den_pos_rat
      have hnum_lt : (q.num.pos : Rat) < (q.num.neg : Rat) := by exact_mod_cast hlt
      have hnum_ne : ((q.num.pos : Rat) - (q.num.neg : Rat)) ≠ 0 := by linarith
      have hnum_ne' : ((q.num.neg : Rat) - (q.num.pos : Rat)) ≠ 0 := by linarith
      push_cast
      rw [hsub_rat]
      field_simp
      ring
    · -- zero case: pos = neg, so q.toRat = 0
      simp only [hlt, ↓reduceDIte]
      have h1 : q.num.pos ≤ q.num.neg := Nat.le_of_not_lt hgt
      have h2 : q.num.neg ≤ q.num.pos := Nat.le_of_not_lt hlt
      have heq : q.num.pos = q.num.neg := Nat.le_antisymm h1 h2
      have h_int : q.num.toInt = 0 := by
        unfold TauInt.toInt
        have : (q.num.pos : Int) = (q.num.neg : Int) := by exact_mod_cast heq
        linarith
      have h_rat : q.toRat = 0 := by
        unfold TauRat.toRat; rw [h_int]; simp
      rw [toRat_zero, h_rat]
      simp
```
