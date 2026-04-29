---
{
  "projection_kind": "taulib_declaration",
  "title": "physics_assembly_check",
  "permalink": "/verify/taulib/docs/book-iii-physics-physics-assembly/physics-assembly-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.PhysicsAssembly`.",
  "declaration_id": "TauLib.BookIII.Physics.PhysicsAssembly::physics_assembly_check",
  "declaration_slug": "physics-assembly-check",
  "kind": "def",
  "name": "physics_assembly_check",
  "module_name": "TauLib.BookIII.Physics.PhysicsAssembly",
  "module_url": "/verify/taulib/docs/book-iii-physics-physics-assembly/",
  "source_line_start": 60,
  "source_line_end": 63,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PhysicsAssembly.lean#L60-L63",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PhysicsAssembly.lean#L60-L63",
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
- Source path: [`TauLib/BookIII/Physics/PhysicsAssembly.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PhysicsAssembly.lean#L60-L63)
- Source range: L60-L63
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T29` — Physics Layer Assembly

## Immediate Comment / Docstring

```lean
/-- [III.T29] Physics assembly: all three E₁ components are satisfied
    simultaneously at each primorial level. -/
```

## Source Excerpt

```lean
def physics_assembly_check (bound db : TauIdx) : Bool :=
  ns_component_check bound db &&
  ym_component_check db &&
  hodge_component_check bound db
```
