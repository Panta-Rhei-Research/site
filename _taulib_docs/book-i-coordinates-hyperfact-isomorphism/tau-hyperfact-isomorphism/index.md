---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_hyperfact_isomorphism",
  "permalink": "/verify/taulib/docs/book-i-coordinates-hyperfact-isomorphism/tau-hyperfact-isomorphism/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.HyperfactIsomorphism`.",
  "declaration_id": "TauLib.BookI.Coordinates.HyperfactIsomorphism::tau_hyperfact_isomorphism",
  "declaration_slug": "tau-hyperfact-isomorphism",
  "kind": "theorem",
  "name": "tau_hyperfact_isomorphism",
  "module_name": "TauLib.BookI.Coordinates.HyperfactIsomorphism",
  "module_url": "/verify/taulib/docs/book-i-coordinates-hyperfact-isomorphism/",
  "source_line_start": 147,
  "source_line_end": 149,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactIsomorphism.lean#L147-L149",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.HyperfactIsomorphism",
        "url": "/verify/taulib/docs/book-i-coordinates-hyperfact-isomorphism/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactIsomorphism.lean#L147-L149",
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

- Module: [TauLib.BookI.Coordinates.HyperfactIsomorphism](/verify/taulib/docs/book-i-coordinates-hyperfact-isomorphism/)
- Source path: [`TauLib/BookI/Coordinates/HyperfactIsomorphism.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactIsomorphism.lean#L147-L149)
- Source range: L147-L149
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §7 Theorem 8.1 `thm:isomorphism-hyper`**: under the
    kernel identification `mathrm{idx} : Obj(τ) → ℕ_{≥1}`, the
    τ-framework ABCD chart agrees with the orthodox ABCD chart.

    In TauLib: since `TauIdx = Nat` (the kernel identification is
    *definitional* at the Lean level), the τ and orthodox charts
    are the *same function*.  This theorem states that fact
    explicitly — `abcd_chart x` projected to the four components
    *is* the tuple of `coord_A/B/C/D` evaluations.

    Per paper Remark on §7.1 (lines 938–964): the isomorphism is
    a *step-by-step* identity (largest prime, A-adic valuation,
    tetration tower, maximal height, quotient — every step
    preserves via `mathrm{idx}`).  In TauLib these are all single
    Lean definitions, so the isomorphism is `rfl`. -/
```

## Source Excerpt

```lean
theorem tau_hyperfact_isomorphism (x : TauIdx) :
    abcd_chart x = (coord_A x, coord_B x, coord_C x, coord_D x) := by
  rfl
```
