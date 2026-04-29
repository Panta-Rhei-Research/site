---
{
  "projection_kind": "taulib_declaration",
  "title": "muon_nnlo_k15_2",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/muon-nnlo-k15-2/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::muon_nnlo_k15_2",
  "declaration_slug": "muon-nnlo-k15-2",
  "kind": "def",
  "name": "muon_nnlo_k15_2",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2153,
  "source_line_end": 2155,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2153-L2155",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2153-L2155",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2153-L2155)
- Source range: L2153-L2155
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.T176` — m_μ/m_e NNLO: k=15/2 at −8.2 ppm (τ-effective, best)

## Immediate Comment / Docstring

```lean
/-- [IV.T176] m_μ/m_e NNLO at −8.2 ppm via k=15/2.
    m_μ/m_e = ι_τ^{−124/25}·(1−ι_τ^{15/2}) = 206.767.
    37.5× improvement over LO. -/
```

## Source Excerpt

```lean
def muon_nnlo_k15_2 : String :=
  "m_μ/m_e = ι_τ^{−124/25}·(1−ι_τ^{15/2}) = 206.767, " ++
  "PDG 206.768, deviation −8.2 ppm. 37.5× improvement over LO."
```
