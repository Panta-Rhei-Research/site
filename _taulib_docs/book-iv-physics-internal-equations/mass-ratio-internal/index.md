---
{
  "projection_kind": "taulib_declaration",
  "title": "mass_ratio_internal",
  "permalink": "/verify/taulib/docs/book-iv-physics-internal-equations/mass-ratio-internal/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.InternalEquations`.",
  "declaration_id": "TauLib.BookIV.Physics.InternalEquations::mass_ratio_internal",
  "declaration_slug": "mass-ratio-internal",
  "kind": "theorem",
  "name": "mass_ratio_internal",
  "module_name": "TauLib.BookIV.Physics.InternalEquations",
  "module_url": "/verify/taulib/docs/book-iv-physics-internal-equations/",
  "source_line_start": 173,
  "source_line_end": 174,
  "registry_ids": [
    "IV.T127"
  ],
  "related_registry_items": [
    {
      "id": "IV.T127",
      "title": "Mass Ratio as Internal Identity",
      "url": "/registry/object/IV.T127/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/InternalEquations.lean#L173-L174",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/InternalEquations.lean#L173-L174",
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
- Source path: [`TauLib/BookIV/Physics/InternalEquations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/InternalEquations.lean#L173-L174)
- Source range: L173-L174
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T127` — Mass Ratio as Internal Identity

## Immediate Comment / Docstring

```lean
/-- [IV.T127] The mass ratio identity lives at Layer 1 (internal physics),
    not Layer 0 (math) or Layer 2 (SI bridge). -/
```

## Source Excerpt

```lean
theorem mass_ratio_internal :
    mass_ratio_identity.layer = .InternalPhysics := rfl
```
