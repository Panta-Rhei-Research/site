---
{
  "projection_kind": "taulib_declaration",
  "title": "theta23_nlo_window",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/theta23-nlo-window/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::theta23_nlo_window",
  "declaration_slug": "theta23-nlo-window",
  "kind": "def",
  "name": "theta23_nlo_window",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1853,
  "source_line_end": 1855,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1853-L1855",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1853-L1855",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1853-L1855)
- Source range: L1853-L1855
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.T174` — θ₂₃ NLO via Window Algebra at +8604 ppm

## Immediate Comment / Docstring

```lean
/-- [IV.T174] θ₂₃ NLO via Window Algebra at +8604 ppm.
    sin²θ₂₃ = 0.5507, PDG 0.546. Halves LO deviation (+18012 → +8604 ppm). -/
```

## Source Excerpt

```lean
def theta23_nlo_window : String :=
  "sin(θ₂₃) = (1-ι_τ^5)/(1+ι_τ), sin²θ₂₃ = 0.5507, " ++
  "PDG 0.546, deviation +8604 ppm. NLO factor (1-ι_τ^5) halves LO error."
```
