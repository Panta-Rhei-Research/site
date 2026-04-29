---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRealQ.from_equiv",
  "permalink": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/from-equiv/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Bridge.TauRealQuotient`.",
  "declaration_id": "TauLib.BookI.Boundary.Bridge.TauRealQuotient::TauRealQ.from_equiv",
  "declaration_slug": "from-equiv",
  "kind": "theorem",
  "name": "TauRealQ.from_equiv",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauRealQuotient",
  "module_url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/",
  "source_line_start": 200,
  "source_line_end": 297,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealQuotient.lean#L200-L297",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Bridge.TauRealQuotient",
        "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealQuotient.lean#L200-L297",
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

- Module: [TauLib.BookI.Boundary.Bridge.TauRealQuotient](/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/)
- Source path: [`TauLib/BookI/Boundary/Bridge/TauRealQuotient.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealQuotient.lean#L200-L297)
- Source range: L200-L297
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Helper: lift an equality of equivalence classes via `Quotient.sound`
    using a TauReal-level `equiv` proof on representatives. -/
```

## Source Excerpt

```lean
private theorem TauRealQ.from_equiv {a b : CauchyTauReal}
    (h : CauchyTauReal.equiv a b) : a.toQ = b.toQ :=
  Quotient.sound h

/-- **Wave 41b KEYSTONE: CommRing instance on TauRealQ**.

    Every ring axiom is proven by `Quotient.inductionOn` on the
    Cauchy reps, then invoking the existing equiv-level ring axioms
    on `TauReal` (`taureal_add_comm`, `taureal_add_assoc`,
    `taureal_mul_comm`, etc.).

    Multiplication is well-defined on the quotient because we
    quotiented the *Cauchy subtype* (Wave 41a `IsCauchy_mul` +
    `mul_respects_equiv_under_cauchy`). -/
instance : CommRing TauRealQ where
  add := TauRealQ.add
  mul := TauRealQ.mul
  neg := TauRealQ.neg
  zero := TauRealQ.zero
  one := TauRealQ.one
  add_assoc x y z := by
    refine Quotient.inductionOn₃ x y z (fun a b c => ?_)
    show ((a.add b).add c).toQ = (a.add (b.add c)).toQ
    apply TauRealQ.from_equiv
    exact taureal_add_assoc a.val b.val c.val
  zero_add x := by
    refine Quotient.inductionOn x (fun a => ?_)
    show (CauchyTauReal.zero.add a).toQ = a.toQ
    apply TauRealQ.from_equiv
    show TauReal.equiv (TauReal.zero.add a.val) a.val
    exact taureal_zero_add a.val
  add_zero x := by
    refine Quotient.inductionOn x (fun a => ?_)
    show (a.add CauchyTauReal.zero).toQ = a.toQ
    apply TauRealQ.from_equiv
    show TauReal.equiv (a.val.add TauReal.zero) a.val
    exact taureal_add_zero a.val
  add_comm x y := by
    refine Quotient.inductionOn₂ x y (fun a b => ?_)
    show (a.add b).toQ = (b.add a).toQ
    apply TauRealQ.from_equiv
    exact taureal_add_comm a.val b.val
  mul_assoc x y z := by
    refine Quotient.inductionOn₃ x y z (fun a b c => ?_)
    show ((a.mul b).mul c).toQ = (a.mul (b.mul c)).toQ
    apply TauRealQ.from_equiv
    exact taureal_mul_assoc a.val b.val c.val
  one_mul x := by
    refine Quotient.inductionOn x (fun a => ?_)
    show (CauchyTauReal.one.mul a).toQ = a.toQ
    apply TauRealQ.from_equiv
    show TauReal.equiv (TauReal.one.mul a.val) a.val
    exact taureal_one_mul a.val
  mul_one x := by
    refine Quotient.inductionOn x (fun a => ?_)
    show (a.mul CauchyTauReal.one).toQ = a.toQ
    apply TauRealQ.from_equiv
    show TauReal.equiv (a.val.mul TauReal.one) a.val
    exact taureal_mul_one a.val
  left_distrib x y z := by
    refine Quotient.inductionOn₃ x y z (fun a b c => ?_)
    show (a.mul (b.add c)).toQ = ((a.mul b).add (a.mul c)).toQ
    apply TauRealQ.from_equiv
    exact taureal_left_distrib a.val b.val c.val
  right_distrib x y z := by
    refine Quotient.inductionOn₃ x y z (fun a b c => ?_)
    show ((a.add b).mul c).toQ = ((a.mul c).add (b.mul c)).toQ
    apply TauRealQ.from_equiv
    exact taureal_right_distrib a.val b.val c.val
  zero_mul x := by
    refine Quotient.inductionOn x (fun a => ?_)
    show (CauchyTauReal.zero.mul a).toQ = CauchyTauReal.zero.toQ
    apply TauRealQ.from_equiv
    show TauReal.equiv (TauReal.zero.mul a.val) TauReal.zero
    exact taureal_zero_mul a.val
  mul_zero x := by
    refine Quotient.inductionOn x (fun a => ?_)
    show (a.mul CauchyTauReal.zero).toQ = CauchyTauReal.zero.toQ
    apply TauRealQ.from_equiv
    -- a*0 ≡ 0 follows from mul_comm + zero_mul
    have h1 : TauReal.equiv (a.val.mul TauReal.zero) (TauReal.zero.mul a.val) :=
      taureal_mul_comm a.val TauReal.zero
    have h2 : TauReal.equiv (TauReal.zero.mul a.val) TauReal.zero :=
      taureal_zero_mul a.val
    exact TauReal.equiv_trans h1 h2
  mul_comm x y := by
    refine Quotient.inductionOn₂ x y (fun a b => ?_)
    show (a.mul b).toQ = (b.mul a).toQ
    apply TauRealQ.from_equiv
    exact taureal_mul_comm a.val b.val
  neg_add_cancel x := by
    refine Quotient.inductionOn x (fun a => ?_)
    show (a.neg.add a).toQ = CauchyTauReal.zero.toQ
    apply TauRealQ.from_equiv
    show TauReal.equiv (a.val.negate.add a.val) TauReal.zero
    exact taureal_negate_add a.val
  nsmul := nsmulRec
  zsmul := zsmulRec
```
