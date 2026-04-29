---
{
  "projection_kind": "taulib_declaration",
  "title": "ASectorPMNSRotation",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/asector-pmnsrotation/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::ASectorPMNSRotation",
  "declaration_slug": "asector-pmnsrotation",
  "kind": "structure",
  "name": "ASectorPMNSRotation",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1088,
  "source_line_end": 1095,
  "registry_ids": [
    "IV.D356"
  ],
  "related_registry_items": [
    {
      "id": "IV.D356",
      "title": "A-Sector PMNS Rotation: pi-Generator Flavor Rotation on tau^1",
      "url": "/registry/object/IV.D356/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1088-L1095",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1088-L1095",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1088-L1095)
- Source range: L1088-L1095
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D356` — A-Sector PMNS Rotation: pi-Generator Flavor Rotation on tau^1

## Immediate Comment / Docstring

```lean
/-- [IV.D356] A-sector PMNS rotation structure (formalized). -/
```

## Source Excerpt

```lean
structure ASectorPMNSRotation where
  /-- Generator index: π is 2nd of {α,π,γ,η,ω}. -/
  pi_generator_index : Nat := 2
  /-- Crossing denominator terms: (1+ι_τ) has 2 terms. -/
  crossing_denom_terms : Nat := 2
  /-- Candidate PMNS angle index: θ₂₃ is angle 2 of 3. -/
  theta_angle_index : Nat := 2
  deriving Repr
```
