---
{
  "projection_kind": "taulib_declaration",
  "title": "BlackHoleTopologicalEvent",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bhbirth-topology/black-hole-topological-event/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BHBirthTopology`.",
  "declaration_id": "TauLib.BookV.Cosmology.BHBirthTopology::BlackHoleTopologicalEvent",
  "declaration_slug": "black-hole-topological-event",
  "kind": "structure",
  "name": "BlackHoleTopologicalEvent",
  "module_name": "TauLib.BookV.Cosmology.BHBirthTopology",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bhbirth-topology/",
  "source_line_start": 143,
  "source_line_end": 154,
  "registry_ids": [
    "V.D166"
  ],
  "related_registry_items": [
    {
      "id": "V.D166",
      "title": "Black Hole (Topological Event)",
      "url": "/registry/object/V.D166/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L143-L154",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BHBirthTopology",
        "url": "/verify/taulib/docs/book-v-cosmology-bhbirth-topology/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L143-L154",
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

- Module: [TauLib.BookV.Cosmology.BHBirthTopology](/verify/taulib/docs/book-v-cosmology-bhbirth-topology/)
- Source path: [`TauLib/BookV/Cosmology/BHBirthTopology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L143-L154)
- Source range: L143-L154
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D166` — Black Hole (Topological Event)

## Immediate Comment / Docstring

```lean
/-- [V.D166] Black hole (topological event): the emergence of a
    non-trivial linking class at a base point α_{n_*} where the
    gravitational tension exceeds the spherical capacity.

    A BH is NOT a region of infinite curvature. It is a topology
    crossing from S² to T² in the fiber at a specific base point. -/
```

## Source Excerpt

```lean
structure BlackHoleTopologicalEvent where
  /-- Birth depth. -/
  birth_depth : Nat
  /-- Birth depth positive. -/
  birth_pos : birth_depth > 0
  /-- The linking class. -/
  linking : LinkingClass
  /-- Horizon topology is T². -/
  topology : HorizonTopology := .T2
  /-- The crossing is smooth (no singularity). -/
  is_smooth : Bool := true
  deriving Repr
```
