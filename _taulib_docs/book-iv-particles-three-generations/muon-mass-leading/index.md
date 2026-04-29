---
{
  "projection_kind": "taulib_declaration",
  "title": "muon_mass_leading",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/muon-mass-leading/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::muon_mass_leading",
  "declaration_slug": "muon-mass-leading",
  "kind": "def",
  "name": "muon_mass_leading",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 562,
  "source_line_end": 565,
  "registry_ids": [
    "IV.T144"
  ],
  "related_registry_items": [
    {
      "id": "IV.T144",
      "title": "m_mu/m_e Leading-Order Formula",
      "url": "/registry/object/IV.T144/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L562-L565",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L562-L565",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L562-L565)
- Source range: L562-L565
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.T144` — m_mu/m_e Leading-Order Formula

## Immediate Comment / Docstring

```lean
/-- [IV.T144] m_μ/m_e leading-order formula: ι_τ^{-5}.
    Leading order: m_μ/m_e ≈ ι_τ^{-5} at 44,258 ppm (4.4% gap).
    Exponent 5 = N_generators = W_3(4) = NLO modulus (same as EW corrections).
    NLO correction c_μ = 0.9576 requires first-principles derivation (OQ-C5a).
    Scope: tau-effective. -/
```

## Source Excerpt

```lean
def muon_mass_leading : String :=
  "iota^{-5} = 215.919 vs m_mu/m_e = 206.768; gap 44258 ppm (4.4%). " ++
  "Exponent 5 = N_generators = W_3(4). " ++
  "NLO correction c_mu = 0.9576 open as OQ-C5a."
```
