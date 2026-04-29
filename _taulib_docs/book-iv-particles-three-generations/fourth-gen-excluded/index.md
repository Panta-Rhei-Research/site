---
{
  "projection_kind": "taulib_declaration",
  "title": "FourthGenExcluded",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/fourth-gen-excluded/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::FourthGenExcluded",
  "declaration_slug": "fourth-gen-excluded",
  "kind": "structure",
  "name": "FourthGenExcluded",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 118,
  "source_line_end": 127,
  "registry_ids": [
    "IV.R111"
  ],
  "related_registry_items": [
    {
      "id": "IV.R111",
      "title": "Fourth generation excluded",
      "url": "/registry/object/IV.R111/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L118-L127",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L118-L127",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L118-L127)
- Source range: L118-L127
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R111` — Fourth generation excluded

## Immediate Comment / Docstring

```lean
/-- [IV.R111] The exclusion of a fourth generation is topological:
    L = S¹ ∨ S¹ has exactly two lobes and one crossing point, so no
    fourth mode class exists regardless of energy. -/
```

## Source Excerpt

```lean
structure FourthGenExcluded where
  /-- Number of lobes. -/
  num_lobes : Nat := 2
  /-- Number of crossing points. -/
  num_crossings : Nat := 1
  /-- Max distinct regions. -/
  max_regions : Nat := 3
  /-- Exclusion mechanism: 1 = topological (not energetic). -/
  exclusion_mechanism : Nat := 1
  deriving Repr
```
