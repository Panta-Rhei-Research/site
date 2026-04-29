---
{
  "projection_kind": "taulib_declaration",
  "title": "structural_agrees_with_physics",
  "permalink": "/verify/taulib/docs/book-iv-sectors-boundary-filtration/structural-agrees-with-physics/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Sectors.BoundaryFiltration`.",
  "declaration_id": "TauLib.BookIV.Sectors.BoundaryFiltration::structural_agrees_with_physics",
  "declaration_slug": "structural-agrees-with-physics",
  "kind": "theorem",
  "name": "structural_agrees_with_physics",
  "module_name": "TauLib.BookIV.Sectors.BoundaryFiltration",
  "module_url": "/verify/taulib/docs/book-iv-sectors-boundary-filtration/",
  "source_line_start": 148,
  "source_line_end": 152,
  "registry_ids": [
    "IV.T130"
  ],
  "related_registry_items": [
    {
      "id": "IV.T130",
      "title": "Structural–Physics Census Equivalence",
      "url": "/registry/object/IV.T130/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/BoundaryFiltration.lean#L148-L152",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Sectors.BoundaryFiltration",
        "url": "/verify/taulib/docs/book-iv-sectors-boundary-filtration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/BoundaryFiltration.lean#L148-L152",
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

- Module: [TauLib.BookIV.Sectors.BoundaryFiltration](/verify/taulib/docs/book-iv-sectors-boundary-filtration/)
- Source path: [`TauLib/BookIV/Sectors/BoundaryFiltration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/BoundaryFiltration.lean#L148-L152)
- Source range: L148-L152
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T130` — Structural–Physics Census Equivalence

## Immediate Comment / Docstring

```lean
/-- [IV.T130] The structural census agrees with the physics-based census
    for ALL BoundaryMode values.

    This is the key theorem resolving OQ.11: the two rules
    (gravitational orthogonality + crossing polarity cancellation)
    reproduce the same census as Standard Model physics input. -/
```

## Source Excerpt

```lean
theorem structural_agrees_with_physics (m : BoundaryMode) :
    emActiveStructural m = m.emActive := by
  cases m with
  | mk g c =>
    cases g <;> cases c <;> rfl
```
