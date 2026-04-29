---
{
  "projection_kind": "taulib_declaration",
  "title": "archetype_existence",
  "permalink": "/verify/taulib/docs/book-vii-meta-archetypes/archetype-existence/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Meta.Archetypes`.",
  "declaration_id": "TauLib.BookVII.Meta.Archetypes::archetype_existence",
  "declaration_slug": "archetype-existence",
  "kind": "theorem",
  "name": "archetype_existence",
  "module_name": "TauLib.BookVII.Meta.Archetypes",
  "module_url": "/verify/taulib/docs/book-vii-meta-archetypes/",
  "source_line_start": 202,
  "source_line_end": 207,
  "registry_ids": [
    "VII.T08"
  ],
  "related_registry_items": [
    {
      "id": "VII.T08",
      "title": "Archetype Existence",
      "url": "/registry/object/VII.T08/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L202-L207",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L202-L207",
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
- Source path: [`TauLib/BookVII/Meta/Archetypes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L202-L207)
- Source range: L202-L207
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T08` — Archetype Existence

## Immediate Comment / Docstring

```lean
/-- [VII.T08] Archetype Existence: for every structural invariant I that is
    exhibited by at least one j-closed subobject of [τ^op, τ], there exists
    a unique (up to iso) archetype 𝔄_I — a minimal j-closed fixed point
    exhibiting I.

    Proof: immediate from VII.L08. The minimum element of the j-closed
    I-exhibiting family satisfies (A1) j-closure (by lattice_closure),
    (A2) I-exhibition (by positive_coherence), (A3) minimality (by construction).
    Uniqueness up to iso from VII.L08 minimum_unique. -/
```

## Source Excerpt

```lean
theorem archetype_existence :
    canonical_archetype.a1_j_closed = true ∧
    canonical_archetype.a2_exhibits_invariant = true ∧
    canonical_archetype.a3_minimal = true ∧
    canonical_j_family.minimum_unique = true :=
  ⟨rfl, rfl, rfl, rfl⟩
```
