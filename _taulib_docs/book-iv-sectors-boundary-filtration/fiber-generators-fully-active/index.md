---
{
  "projection_kind": "taulib_declaration",
  "title": "fiber_generators_fully_active",
  "permalink": "/verify/taulib/docs/book-iv-sectors-boundary-filtration/fiber-generators-fully-active/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Sectors.BoundaryFiltration`.",
  "declaration_id": "TauLib.BookIV.Sectors.BoundaryFiltration::fiber_generators_fully_active",
  "declaration_slug": "fiber-generators-fully-active",
  "kind": "theorem",
  "name": "fiber_generators_fully_active",
  "module_name": "TauLib.BookIV.Sectors.BoundaryFiltration",
  "module_url": "/verify/taulib/docs/book-iv-sectors-boundary-filtration/",
  "source_line_start": 188,
  "source_line_end": 198,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/BoundaryFiltration.lean#L188-L198",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/BoundaryFiltration.lean#L188-L198",
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
- Source path: [`TauLib/BookIV/Sectors/BoundaryFiltration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/BoundaryFiltration.lean#L188-L198)
- Source range: L188-L198
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- All fiber generators are fully active (all 3 configs). -/
```

## Source Excerpt

```lean
theorem fiber_generators_fully_active :
    emActiveStructural ⟨.gamma, .lobePos⟩ = true ∧
    emActiveStructural ⟨.gamma, .lobeNeg⟩ = true ∧
    emActiveStructural ⟨.gamma, .crossing⟩ = true ∧
    emActiveStructural ⟨.eta, .lobePos⟩ = true ∧
    emActiveStructural ⟨.eta, .lobeNeg⟩ = true ∧
    emActiveStructural ⟨.eta, .crossing⟩ = true ∧
    emActiveStructural ⟨.omega, .lobePos⟩ = true ∧
    emActiveStructural ⟨.omega, .lobeNeg⟩ = true ∧
    emActiveStructural ⟨.omega, .crossing⟩ = true := by
  exact ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩
```
