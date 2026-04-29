---
{
  "projection_kind": "taulib_declaration",
  "title": "SU2LIdentification",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-chirality2/su2-lidentification/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.WeakChirality2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakChirality2::SU2LIdentification",
  "declaration_slug": "su2-lidentification",
  "kind": "structure",
  "name": "SU2LIdentification",
  "module_name": "TauLib.BookIV.Electroweak.WeakChirality2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality2/",
  "source_line_start": 158,
  "source_line_end": 168,
  "registry_ids": [
    "IV.P55"
  ],
  "related_registry_items": [
    {
      "id": "IV.P55",
      "title": "SU(2)_L from Lemniscate Automorphisms",
      "url": "/registry/object/IV.P55/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L158-L168",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakChirality2",
        "url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L158-L168",
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

- Module: [TauLib.BookIV.Electroweak.WeakChirality2](/verify/taulib/docs/book-iv-electroweak-weak-chirality2/)
- Source path: [`TauLib/BookIV/Electroweak/WeakChirality2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L158-L168)
- Source range: L158-L168
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P55` — SU(2)_L from Lemniscate Automorphisms

## Immediate Comment / Docstring

```lean
/-- [IV.P55] SU(2)_L as the automorphism group of the A-sector
    left-handed doublet structure. The subscript L means "left":
    only left-handed fermions transform under SU(2)_L.

    Structural encoding: gauge_group_dim = 3 (dim of SU(2)),
    chirality = Left (only left-handed transforms). -/
```

## Source Excerpt

```lean
structure SU2LIdentification where
  /-- Gauge group dimension: dim SU(2) = 3. -/
  gauge_dim : Nat
  gauge_dim_eq : gauge_dim = 3
  /-- Number of generators = 3 (Pauli matrices). -/
  num_generators : Nat
  num_gen_eq : num_generators = 3
  /-- Only left-handed chirality. -/
  chirality : ChiralityType
  chirality_left : chirality = .Left
  deriving Repr
```
