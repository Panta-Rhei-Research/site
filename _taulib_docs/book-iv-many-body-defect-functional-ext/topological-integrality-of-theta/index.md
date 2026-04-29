---
{
  "projection_kind": "taulib_declaration",
  "title": "TopologicalIntegralityOfTheta",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/topological-integrality-of-theta/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt::TopologicalIntegralityOfTheta",
  "declaration_slug": "topological-integrality-of-theta",
  "kind": "structure",
  "name": "TopologicalIntegralityOfTheta",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/",
  "source_line_start": 66,
  "source_line_end": 73,
  "registry_ids": [
    "IV.P133"
  ],
  "related_registry_items": [
    {
      "id": "IV.P133",
      "title": "Topological integrality of theta",
      "url": "/registry/object/IV.P133/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L66-L73",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.DefectFunctionalExt",
        "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L66-L73",
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

- Module: [TauLib.BookIV.ManyBody.DefectFunctionalExt](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/)
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L66-L73)
- Source range: L66-L73
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P133` — Topological integrality of theta

## Immediate Comment / Docstring

```lean
/-- [IV.P133] The topological charge theta(d) of a defect configuration
    on T^2 is integer-valued (winding number in pi_1(T^2) = Z^2) and
    is a deformation invariant preserved under continuous deformations
    within the boundary Hilbert space H_partial[omega]. -/
```

## Source Excerpt

```lean
structure TopologicalIntegralityOfTheta where
  /-- Topological charge is integer-valued. -/
  integer_valued : Bool := true
  /-- Homotopy group: pi_1(T^2) = Z^2. -/
  homotopy_group : String := "pi_1(T^2) = Z^2"
  /-- Deformation invariant. -/
  deformation_invariant : Bool := true
  deriving Repr
```
