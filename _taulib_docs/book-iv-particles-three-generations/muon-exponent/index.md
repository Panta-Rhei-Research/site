---
{
  "projection_kind": "taulib_declaration",
  "title": "MuonExponent",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/muon-exponent/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::MuonExponent",
  "declaration_slug": "muon-exponent",
  "kind": "structure",
  "name": "MuonExponent",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 190,
  "source_line_end": 201,
  "registry_ids": [
    "IV.P122"
  ],
  "related_registry_items": [
    {
      "id": "IV.P122",
      "title": "Muon mass exponent",
      "url": "/registry/object/IV.P122/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L190-L201",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L190-L201",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L190-L201)
- Source range: L190-L201
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P122` — Muon mass exponent

## Immediate Comment / Docstring

```lean
/-- [IV.P122] m_μ/m_e = ι_τ^(-5)(1 + δ_μ) where δ_μ ≈ −0.04 is O(α).
    Bare topological exponent: 5.
    Corrected prediction: m_e·ι_τ^(-4.96) ≈ 106.1 MeV (experiment: 105.66 MeV, 0.4%).

    Mass values in MeV (scaled ×1000):
    - Predicted: 106100 / 1000 = 106.1 MeV
    - Experimental: 105658 / 1000 = 105.658 MeV -/
```

## Source Excerpt

```lean
structure MuonExponent where
  /-- Bare topological exponent. -/
  bare_exp : Nat := 5
  /-- Effective exponent (×100). -/
  effective_exp_x100 : Nat := 496
  /-- Predicted mass (MeV ×1000). -/
  predicted_x1000 : Nat := 106100
  /-- Experimental mass (MeV ×1000). -/
  experimental_x1000 : Nat := 105658
  /-- Agreement (percent ×100). -/
  agreement_pct_x100 : Nat := 40
  deriving Repr
```
