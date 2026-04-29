---
{
  "projection_kind": "taulib_declaration",
  "title": "BoundaryCompleteness",
  "permalink": "/verify/taulib/docs/book-v-cosmology-boundary-unification/boundary-completeness/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BoundaryUnification`.",
  "declaration_id": "TauLib.BookV.Cosmology.BoundaryUnification::BoundaryCompleteness",
  "declaration_slug": "boundary-completeness",
  "kind": "structure",
  "name": "BoundaryCompleteness",
  "module_name": "TauLib.BookV.Cosmology.BoundaryUnification",
  "module_url": "/verify/taulib/docs/book-v-cosmology-boundary-unification/",
  "source_line_start": 119,
  "source_line_end": 128,
  "registry_ids": [
    "V.T120"
  ],
  "related_registry_items": [
    {
      "id": "V.T120",
      "title": "Boundary Completeness",
      "url": "/registry/object/V.T120/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BoundaryUnification.lean#L119-L128",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BoundaryUnification.lean#L119-L128",
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
- Source path: [`TauLib/BookV/Cosmology/BoundaryUnification.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BoundaryUnification.lean#L119-L128)
- Source range: L119-L128
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T120` — Boundary Completeness

## Immediate Comment / Docstring

```lean
/-- [V.T120] Boundary completeness theorem: all C(4,2) = 6 pairs
    of primitive sectors satisfy commuting Hartogs squares in H_∂[ω].

    Each pair has a well-defined cross-coupling κ(X,Y) that is a
    rational function of ι_τ. No pair is "missing" or "decoupled."

    This is the culminating theorem of Book V: the τ-framework
    provides a complete, self-consistent description of all
    inter-sector relations. -/
```

## Source Excerpt

```lean
structure BoundaryCompleteness where
  /-- Number of sector pairs with Hartogs squares. -/
  num_pairs : Nat
  /-- All 6 pairs present. -/
  all_six : num_pairs = 6
  /-- Whether all Hartogs squares commute. -/
  all_commute : Bool := true
  /-- Whether all cross-couplings are ι_τ-rational. -/
  all_iota_rational : Bool := true
  deriving Repr
```
