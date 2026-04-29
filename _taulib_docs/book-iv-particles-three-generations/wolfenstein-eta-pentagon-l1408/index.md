---
{
  "projection_kind": "taulib_declaration",
  "title": "WolfensteinEtaPentagon",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/wolfenstein-eta-pentagon-l1408/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::WolfensteinEtaPentagon",
  "declaration_slug": "wolfenstein-eta-pentagon-l1408",
  "kind": "structure",
  "name": "WolfensteinEtaPentagon",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1408,
  "source_line_end": 1417,
  "registry_ids": [
    "IV.D359"
  ],
  "related_registry_items": [
    {
      "id": "IV.D359",
      "title": "Wolfenstein η̄ from 5-Generator Pentagon: CP Violation from ω-Period",
      "url": "/registry/object/IV.D359/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1408-L1417",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1408-L1417",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1408-L1417)
- Source range: L1408-L1417
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D359` — Wolfenstein η̄ from 5-Generator Pentagon: CP Violation from ω-Period

## Immediate Comment / Docstring

```lean
/-- [IV.D359] Wolfenstein η̄ pentagon structure (formalized). -/
```

## Source Excerpt

```lean
structure WolfensteinEtaPentagon where
  /-- Number of generators in pentagon. -/
  n_generators : Nat := 5
  /-- Step angle in degrees. -/
  step_degrees : Nat := 72
  /-- Improvement factor over baseline (×1). -/
  improvement_factor : Nat := 10
  /-- Deviation from PDG in ppm. -/
  deviation_ppm : Nat := 2285
  deriving Repr
```
