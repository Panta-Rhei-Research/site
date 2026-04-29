---
{
  "projection_kind": "taulib_declaration",
  "title": "toRat_inv",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-rat-inv/to-rat-inv/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRatInv`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRatInv::toRat_inv",
  "declaration_slug": "to-rat-inv",
  "kind": "theorem",
  "name": "toRat_inv",
  "module_name": "TauLib.BookI.Boundary.TauRatInv",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-rat-inv/",
  "source_line_start": 93,
  "source_line_end": 131,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatInv.lean#L93-L131",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRatInv",
        "url": "/verify/taulib/docs/book-i-boundary-tau-rat-inv/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatInv.lean#L93-L131",
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

- Module: [TauLib.BookI.Boundary.TauRatInv](/verify/taulib/docs/book-i-boundary-tau-rat-inv/)
- Source path: [`TauLib/BookI/Boundary/TauRatInv.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatInv.lean#L93-L131)
- Source range: L93-L131
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `toRat` is a homomorphism with respect to inverses: the toRat of
    `q.inv h` equals `q.toRat⁻¹`.

    Strategy: route `Int.natAbs` through the `|·|` notation on `Rat` via
    `Int.cast_natAbs` (which says `((n.natAbs : Nat) : α) = |(n : α)|` on a
    suitable ordered type).  Then close each sign branch with
    `abs_of_pos` / `abs_of_neg`. -/
```

## Source Excerpt

```lean
theorem toRat_inv (q : TauRat) (h : q.is_nonzero) :
    (q.inv h).toRat = q.toRat⁻¹ := by
  have h_num_ne : (q.num.toInt : Rat) ≠ 0 := by
    intro hcontra
    apply h
    exact_mod_cast hcontra
  have h_den_ne : (q.den : Rat) ≠ 0 := q.den_ne_zero_rat
  -- Route natAbs through the Int-level `|·|` via `Nat.cast_natAbs`
  -- (which gives `(n.natAbs : α) = ((|n| : Int) : α)`), then resolve
  -- `|q.num.toInt|` by sign case at the Int level.
  by_cases hpos : 0 < q.num.toInt
  · -- Positive branch
    have h_abs_int : |q.num.toInt| = q.num.toInt := abs_of_pos hpos
    have h_natAbs_rat : ((q.num.toInt.natAbs : Nat) : Rat) = (q.num.toInt : Rat) := by
      rw [Nat.cast_natAbs, h_abs_int]
    have hLHS : (q.inv h).toRat =
                ((q.den : Int) : Rat) / ((q.num.toInt.natAbs : Nat) : Rat) := by
      show (((if 0 < q.num.toInt then (⟨q.den, 0⟩ : TauInt)
              else ⟨0, q.den⟩).toInt : Int) : Rat)
             / ((q.num.toInt.natAbs : Nat) : Rat) = _
      rw [if_pos hpos, TauRat.inv_num_toInt_pos]
    rw [hLHS, h_natAbs_rat, TauRat.toRat, inv_div]
    push_cast; ring
  · -- Nonpositive (hence negative by nonzero) branch
    push_neg at hpos
    have hneg : q.num.toInt < 0 := lt_of_le_of_ne hpos h
    have h_abs_int : |q.num.toInt| = -q.num.toInt := abs_of_neg hneg
    have h_natAbs_rat : ((q.num.toInt.natAbs : Nat) : Rat) = -(q.num.toInt : Rat) := by
      rw [Nat.cast_natAbs, h_abs_int]
      push_cast; ring
    have hLHS : (q.inv h).toRat =
                (-(q.den : Int) : Rat) / ((q.num.toInt.natAbs : Nat) : Rat) := by
      show (((if 0 < q.num.toInt then (⟨q.den, 0⟩ : TauInt)
              else ⟨0, q.den⟩).toInt : Int) : Rat)
             / ((q.num.toInt.natAbs : Nat) : Rat) = _
      rw [if_neg (not_lt.mpr hpos), TauRat.inv_num_toInt_neg]
      push_cast; ring
    rw [hLHS, h_natAbs_rat, TauRat.toRat, inv_div]
    push_cast; ring
```
