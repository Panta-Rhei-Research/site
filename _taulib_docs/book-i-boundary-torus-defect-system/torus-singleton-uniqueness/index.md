---
{
  "projection_kind": "taulib_declaration",
  "title": "torusSingletonUniqueness",
  "permalink": "/verify/taulib/docs/book-i-boundary-torus-defect-system/torus-singleton-uniqueness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TorusDefectSystem`.",
  "declaration_id": "TauLib.BookI.Boundary.TorusDefectSystem::torusSingletonUniqueness",
  "declaration_slug": "torus-singleton-uniqueness",
  "kind": "theorem",
  "name": "torusSingletonUniqueness",
  "module_name": "TauLib.BookI.Boundary.TorusDefectSystem",
  "module_url": "/verify/taulib/docs/book-i-boundary-torus-defect-system/",
  "source_line_start": 283,
  "source_line_end": 289,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L283-L289",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TorusDefectSystem",
        "url": "/verify/taulib/docs/book-i-boundary-torus-defect-system/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L283-L289",
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

- Module: [TauLib.BookI.Boundary.TorusDefectSystem](/verify/taulib/docs/book-i-boundary-torus-defect-system/)
- Source path: [`TauLib/BookI/Boundary/TorusDefectSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L283-L289)
- Source range: L283-L289
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Singleton uniqueness, the Wave 13 hypothesis discharged
    unconditionally.**

    On `TorusDefectSystem`, any two crossing-point threads are
    equal — because σ-fixedness alone (without the crossing-point
    condition) already forces equality with `crossingThread`. -/
```

## Source Excerpt

```lean
theorem torusSingletonUniqueness
    (t₁ t₂ : DefectInverseSystem.SigmaFixedThread TorusDefectSystem)
    (_h₁ : DefectInverseSystem.IsCrossingPoint torusAnchor torusMwd t₁)
    (_h₂ : DefectInverseSystem.IsCrossingPoint torusAnchor torusMwd t₂) :
    t₁ = t₂ := by
  rw [TorusDefectSystem.sigma_fixed_thread_is_crossing t₁,
      TorusDefectSystem.sigma_fixed_thread_is_crossing t₂]
```
