---
{
  "projection_kind": "taulib_declaration",
  "title": "NucleonMassDecomp",
  "permalink": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/nucleon-mass-decomp/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.HadronsNuclei`.",
  "declaration_id": "TauLib.BookIV.Particles.HadronsNuclei::NucleonMassDecomp",
  "declaration_slug": "nucleon-mass-decomp",
  "kind": "structure",
  "name": "NucleonMassDecomp",
  "module_name": "TauLib.BookIV.Particles.HadronsNuclei",
  "module_url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/",
  "source_line_start": 157,
  "source_line_end": 170,
  "registry_ids": [
    "IV.P128"
  ],
  "related_registry_items": [
    {
      "id": "IV.P128",
      "title": "Nucleon mass decomposition",
      "url": "/registry/object/IV.P128/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L157-L170",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L157-L170",
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

- Module: [TauLib.BookIV.Particles.HadronsNuclei](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/)
- Source path: [`TauLib/BookIV/Particles/HadronsNuclei.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L157-L170)
- Source range: L157-L170
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P128` — Nucleon mass decomposition

## Immediate Comment / Docstring

```lean
/-- [IV.P128] m_N = E_vac + E_kin + Σm_qi
    - C-sector vacuum energy: ~400 MeV (42%)
    - Quark kinetic energy: ~500 MeV (53%)
    - Bare quark rest masses: ~12 MeV (1%)
    - Trace anomaly + sigma terms: ~27 MeV (3%)

    Vacuum + kinetic ≈ 99% of nucleon mass.
    All energies in MeV. -/
```

## Source Excerpt

```lean
structure NucleonMassDecomp where
  /-- Vacuum energy (MeV). -/
  e_vac_mev : Nat := 400
  /-- Kinetic energy (MeV). -/
  e_kin_mev : Nat := 500
  /-- Quark rest masses (MeV). -/
  e_quark_mev : Nat := 12
  /-- Other (trace anomaly, sigma). -/
  e_other_mev : Nat := 27
  /-- Total nucleon mass (MeV, approximate). -/
  total_mev : Nat := 939
  /-- Percentage from non-quark-mass sources. -/
  nonquark_pct : Nat := 99
  deriving Repr
```
