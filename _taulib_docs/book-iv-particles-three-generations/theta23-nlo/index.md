---
{
  "projection_kind": "taulib_declaration",
  "title": "Theta23NLO",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/theta23-nlo/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::Theta23NLO",
  "declaration_slug": "theta23-nlo",
  "kind": "structure",
  "name": "Theta23NLO",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1858,
  "source_line_end": 1865,
  "registry_ids": [
    "IV.T174"
  ],
  "related_registry_items": [
    {
      "id": "IV.T174",
      "title": "θ₂₃ NLO via Window Algebra at +8604 ppm",
      "url": "/registry/object/IV.T174/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1858-L1865",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1858-L1865",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1858-L1865)
- Source range: L1858-L1865
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T174` — θ₂₃ NLO via Window Algebra at +8604 ppm

## Immediate Comment / Docstring

```lean
/-- [IV.T174] θ₂₃ NLO structure. -/
```

## Source Excerpt

```lean
structure Theta23NLO where
  /-- Window exponent W₃(4) = 5. -/
  window_exp : Nat := 5
  /-- Deviation from PDG in ppm (+8604). -/
  deviation_ppm : Nat := 8604
  /-- LO deviation in ppm (+18012), NLO halves it. -/
  lo_deviation_ppm : Nat := 18012
  deriving Repr
```
