---
{
  "projection_kind": "taulib_declaration",
  "title": "slippage_breaks_omega",
  "permalink": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/slippage-breaks-omega/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.MetaLogic.OnticInvariance`.",
  "declaration_id": "TauLib.BookI.MetaLogic.OnticInvariance::slippage_breaks_omega",
  "declaration_slug": "slippage-breaks-omega",
  "kind": "theorem",
  "name": "slippage_breaks_omega",
  "module_name": "TauLib.BookI.MetaLogic.OnticInvariance",
  "module_url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/",
  "source_line_start": 151,
  "source_line_end": 158,
  "registry_ids": [
    "I.T47"
  ],
  "related_registry_items": [
    {
      "id": "I.T47",
      "title": "Slippage Breaks Unique Omega",
      "url": "/registry/object/I.T47/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/OnticInvariance.lean#L151-L158",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.MetaLogic.OnticInvariance",
        "url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/OnticInvariance.lean#L151-L158",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.MetaLogic.OnticInvariance](/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/)
- Source path: [`TauLib/BookI/MetaLogic/OnticInvariance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/OnticInvariance.lean#L151-L158)
- Source range: L151-L158
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `I.T47` — Slippage Breaks Unique Omega

## Immediate Comment / Docstring

```lean
/-- [I.T47] Slippage Breaks Unique Omega: a foundation with full diagonal
    resonance cannot internalize a unique absolute infinity omega.

    If identity slippage is present (full resonance = true), then
    UniqueOmegaCapability is impossible for that resonance profile. -/
```

## Source Excerpt

```lean
theorem slippage_breaks_omega (dr : DiagonalResonance)
    (h : dr.isFullResonance = true) :
    ¬ ∃ (u : UniqueOmegaCapability), u.resonance = dr := by
  intro ⟨u, hu⟩
  have := u.no_resonance
  rw [hu] at this
  rw [this] at h
  exact absurd h (by simp)
```
