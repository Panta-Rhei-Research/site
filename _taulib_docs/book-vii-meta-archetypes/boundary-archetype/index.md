---
{
  "projection_kind": "taulib_declaration",
  "title": "BoundaryArchetype",
  "permalink": "/verify/taulib/docs/book-vii-meta-archetypes/boundary-archetype/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Archetypes`.",
  "declaration_id": "TauLib.BookVII.Meta.Archetypes::BoundaryArchetype",
  "declaration_slug": "boundary-archetype",
  "kind": "structure",
  "name": "BoundaryArchetype",
  "module_name": "TauLib.BookVII.Meta.Archetypes",
  "module_url": "/verify/taulib/docs/book-vii-meta-archetypes/",
  "source_line_start": 254,
  "source_line_end": 267,
  "registry_ids": [
    "VII.D18"
  ],
  "related_registry_items": [
    {
      "id": "VII.D18",
      "title": "Boundary Archetype",
      "url": "/registry/object/VII.D18/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L254-L267",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L254-L267",
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

- Module: [TauLib.BookVII.Meta.Archetypes](/verify/taulib/docs/book-vii-meta-archetypes/)
- Source path: [`TauLib/BookVII/Meta/Archetypes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L254-L267)
- Source range: L254-L267
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D18` — Boundary Archetype

## Immediate Comment / Docstring

```lean
/-- [VII.D18] Boundary Archetype: the minimal j-closed fixed point exhibiting
    the threshold-crossing invariant I_bnd. Geometric carrier: L = S¹ ∨ S¹.

    L satisfies (B1)–(B4):
    - (B1): Two loops S¹₊, S¹₋; L \ {p₀} = (S¹₊ \ {p₀}) ⊔ (S¹₋ \ {p₀})
    - (B2): Wedge point p₀; S¹₊ ∩ S¹₋ = {p₀}
    - (B3): π₁(L, p₀) ≅ ℤ * ℤ, free on two generators
    - (B4): Every path from S¹₊ to S¹₋ passes through p₀ -/
```

## Source Excerpt

```lean
structure BoundaryArchetype where
  /-- Archetype conditions (A1)–(A3) satisfied. -/
  archetype : ArchetypeFixedPoint := {}
  /-- Threshold-crossing conditions (B1)–(B4) satisfied. -/
  invariant : ThresholdCrossingInvariant := i_bnd
  /-- Carrier is lemniscate L = S¹ ∨ S¹. -/
  carrier_is_lemniscate : Bool := true
  /-- Fundamental group: π₁(L, p₀) ≅ ℤ * ℤ (free on two generators). -/
  pi1_free_rank : Nat := 2
  /-- Number of lobes. -/
  lobe_count : Nat := 2
  /-- Number of crossing points. -/
  crossing_count : Nat := 1
  deriving Repr
```
