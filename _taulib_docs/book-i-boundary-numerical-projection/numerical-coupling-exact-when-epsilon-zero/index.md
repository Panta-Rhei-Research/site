---
{
  "projection_kind": "taulib_declaration",
  "title": "numerical_coupling_exact_when_epsilon_zero",
  "permalink": "/verify/taulib/docs/book-i-boundary-numerical-projection/numerical-coupling-exact-when-epsilon-zero/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.NumericalProjection`.",
  "declaration_id": "TauLib.BookI.Boundary.NumericalProjection::numerical_coupling_exact_when_epsilon_zero",
  "declaration_slug": "numerical-coupling-exact-when-epsilon-zero",
  "kind": "theorem",
  "name": "numerical_coupling_exact_when_epsilon_zero",
  "module_name": "TauLib.BookI.Boundary.NumericalProjection",
  "module_url": "/verify/taulib/docs/book-i-boundary-numerical-projection/",
  "source_line_start": 199,
  "source_line_end": 203,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumericalProjection.lean#L199-L203",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumericalProjection.lean#L199-L203",
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
- Source path: [`TauLib/BookI/Boundary/NumericalProjection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumericalProjection.lean#L199-L203)
- Source range: L199-L203
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Numerical observation**: from Wave 15's `#eval` evidence,
    `finiteStageEpsilon` evaluates to `0` exactly at every
    `n ≥ N₀` where `N₀` is Wave 4's `boundedAwayFromZero`
    modulus.  This is the operational manifestation of
    `coupling_identity_at_omega` at finite depth.

    Combined with `numerical_coupling_at_depth`, this gives the
    cleanest possible numerical form: when `ε_N = 0`,

      `ι_τ^(N) · (π_τ^(N) + e_τ^(N)) = 2`   exactly.

    The exact-zero finite-stage normalisation is **stronger** than
    paper §6.2's qualitative `ε_n → 0` claim — a TauLib bonus
    arising from Wave 4's operational construction of `ι_τ` as
    `2 / (π + e)`. -/
```

## Source Excerpt

```lean
theorem numerical_coupling_exact_when_epsilon_zero (N : TauIdx)
    (h : (finiteStageEpsilon N).toRat = 0) :
    (iotaNumericalAt N) *
      ((piNumericalAt N) + (eNumericalAt N)) = 2 := by
  rw [numerical_coupling_at_depth, h]; ring
```
