---
{
  "projection_kind": "taulib_declaration",
  "title": "CanonicalBHNeighborhood",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bhbirth-topology/canonical-bhneighborhood/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BHBirthTopology`.",
  "declaration_id": "TauLib.BookV.Cosmology.BHBirthTopology::CanonicalBHNeighborhood",
  "declaration_slug": "canonical-bhneighborhood",
  "kind": "structure",
  "name": "CanonicalBHNeighborhood",
  "module_name": "TauLib.BookV.Cosmology.BHBirthTopology",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bhbirth-topology/",
  "source_line_start": 217,
  "source_line_end": 226,
  "registry_ids": [
    "V.D167"
  ],
  "related_registry_items": [
    {
      "id": "V.D167",
      "title": "Canonical BH Neighborhood",
      "url": "/registry/object/V.D167/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L217-L226",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L217-L226",
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
- Source path: [`TauLib/BookV/Cosmology/BHBirthTopology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L217-L226)
- Source range: L217-L226
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D167` — Canonical BH Neighborhood

## Immediate Comment / Docstring

```lean
/-- [V.D167] Canonical BH neighborhood N_BH: the open subset of τ³
    consisting of all points (α_n, x) with n ≥ n_* and x in the
    linking boundary region of T².

    The neighborhood is the causal future of the birth event. -/
```

## Source Excerpt

```lean
structure CanonicalBHNeighborhood where
  /-- The BH event. -/
  event : BlackHoleTopologicalEvent
  /-- Outer radius (scaled). -/
  outer_radius_numer : Nat
  /-- Outer radius denominator. -/
  outer_radius_denom : Nat
  /-- Denominator positive. -/
  denom_pos : outer_radius_denom > 0
  deriving Repr
```
