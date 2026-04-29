---
{
  "projection_kind": "taulib_declaration",
  "title": "MuonNNLOCorrection",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/muon-nnlocorrection/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::MuonNNLOCorrection",
  "declaration_slug": "muon-nnlocorrection",
  "kind": "structure",
  "name": "MuonNNLOCorrection",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 961,
  "source_line_end": 972,
  "registry_ids": [
    "IV.T156"
  ],
  "related_registry_items": [
    {
      "id": "IV.T156",
      "title": "m_μ/m_e NNLO Correction: δ = 1/W₃(4)² = 1/25",
      "url": "/registry/object/IV.T156/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L961-L972",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L961-L972",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L961-L972)
- Source range: L961-L972
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T156` — m_μ/m_e NNLO Correction: δ = 1/W₃(4)² = 1/25

## Immediate Comment / Docstring

```lean
/-- m_μ/m_e = ι_τ^(-124/25) = ι_τ^(-5+1/25) at +307.1 ppm from PDG 206.768.
    Correction exponent δ = 1/25 = 1/W₃(4)² — NNLO Window Rule.
    Key: -124/25 = -4.96 exactly, matching Wave 3A numerical fit.
    NLO: W₃(4)=5; NNLO correction: W₃(4)²=25. [IV.T156] -/
```

## Source Excerpt

```lean
structure MuonNNLOCorrection where
  /-- NNLO correction numerator: δ = 1/25. -/
  delta_numer : Nat := 1
  /-- NNLO correction denominator: W₃(4)² = 25. -/
  delta_denom : Nat := 25
  /-- Window power in NNLO rule: W₃(4)^window_power = 5^2 = 25. -/
  window_power : Nat := 2
  /-- Full exponent numerator: 124. -/
  exponent_numer : Nat := 124
  /-- Full exponent denominator: 25. -/
  exponent_denom : Nat := 25
  deriving Repr
```
