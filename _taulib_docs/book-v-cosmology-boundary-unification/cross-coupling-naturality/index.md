---
{
  "projection_kind": "taulib_declaration",
  "title": "CrossCouplingNaturality",
  "permalink": "/verify/taulib/docs/book-v-cosmology-boundary-unification/cross-coupling-naturality/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BoundaryUnification`.",
  "declaration_id": "TauLib.BookV.Cosmology.BoundaryUnification::CrossCouplingNaturality",
  "declaration_slug": "cross-coupling-naturality",
  "kind": "structure",
  "name": "CrossCouplingNaturality",
  "module_name": "TauLib.BookV.Cosmology.BoundaryUnification",
  "module_url": "/verify/taulib/docs/book-v-cosmology-boundary-unification/",
  "source_line_start": 144,
  "source_line_end": 155,
  "registry_ids": [
    "V.P103"
  ],
  "related_registry_items": [
    {
      "id": "V.P103",
      "title": "Cross-coupling as naturality",
      "url": "/registry/object/V.P103/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BoundaryUnification.lean#L144-L155",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BoundaryUnification",
        "url": "/verify/taulib/docs/book-v-cosmology-boundary-unification/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BoundaryUnification.lean#L144-L155",
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

- Module: [TauLib.BookV.Cosmology.BoundaryUnification](/verify/taulib/docs/book-v-cosmology-boundary-unification/)
- Source path: [`TauLib/BookV/Cosmology/BoundaryUnification.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BoundaryUnification.lean#L144-L155)
- Source range: L144-L155
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P103` — Cross-coupling as naturality

## Immediate Comment / Docstring

```lean
/-- [V.P103] Cross-coupling as naturality: for each sector pair (X,Y),
    κ(X,Y) is the leading spectral weight of a natural transformation
    η_{X,Y} between the sector functors.

    Naturality (functorial coherence) replaces gauge invariance as the
    organizing principle for inter-sector relations. -/
```

## Source Excerpt

```lean
structure CrossCouplingNaturality where
  /-- The sector pair. -/
  pair : SectorPair
  /-- Coupling numerator. -/
  coupling_numer : Nat
  /-- Coupling denominator. -/
  coupling_denom : Nat
  /-- Denominator positive. -/
  denom_pos : coupling_denom > 0
  /-- Whether the coupling arises from a natural transformation. -/
  from_naturality : Bool := true
  deriving Repr
```
