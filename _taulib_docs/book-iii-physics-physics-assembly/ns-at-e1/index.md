---
{
  "projection_kind": "taulib_declaration",
  "title": "ns_at_e1",
  "permalink": "/verify/taulib/docs/book-iii-physics-physics-assembly/ns-at-e1/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Physics.PhysicsAssembly`.",
  "declaration_id": "TauLib.BookIII.Physics.PhysicsAssembly::ns_at_e1",
  "declaration_slug": "ns-at-e1",
  "kind": "theorem",
  "name": "ns_at_e1",
  "module_name": "TauLib.BookIII.Physics.PhysicsAssembly",
  "module_url": "/verify/taulib/docs/book-iii-physics-physics-assembly/",
  "source_line_start": 139,
  "source_line_end": 139,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PhysicsAssembly.lean#L139-L139",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PhysicsAssembly.lean#L139-L139",
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

- Module: [TauLib.BookIII.Physics.PhysicsAssembly](/verify/taulib/docs/book-iii-physics-physics-assembly/)
- Source path: [`TauLib/BookIII/Physics/PhysicsAssembly.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PhysicsAssembly.lean#L139-L139)
- Source range: L139-L139
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T29` — Physics Layer Assembly

## Immediate Comment / Docstring

```lean
/-- [III.T29] Structural: NS is at E₁. -/
```

## Source Excerpt

```lean
theorem ns_at_e1 : problem_level .NS = .E1 := rfl
```
