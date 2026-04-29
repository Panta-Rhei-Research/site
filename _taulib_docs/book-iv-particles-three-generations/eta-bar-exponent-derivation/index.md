---
{
  "projection_kind": "taulib_declaration",
  "title": "eta_bar_exponent_derivation",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/eta-bar-exponent-derivation/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::eta_bar_exponent_derivation",
  "declaration_slug": "eta-bar-exponent-derivation",
  "kind": "def",
  "name": "eta_bar_exponent_derivation",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2022,
  "source_line_end": 2024,
  "registry_ids": [
    "IV.T173"
  ],
  "related_registry_items": [
    {
      "id": "IV.T173",
      "title": "η̄ Exponent Derivation: All from |lobes|=2, |gen|=5 (τ-effective)",
      "url": "/registry/object/IV.T173/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2022-L2024",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2022-L2024",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2022-L2024)
- Source range: L2022-L2024
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.T173` — η̄ Exponent Derivation: All from |lobes|=2, |gen|=5 (τ-effective)

## Immediate Comment / Docstring

```lean
/-- [IV.T173] η̄ Exponent Derivation.
    η̄ = ι_τ^{−1/4}·κ_D^{5/4}/√5 at −2285 ppm from PDG. -/
```

## Source Excerpt

```lean
def eta_bar_exponent_derivation : String :=
  "η̄ = ι_τ^{−1/4}·κ_D^{5/4}/√5 = 0.34720, PDG 0.349±0.013, " ++
  "deviation −2285 ppm (within 1σ). Three topological factors."
```
