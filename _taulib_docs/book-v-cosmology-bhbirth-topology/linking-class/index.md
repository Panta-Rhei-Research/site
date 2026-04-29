---
{
  "projection_kind": "taulib_declaration",
  "title": "LinkingClass",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bhbirth-topology/linking-class/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BHBirthTopology`.",
  "declaration_id": "TauLib.BookV.Cosmology.BHBirthTopology::LinkingClass",
  "declaration_slug": "linking-class",
  "kind": "structure",
  "name": "LinkingClass",
  "module_name": "TauLib.BookV.Cosmology.BHBirthTopology",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bhbirth-topology/",
  "source_line_start": 110,
  "source_line_end": 117,
  "registry_ids": [
    "V.D165"
  ],
  "related_registry_items": [
    {
      "id": "V.D165",
      "title": "Linking Class",
      "url": "/registry/object/V.D165/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L110-L117",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L110-L117",
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
- Source path: [`TauLib/BookV/Cosmology/BHBirthTopology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBirthTopology.lean#L110-L117)
- Source range: L110-L117
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D165` — Linking Class

## Immediate Comment / Docstring

```lean
/-- [V.D165] Linking class: a non-contractible cycle ℓ ∈ H₁(T²; ℤ) = ℤ ⊕ ℤ
    that links the two generators of π₁(T²).

    A linking class ℓ = (a, b) is non-trivial when a ≠ 0 or b ≠ 0.
    It wraps both the γ-circle and the η-circle of T². -/
```

## Source Excerpt

```lean
structure LinkingClass where
  /-- First component (wrapping γ-circle). -/
  a : Int
  /-- Second component (wrapping η-circle). -/
  b : Int
  /-- Non-trivial: at least one component nonzero. -/
  nontrivial : a ≠ 0 ∨ b ≠ 0
  deriving Repr
```
