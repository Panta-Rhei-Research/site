---
{
  "projection_kind": "taulib_declaration",
  "title": "ns_component_check",
  "permalink": "/verify/taulib/docs/book-iii-physics-physics-assembly/ns-component-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.PhysicsAssembly`.",
  "declaration_id": "TauLib.BookIII.Physics.PhysicsAssembly::ns_component_check",
  "declaration_slug": "ns-component-check",
  "kind": "def",
  "name": "ns_component_check",
  "module_name": "TauLib.BookIII.Physics.PhysicsAssembly",
  "module_url": "/verify/taulib/docs/book-iii-physics-physics-assembly/",
  "source_line_start": 40,
  "source_line_end": 43,
  "registry_ids": [
    "III.T29"
  ],
  "related_registry_items": [
    {
      "id": "III.T29",
      "title": "Physics Layer Assembly",
      "url": "/registry/object/III.T29/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PhysicsAssembly.lean#L40-L43",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.PhysicsAssembly",
        "url": "/verify/taulib/docs/book-iii-physics-physics-assembly/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PhysicsAssembly.lean#L40-L43",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookIII.Physics.PhysicsAssembly](/verify/taulib/docs/book-iii-physics-physics-assembly/)
- Source path: [`TauLib/BookIII/Physics/PhysicsAssembly.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PhysicsAssembly.lean#L40-L43)
- Source range: L40-L43
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T29` — Physics Layer Assembly

## Immediate Comment / Docstring

```lean
/-- [III.T29] NS component: fluid data admissibility + flow stabilization +
    positive regularity. -/
```

## Source Excerpt

```lean
def ns_component_check (bound db : TauIdx) : Bool :=
  fluid_data_check db &&
  flow_stabilization_check bound db &&
  positive_regularity_check bound db
```
