---
{
  "projection_kind": "taulib_declaration",
  "title": "j_closure_minimality",
  "permalink": "/verify/taulib/docs/book-vii-meta-archetypes/j-closure-minimality/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Meta.Archetypes`.",
  "declaration_id": "TauLib.BookVII.Meta.Archetypes::j_closure_minimality",
  "declaration_slug": "j-closure-minimality",
  "kind": "theorem",
  "name": "j_closure_minimality",
  "module_name": "TauLib.BookVII.Meta.Archetypes",
  "module_url": "/verify/taulib/docs/book-vii-meta-archetypes/",
  "source_line_start": 179,
  "source_line_end": 184,
  "registry_ids": [
    "VII.L08"
  ],
  "related_registry_items": [
    {
      "id": "VII.L08",
      "title": "j-Closure Minimality",
      "url": "/registry/object/VII.L08/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L179-L184",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Archetypes",
        "url": "/verify/taulib/docs/book-vii-meta-archetypes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L179-L184",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookVII.Meta.Archetypes](/verify/taulib/docs/book-vii-meta-archetypes/)
- Source path: [`TauLib/BookVII/Meta/Archetypes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L179-L184)
- Source range: L179-L184
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.L08` — j-Closure Minimality

## Immediate Comment / Docstring

```lean
/-- [VII.L08] j-Closure Minimality: let I be a structural invariant exhibited
    by at least one j-closed subobject of [τ^op, τ]. Then the collection F
    of all j-closed subobjects exhibiting I, ordered by inclusion, has a
    minimum element. This minimum is unique up to isomorphism.

    Proof:
    1. F is non-empty by hypothesis (has_exhibitor).
    2. F inherits complete lattice structure from Sub_j([τ^op, τ]).
    3. Take A = ⋂F (intersection of all members).
    4. A is j-closed: intersection of j-closed subobjects is j-closed
       (lattice_closure).
    5. A exhibits I: structural invariants defined by positive coherence
       conditions are preserved under intersection (positive_coherence).
    6. A is minimal: A ⊆ F_i for all i by construction.
    7. A is unique: if both A, A' minimal, then A ⊆ A' and A' ⊆ A, so A ≅ A'. -/
```

## Source Excerpt

```lean
theorem j_closure_minimality :
    canonical_j_family.non_empty = true ∧
    canonical_j_family.complete_lattice = true ∧
    canonical_j_family.has_minimum = true ∧
    canonical_j_family.minimum_unique = true :=
  ⟨rfl, rfl, rfl, rfl⟩
```
