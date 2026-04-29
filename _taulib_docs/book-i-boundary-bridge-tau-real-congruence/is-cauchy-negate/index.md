---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.IsCauchy_negate",
  "permalink": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/is-cauchy-negate/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Bridge.TauRealCongruence`.",
  "declaration_id": "TauLib.BookI.Boundary.Bridge.TauRealCongruence::TauReal.IsCauchy_negate",
  "declaration_slug": "is-cauchy-negate",
  "kind": "theorem",
  "name": "TauReal.IsCauchy_negate",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauRealCongruence",
  "module_url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-congruence/",
  "source_line_start": 183,
  "source_line_end": 197,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean#L183-L197",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean#L183-L197",
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
- Source path: [`TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealCongruence.lean#L183-L197)
- Source range: L183-L197
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Negation of Cauchy is Cauchy.** Same modulus. -/
```

## Source Excerpt

```lean
theorem TauReal.IsCauchy_negate (a : TauReal) (h : a.IsCauchy) :
    a.negate.IsCauchy := by
  obtain ⟨μ, hm⟩ := h
  refine ⟨μ, fun k m n hm_le hn_le => ?_⟩
  have h_step := hm k m n hm_le hn_le
  unfold TauRat.lt at h_step ⊢
  rw [TauRat.toRat_abs, toRat_sub] at h_step
  rw [TauRat.toRat_abs, toRat_sub]
  have h_lhs_eq :
      (a.negate.approx m).toRat - (a.negate.approx n).toRat
        = -((a.approx m).toRat - (a.approx n).toRat) := by
    show ((a.approx m).negate).toRat - ((a.approx n).negate).toRat = _
    rw [toRat_negate, toRat_negate]; ring
  rw [h_lhs_eq, abs_neg]
  exact h_step
```
