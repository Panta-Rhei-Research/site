---
{
  "projection_kind": "taulib_declaration",
  "title": "internal_identity_dimensionless",
  "permalink": "/verify/taulib/docs/book-iv-physics-internal-equations/internal-identity-dimensionless/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.InternalEquations`.",
  "declaration_id": "TauLib.BookIV.Physics.InternalEquations::internal_identity_dimensionless",
  "declaration_slug": "internal-identity-dimensionless",
  "kind": "theorem",
  "name": "internal_identity_dimensionless",
  "module_name": "TauLib.BookIV.Physics.InternalEquations",
  "module_url": "/verify/taulib/docs/book-iv-physics-internal-equations/",
  "source_line_start": 163,
  "source_line_end": 169,
  "registry_ids": [
    "IV.P176"
  ],
  "related_registry_items": [
    {
      "id": "IV.P176",
      "title": "Internal Equations Dimensionless",
      "url": "/registry/object/IV.P176/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/InternalEquations.lean#L163-L169",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.InternalEquations",
        "url": "/verify/taulib/docs/book-iv-physics-internal-equations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/InternalEquations.lean#L163-L169",
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

- Module: [TauLib.BookIV.Physics.InternalEquations](/verify/taulib/docs/book-iv-physics-internal-equations/)
- Source path: [`TauLib/BookIV/Physics/InternalEquations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/InternalEquations.lean#L163-L169)
- Source range: L163-L169
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P176` — Internal Equations Dimensionless

## Immediate Comment / Docstring

```lean
/-- [IV.P176] All internal physics identities are dimensionless
    (involve same-sector or sector-ratio morphisms, no SI dimensions). -/
```

## Source Excerpt

```lean
theorem internal_identity_dimensionless :
    mass_ratio_identity.is_dimensionless = true ∧
    alpha_identity.is_dimensionless = true ∧
    gravity_coupling_identity.is_dimensionless = true ∧
    temporal_complement_identity.is_dimensionless = true ∧
    confinement_identity.is_dimensionless = true := by
  exact ⟨rfl, rfl, rfl, rfl, rfl⟩
```
