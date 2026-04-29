---
{
  "projection_kind": "taulib_declaration",
  "title": "BoundaryDetermination",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/boundary-determination/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.HilbertSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.HilbertSpace::BoundaryDetermination",
  "declaration_slug": "boundary-determination",
  "kind": "structure",
  "name": "BoundaryDetermination",
  "module_name": "TauLib.BookIV.QuantumMechanics.HilbertSpace",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/",
  "source_line_start": 195,
  "source_line_end": 204,
  "registry_ids": [
    "IV.P19"
  ],
  "related_registry_items": [
    {
      "id": "IV.P19",
      "title": "Central Theorem Implies Boundary Determination",
      "url": "/registry/object/IV.P19/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L195-L204",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.HilbertSpace",
        "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L195-L204",
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

- Module: [TauLib.BookIV.QuantumMechanics.HilbertSpace](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/)
- Source path: [`TauLib/BookIV/QuantumMechanics/HilbertSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L195-L204)
- Source range: L195-L204
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P19` — Central Theorem Implies Boundary Determination

## Immediate Comment / Docstring

```lean
/-- [IV.P19] Central Theorem (II.T15) implies H_tau = L^2(L_hat, d_nu_spec):
    states on the interior tau^3 are completely determined by spectral data
    on the boundary L = S^1 v S^1.
    Formalized: both representations have the same structure. -/
```

## Source Excerpt

```lean
structure BoundaryDetermination where
  /-- Interior representation dimension (characters on T^2). -/
  interior_dim : Nat
  interior_eq : interior_dim = 2
  /-- Boundary representation dimension (spectral data on L). -/
  boundary_dim : Nat
  boundary_eq : boundary_dim = 2
  /-- They agree (isomorphism from Central Theorem). -/
  iso : interior_dim = boundary_dim
  deriving Repr
```
