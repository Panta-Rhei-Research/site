---
{
  "projection_kind": "taulib_declaration",
  "title": "boundary_archetype_minimality",
  "permalink": "/verify/taulib/docs/book-vii-meta-archetypes/boundary-archetype-minimality/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Meta.Archetypes`.",
  "declaration_id": "TauLib.BookVII.Meta.Archetypes::boundary_archetype_minimality",
  "declaration_slug": "boundary-archetype-minimality",
  "kind": "theorem",
  "name": "boundary_archetype_minimality",
  "module_name": "TauLib.BookVII.Meta.Archetypes",
  "module_url": "/verify/taulib/docs/book-vii-meta-archetypes/",
  "source_line_start": 291,
  "source_line_end": 306,
  "registry_ids": [
    "VII.P05"
  ],
  "related_registry_items": [
    {
      "id": "VII.P05",
      "title": "Boundary Archetype Minimality",
      "url": "/registry/object/VII.P05/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L291-L306",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L291-L306",
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
- Source path: [`TauLib/BookVII/Meta/Archetypes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L291-L306)
- Source range: L291-L306
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.P05` — Boundary Archetype Minimality

## Immediate Comment / Docstring

```lean
/-- [VII.P05] Boundary Archetype Minimality: L = S¹ ∨ S¹ is the minimal
    j-closed fixed point exhibiting I_bnd. No proper j-closed subobject
    of L exhibits I_bnd.

    Proof:
    1. j-closure of L: L is j-closed because it is the boundary of a J_τ-sheaf.
       O(τ³) restricts to L, and restriction of a sheaf to a closed subspace
       is a sheaf on the induced topology.
    2. I_bnd-exhibition: L satisfies (B1)–(B4) as verified in VII.D18.
    3. Minimality: Suppose F ↪ L is a proper j-closed subobject exhibiting I_bnd.
       By (B1), F has two connected components away from p₀.
       By (B2), F contains p₀.
       By (B3), π₁(F, p₀) must be free on two generators.
       The only subspace of S¹ ∨ S¹ with π₁ ≅ ℤ * ℤ containing p₀
       and two loop generators is S¹ ∨ S¹ itself — removing any arc
       destroys that generator. Therefore F = L. -/
```

## Source Excerpt

```lean
theorem boundary_archetype_minimality :
    -- Archetype conditions
    boundary_archetype.archetype.a1_j_closed = true ∧
    boundary_archetype.archetype.a2_exhibits_invariant = true ∧
    boundary_archetype.archetype.a3_minimal = true ∧
    -- Boundary conditions (B1)–(B4)
    boundary_archetype.invariant.b1_two_domains = true ∧
    boundary_archetype.invariant.b2_crossing_point = true ∧
    boundary_archetype.invariant.b3_monodromy_exchange = true ∧
    boundary_archetype.invariant.b4_transition_morphism = true ∧
    -- Carrier data
    boundary_archetype.carrier_is_lemniscate = true ∧
    boundary_archetype.pi1_free_rank = 2 ∧
    boundary_archetype.lobe_count = 2 ∧
    boundary_archetype.crossing_count = 1 :=
  ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩
```
