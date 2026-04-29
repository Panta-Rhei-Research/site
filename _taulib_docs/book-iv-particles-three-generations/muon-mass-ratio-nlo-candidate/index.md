---
{
  "projection_kind": "taulib_declaration",
  "title": "muon_mass_ratio_nlo_candidate",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/muon-mass-ratio-nlo-candidate/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::muon_mass_ratio_nlo_candidate",
  "declaration_slug": "muon-mass-ratio-nlo-candidate",
  "kind": "def",
  "name": "muon_mass_ratio_nlo_candidate",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 689,
  "source_line_end": 691,
  "registry_ids": [
    "IV.T148"
  ],
  "related_registry_items": [
    {
      "id": "IV.T148",
      "title": "m_μ/m_e Best NLO Formula: ι_τ⁻⁴·⁹⁶ at +307 ppm",
      "url": "/registry/object/IV.T148/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L689-L691",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L689-L691",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L689-L691)
- Source range: L689-L691
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.T148` — m_μ/m_e Best NLO Formula: ι_τ⁻⁴·⁹⁶ at +307 ppm

## Immediate Comment / Docstring

```lean
/-- The NLO approximation for m_μ/m_e from Wave 3A 14-formula scan.
    Best: ι_τ^(-4.96) = 206.832 at +307 ppm from PDG 206.768.
    Effective exponent 4.96 = 5 - 0.04; gap 0.04 ≈ 1/25 open as OQ-C5a.
    [IV.T148] -/
```

## Source Excerpt

```lean
def muon_mass_ratio_nlo_candidate : String :=
  "iota_tau^(-4.96) = 206.832, +307 ppm from PDG 206.768. " ++
  "Exponent 4.96 = 5 - 0.04; delta=0.04 open as OQ-C5a (IV.R398)."
```
