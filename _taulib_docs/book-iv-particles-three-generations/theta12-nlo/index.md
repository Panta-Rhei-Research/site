---
{
  "projection_kind": "taulib_declaration",
  "title": "Theta12NLO",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/theta12-nlo/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::Theta12NLO",
  "declaration_slug": "theta12-nlo",
  "kind": "structure",
  "name": "Theta12NLO",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1894,
  "source_line_end": 1901,
  "registry_ids": [
    "IV.T175"
  ],
  "related_registry_items": [
    {
      "id": "IV.T175",
      "title": "θ₁₂ from QLC + Higgs NLO at +3106 ppm",
      "url": "/registry/object/IV.T175/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1894-L1901",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1894-L1901",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1894-L1901)
- Source range: L1894-L1901
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T175` — θ₁₂ from QLC + Higgs NLO at +3106 ppm

## Immediate Comment / Docstring

```lean
/-- [IV.T175] θ₁₂ NLO from QLC + Higgs correction structure. -/
```

## Source Excerpt

```lean
structure Theta12NLO where
  /-- Higgs correction power: ι_τ² in δ = ι_τ²κ_ω. -/
  higgs_correction_power : Nat := 2
  /-- Deviation from PDG in ppm (+3106). -/
  deviation_ppm : Nat := 3106
  /-- Number of free parameters (zero: all from ι_τ). -/
  free_params : Nat := 0
  deriving Repr
```
