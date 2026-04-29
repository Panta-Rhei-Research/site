---
{
  "projection_kind": "taulib_declaration",
  "title": "structural_instability_theorem",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-reception-criterion/structural-instability-theorem/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.MetaLogic.ReceptionCriterion`.",
  "declaration_id": "TauLib.BookI.MetaLogic.ReceptionCriterion::structural_instability_theorem",
  "declaration_slug": "structural-instability-theorem",
  "kind": "theorem",
  "name": "structural_instability_theorem",
  "module_name": "TauLib.BookI.MetaLogic.ReceptionCriterion",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-reception-criterion/",
  "source_line_start": 107,
  "source_line_end": 115,
  "registry_ids": [
    "I.T48"
  ],
  "related_registry_items": [
    {
      "id": "I.T48",
      "title": "Structural Instability Theorem",
      "url": "/registry/object/I.T48/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L107-L115",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.MetaLogic.ReceptionCriterion",
        "url": "/verify/taulib/docs/book-i-meta-logic-reception-criterion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L107-L115",
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

- Module: [TauLib.BookI.MetaLogic.ReceptionCriterion](/verify/taulib/docs/book-i-meta-logic-reception-criterion/)
- Source path: [`TauLib/BookI/MetaLogic/ReceptionCriterion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L107-L115)
- Source range: L107-L115
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.T48` — Structural Instability Theorem

## Immediate Comment / Docstring

```lean
/-- [I.T48] The Structural Instability Theorem: diagonal-resonant foundations
    cannot host identity-faithful reception of τ.

    If host has full resonance, reception conditions cannot be met. -/
```

## Source Excerpt

```lean
theorem structural_instability_theorem (dr : DiagonalResonance)
    (h : dr.isFullResonance = true) :
    ¬ ∃ (r : IdentityFaithfulReception), r.host_resonance = dr ∧ r.all_conditions_met = true := by
  intro ⟨r, hr, hc⟩
  have hblock := r.resonance_blocks
  rw [hr] at hblock
  have := hblock h
  rw [this] at hc
  exact absurd hc (by decide)
```
