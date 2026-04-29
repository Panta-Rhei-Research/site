---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.negate_respects_equiv",
  "permalink": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/negate-respects-equiv/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Bridge.TauRealCongruence`.",
  "declaration_id": "TauLib.BookI.Boundary.Bridge.TauRealCongruence::TauReal.negate_respects_equiv",
  "declaration_slug": "negate-respects-equiv",
  "kind": "theorem",
  "name": "TauReal.negate_respects_equiv",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauRealCongruence",
  "module_url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/",
  "source_line_start": 127,
  "source_line_end": 143,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean#L127-L143",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean#L127-L143",
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
- Source path: [`TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean#L127-L143)
- Source range: L127-L143
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Negation respects Cauchy equivalence.**

    If `a₁ ≡ a₂` then `-a₁ ≡ -a₂`. Same modulus; `|-a₁ - (-a₂)| = |a₂ - a₁|
    = |a₁ - a₂|`. -/
```

## Source Excerpt

```lean
theorem TauReal.negate_respects_equiv
    (a₁ a₂ : TauReal) (h : TauReal.equiv a₁ a₂) :
    TauReal.equiv a₁.negate a₂.negate := by
  obtain ⟨μ, hm⟩ := h
  refine ⟨μ, fun k n hn => ?_⟩
  have h_step := hm k n hn
  unfold TauRat.lt at h_step ⊢
  rw [TauRat.toRat_abs, toRat_sub] at h_step
  rw [TauRat.toRat_abs, toRat_sub]
  -- Goal: |negate.approx n .toRat - negate.approx n .toRat| < 1/(k+1)
  have h_lhs_eq :
      (a₁.negate.approx n).toRat - (a₂.negate.approx n).toRat
        = -((a₁.approx n).toRat - (a₂.approx n).toRat) := by
    show ((a₁.approx n).negate).toRat - ((a₂.approx n).negate).toRat = _
    rw [toRat_negate, toRat_negate]; ring
  rw [h_lhs_eq, abs_neg]
  exact h_step
```
