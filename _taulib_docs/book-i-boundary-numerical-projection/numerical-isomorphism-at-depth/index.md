---
{
  "projection_kind": "taulib_declaration",
  "title": "numerical_isomorphism_at_depth",
  "permalink": "/verify/taulib/docs/book-i-boundary-numerical-projection/numerical-isomorphism-at-depth/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.NumericalProjection`.",
  "declaration_id": "TauLib.BookI.Boundary.NumericalProjection::numerical_isomorphism_at_depth",
  "declaration_slug": "numerical-isomorphism-at-depth",
  "kind": "theorem",
  "name": "numerical_isomorphism_at_depth",
  "module_name": "TauLib.BookI.Boundary.NumericalProjection",
  "module_url": "/verify/taulib/docs/book-i-boundary-numerical-projection/",
  "source_line_start": 222,
  "source_line_end": 229,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumericalProjection.lean#L222-L229",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumericalProjection.lean#L222-L229",
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
- Source path: [`TauLib/BookI/Boundary/NumericalProjection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumericalProjection.lean#L222-L229)
- Source range: L222-L229
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §7.3 Corollary 7.2 `cor:numerical-iso`**:
    `Read_F^orth(GerIota) = 2 / (π + e) ≈ 0.341304238875`.

    Structural form: at every depth `N` past Wave 4's modulus,
    the numerical readout of `ι_τ` equals `2 / (numerical readout
    of π + numerical readout of e)`, *exactly*.

    From `numerical_coupling_exact_when_epsilon_zero`: when
    `ε_N = 0`, dividing both sides of
    `ι_τ^(N) · (π_τ^(N) + e_τ^(N)) = 2` by `(π_τ^(N) +
    e_τ^(N))` yields the corollary, provided the denominator is
    nonzero (which holds past Wave 11's `boundedAwayFromZero`
    modulus). -/
```

## Source Excerpt

```lean
theorem numerical_isomorphism_at_depth (N : TauIdx)
    (h_eps : (finiteStageEpsilon N).toRat = 0)
    (h_denom : piNumericalAt N + eNumericalAt N ≠ 0) :
    iotaNumericalAt N = 2 / (piNumericalAt N + eNumericalAt N) := by
  have h_prod := numerical_coupling_exact_when_epsilon_zero N h_eps
  -- iota * (pi + e) = 2, divide both sides by (pi + e).
  field_simp at h_prod ⊢
  linarith
```
