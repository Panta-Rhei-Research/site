---
{
  "projection_kind": "taulib_declaration",
  "title": "DomainWallEnergy",
  "permalink": "/verify/taulib/docs/book-iv-many-body-magnetism/domain-wall-energy/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.Magnetism`.",
  "declaration_id": "TauLib.BookIV.ManyBody.Magnetism::DomainWallEnergy",
  "declaration_slug": "domain-wall-energy",
  "kind": "structure",
  "name": "DomainWallEnergy",
  "module_name": "TauLib.BookIV.ManyBody.Magnetism",
  "module_url": "/verify/taulib/docs/book-iv-many-body-magnetism/",
  "source_line_start": 183,
  "source_line_end": 192,
  "registry_ids": [
    "IV.P227"
  ],
  "related_registry_items": [
    {
      "id": "IV.P227",
      "title": "Domain Wall Energy from T² Winding",
      "url": "/registry/object/IV.P227/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/Magnetism.lean#L183-L192",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.Magnetism",
        "url": "/verify/taulib/docs/book-iv-many-body-magnetism/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/Magnetism.lean#L183-L192",
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

- Module: [TauLib.BookIV.ManyBody.Magnetism](/verify/taulib/docs/book-iv-many-body-magnetism/)
- Source path: [`TauLib/BookIV/ManyBody/Magnetism.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/Magnetism.lean#L183-L192)
- Source range: L183-L192
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P227` — Domain Wall Energy from T² Winding

## Immediate Comment / Docstring

```lean
/-- [IV.P227] Domain wall energy σ_wall = 4√(AK), where A = exchange
    stiffness, K = anisotropy constant. Width δ = π√(A/K).
    On T², non-contractible cycles impose global consistency:
    total winding change must be compatible with H₁(T²; ℤ) ≅ ℤ². -/
```

## Source Excerpt

```lean
structure DomainWallEnergy where
  /-- Energy from exchange × anisotropy. -/
  energy_formula : String := "σ_wall = 4√(AK)"
  /-- Width formula. -/
  width_formula : String := "δ = π√(A/K)"
  /-- T² global consistency constraint. -/
  torus_consistency : Bool := true
  /-- H₁(T²; ℤ) ≅ ℤ² constraint. -/
  first_homology : String := "ℤ²"
  deriving Repr
```
