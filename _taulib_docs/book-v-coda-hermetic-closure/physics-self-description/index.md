---
{
  "projection_kind": "taulib_declaration",
  "title": "PhysicsSelfDescription",
  "permalink": "/verify/taulib/docs/book-v-coda-hermetic-closure/physics-self-description/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Coda.HermeticClosure`.",
  "declaration_id": "TauLib.BookV.Coda.HermeticClosure::PhysicsSelfDescription",
  "declaration_slug": "physics-self-description",
  "kind": "structure",
  "name": "PhysicsSelfDescription",
  "module_name": "TauLib.BookV.Coda.HermeticClosure",
  "module_url": "/verify/taulib/docs/book-v-coda-hermetic-closure/",
  "source_line_start": 130,
  "source_line_end": 141,
  "registry_ids": [
    "V.T160"
  ],
  "related_registry_items": [
    {
      "id": "V.T160",
      "title": "Physics as self-description",
      "url": "/registry/object/V.T160/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L130-L141",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Coda.HermeticClosure",
        "url": "/verify/taulib/docs/book-v-coda-hermetic-closure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L130-L141",
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

- Module: [TauLib.BookV.Coda.HermeticClosure](/verify/taulib/docs/book-v-coda-hermetic-closure/)
- Source path: [`TauLib/BookV/Coda/HermeticClosure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L130-L141)
- Source range: L130-L141
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T160` — Physics as self-description

## Immediate Comment / Docstring

```lean
/-- [V.T160] Physics as self-description:
    H_∂[ω] = h_{τ³}|_L

    Every physical observable is a section of the Yoneda restriction
    to the boundary L = S¹ ∨ S¹. The τ³ fibration describes itself
    through its boundary characters. -/
```

## Source Excerpt

```lean
structure PhysicsSelfDescription where
  /-- Yoneda restriction holds. -/
  yoneda_restriction : Bool := true
  /-- Every observable is a boundary section. -/
  all_observables_boundary : Bool := true
  /-- Self-description is exact. -/
  self_description_exact : Bool := true
  /-- Boundary components (S¹ ∨ S¹ = 2 circles). -/
  boundary_components : Nat := 2
  /-- Total generators on boundary. -/
  total_generators : Nat := 5
  deriving Repr
```
