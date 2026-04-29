---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRatQ.inv",
  "permalink": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/inv-l243/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Bridge.TauRatQuotient`.",
  "declaration_id": "TauLib.BookI.Boundary.Bridge.TauRatQuotient::TauRatQ.inv",
  "declaration_slug": "inv-l243",
  "kind": "def",
  "name": "TauRatQ.inv",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauRatQuotient",
  "module_url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/",
  "source_line_start": 243,
  "source_line_end": 369,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L243-L369",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L243-L369",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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
- Source path: [`TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L243-L369)
- Source range: L243-L369
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
def TauRatQ.inv : TauRatQ → TauRatQ :=
  Quotient.lift (fun a => a.inv.toQ)
    (fun a b h => Quotient.sound (TauRat.inv_respects_equiv a b h))

@[simp] theorem TauRatQ.inv_mk (a : TauRat) :
    TauRatQ.inv a.toQ = a.inv.toQ := rfl

@[simp] theorem TauRatQ.toRat_inv (x : TauRatQ) :
    (TauRatQ.inv x).toRat = x.toRat⁻¹ := by
  refine Quotient.inductionOn x (fun a => ?_)
  show a.inv.toRat = (a.toRat)⁻¹
  exact Tau.Boundary.toRat_inv a

-- ============================================================
-- PART 6: Bare typeclass instances (for nsmulRec / zsmulRec)
-- ============================================================

instance : Zero TauRatQ := ⟨TauRatQ.zero⟩
instance : One TauRatQ := ⟨TauRatQ.one⟩
instance : Add TauRatQ := ⟨TauRatQ.add⟩
instance : Mul TauRatQ := ⟨TauRatQ.mul⟩
instance : Neg TauRatQ := ⟨TauRatQ.neg⟩
instance : Inv TauRatQ := ⟨TauRatQ.inv⟩

-- ============================================================
-- PART 7: Field instance on TauRatQ (KEYSTONE)
-- ============================================================

/-- **Wave 40 KEYSTONE: Field instance on TauRatQ**.

    Every field axiom is proven by pulling back through `toRat` to ℚ
    where Mathlib's `field_simp` / `ring` tactics discharge.

    This makes TauRatQ a first-class citizen of Mathlib's field
    ecosystem — Galois theory, finite extensions of ℚ, classical
    algebraic number theory at the field level all unlock. -/
