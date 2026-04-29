---
{
  "projection_kind": "taulib_declaration",
  "title": "LeptonSigmaExponents",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/lepton-sigma-exponents/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::LeptonSigmaExponents",
  "declaration_slug": "lepton-sigma-exponents",
  "kind": "structure",
  "name": "LeptonSigmaExponents",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 668,
  "source_line_end": 675,
  "registry_ids": [
    "IV.T149"
  ],
  "related_registry_items": [
    {
      "id": "IV.T149",
      "title": "Lepton σ-Matrix Exponents from PDG Back-Solve",
      "url": "/registry/object/IV.T149/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L668-L675",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L668-L675",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L668-L675)
- Source range: L668-L675
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T149` — Lepton σ-Matrix Exponents from PDG Back-Solve

## Immediate Comment / Docstring

```lean
/-- Lepton σ-matrix back-solve: M eigenvalues = (m_e, m_μ, m_τ) MeV.
    Setting a = m_μ (σ-odd eigenvalue): c = m_e + m_τ - m_μ = 1671.713 MeV,
    b = √((m_μ·c - m_e·m_τ)/2) = 296.414 MeV. In ι_τ-units (relative to m_n):
    p_l = 2.033, q_l = 1.073, r_l = −0.536. [IV.T149] -/
```

## Source Excerpt

```lean
structure LeptonSigmaExponents where
  /-- σ-odd diagonal entry exponent: a = m_n·ι_τ^p_l ≈ m_μ. -/
  p_l : Float  -- ≈ 2.033
  /-- Off-diagonal entry exponent: b = m_n·ι_τ^q_l ≈ 296.4 MeV. -/
  q_l : Float  -- ≈ 1.073
  /-- Central crossing entry exponent: c = m_n·ι_τ^r_l ≈ 1671.7 MeV. -/
  r_l : Float  -- ≈ -0.536 (negative: c > m_n)
  deriving Repr
```
