---
{
  "projection_kind": "taulib_declaration",
  "title": "cayley_metric_properties",
  "permalink": "/corpus/taulib/docs/book-i-addressability-hinge-integration/cayley-metric-properties/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Addressability.HingeIntegration`.",
  "declaration_id": "TauLib.BookI.Addressability.HingeIntegration::cayley_metric_properties",
  "declaration_slug": "cayley-metric-properties",
  "kind": "theorem",
  "name": "cayley_metric_properties",
  "module_name": "TauLib.BookI.Addressability.HingeIntegration",
  "module_url": "/corpus/taulib/docs/book-i-addressability-hinge-integration/",
  "source_line_start": 193,
  "source_line_end": 198,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/HingeIntegration.lean#L193-L198",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Addressability.HingeIntegration",
        "url": "/corpus/taulib/docs/book-i-addressability-hinge-integration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/HingeIntegration.lean#L193-L198",
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

- Module: [TauLib.BookI.Addressability.HingeIntegration](/corpus/taulib/docs/book-i-addressability-hinge-integration/)
- Source path: [`TauLib/BookI/Addressability/HingeIntegration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/HingeIntegration.lean#L193-L198)
- Source range: L193-L198
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper Theorem 4 (Cayley Word Metric) statement form**:
    CayleyDist is a metric (symmetry + triangle + zero-iff).  All
    three properties already shipped via Wave 5. -/
```

## Source Excerpt

```lean
theorem cayley_metric_properties (nf₁ nf₂ nf₃ : NormalForm) :
    -- Symmetry
    CayleyDist nf₁ nf₂ = CayleyDist nf₂ nf₁ ∧
    -- Triangle inequality
    CayleyDist nf₁ nf₃ ≤ CayleyDist nf₁ nf₂ + CayleyDist nf₂ nf₃ :=
  ⟨CayleyDist_symm nf₁ nf₂, CayleyDist_triangle nf₁ nf₂ nf₃⟩
```