instance : Field TauRatQ where
  add := TauRatQ.add
  mul := TauRatQ.mul
  neg := TauRatQ.neg
  zero := TauRatQ.zero
  one := TauRatQ.one
  inv := TauRatQ.inv
  add_assoc x y z := by
    apply TauRatQ.lift_via_toRat
    change TauRatQ.toRat (TauRatQ.add (TauRatQ.add x y) z) =
           TauRatQ.toRat (TauRatQ.add x (TauRatQ.add y z))
    simp only [TauRatQ.toRat_add]; ring
  zero_add x := by
    apply TauRatQ.lift_via_toRat
    change TauRatQ.toRat (TauRatQ.add TauRatQ.zero x) = TauRatQ.toRat x
    simp only [TauRatQ.toRat_add, TauRatQ.toRat_zero]; ring
  add_zero x := by
    apply TauRatQ.lift_via_toRat
    change TauRatQ.toRat (TauRatQ.add x TauRatQ.zero) = TauRatQ.toRat x
    simp only [TauRatQ.toRat_add, TauRatQ.toRat_zero]; ring
  add_comm x y := by
    apply TauRatQ.lift_via_toRat
    change TauRatQ.toRat (TauRatQ.add x y) = TauRatQ.toRat (TauRatQ.add y x)
    simp only [TauRatQ.toRat_add]; ring
  mul_assoc x y z := by
    apply TauRatQ.lift_via_toRat
    change TauRatQ.toRat (TauRatQ.mul (TauRatQ.mul x y) z) =
           TauRatQ.toRat (TauRatQ.mul x (TauRatQ.mul y z))
    simp only [TauRatQ.toRat_mul]; ring
  one_mul x := by
    apply TauRatQ.lift_via_toRat
    change TauRatQ.toRat (TauRatQ.mul TauRatQ.one x) = TauRatQ.toRat x
    simp only [TauRatQ.toRat_mul, TauRatQ.toRat_one]; ring
  mul_one x := by
    apply TauRatQ.lift_via_toRat
    change TauRatQ.toRat (TauRatQ.mul x TauRatQ.one) = TauRatQ.toRat x
    simp only [TauRatQ.toRat_mul, TauRatQ.toRat_one]; ring
  left_distrib x y z := by
    apply TauRatQ.lift_via_toRat
    change TauRatQ.toRat (TauRatQ.mul x (TauRatQ.add y z)) =
           TauRatQ.toRat (TauRatQ.add (TauRatQ.mul x y) (TauRatQ.mul x z))
    simp only [TauRatQ.toRat_mul, TauRatQ.toRat_add]; ring
  right_distrib x y z := by
    apply TauRatQ.lift_via_toRat
    change TauRatQ.toRat (TauRatQ.mul (TauRatQ.add x y) z) =
           TauRatQ.toRat (TauRatQ.add (TauRatQ.mul x z) (TauRatQ.mul y z))
    simp only [TauRatQ.toRat_mul, TauRatQ.toRat_add]; ring
  zero_mul x := by
    apply TauRatQ.lift_via_toRat
    change TauRatQ.toRat (TauRatQ.mul TauRatQ.zero x) = TauRatQ.toRat TauRatQ.zero
    simp only [TauRatQ.toRat_mul, TauRatQ.toRat_zero]; ring
  mul_zero x := by
    apply TauRatQ.lift_via_toRat
    change TauRatQ.toRat (TauRatQ.mul x TauRatQ.zero) = TauRatQ.toRat TauRatQ.zero
    simp only [TauRatQ.toRat_mul, TauRatQ.toRat_zero]; ring
  mul_comm x y := by
    apply TauRatQ.lift_via_toRat
    change TauRatQ.toRat (TauRatQ.mul x y) = TauRatQ.toRat (TauRatQ.mul y x)
    simp only [TauRatQ.toRat_mul]; ring
  neg_add_cancel x := by
    apply TauRatQ.lift_via_toRat
    change TauRatQ.toRat (TauRatQ.add (TauRatQ.neg x) x) = TauRatQ.toRat TauRatQ.zero
    refine Quotient.inductionOn x (fun a => ?_)
    show ((a.negate.add a).toRat = TauRat.zero.toRat)
    rw [toRat_add, toRat_negate, Tau.Boundary.toRat_zero]
    ring
  exists_pair_ne := ⟨TauRatQ.zero, TauRatQ.one, by
    intro h
    have : TauRatQ.zero.toRat = TauRatQ.one.toRat :=
      congrArg TauRatQ.toRat h
    simp [TauRatQ.toRat_zero, TauRatQ.toRat_one] at this⟩
  mul_inv_cancel x hx := by
    apply TauRatQ.lift_via_toRat
    change TauRatQ.toRat (TauRatQ.mul x (TauRatQ.inv x)) = TauRatQ.toRat TauRatQ.one
    have hx_rat : x.toRat ≠ 0 := by
      intro h
      apply hx
      show x = (0 : TauRatQ)
      apply TauRatQ.lift_via_toRat
      show x.toRat = TauRatQ.zero.toRat
      rw [h, TauRatQ.toRat_zero]
    simp only [TauRatQ.toRat_mul, TauRatQ.toRat_inv, TauRatQ.toRat_one]
    field_simp
  inv_zero := by
    apply TauRatQ.lift_via_toRat
    change TauRatQ.toRat (TauRatQ.inv TauRatQ.zero) = TauRatQ.toRat TauRatQ.zero
    simp only [TauRatQ.toRat_inv, TauRatQ.toRat_zero, inv_zero]
  nsmul := nsmulRec
  zsmul := zsmulRec
  nnqsmul := _
  qsmul := _
```
