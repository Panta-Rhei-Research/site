---
{
  "projection_kind": "taulib_declaration",
  "title": "ExactlyThreeGens",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/exactly-three-gens/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::ExactlyThreeGens",
  "declaration_slug": "exactly-three-gens",
  "kind": "structure",
  "name": "ExactlyThreeGens",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 94,
  "source_line_end": 105,
  "registry_ids": [
    "IV.T83"
  ],
  "related_registry_items": [
    {
      "id": "IV.T83",
      "title": "Exactly three generations",
      "url": "/registry/object/IV.T83/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L94-L105",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.ThreeGenerations",
        "url": "/verify/taulib/docs/book-iv-particles-three-generations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L94-L105",
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L94-L105)
- Source range: L94-L105
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T83` — Exactly three generations

## Immediate Comment / Docstring

```lean
/-- [IV.T83] The lemniscate supports exactly three topologically
    distinct mode classes and no fourth class exists.

    L has exactly three structurally distinct regions:
    1. The crossing point (genus-changing singularity)
    2. A single lobe (S¹)
    3. The full figure (both lobes)

    This is topological, not energetic: no amount of energy creates a
    fourth class. LEP measurement N_ν = 2.9840 ± 0.0082 confirms. -/
```

## Source Excerpt

```lean
structure ExactlyThreeGens where
  /-- Number of generations. -/
  count : Nat := 3
  /-- Topological origin. -/
  origin : String := "L = S^1 v S^1 has 3 structurally distinct regions"
  /-- Number of topological regions on L = S¹ ∨ S¹ (crossing, lobe, full). -/
  n_topological_regions : Nat := 3
  /-- LEP confirmation N_ν numerator (×10000). -/
  lep_numer : Nat := 29840
  /-- LEP confirmation N_ν denominator. -/
  lep_denom : Nat := 10000
  deriving Repr
```
