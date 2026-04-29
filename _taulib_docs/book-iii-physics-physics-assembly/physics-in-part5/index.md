---
{
  "projection_kind": "taulib_declaration",
  "title": "physics_in_part5",
  "permalink": "/verify/taulib/docs/book-iii-physics-physics-assembly/physics-in-part5/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.PhysicsAssembly`.",
  "declaration_id": "TauLib.BookIII.Physics.PhysicsAssembly::physics_in_part5",
  "declaration_slug": "physics-in-part5",
  "kind": "def",
  "name": "physics_in_part5",
  "module_name": "TauLib.BookIII.Physics.PhysicsAssembly",
  "module_url": "/verify/taulib/docs/book-iii-physics-physics-assembly/",
  "source_line_start": 92,
  "source_line_end": 95,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PhysicsAssembly.lean#L92-L95",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PhysicsAssembly.lean#L92-L95",
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
- Source path: [`TauLib/BookIII/Physics/PhysicsAssembly.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PhysicsAssembly.lean#L92-L95)
- Source range: L92-L95
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T29` — Physics Layer Assembly

## Immediate Comment / Docstring

```lean
/-- [III.T29] Part assignment: all three problems are in Part V. -/
```

## Source Excerpt

```lean
def physics_in_part5 : Bool :=
  problem_part .NS == 5 &&
  problem_part .YM == 5 &&
  problem_part .Hodge == 5
```
