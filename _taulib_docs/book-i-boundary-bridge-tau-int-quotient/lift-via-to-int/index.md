---
{
  "projection_kind": "taulib_declaration",
  "title": "TauIntQ.lift_via_toInt",
  "permalink": "/verify/taulib/docs/book-i-boundary-bridge-tau-int-quotient/lift-via-to-int/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Bridge.TauIntQuotient`.",
  "declaration_id": "TauLib.BookI.Boundary.Bridge.TauIntQuotient::TauIntQ.lift_via_toInt",
  "declaration_slug": "lift-via-to-int",
  "kind": "theorem",
  "name": "TauIntQ.lift_via_toInt",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauIntQuotient",
  "module_url": "/verify/taulib/docs/book-i-boundary-bridge-tau-int-quotient/",
  "source_line_start": 189,
  "source_line_end": 273,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean#L189-L273",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Bridge.TauIntQuotient",
        "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-int-quotient/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean#L189-L273",
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

- Module: [TauLib.BookI.Boundary.Bridge.TauIntQuotient](/verify/taulib/docs/book-i-boundary-bridge-tau-int-quotient/)
- Source path: [`TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean#L189-L273)
- Source range: L189-L273
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Helper: convert a ring axiom on `TauIntQ` to a ring axiom on `Int`
    via the homomorphism `toInt`. -/
```

## Source Excerpt

```lean
private theorem TauIntQ.lift_via_toInt (x y : TauIntQ)
    (h : x.toInt = y.toInt) : x = y :=
  (TauIntQ.eq_iff_toInt_eq x y).mpr h

-- Bare typeclass instances so `nsmulRec` / `zsmulRec` can resolve
-- inside the `CommRing` instance below.
instance : Zero TauIntQ := ⟨TauIntQ.zero⟩
instance : One TauIntQ := ⟨TauIntQ.one⟩
instance : Add TauIntQ := ⟨TauIntQ.add⟩
instance : Mul TauIntQ := ⟨TauIntQ.mul⟩
instance : Neg TauIntQ := ⟨TauIntQ.neg⟩

/-- **Wave 39 KEYSTONE: CommRing instance on TauIntQ**.

    Every ring axiom is proven by:
    1. Lifting the obligation to `toInt` via the homomorphism theorems
    2. Reducing to a Mathlib `Int` ring identity
    3. Discharging via Mathlib's `ring` tactic.

    This makes TauIntQ a first-class citizen of Mathlib's algebraic
    ecosystem. -/
instance : CommRing TauIntQ where
  add := TauIntQ.add
  mul := TauIntQ.mul
  neg := TauIntQ.neg
  zero := TauIntQ.zero
  one := TauIntQ.one
  add_assoc x y z := by
    apply TauIntQ.lift_via_toInt
    change TauIntQ.toInt (TauIntQ.add (TauIntQ.add x y) z) =
           TauIntQ.toInt (TauIntQ.add x (TauIntQ.add y z))
    simp only [TauIntQ.toInt_add]; ring
  zero_add x := by
    apply TauIntQ.lift_via_toInt
    change TauIntQ.toInt (TauIntQ.add TauIntQ.zero x) = TauIntQ.toInt x
    simp only [TauIntQ.toInt_add, TauIntQ.toInt_zero]; ring
  add_zero x := by
    apply TauIntQ.lift_via_toInt
    change TauIntQ.toInt (TauIntQ.add x TauIntQ.zero) = TauIntQ.toInt x
    simp only [TauIntQ.toInt_add, TauIntQ.toInt_zero]; ring
  add_comm x y := by
    apply TauIntQ.lift_via_toInt
    change TauIntQ.toInt (TauIntQ.add x y) = TauIntQ.toInt (TauIntQ.add y x)
    simp only [TauIntQ.toInt_add]; ring
  mul_assoc x y z := by
    apply TauIntQ.lift_via_toInt
    change TauIntQ.toInt (TauIntQ.mul (TauIntQ.mul x y) z) =
           TauIntQ.toInt (TauIntQ.mul x (TauIntQ.mul y z))
    simp only [TauIntQ.toInt_mul]; ring
  one_mul x := by
    apply TauIntQ.lift_via_toInt
    change TauIntQ.toInt (TauIntQ.mul TauIntQ.one x) = TauIntQ.toInt x
    simp only [TauIntQ.toInt_mul, TauIntQ.toInt_one]; ring
  mul_one x := by
    apply TauIntQ.lift_via_toInt
    change TauIntQ.toInt (TauIntQ.mul x TauIntQ.one) = TauIntQ.toInt x
    simp only [TauIntQ.toInt_mul, TauIntQ.toInt_one]; ring
  left_distrib x y z := by
    apply TauIntQ.lift_via_toInt
    change TauIntQ.toInt (TauIntQ.mul x (TauIntQ.add y z)) =
           TauIntQ.toInt (TauIntQ.add (TauIntQ.mul x y) (TauIntQ.mul x z))
    simp only [TauIntQ.toInt_mul, TauIntQ.toInt_add]; ring
  right_distrib x y z := by
    apply TauIntQ.lift_via_toInt
    change TauIntQ.toInt (TauIntQ.mul (TauIntQ.add x y) z) =
           TauIntQ.toInt (TauIntQ.add (TauIntQ.mul x z) (TauIntQ.mul y z))
    simp only [TauIntQ.toInt_mul, TauIntQ.toInt_add]; ring
  zero_mul x := by
    apply TauIntQ.lift_via_toInt
    change TauIntQ.toInt (TauIntQ.mul TauIntQ.zero x) = TauIntQ.toInt TauIntQ.zero
    simp only [TauIntQ.toInt_mul, TauIntQ.toInt_zero]; ring
  mul_zero x := by
    apply TauIntQ.lift_via_toInt
    change TauIntQ.toInt (TauIntQ.mul x TauIntQ.zero) = TauIntQ.toInt TauIntQ.zero
    simp only [TauIntQ.toInt_mul, TauIntQ.toInt_zero]; ring
  mul_comm x y := by
    apply TauIntQ.lift_via_toInt
    change TauIntQ.toInt (TauIntQ.mul x y) = TauIntQ.toInt (TauIntQ.mul y x)
    simp only [TauIntQ.toInt_mul]; ring
  neg_add_cancel x := by
    apply TauIntQ.lift_via_toInt
    change TauIntQ.toInt (TauIntQ.add (TauIntQ.neg x) x) = TauIntQ.toInt TauIntQ.zero
    simp only [TauIntQ.toInt_add, TauIntQ.toInt_neg, TauIntQ.toInt_zero]; ring
  nsmul := nsmulRec
  zsmul := zsmulRec
```
