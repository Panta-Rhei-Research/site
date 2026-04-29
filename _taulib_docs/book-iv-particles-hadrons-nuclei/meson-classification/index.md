---
{
  "projection_kind": "taulib_declaration",
  "title": "MesonClassification",
  "permalink": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/meson-classification/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.HadronsNuclei`.",
  "declaration_id": "TauLib.BookIV.Particles.HadronsNuclei::MesonClassification",
  "declaration_slug": "meson-classification",
  "kind": "structure",
  "name": "MesonClassification",
  "module_name": "TauLib.BookIV.Particles.HadronsNuclei",
  "module_url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/",
  "source_line_start": 70,
  "source_line_end": 81,
  "registry_ids": [
    "IV.D200"
  ],
  "related_registry_items": [
    {
      "id": "IV.D200",
      "title": "Meson classification",
      "url": "/registry/object/IV.D200/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L70-L81",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L70-L81",
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
- Source path: [`TauLib/BookIV/Particles/HadronsNuclei.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L70-L81)
- Source range: L70-L81
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D200` — Meson classification

## Immediate Comment / Docstring

```lean
/-- [IV.D200] A meson |q_i q̄_j⟩ classified by:
    1. Flavor content (quark flavors from {u,d,s,c,b,t})
    2. Spin-parity J^PC (angular momentum + spin)
    3. Generation class (lemniscate mode classes of constituents)

    Pseudoscalar (J=0): anti-aligned spins.
    Vector (J=1): aligned spins. -/
```

## Source Excerpt

```lean
structure MesonClassification where
  /-- Name. -/
  name : String
  /-- Quark content. -/
  quark : String
  /-- Antiquark content. -/
  antiquark : String
  /-- Spin J. -/
  spin : Nat
  /-- Approximate mass (MeV). -/
  mass_mev : Nat
  deriving Repr
```
