---
{
  "projection_kind": "taulib_declaration",
  "title": "MuonNNLOK15_2",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/muon-nnlok15-2/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::MuonNNLOK15_2",
  "declaration_slug": "muon-nnlok15-2",
  "kind": "structure",
  "name": "MuonNNLOK15_2",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2158,
  "source_line_end": 2167,
  "registry_ids": [
    "IV.T176"
  ],
  "related_registry_items": [
    {
      "id": "IV.T176",
      "title": "m_μ/m_e NNLO: k=15/2 at −8.2 ppm (τ-effective, best)",
      "url": "/registry/object/IV.T176/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2158-L2167",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2158-L2167",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2158-L2167)
- Source range: L2158-L2167
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T176` — m_μ/m_e NNLO: k=15/2 at −8.2 ppm (τ-effective, best)

## Immediate Comment / Docstring

```lean
/-- [IV.T176] m_μ/m_e NNLO via k=15/2 structure (formalized). -/
```

## Source Excerpt

```lean
structure MuonNNLOK15_2 where
  /-- Numerator of k: 15. -/
  k_numer : Nat := 15
  /-- Denominator of k: 2. -/
  k_denom : Nat := 2
  /-- Deviation from PDG in ppm (×10). -/
  deviation_ppm : Nat := 8
  /-- Improvement factor over LO (×10). -/
  improvement_over_lo : Nat := 37
  deriving Repr
```
