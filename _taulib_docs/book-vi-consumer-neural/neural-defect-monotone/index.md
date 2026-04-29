---
{
  "projection_kind": "taulib_declaration",
  "title": "NeuralDefectMonotone",
  "permalink": "/verify/taulib/docs/book-vi-consumer-neural/neural-defect-monotone/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Consumer.Neural`.",
  "declaration_id": "TauLib.BookVI.Consumer.Neural::NeuralDefectMonotone",
  "declaration_slug": "neural-defect-monotone",
  "kind": "structure",
  "name": "NeuralDefectMonotone",
  "module_name": "TauLib.BookVI.Consumer.Neural",
  "module_url": "/verify/taulib/docs/book-vi-consumer-neural/",
  "source_line_start": 238,
  "source_line_end": 247,
  "registry_ids": [
    "VI.P23"
  ],
  "related_registry_items": [
    {
      "id": "VI.P23",
      "title": "Neural Defect Monotonicity",
      "url": "/registry/object/VI.P23/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L238-L247",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Consumer.Neural",
        "url": "/verify/taulib/docs/book-vi-consumer-neural/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L238-L247",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
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

- Module: [TauLib.BookVI.Consumer.Neural](/verify/taulib/docs/book-vi-consumer-neural/)
- Source path: [`TauLib/BookVI/Consumer/Neural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L238-L247)
- Source range: L238-L247
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.P23` — Neural Defect Monotonicity

## Immediate Comment / Docstring

```lean
/-- [VI.P23] Neural Defect Monotonicity.
    At each level i of the NeuralDefectTower, the defect functional
    Δᵢ(n) is monotonically non-decreasing in the refinement step n.
    This is a specialization of VI.D43 (AgingDefect: Δ(n) monotonically
    increasing) to the 4-level neural decomposition: the total neural
    defect Δ_neural(n) = Σᵢ Δᵢ(n) inherits monotonicity from each
    component, and each component inherits it from VI.D43 restricted
    to the neural subsystem.
    Scope: τ-effective. -/
```

## Source Excerpt

```lean
structure NeuralDefectMonotone where
  /-- Each level's defect is monotone non-decreasing. -/
  per_level_monotone : Bool := true
  /-- Total neural defect inherits monotonicity. -/
  total_monotone : Bool := true
  /-- Specializes VI.D43. -/
  specializes_d43 : Bool := true
  /-- Scope: τ-effective. -/
  scope : String := "tau-effective"
  deriving Repr
```
