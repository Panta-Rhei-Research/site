---
{
  "projection_kind": "taulib_declaration",
  "title": "composite_winding_suppressed",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/composite-winding-suppressed/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::composite_winding_suppressed",
  "declaration_slug": "composite-winding-suppressed",
  "kind": "theorem",
  "name": "composite_winding_suppressed",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 652,
  "source_line_end": 653,
  "registry_ids": [
    "IV.T147"
  ],
  "related_registry_items": [
    {
      "id": "IV.T147",
      "title": "Three-Generation Closure: Spectral Gap on T²",
      "url": "/registry/object/IV.T147/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L652-L653",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L652-L653",
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L652-L653)
- Source range: L652-L653
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T147` — Three-Generation Closure: Spectral Gap on T²

## Immediate Comment / Docstring

```lean
/-- Exactly three primitive winding classes exist below the first composite
    primitive mode (2,1) at λ=4+ι_τ⁻²≈12.58. Spectral gap ratio
    λ_(2,0)/λ_(1,1) = 4/(1+ι_τ⁻²) ≈ 0.4173 isolates the three light
    generations. No fourth light generation below the dark-sector cutoff.
    [IV.T147] -/
```

## Source Excerpt

```lean
theorem composite_winding_suppressed :
    primitive_winding_classes.length = 3 := by rfl
```
