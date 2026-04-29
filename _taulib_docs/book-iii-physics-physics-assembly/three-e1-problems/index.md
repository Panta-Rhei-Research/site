---
{
  "projection_kind": "taulib_declaration",
  "title": "three_e1_problems",
  "permalink": "/verify/taulib/docs/book-iii-physics-physics-assembly/three-e1-problems/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Physics.PhysicsAssembly`.",
  "declaration_id": "TauLib.BookIII.Physics.PhysicsAssembly::three_e1_problems",
  "declaration_slug": "three-e1-problems",
  "kind": "theorem",
  "name": "three_e1_problems",
  "module_name": "TauLib.BookIII.Physics.PhysicsAssembly",
  "module_url": "/verify/taulib/docs/book-iii-physics-physics-assembly/",
  "source_line_start": 153,
  "source_line_end": 157,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PhysicsAssembly.lean#L153-L157",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PhysicsAssembly.lean#L153-L157",
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
- Source path: [`TauLib/BookIII/Physics/PhysicsAssembly.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PhysicsAssembly.lean#L153-L157)
- Source range: L153-L157
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T29` — Physics Layer Assembly

## Immediate Comment / Docstring

```lean
/-- [III.T29] Structural: the three E₁ problems exhaust the E₁ level. -/
```

## Source Excerpt

```lean
theorem three_e1_problems :
    [problem_level .NS, problem_level .YM, problem_level .Hodge] =
    [EnrLevel.E1, EnrLevel.E1, EnrLevel.E1] := rfl

end Tau.BookIII.Physics
```
