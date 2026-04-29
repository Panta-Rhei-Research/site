---
{
  "projection_kind": "taulib_declaration",
  "title": "numerical_coupling_at_depth",
  "permalink": "/verify/taulib/docs/book-i-boundary-numerical-projection/numerical-coupling-at-depth/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.NumericalProjection`.",
  "declaration_id": "TauLib.BookI.Boundary.NumericalProjection::numerical_coupling_at_depth",
  "declaration_slug": "numerical-coupling-at-depth",
  "kind": "theorem",
  "name": "numerical_coupling_at_depth",
  "module_name": "TauLib.BookI.Boundary.NumericalProjection",
  "module_url": "/verify/taulib/docs/book-i-boundary-numerical-projection/",
  "source_line_start": 163,
  "source_line_end": 182,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumericalProjection.lean#L163-L182",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.NumericalProjection",
        "url": "/verify/taulib/docs/book-i-boundary-numerical-projection/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumericalProjection.lean#L163-L182",
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

- Module: [TauLib.BookI.Boundary.NumericalProjection](/verify/taulib/docs/book-i-boundary-numerical-projection/)
- Source path: [`TauLib/BookI/Boundary/NumericalProjection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumericalProjection.lean#L163-L182)
- Source range: L163-L182
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **The numerical coupling identity at depth `N`**: at the
    rational level, `iota^(N) · (pi^(N) + e^(N)) = 2 + ε_N` where
    `ε_N` is the finite-stage correction from Wave 15.

    Combining this with Wave 15's `finiteStageEpsilon = 0` past
    Wave 4's modulus, the coupling identity holds **exactly** at
    sufficient depth — the strongest possible numerical statement.

    Note: at the toRat level, `(π+e).approx n .toRat ≠
    (π.approx n).toRat + (e.approx n).toRat` only if there's a
    structural definitional mismatch — but both unfold via
    `toRat_add`, so they agree.

    Concrete bridge: combining `iotaApproxAt` (Wave 15) and
    `numericalReadoutAtDepth`: -/
```

## Source Excerpt

```lean
theorem numerical_coupling_at_depth (N : TauIdx) :
    (iotaNumericalAt N) *
      ((piNumericalAt N) + (eNumericalAt N)) =
    2 + (finiteStageEpsilon N).toRat := by
  -- Unfold the numerical convenience names back to their
  -- iotaApproxAt / piApproxAt / eApproxAt forms (which are
  -- definitionally equal at the .toRat level).
  show (TauReal.iota_tau.approx N).toRat *
         ((TauReal.pi.approx N).toRat + (TauReal.e.approx N).toRat) =
       2 + (finiteStageEpsilon N).toRat
  -- LHS = (iota.approx N).toRat * ((pi.approx N).toRat + (e.approx N).toRat)
  --     = (iota.approx N * (pi.approx N + e.approx N)).toRat   [toRat_mul, toRat_add]
  --     = (finiteStageNormalisation_toRat: 2 + epsilon.toRat)
  -- Apply finiteStageNormalisation_toRat with rewriting
  rw [show (TauReal.iota_tau.approx N).toRat *
        ((TauReal.pi.approx N).toRat + (TauReal.e.approx N).toRat) =
      ((TauReal.iota_tau.approx N).mul
        ((TauReal.pi.approx N).add (TauReal.e.approx N))).toRat by
    rw [toRat_mul, toRat_add]]
  exact finiteStageNormalisation_toRat N
```
