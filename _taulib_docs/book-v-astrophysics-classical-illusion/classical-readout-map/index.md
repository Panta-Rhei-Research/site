---
{
  "projection_kind": "taulib_declaration",
  "title": "ClassicalReadoutMap",
  "permalink": "/corpus/taulib/docs/book-v-astrophysics-classical-illusion/classical-readout-map/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.ClassicalIllusion`.",
  "declaration_id": "TauLib.BookV.Astrophysics.ClassicalIllusion::ClassicalReadoutMap",
  "declaration_slug": "classical-readout-map",
  "kind": "structure",
  "name": "ClassicalReadoutMap",
  "module_name": "TauLib.BookV.Astrophysics.ClassicalIllusion",
  "module_url": "/corpus/taulib/docs/book-v-astrophysics-classical-illusion/",
  "source_line_start": 87,
  "source_line_end": 98,
  "registry_ids": [
    "V.D117"
  ],
  "related_registry_items": [
    {
      "id": "V.D117",
      "title": "Classical Validity Scale --- V.D50",
      "url": "/registry/object/V.D117/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/ClassicalIllusion.lean#L87-L98",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.ClassicalIllusion",
        "url": "/corpus/taulib/docs/book-v-astrophysics-classical-illusion/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/ClassicalIllusion.lean#L87-L98",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookV.Astrophysics.ClassicalIllusion](/corpus/taulib/docs/book-v-astrophysics-classical-illusion/)
- Source path: [`TauLib/BookV/Astrophysics/ClassicalIllusion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/ClassicalIllusion.lean#L87-L98)
- Source range: L87-L98
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `V.D117` — Classical Validity Scale --- V.D50

## Immediate Comment / Docstring

```lean
/-- [V.D117] Classical readout map: projects the τ³ arena onto
    a classical phase space by forgetting fiber modes and
    coarse-graining the refinement tower.

    The map is parameterized by a cutoff depth n_cl and a
    regime classification. -/
```

## Source Excerpt

```lean
structure ClassicalReadoutMap where
  /-- Cutoff depth in the refinement tower. -/
  cutoff_depth : Nat
  /-- Regime of the readout. -/
  regime : ReadoutRegime
  /-- Cutoff depth must be positive. -/
  depth_pos : cutoff_depth > 0
  /-- Number of spatial dimensions in the readout. -/
  spatial_dim : Nat := 3
  /-- Whether fiber modes are frozen (classical limit). -/
  fiber_frozen : Bool := true
  deriving Repr
```
