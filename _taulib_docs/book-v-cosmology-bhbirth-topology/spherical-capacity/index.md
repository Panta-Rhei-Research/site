---
{
  "projection_kind": "taulib_declaration",
  "title": "SphericalCapacity",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bhbirth-topology/spherical-capacity/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BHBirthTopology`.",
  "declaration_id": "TauLib.BookV.Cosmology.BHBirthTopology::SphericalCapacity",
  "declaration_slug": "spherical-capacity",
  "kind": "structure",
  "name": "SphericalCapacity",
  "module_name": "TauLib.BookV.Cosmology.BHBirthTopology",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bhbirth-topology/",
  "source_line_start": 88,
  "source_line_end": 99,
  "registry_ids": [
    "V.D164"
  ],
  "related_registry_items": [
    {
      "id": "V.D164",
      "title": "Spherical Capacity",
      "url": "/registry/object/V.D164/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L88-L99",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L88-L99",
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
- Source path: [`TauLib/BookV/Cosmology/BHBirthTopology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L88-L99)
- Source range: L88-L99
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D164` — Spherical Capacity

## Immediate Comment / Docstring

```lean
/-- [V.D164] Spherical capacity C_sph(n): the supremum of gravitational
    tension over all S²-topology configurations at base point α_n.

    When tension exceeds capacity, the S² branch is no longer
    energetically preferred and the topology crosses to T². -/
```

## Source Excerpt

```lean
structure SphericalCapacity where
  /-- Capacity numerator (scaled). -/
  capacity_numer : Nat
  /-- Capacity denominator. -/
  capacity_denom : Nat
  /-- Denominator positive. -/
  denom_pos : capacity_denom > 0
  /-- Refinement depth. -/
  depth : Nat
  /-- Depth positive. -/
  depth_pos : depth > 0
  deriving Repr
```
