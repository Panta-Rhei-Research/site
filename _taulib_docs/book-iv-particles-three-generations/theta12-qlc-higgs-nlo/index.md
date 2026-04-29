---
{
  "projection_kind": "taulib_declaration",
  "title": "theta12_qlc_higgs_nlo",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/theta12-qlc-higgs-nlo/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::theta12_qlc_higgs_nlo",
  "declaration_slug": "theta12-qlc-higgs-nlo",
  "kind": "def",
  "name": "theta12_qlc_higgs_nlo",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1889,
  "source_line_end": 1891,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1889-L1891",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1889-L1891",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1889-L1891)
- Source range: L1889-L1891
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.T175` — θ₁₂ from QLC + Higgs NLO at +3106 ppm

## Immediate Comment / Docstring

```lean
/-- [IV.T175] θ₁₂ from QLC + Higgs NLO at +3106 ppm.
    θ₁₂ = π/4 − θ_C + ι_τ²κ_ω. Major improvement over bare QLC (−84888 ppm). -/
```

## Source Excerpt

```lean
def theta12_qlc_higgs_nlo : String :=
  "θ₁₂ = π/4 − θ_C + ι_τ²κ_ω, sin²θ₁₂ = 0.3080, " ++
  "PDG 0.307, deviation +3106 ppm. Approaches τ-effective threshold."
```
