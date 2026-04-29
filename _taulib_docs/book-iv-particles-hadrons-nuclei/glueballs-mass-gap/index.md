---
{
  "projection_kind": "taulib_declaration",
  "title": "glueballs_mass_gap",
  "permalink": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/glueballs-mass-gap/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.HadronsNuclei`.",
  "declaration_id": "TauLib.BookIV.Particles.HadronsNuclei::glueballs_mass_gap",
  "declaration_slug": "glueballs-mass-gap",
  "kind": "def",
  "name": "glueballs_mass_gap",
  "module_name": "TauLib.BookIV.Particles.HadronsNuclei",
  "module_url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/",
  "source_line_start": 142,
  "source_line_end": 143,
  "registry_ids": [
    "IV.R129"
  ],
  "related_registry_items": [
    {
      "id": "IV.R129",
      "title": "Glueballs and the mass gap",
      "url": "/registry/object/IV.R129/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L142-L143",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.HadronsNuclei",
        "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L142-L143",
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

- Module: [TauLib.BookIV.Particles.HadronsNuclei](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/)
- Source path: [`TauLib/BookIV/Particles/HadronsNuclei.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L142-L143)
- Source range: L142-L143
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.R129` — Glueballs and the mass gap

## Immediate Comment / Docstring

```lean
/-- [IV.R129] Glueball existence is a direct consequence of the mass gap:
    confinement ensures every excitation above vacuum carries positive mass.
    m_gb ≈ 2π/σ_τ^(1/2) ≈ 1.5 GeV. -/
```

## Source Excerpt

```lean
def glueballs_mass_gap : String :=
  "Glueball existence: structural consequence of mass gap (confinement)"
```
